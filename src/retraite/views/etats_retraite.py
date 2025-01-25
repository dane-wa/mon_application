from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from ..models.RetraiteDeces import RetraiteDeces
from ..models.RetraiteVirement import RetraiteVirement
from ..models.Retraite import Retraite
from ..models.Prefecture import Prefecture
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import OuterRef, Sum

@login_required
def retraite_etats(request):
    # Récupérer toutes les préfectures pour le menu déroulant
    prefecture = Prefecture.objects.all()

    # Récupérer la préfecture sélectionnée à partir des paramètres GET
    prefecture_id = request.GET.get('prefecture')

    # Sous-requête pour obtenir les nPension dans RetraiteDeces
    retraite_deces_subquery = RetraiteDeces.objects.filter(
        retraite_id=OuterRef('id')
    ).values('retraite__nPension')

    # Sous-requête pour obtenir les nPension dans Virementretraite
    retraite_virement_subquery = RetraiteVirement.objects.filter(
        retraite_id=OuterRef('id')
    ).values('retraite__nPension')

    # Exclusion des retraites ayant un nPension dans RetraiteDeces ou Virementretraite
    retraites_etats = Retraite.objects.exclude(
        nPension__in=retraite_deces_subquery
    ).exclude(
        nPension__in=retraite_virement_subquery
    )

    # Si une préfecture est sélectionnée, filtrer les retraites par cette préfecture
    if prefecture_id:
        retraites_etats = retraites_etats.filter(prefecture_id=prefecture_id)

    # Calcul des totaux pour les retraites filtrées
    total_montantTrim = retraites_etats.aggregate(Sum('montantTrim'))['montantTrim__sum'] or 0
    total_allocation = retraites_etats.aggregate(Sum('allocation'))['allocation__sum'] or 0
    total_montantTotal = retraites_etats.aggregate(Sum('montantTotal'))['montantTotal__sum'] or 0
    total_montantMensuel = sum(r.montantMensuel() for r in retraites_etats)
    total_montantComp = retraites_etats.aggregate(Sum('montantComp'))['montantComp__sum'] or 0
    total_montantPaye = sum(r.montantPaye() for r in retraites_etats)

    # création de la paggination
    paginator = Paginator(retraites_etats.order_by('id'), per_page=10)
    page = request.GET.get('page', 1)
    try:
        retraites_etats = paginator.get_page(page)
    except:
        retraites_etats = paginator.get_page(1)


    context = {
        'retraites_etats': retraites_etats,
        'prefecture': prefecture,
        'selected_prefecture': prefecture_id,
        'totaux': {
            'montantTrim': total_montantTrim,
            'allocation': total_allocation,
            'montantTotal': total_montantTotal,
            'montantMensuel': total_montantMensuel,
            'montantComp': total_montantComp,
            'montantPaye': total_montantPaye,
        },
    }

    return render(request, 'retraite/etats/retraite_etats.html', context)
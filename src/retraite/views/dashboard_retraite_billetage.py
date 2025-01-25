from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from ..models.RetraiteDeces import RetraiteDeces
from ..models.RetraiteVirement import RetraiteVirement
from ..models.Retraite import Retraite
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import OuterRef, Subquery


@login_required
def dashboard_retraite_billetage(request):
    # Sous-requête pour obtenir les nPension dans RetraiteDeces
    retraite_deces_subquery = RetraiteDeces.objects.filter(
        retraite_id=OuterRef('id')
    ).values('retraite__nPension')

    # Sous-requête pour obtenir les nPension dans Virementretraite
    retraite_virement_subquery = RetraiteVirement.objects.filter(
        retraite_id=OuterRef('id')
    ).values('retraite__nPension')

    # Exclusion des retraites ayant un nPension dans RetraiteDeces ou Virementretraite
    retraites_disponibles = Retraite.objects.exclude(
        nPension__in=retraite_deces_subquery
    ).exclude(
        nPension__in=retraite_virement_subquery
    )

    # Calcul des totaux
    total_montantTrim = sum(r.montantTrim for r in retraites_disponibles)
    total_allocation = sum(r.allocation for r in retraites_disponibles)
    total_montantTotal = sum(r.montantTotal for r in retraites_disponibles)
    total_montantMensuel = sum(r.montantMensuel() for r in retraites_disponibles)
    total_montantComp = sum(r.montantComp for r in retraites_disponibles)
    total_montantPaye = sum(r.montantPaye() for r in retraites_disponibles)

    # création de la paggination
    paginator = Paginator(retraites_disponibles.order_by('id'), per_page=10)
    page = request.GET.get('page', 1)
    try:
        retraites_disponibles = paginator.get_page(page)
    except:
        retraites_disponibles = paginator.get_page(1)

    context = {
        'retraites_disponibles': retraites_disponibles,
        'totaux': {
            'montantTrim': total_montantTrim,
            'allocation': total_allocation,
            'montantTotal': total_montantTotal,
            'montantMensuel': total_montantMensuel,
            'montantComp': total_montantComp,
            'montantPaye': total_montantPaye,
        },
    }

    return render(request, 'retraite/dashboard/retraite_billetage.html', context)
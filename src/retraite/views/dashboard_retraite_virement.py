from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from ..models.RetraiteDeces import RetraiteDeces
from ..models.RetraiteVirement import RetraiteVirement
from ..forms.RetraiteVirementForm import RetraiteVirementForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def dashboard_retraite_virement_index(request):
    # Récupérer les ID des retraites qui sont dans RetraiteDeces
    retraites_decedes_ids = RetraiteDeces.objects.values_list('retraite_id', flat=True)

    # Exclure les virements liés aux retraites dans la table RetraiteDeces
    retraite_virement = RetraiteVirement.objects.exclude(retraite_id__in=retraites_decedes_ids)

    # création de la pagination
    paginator = Paginator(retraite_virement.order_by('id'), per_page=10)
    page = request.GET.get('page', 1)
    try:
        retraite_virement = paginator.get_page(page)
    except:
        retraite_virement = paginator.get_page(1)

    context = {
        'retraite_virement': retraite_virement
    }

    return render(request, 'retraite/dashboard/dashboard_retraite_virement_index.html', context)

@login_required
def add_retraite_virement(request):
    if request.method == 'POST':
        retraite_virement_form = RetraiteVirementForm(request.POST)
        if retraite_virement_form.is_valid():
            retraite_virement_form.save()
            messages.success(request, "Ajouté avec succès!")
            return redirect('retraite:retraite_virement_liste')
    else:
        retraite_virement_form = RetraiteVirementForm()
    return render(request, 'retraite/dashboard/add_retraite_virement.html', {'retraite_virement_form': retraite_virement_form})

@login_required
def edit_retraite_virement(request, id):
    retraitevirement = get_object_or_404(RetraiteVirement, id=id)

    if request.method == 'POST':
        if request.POST.get('_method') == 'PUT':
            retraite_virement_form = RetraiteVirementForm(request.POST, instance=retraitevirement)
            if retraite_virement_form.is_valid():
                retraite_virement_form.save()
                messages.success(request, "Modifié avec success !")
                return redirect('retraite:retraite_virement_liste')
        else:
            retraite_virement_form = RetraiteVirementForm(instance=retraitevirement)
    else:
        retraite_virement_form = RetraiteVirementForm(instance=retraitevirement)
    return render(request, 'retraite/dashboard/add_retraite_virement.html', {'retraite_virement_form': retraite_virement_form, 'retraitevirement': retraitevirement})

@login_required
def delete_retraite_viremnt(request, id):
    retraitevirement = get_object_or_404(RetraiteVirement, id=id)
    if request.method == 'POST':
        if request.POST.get('_method') == 'DELETE':
            retraitevirement.delete()
            messages.success(request, "Enregistrement supprimé !")
            return redirect('retraite:retraite_virement_liste')
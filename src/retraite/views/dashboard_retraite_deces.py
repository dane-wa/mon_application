from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from ..models.RetraiteDeces import RetraiteDeces
from django.contrib.auth.decorators import login_required
from ..forms.RetraiteDecesForm import RetraiteDecesForm
from django.contrib import messages

@login_required
def dashboard_retraite_deces_index(request):
    # affichage de tout le contenu retraite
    retraitedeces = RetraiteDeces.objects.all()

    #création du champ recherche
    if request.method == 'GET':
       name = request.GET.get('recherche')
       if name != '' and name is not None:
          retraitedeces = RetraiteDeces.objects.filter(id=name)

       # création de la pagination
       paginator= Paginator(retraitedeces.order_by('id'), per_page=10)
       page = request.GET.get('page', 1)
       try:
          retraitedeces = paginator.get_page(page)
       except:
          retraitedeces = paginator.get_page(1)

    return render(request, 'retraite/dashboard/dashboard_retraite_deces_index.html', {'retraitedeces': retraitedeces})

# création de la page d'ajout
@login_required
def add_retraite_deces(request):
    if request.method == 'POST':
        retraite_deces_form = RetraiteDecesForm(request.POST)
        if retraite_deces_form.is_valid():
            retraite_deces_form.save()
            messages.success(request, "Ajouté avec succès!")
            return redirect('retraite:retraite_deces_liste')
    else:
        retraite_deces_form = RetraiteDecesForm()

    return render(request, 'retraite/dashboard/add_retraite_deces.html', {'retraite_deces_form': retraite_deces_form})

# création de la modification
@login_required
def edit_retraite_deces(request, id):
    retraitedeces = get_object_or_404(RetraiteDeces, id=id)

    if request.method == "POST":
        if request.POST.get('_method') == 'PUT':
            retraite_deces_form = RetraiteDecesForm(request.POST, instance=retraitedeces)
            if retraite_deces_form.is_valid():
                retraite_deces_form.save()
                messages.success(request, "Modifié avec success !")
                return redirect('retraite:retraite_deces_liste')
        else:
            retraite_deces_form = RetraiteDecesForm(instance=retraitedeces)

    else:
        retraite_deces_form = RetraiteDecesForm(instance=retraitedeces)
    return render(request, 'retraite/dashboard/add_retraite_deces.html', {'retraite_deces_form': retraite_deces_form, 'retraitedeces': retraitedeces})



# création de la suppression
@login_required
def delete_retraite_deces(request, id):
    retraitedeces = get_object_or_404(RetraiteDeces, id=id)
    if request.method == "POST":
        if request.POST.get('_method') == 'DELETE':
            retraitedeces.delete()
            messages.success(request, "Enregistrement supprimé !")
            return redirect('retraite:retraite_deces_liste')
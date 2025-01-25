from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from ..models.Retraite import Retraite
from django.contrib.auth.decorators import login_required
from ..forms.RetraiteForm import RetraiteForm
from django.contrib import messages
import os
from django.conf import settings

@login_required
def dashboard_retraite_index(request):
    # affichage de tout le contenu retraite
    retraite = Retraite.objects.all()

    #création du champ recherche
    if request.method == 'GET':
       name = request.GET.get('recherche')
       if name != '' and name is not None:
          retraite = Retraite.objects.filter(nPension__contains=name)


       # création de la pagination
       paginator= Paginator(retraite.order_by('id'), per_page=10)
       page = request.GET.get('page', 1)
       try:
          retraite = paginator.get_page(page)
       except:
          retraite = paginator.get_page(1)

    return render(request, 'retraite/dashboard/dashboard_retraite_index.html', {'retraite': retraite})

# création de la page d'ajout
@login_required
def add_retraite(request):
    if request.method == 'POST':
        retraite_form = RetraiteForm(request.POST, request.FILES)
        if retraite_form.is_valid():
            retraite_form.save()
            messages.success(request, "Ajouté avec succès!")
            return redirect('retraite:retraite_liste')
    else:
        retraite_form = RetraiteForm()

    return render(request, 'retraite/dashboard/add_retraite.html', {'retraite_form': retraite_form})

# création de la modification
@login_required
def edit_retraite(request, nPension):
    retraite = get_object_or_404(Retraite, nPension=nPension)
    old_image = retraite.image.path if retraite.image else None  # Stockez l'ancienne image

    if request.method == "POST":
        if request.POST.get('_method') == 'PUT':
            retraite_form = RetraiteForm(request.POST, request.FILES, instance=retraite)
            if retraite_form.is_valid():
                # Vérifiez si une nouvelle image a été téléchargée
                new_image = request.FILES.get('image')
                if new_image and old_image:
                    # Supprimez l'ancienne image
                    if os.path.exists(old_image):
                        os.remove(old_image)

                retraite_form.save()
                messages.success(request, "Modifié avec success !")
                return redirect('retraite:retraite_liste')
        else:
            retraite_form = RetraiteForm(instance=retraite)

    else:
        retraite_form = RetraiteForm(instance=retraite)
    return render(request, 'retraite/dashboard/add_retraite.html', {'retraite_form': retraite_form, 'retraite': retraite})



# création de la page de visualisation
@login_required
def view_retraite(request, nPension):
    retraite = get_object_or_404(Retraite, nPension=nPension)
    return render(request, 'retraite/dashboard/view_retraite.html', {'retraite': retraite})

# création de la suppression
@login_required
def delete_retraite(request, nPension):
    retraite = get_object_or_404(Retraite, nPension=nPension)
    if request.method == "POST":
        if request.POST.get('_method') == 'DELETE':
            if retraite.image:
                image_path = retraite.image.path
                if(os.path.exists(image_path)):
                    os.remove(image_path)
            retraite.delete()
            messages.success(request, "Enregistrement supprimé !")
            return redirect('retraite:retraite_liste')
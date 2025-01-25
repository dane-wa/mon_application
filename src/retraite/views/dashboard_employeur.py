from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from ..models.Employeur import Employeur
from django.contrib.auth.decorators import login_required
from ..forms.EmployeurForm import EmployeurForm
from django.contrib import messages



@login_required
def dashboard_employeur_index(request):
    # affichage de tout le contenu de préfecture
    employeur = Employeur.objects.all()

    # création du champ de recherche
    if request.method == 'GET':
        name = request.GET.get('recherche')
        if name != '' and name is not None:
            employeur = Employeur.objects.filter(codeEmployeur__contains=name)

        # création de la paggination
        paginator = Paginator(employeur.order_by('id'), per_page=10)
        page = request.GET.get('page', 1)
        try:
            employeur = paginator.get_page(page)
        except:
            employeur = paginator.get_page(1)

    return render(request, 'retraite/dashboard/dashboard_employeur_index.html', {'employeur': employeur})

@login_required
def add_employeur(request):
    if request.method == 'POST':
        employeur_form = EmployeurForm(request.POST)
        if employeur_form.is_valid():
            employeur_form.save()
            messages.success(request, "Ajouté avec succès!")
            return redirect('retraite:employeur_liste')
    else:
        employeur_form = EmployeurForm()

    return render(request, 'retraite/dashboard/add_employeur.html', {'employeur_form': employeur_form})

@login_required
def edit_employeur(request, codeEmployeur):
    employeur = get_object_or_404(Employeur, codeEmployeur=codeEmployeur)
    if request.method == 'POST':
        if request.POST.get('_method') == 'PUT':
            employeur_form = EmployeurForm(request.POST, instance=employeur)

            if employeur_form.is_valid():
                employeur_form.save()
                messages.success(request, "Modifié avec success !")
                return redirect('retraite:employeur_liste')
        else:
            employeur_form = EmployeurForm(instance=employeur)
    else:
        employeur_form = EmployeurForm(instance=employeur)

    return render(request, 'retraite/dashboard/add_employeur.html', {'employeur_form': employeur_form, 'employeur': employeur})

@login_required
def delete_employeur(request, codeEmployeur):
    employeur = get_object_or_404(Employeur, codeEmployeur=codeEmployeur)
    if request.method == 'POST':
        if request.POST.get('_method') == 'DELETE':
            employeur.delete()
            messages.success(request, "Supprimé avec success !")
            return redirect('retraite:employeur_liste')
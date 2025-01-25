from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from ..models.Prefecture import Prefecture
from django.contrib.auth.decorators import login_required
from ..forms.PrefectureForm import PrefectureForm
from django.contrib import messages


@login_required
def dashboard_prefecture_index(request):
    # affichage de tout le contenu de préfecture
    prefecture = Prefecture.objects.all()

    # création du champ de recherche
    if request.method == 'GET':
        name = request.GET.get('recherche')
        if name != '' and name is not None:
            prefecture = Prefecture.objects.filter(codePrefecture__contains=name)

        # création de la paggination
        paginator = Paginator(prefecture.order_by('id'), per_page=10)
        page = request.GET.get('page', 1)
        try:
            prefecture = paginator.get_page(page)
        except:
            prefecture = paginator.get_page(1)

    return render(request, 'retraite/dashboard/dashboard_prefecture_index.html', {'prefecture': prefecture})

@login_required
def add_prefecture(request):
    if request.method == 'POST':
        prefecture_form = PrefectureForm(request.POST)
        if prefecture_form.is_valid():
            prefecture_form.save()
            messages.success(request, "Ajouté avec succès!")
            return redirect('retraite:prefecture_liste')
    else:
        prefecture_form = PrefectureForm()

    return render(request, 'retraite/dashboard/add_prefecture.html', {'prefecture_form': prefecture_form})

@login_required
def edit_prefecture(request, codePrefecture):
    prefecture = get_object_or_404(Prefecture, codePrefecture=codePrefecture)
    if request.method == 'POST':
        if request.POST.get('_method') == 'PUT':
            prefecture_form = PrefectureForm(request.POST, instance=prefecture)

            if prefecture_form.is_valid():
                prefecture_form.save()
                messages.success(request, "Modifié avec success !")
                return redirect('retraite:prefecture_liste')
        else:
            prefecture_form = PrefectureForm(instance=prefecture)
    else:
        prefecture_form = PrefectureForm(instance=prefecture)

    return render(request, 'retraite/dashboard/add_prefecture.html', {'prefecture_form': prefecture_form, 'prefecture': prefecture})

@login_required
def delete_prefecture(request, codePrefecture):
    prefecture = get_object_or_404(Prefecture, codePrefecture=codePrefecture)
    if request.method == 'POST':
        if request.POST.get('_method') == 'DELETE':
            prefecture.delete()
            messages.success(request, "Supprimé avec success !")
            return redirect('retraite:prefecture_liste')
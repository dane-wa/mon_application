from django.urls import path
from .views import (retraite_home, dashboard_retraite, dashboard_prefecture, dashboard_employeur, dashboard_retraite_deces, dashboard_retraite_billetage,
                    dashboard_retraite_virement, etats_retraite, test_retraite)

app_name = 'retraite'

urlpatterns = [
    # Home
    path('', retraite_home.index, name= 'home'),
    path('retraite', retraite_home.retraite, name= 'retraite_home'),
    # dashboard Retraite
    path('retraite_liste', dashboard_retraite.dashboard_retraite_index, name= 'retraite_liste'),
    path('retraite/add', dashboard_retraite.add_retraite, name= 'retraite_add'),
    path('retraite/view/<int:nPension>/', dashboard_retraite.view_retraite, name= 'retraite_view'),
    path('retraite/edit/<int:nPension>/', dashboard_retraite.edit_retraite, name= 'retraite_edit'),
    path('retraite/delete/<int:nPension>/', dashboard_retraite.delete_retraite, name= 'retraite_delete'),
    # dashboard Prefecture
    path('prefecture_liste', dashboard_prefecture.dashboard_prefecture_index, name= 'prefecture_liste'),
    path('prefecture/add', dashboard_prefecture.add_prefecture, name= 'prefecture_add'),
    path('prefecture/edit/<str:codePrefecture>/', dashboard_prefecture.edit_prefecture, name= 'prefecture_edit'),
    path('prefecture/delete/<str:codePrefecture>/', dashboard_prefecture.delete_prefecture, name= 'prefecture_delete'),
    # dashboard Prefecture
    path('employeur_liste', dashboard_employeur.dashboard_employeur_index, name= 'employeur_liste'),
    path('employeur/add', dashboard_employeur.add_employeur, name= 'employeur_add'),
    path('employeur/edit/<str:codeEmployeur>/', dashboard_employeur.edit_employeur, name= 'employeur_edit'),
    path('employeur/delete/<str:codeEmployeur>/', dashboard_employeur.delete_employeur, name= 'employeur_delete'),
    # dashboard RetraiteDecès
    path('retraite_deces_liste', dashboard_retraite_deces.dashboard_retraite_deces_index, name= 'retraite_deces_liste'),
    path('retraite_deces/add', dashboard_retraite_deces.add_retraite_deces, name= 'retraite_deces_add'),
    path('retraite_deces/edit/<int:id>/', dashboard_retraite_deces.edit_retraite_deces, name= 'retraite_deces_edit'),
    path('retraite_deces/delete/<int:id>/', dashboard_retraite_deces.delete_retraite_deces, name= 'retraite_deces_delete'),
    # dashboard RetraiteBilletage
    path('retraite/billetage', dashboard_retraite_billetage.dashboard_retraite_billetage, name= 'retraite_billetage'),
    # dashboard RetraiteVirement
    path('retraite/virement_liste', dashboard_retraite_virement.dashboard_retraite_virement_index, name= 'retraite_virement_liste'),
    path('retraite_virement/add', dashboard_retraite_virement.add_retraite_virement, name= 'retraite_virement_add'),
    path('retraite_virement/edit/<int:id>/', dashboard_retraite_virement.edit_retraite_virement, name= 'retraite_virement_edit'),
    path('retraite_virement/delete/<int:id>/', dashboard_retraite_virement.delete_retraite_viremnt, name= 'retraite_virement_delete'),
    # états
    path('retraite/etats_liste', etats_retraite.retraite_etats, name='retraite_etats'),
    # test
    path('retraite/test', test_retraite.retraite_test, name='retraite_test'),
    ]
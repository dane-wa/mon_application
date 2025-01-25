from django.shortcuts import render
from ..models.RetraiteVirement import RetraiteVirement
from ..models.RetraiteDeces import RetraiteDeces
from django.db.models import OuterRef


def retraite_test(request):
    # Pour récupérer les npension dans retraitedeces
    test = RetraiteDeces.objects.filter(
        retraite_id = OuterRef('id')
    ).values('retraite__nPension')
    return render(request, 'retraite_test.html', {'test':test})
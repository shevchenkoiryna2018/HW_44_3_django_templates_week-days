from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):

    weekday = datetime.now().weekday()

    return render(request, 'index.html', {'weekday': weekday})

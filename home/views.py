from django.shortcuts import render
from tur.models import Dersler
#import random

# Create your views here.
def home_view(request):
	lessons = Dersler.objects.filter(filtre2 = "ana")
		
	context = {
		'lessons':lessons,
	}
	return render(request,'home.html',context)

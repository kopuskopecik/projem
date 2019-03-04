from django.shortcuts import render
from tur.models import Dersler
#import random

# Create your views here.
def home_view(request):
	lessons = Dersler.objects.filter(filtre2__contains = "ana")
	
	genel1 = Dersler.objects.filter(filtre2 = "ana1")
	genel2 = Dersler.objects.filter(filtre2 = "ana2")
	moduller = Dersler.objects.filter(filtre2 = "ana3")
	paketler1 = Dersler.objects.filter(filtre2 = "ana4")
	paketler2 = Dersler.objects.filter(filtre2 = "ana5")
		
	context = {
		'lessons':lessons,
		'genel1':genel1,
		'genel2':genel2,
		'moduller':moduller,
		'paketler1':paketler1,
		'paketler2':paketler2,
	}
	return render(request,'home.html',context)

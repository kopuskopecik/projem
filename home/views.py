from django.shortcuts import render, redirect
from tur.models import Dersler, Baslik
#import random

# Create your views here.
def home_view(request):
	basliklar = Baslik.objects.filter(modul_mu = True)
	
	context = {
		"basliklar": basliklar,
	}
	return render(request,'home.html',context)
	
def view_404(request, exception):
    # make a redirect to homepage
    # you can use the name of url or just the plain link
    return redirect('/')

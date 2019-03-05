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
	
	query = request.GET.get('q')
	if query:
		query = query.replace("I", "ı").replace("İ", "i").lower()
		b = Dersler.objects.filter(headline__icontains = query).distinct()
	#print(query, type(query))
		if b:
			context = {
			'b':b,
			'genel1':genel1,
			'genel2':genel2,
			'moduller':moduller,
			'paketler1':paketler1,
			'paketler2':paketler2,
			}
			return render(request, 'searching.html', context)
		else:
			b = Dersler.objects.filter(content__icontains = query).distinct()
			if b:
				context = {
				'b':b,
				'genel1':genel1,
				'genel2':genel2,
				'moduller':moduller,
				'paketler1':paketler1,
				'paketler2':paketler2,
				}
				return render(request, 'searching.html', context)	
		
	context = {
		'lessons':lessons,
		'genel1':genel1,
		'genel2':genel2,
		'moduller':moduller,
		'paketler1':paketler1,
		'paketler2':paketler2,
	}
	return render(request,'home.html',context)

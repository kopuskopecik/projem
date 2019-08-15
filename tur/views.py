from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, Http404, redirect, HttpResponseRedirect, get_list_or_404
from tur.models import Dersler, Baslik
from .forms import DerslerForm, AramaFormu
from django.contrib import messages

from ingilizce.models import Lesson

# Create your views here.
def tur_index(request):
	basliklar = Baslik.objects.all()
	context = {
		"basliklar": basliklar,
	}
	
	return render(request, 'tur/index.html', context)

def django_index(request):
	baslik = get_object_or_404(Baslik, sıra = 1)
	context = {
		"baslik": baslik,
	}
	
	return render(request, 'tur/baslik_index.html', context)

def tkinter_index(request):
	baslik = get_object_or_404(Baslik, sıra = 2)
	context = {
		"baslik": baslik,
	}
	
	return render(request, 'tur/baslik_index.html', context)

def modul_index(request):
	basliklar = get_list_or_404(Baslik, modul_mu = True)
	context = {
		"basliklar": basliklar,
	}
	
	return render(request, 'tur/modul-index.html', context)
	
def baslik_index(request, slug):	
	
	baslik = get_object_or_404(Baslik, slug = slug)
	
	context = {
		"baslik": baslik,
	}
	
	return render(request, 'tur/baslik_index.html', context)

def tur_detail(request, slug, slug2):

			
	baslik = get_object_or_404(Baslik, slug = slug2)
	lesson = get_object_or_404(Dersler, slug=slug, baslık = baslik)
	lessons = Dersler.objects.filter(baslık = baslik)
	
	session_key = 'viewed_topic_{}'.format(lesson.pk)
	if not request.session.get(session_key, False):
		lesson.views += 1
		lesson.save()
		request.session[session_key] = True
	
	#lessons = Dersler.objects.filter(filtre1 = lesson.filtre1)
	other_lessons = Dersler.objects.exclude(slug = slug).filter(filtre2__contains = "ana").filter(number__gte = lesson.number)[0:6]
	if lesson== Dersler.objects.last():
		next_lesson = get_object_or_404(Dersler, number=1)
	else:
		next_lesson = get_object_or_404(Dersler, number= lesson.number + 1)
	
	if lesson== Dersler.objects.first():
		previous_lesson = get_object_or_404(Dersler, number=Dersler.objects.last().number)
	else:
		previous_lesson = get_object_or_404(Dersler, number= lesson.number - 1)
			
	if lesson.number <= 531:
		if Lesson.objects.filter(number = lesson.number).exists():
			href_lesson = Lesson.objects.get(number = lesson.number)
			
			hreflang = reverse('ingilizce:detail', kwargs={'slug':href_lesson.slug, 'slug2':href_lesson.slug2})
		else:
			hreflang = reverse('ingilizce:index')
	
	else:
		hreflang = reverse('ingilizce:index')
	
	
	context = {
		'hreflang': hreflang,
		'lesson': lesson,
		'lessons': lessons,
		'next_lesson': next_lesson,
		'previous_lesson': previous_lesson,
		'other_lessons': other_lessons,
		'baslik' : baslik,
	}
	return render(request,'tur/yeni-detail.html',context)

def tur_create(request):
	if not request.user.is_authenticated:
		return Http404()
		
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
	
	form = DerslerForm(request.POST or None)
	if form.is_valid():
		lesson=form.save()
		messages.success(request, "Yeni Ders Başarılı Bir Şekilde Oluşturuldu.",extra_tags="mesaj-basarili")
		#return HttpResponseRedirect(kelime.get_absolute_url())
		return redirect('tur:create')
	context = {
		'form':form,
		'genel1':genel1,
		'genel2':genel2,
		'moduller':moduller,
		'paketler1':paketler1,
		'paketler2':paketler2,
	}

	return render(request, 'tur/form.html',context)
	
def tur_update(request, slug, slug2):
	if not request.user.is_authenticated:
		return Http404()
		
	lesson = get_object_or_404(Dersler, slug=slug)
	form = DerslerForm(request.POST or None, instance=lesson)
	if form.is_valid():
		form.save()
		messages.success(request, "Ders Başarılı Bir Şekilde Değiştirildi.")
		return HttpResponseRedirect(lesson.get_absolute_url())
		
	context = {
		'form':form,
		'genel1':genel1,
		'genel2':genel2,
		'moduller':moduller,
		'paketler1':paketler1,
		'paketler2':paketler2,
	}
	return render(request, 'tur/form.html',context)

def tur_delete(request, slug, slug2):
	if not request.user.is_authenticated:
		return Http404()
		
	lesson = get_object_or_404(Dersler, slug=slug)
	lesson.delete()
	lesson.delete_number()
	return redirect("tur:index")
	
def tur_ara(request):
	
	form = AramaFormu(request.GET or None)
	query = request.GET.get('q')
	if query:
		query = query.replace("I", "ı").replace("İ", "i").lower()
		b = Dersler.objects.filter(headline__icontains = query).distinct()
		if b:
			context = {
			'form': form,
			'b':b,
			}
			return render(request, 'form.html', context)
		else:
			b = Dersler.objects.filter(content__icontains = query).distinct()
			if b:
				context = {
				'b':b,
				'form': form,
				}
				return render(request, 'form.html', context)
	context = {
		'form': form,	
	}
	
	return render(request, 'form.html', context)
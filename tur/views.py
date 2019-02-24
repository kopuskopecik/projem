from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render, Http404, redirect, HttpResponseRedirect
from .models import Dersler
from .forms import DerslerForm
from django.contrib import messages

# Create your views here.
def tur_index(request):
	lessons = Dersler.objects.all()
	lesson1 = get_object_or_404(Dersler, number=1)
	
	context = {
		'lessons':lessons,
		'lesson1':lesson1,
	}
	
	return render(request, 'tur/index.html', context)

def tur_detail(request, slug):
	lesson = get_object_or_404(Dersler, slug=slug)
	lessons = Dersler.objects.filter(filtre1 = lesson.filtre1)
	other_lessons = Dersler.objects.exclude(slug = slug).filter(filtre2 = "ana").filter(number__gte = lesson.number)[0:6]
	if lesson== Dersler.objects.last():
		next_lesson = get_object_or_404(Dersler, number=1)
	else:
		next_lesson = get_object_or_404(Dersler, number= lesson.number + 1)
	
	if lesson== Dersler.objects.first():
		previous_lesson = get_object_or_404(Dersler, number=Dersler.objects.last().number)
	else:
		previous_lesson = get_object_or_404(Dersler, number= lesson.number - 1)
	
	
	
	context = {
		'lesson': lesson,
		'lessons': lessons,
		'next_lesson': next_lesson,
		'previous_lesson': previous_lesson,
		'other_lessons': other_lessons,
	}
	return render(request,'tur/detail.html',context)

def tur_create(request):
	if not request.user.is_authenticated:
		return Http404()
		
	form = DerslerForm(request.POST or None)
	if form.is_valid():
		lesson=form.save()
		messages.success(request, "Yeni Ders Başarılı Bir Şekilde Oluşturuldu.",extra_tags="mesaj-basarili")
		#return HttpResponseRedirect(kelime.get_absolute_url())
		return redirect('tur:create')
	context = {
		'form':form,
	}

	return render(request, 'tur/form.html',context)
	
def tur_update(request,slug):
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
	}
	return render(request, 'tur/form.html',context)

def tur_delete(request,slug):
	if not request.user.is_authenticated:
		return Http404()
		
	lesson = get_object_or_404(Dersler, slug=slug)
	lesson.delete()
	lesson.delete_number()
	return redirect("tur:index")

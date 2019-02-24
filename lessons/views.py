from django.shortcuts import get_object_or_404, render, Http404, redirect, HttpResponseRedirect
from .models import Lesson
from .forms import LessonForm
from django.contrib import messages
from django.db.models import Q
# Create your views here.
def lesson_index(request):
	lessons = Lesson.objects.all()
	lesson1 = get_object_or_404(Lesson, number=1)
	
	query = request.GET.get('q')
	if query:
		query = query.replace("I", "ı").replace("İ", "i").lower()
		b = Lesson.objects.filter(
		Q(headline__icontains = query) |
		Q(content__icontains = query)
		).distinct()
	#print(query, type(query))
		if b:
			context = {
			'b':b,
			}
			return render(request, 'lessons/searching.html', context)
	
	context = {
		'lessons':lessons,
		'lesson1':lesson1,
	}
	
	return render(request, 'lessons/index.html', context)
	

def lesson_detail(request, slug):
	lessons = Lesson.objects.all()
	lesson = get_object_or_404(Lesson, slug=slug)
	if lesson== Lesson.objects.last():
		next_lesson = get_object_or_404(Lesson, number=1)
	else:
		next_lesson = get_object_or_404(Lesson, number= lesson.number + 1)
	
	if lesson== Lesson.objects.first():
		previous_lesson = get_object_or_404(Lesson, number=Lesson.objects.last().number)
	else:
		previous_lesson = get_object_or_404(Lesson, number= lesson.number - 1)
	
	
	
	context = {
		'lesson':lesson,
		'lessons':lessons,
		'next_lesson':next_lesson,
		'previous_lesson':previous_lesson,
	}
	return render(request,'lessons/detail.html',context)
	
def lesson_create(request):
	if not request.user.is_authenticated:
		return Http404()
		
	form = LessonForm(request.POST or None)
	if form.is_valid():
		lesson=form.save()
		messages.success(request, "Yeni Ders Başarılı Bir Şekilde Oluşturuldu.",extra_tags="mesaj-basarili")
		#return HttpResponseRedirect(kelime.get_absolute_url())
		return redirect('lessons:create')
	context = {
		'form':form,
	}

	return render(request, 'lessons/form.html',context)
	
def lesson_update(request,slug):
	if not request.user.is_authenticated:
		return Http404()
		
	lesson = get_object_or_404(Lesson, slug=slug)
	form = LessonForm(request.POST or None, instance=lesson)
	if form.is_valid():
		form.save()
		messages.success(request, "Ders Başarılı Bir Şekilde Değiştirildi.")
		return HttpResponseRedirect(lesson.get_absolute_url())
		
	context = {
		'form':form,
	}
	return render(request, 'lessons/form.html',context)

def lesson_delete(request,slug):
	if not request.user.is_authenticated:
		return Http404()
		
	lesson = get_object_or_404(Lesson, slug=slug)
	lesson.delete()
	return redirect("lessons:index")



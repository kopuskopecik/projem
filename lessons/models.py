from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Lesson(models.Model):
	headline = models.CharField(max_length=100)
	content = RichTextField()
	slug = models.SlugField(unique=True, editable=False, max_length=130)
	number = models.PositiveSmallIntegerField()
	publishing_date = models.DateTimeField(verbose_name="yayımlanma_tarihi",auto_now_add=True)
	
	def __str__(self):
		return self.headline
	
	class Meta:
		ordering = ['number']
	
	def get_absolute_url(self):
		return reverse('lessons:detail', kwargs={'slug':self.slug})
	
	def get_create_url(self):
		return reverse('lessons:create')
	
	def get_update_url(self):
		return reverse('lessons:update', kwargs={'slug':self.slug})
	
	def get_delete_url(self):
		return reverse('lessons:delete', kwargs={'slug':self.slug})
	
	def get_unique_slug(self):
		slug = slugify(self.headline.replace("ı","i"))
		unique_slug = slug
		counter = 1
		while Lesson.objects.filter(slug=unique_slug).exists():
			unique_slug = "{}-{}".format(slug, counter)
			counter +=1 
		return unique_slug
		
	def save(self, *args, **kwargs):
		self.slug = self.get_unique_slug()
		return super(Lesson, self).save(*args, **kwargs)

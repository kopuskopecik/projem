from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Dersler(models.Model):
	headline = models.CharField(max_length=100)
	content = RichTextField()
	slug = models.SlugField(unique=True, editable=False, max_length=130)
	number = models.PositiveSmallIntegerField()
	publishing_date = models.DateTimeField(verbose_name="yayımlanma_tarihi",auto_now_add=True)
	updating_date = models.DateTimeField(verbose_name="yayımlanma_tarihi",auto_now=True)
	filtre1 = models.CharField(max_length=100, default = "-")
	filtre2 = models.CharField(max_length=100, default = "-")
	
	def __str__(self):
		return self.headline
	
	class Meta:
		ordering = ['number']
	
	def get_absolute_url(self):
		return reverse('tur:detail', kwargs={'slug':self.slug})
	
	def get_create_url(self):
		return reverse('tur:create')
	
	def get_update_url(self):
		return reverse('tur:update', kwargs={'slug':self.slug})
	
	def get_delete_url(self):
		return reverse('tur:delete', kwargs={'slug':self.slug})
		
	def get_unique_slug(self):
		slug = slugify(self.headline.replace("ı","i"))
		unique_slug = slug
		counter = 1
		while Dersler.objects.filter(slug=unique_slug).exclude(publishing_date = self.publishing_date).exists():
			unique_slug = "{}-{}".format(slug, counter)
			counter +=1 
		return unique_slug
	
	def set_number(self):
		for i in Dersler.objects.filter(number__gte = self.number):
			i.number = i.number + 1
			i.save()
	
	def delete_number(self):
		for i in Dersler.objects.filter(number__gte = self.number):
			print(i)
			i.number = i.number - 1
			i.save()
		
	def save(self, *args, **kwargs):
		self.slug = self.get_unique_slug()
		if Dersler.objects.filter(publishing_date = self.publishing_date).exists():
			pass
		else:
			self.set_number()
		
		return super(Dersler, self).save(*args, **kwargs)
	

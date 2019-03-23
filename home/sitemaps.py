from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from tur.models import Dersler

class DerslerSitemap(Sitemap):
	def items(self):
		return Dersler.objects.all()

#class StaticViewSitemap(Sitemap):
	
#	def items(self):
#		return ['hakkimizda:hak']
	
#	def locations(self, item):
#		return reverse(item)
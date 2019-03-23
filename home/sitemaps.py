from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from tur.models import Dersler



class DerslerSitemap(Sitemap):
	protocol = "https"

	def items(self):
		return Dersler.objects.all()
		
	def lastmod(self, obj):
		return obj.updating_date


class StaticViewSitemap(Sitemap):
	protocol = "https"
	
	def items(self):
		return ['hakkimizda:hak', 'tur:index']
	
	def location(self, item):
		return reverse(item)

class StaticDerslerViewSitemap(Sitemap):
	protocol = "https"
	
	def items(self):		
		return Dersler.objects.filter(filtre2__contains = "ana")
		
	def location(self, item):
		return "/" + item.slug2+ "/"
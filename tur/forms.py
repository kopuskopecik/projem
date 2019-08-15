from django import forms
from .models import Dersler

class DerslerForm(forms.ModelForm):
	
	class Meta:
		model = Dersler
		fields = [
			'headline',
			'content',
			'number',			
			]

class AramaFormu(forms.Form):
	q = forms.CharField(label = "Ara", max_length=100)
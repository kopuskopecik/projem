from django import forms
from .models import Iletisim

class IletisimForm(forms.ModelForm):
	
	class Meta:
		model = Iletisim
		fields = [
			'isim',
			'email',
			'content',			
			]
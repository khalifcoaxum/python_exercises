from NLP.models import User
from django.forms import ModelForm

Class UserForm (ModelForm):
	class Meta:
		model = User
		fields = ('first_name','last_name','date_of_birth','age','title')
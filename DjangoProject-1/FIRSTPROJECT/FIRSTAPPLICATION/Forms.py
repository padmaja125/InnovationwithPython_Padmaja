from django import forms
from .models import Name, Id, Address
class FeedbackForm(forms.Form):
	Name = forms.CharField(label='Name', max_length=20)
	Email =forms.EmailField(label ='Email',max_length=20)


class Name_Form(forms.ModelForm):
	class Meta:
		model = Name
		fields = "__all__"

class Id_Form(forms.ModelForm):
	class Meta:
		model = Id
		fields = "__all__"

class Address_Form(forms.ModelForm):
	class Meta:
		model = Address
		fields = "__all__"
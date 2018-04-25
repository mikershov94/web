from django import forms

class AskForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text']


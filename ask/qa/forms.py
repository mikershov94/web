from django import forms
from qa.models import Question, Answer

class AskForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title']
	text = forms.CharField(widget=forms.TextArea)

	def clean(self):
		if is_spam(self.cleaned_data):
			raise forms.ValidationError(u'This is spam', code='spam') 

class AnswerForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextArea)
    question = forms.CharField()

    def clean(self):
		if is_spam(self.cleaned_data):
			raise forms.ValidationError(u'This is spam', code='spam') 

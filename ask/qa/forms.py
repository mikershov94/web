from django import forms
from qa.models import Question, Answer

class AskForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text']

	def clean(self):
		if forms.is_spam(self.cleaned_data):
			raise forms.ValidationError(u'This is spam', code='spam') 

class AnswerForm(forms.ModelForm):
    class Meta:
    	model = Answer
    	fields = ['text', 'question']

    def clean(self):
    	if forms.is_spam(self.cleaned_data):
    		raise forms.ValidationError(u'This is spam', code='spam') 

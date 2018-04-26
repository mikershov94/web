from django import forms
from qa.models import Question, Answer

def is_ask(cleaned_data):
	text = cleaned_data['text']
	if text[len(text)-1] == '?':
		return True
	else:
		return False

def is_answer(cleaned_data):
	text = cleaned_data['text']
	if text[len(text)-1] != '?':
		return True
	else:
		return False

class AskForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text']

	def clean(self):
		if not is_ask(self.cleaned_data):
			raise forms.ValidationError(u'This is not ask', code='12') 

class AnswerForm(forms.ModelForm):
    class Meta:
    	model = Answer
    	fields = ['text', 'question']

    def clean(self):
    	if not is_answer(self.cleaned_data):
    		raise forms.ValidationError(u'This is not answer', code='12') 

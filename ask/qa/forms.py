from django import forms

class AskForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title']
	text = forms.CharField(widget=forms.TextArea)

	def clean(self):
		if is_spam(self.cleaned_data):
			raise forms.ValidationError(u'Сообщение похоже на спам', code='spam') 

class AnswerForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextArea)
    question = forms.CharField()

    def clean(self):
		if is_spam(self.cleaned_data):
			raise forms.ValidationError(u'Сообщение похоже на спам', code='spam') 

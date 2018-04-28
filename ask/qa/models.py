from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class QuestionManager(models.Manager):
	def new(self):
		return self.order_by('-added_at')

	def popular(self):
		return self.order_by('-rating')

class Question(models.Model):
	objects = QuestionManager()
	title = models.CharField(max_length=50)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	#author = models.ForeignKey(User)
	likes = models.ManyToManyField(User, related_name='likes_set')

	def __unicode__(self):
		return self.title

	def get_url(self):
		return reverse('question_details', kwargs={'id': self.id})

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question)
	#author = models.ForeignKey(User)

	def __unicode__(self):
		return self.title	
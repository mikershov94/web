from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from qa.models import Question, Answer

# Create your views here.
def test(request, *args, **kwargs):
	return HttpResponse('OK')
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from qa.models import Question, Answer

# Create your views here.
def test(request, *args, **kwargs):
	return HttpResponse('OK')

def paginate(request, queryset):
	try:
		limit = int(request.GET.get('limit', 10))
	except ValueError:
		limit = 10
	if limit > 100:
		limit = 10 
	paginator = Paginator(queryset, limit) 
	return paginator
	
def last_page(request, paginator):
	try:
		numpage = int(request.GET.get('page', 1)) 
	except ValueError:
		raise Http404
	try:
		page = paginator.page(numpage)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	return page


def question_list_new(request):
	questions = Question.objects.new()
	paginator = paginate(request, questions)
	paginator.baseurl = '/?page='
	page = last_page(request, paginator)
	return render(request, 'templates/news.html',
		{
			'questions': page.object_list,
			'paginator': paginator,
			'page': page,
		})

def question_popular(request):
	questions = Question.objects.popular()
	paginator = paginate(request, questions)
	paginator.baseurl = '/popular/?page='
	page = last_page(request, paginator)
	return render(request, 'templates/popular.html',
		{
			'questions': page.object_list,
			'paginator': paginator,
			'page': page,
		})

def question_details(request, question_id):
	try:
		question = Question.objects.get(id=question_id)
	except Question.DoesNotExist:
		raise Http404
	try:
		answers = question.answers.all()
	except Answer.DoesNotExist:
		answers = None
	return render(request, 'templates/question_details.html',
		{
		'question': question,
		'answers': answers,
		})

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator
from qa.models import Question, Answer
from qa.helper import do_login
from qa.forms import AskForm, AnswerForm, SignupForm
from django.core.urlresolvers import reverse



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
	return render(request, 'news.html',
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
		answers = Answer.objects.filter(question = question)
	except Answer.DoesNotExist:
		answers = None
	return render(request, 'question_details.html',
		{
		'question': question,
		'answers': answers,
		})

def question_add(request):
	if request.method == 'POST':
		form = AskForm(request.POST)
		form._user = request.user
		if form.is_valid():
			question = form.save()
			return HttpResponseRedirect(reverse(question_details, args=[question.id]))
	else:
		form = AskForm()
	return render(request, 'ask.html',
		{
			'form': form,
		})

def answer_add(request, question_id):
	question = Question.objects.get(id=question_id)
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		form._user = request.user
		if form.is_valid():
			answer = form.save()
			url = question.get_url()
			return HttpResponseRedirect(url)
	else:
		form = AnswerForm()
	return render(request, 'question_details.html',
		{
			'form': form,
		})

def user_add(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			login = request.POST.get('username')
			password = request.POST.get('password')
			user = form.save()
			url = request.POST.get('continue', '/')
			sessid = do_login(login, password)
			if sessid:
				response = HttpResponseRedirect(url)
				response.set_cookie('sessionid', sessid)
				return response
	else:
		form = SignupForm()
	return render(request, 'registration.html',
		{
			'form': form,
		})

def login(request):
	error = ''
	if request.method == 'POST':
		login = request.POST.get('username')
		password = request.POST.get('password')
		url = request.POST.get('continue', '/')
		sessid = do_login(login, password)
		if sessid:
			response = HttpResponseRedirect(url)
			response.set_cookie('sessionid', sessid)
			return response
		else:
			error = 'Bad login or password'
	else:
		form = LoginForm()
	return render(request, 'login.html',
		{
		'form': form,
		'error': error,
		})

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from qa.models import Question, Answer

# Create your views here.
#def test(request, *args, **kwargs):
	#return HttpResponse('OK')
def paginate(request, queryset):
	try:
		limit = int(request.GET.get('limit', 10)) #достаем limit из URL. Он всегда целочисленный. По умолчанию 10.
	except ValueError:
		limit = 10
	if limit > 100:
		limit = 10 #limit не должен быть больше 100
	try:
		page = int(request.GET.get('page', 1)) #номер страницы всегда целочислен. Достаем из URL
	except ValueError:
		raise Http404
	paginator = Paginator(queryset, limit) #создаем объект paginator
	try:
		page = paginator.page(page) #устанавливаем запрашиваемую страницу
	except EmptyPage:
		page = paginator.page(paginator.num_pages) #если ее нет, то отправляем последнюю
	return page


def question_list_new(request):
	questions = Question.objects.new()
	page = request.GET.get('page', 1)
	paginator = paginate(questions, 10)
	page = paginator.page(page)
	return render(request, 'qa/index.html',
		{
			'questions': page.object_list,
			'paginator': paginator,
			'page': page,
		})

def question_popular(request):
	questions = Question.objects.popular()
	page = request.GET.get('page', 1)
	paginator = paginate(questions, 10)
	page = paginator.page(page)
	return render(request, 'qa/popular.html',
		{
			'questions': page.object_list,
			'paginator': paginator,
			'page': page,
		})

def question_details(request, slug):
	question = get_object_or_404(Question, slug=slug)
	try:
		answers = question.answers.all()
	except Answer.DoesNotExist:
		answers = None
	return render(request, 'qa/question_details.html'
		{
		'question': question,
		'answers': answers,
		})

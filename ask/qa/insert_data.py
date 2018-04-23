from qa.models import Question, Answer
from django.contrib.auth.models import User, UserManager

u1 = UserManager.create_user(John, email = 'john@qa.com', password = '')
u2 = UserManager.create_user(Bill, email = 'bill@qa.com', password = '')
u3 = UserManager.create_user(Jane, email = 'jane@qa.com', password = '')
u4 = UserManager.create_user(Helen, email = 'helen@qa.com', password = '')
u5 = UserManager.create_user(Patrick, email = 'pat@qa.com', password = '')

q1 = Question.objects.create(
		title = 'Computer',
		text = 'How connect Internet?',
		rating = 3,
		author = u1,
	)
q2 = Question.objects.create(
		title = 'Computer',
		text = 'How connect Internet?',
		rating = 3,
		author = u1,
	)
q3 = Question.objects.create(
		title = 'Computer',
		text = 'How connect Internet?',
		rating = 3,
		author = u1,
	)
q4 = Question.objects.create(
		title = 'Computer',
		text = 'How connect Internet?',
		rating = 3,
		author = u1,
	)
q5 = Question.objects.create(
		title = 'Computer',
		text = 'How connect Internet?',
		rating = 3,
		author = u1,
	)
q6 = Question.objects.create(
		title = 'Computer',
		text = 'How connect Internet?',
		rating = 3,
		author = u1,
	)
q7 = Question.objects.create(
		title = 'Computer',
		text = 'How connect Internet?',
		rating = 3,
		author = u1,
	)
q8 = Question.objects.create(
		title = 'Computer',
		text = 'How connect Internet?',
		rating = 3,
		author = u1,
	)
q9 = Question.objects.create(
		title = 'Computer',
		text = 'How connect Internet?',
		rating = 3,
		author = u1,
	)
q10 = Question.objects.create(
		title = 'Computer',
		text = 'How connect Internet?',
		rating = 3,
		author = u1,
	)
q11 = Question.objects.create(
		title = 'Computer',
		text = 'How connect Internet?',
		rating = 3,
		author = u1,
	)
q12 = Question.objects.create(
		title = 'Computer',
		text = 'How connect Internet?',
		rating = 3,
		author = u1,
	)
q13 = Question.objects.create(
		title = 'Computer',
		text = 'How connect Internet?',
		rating = 3,
		author = u1,
	)
q14 = Question.objects.create(
		title = 'Computer',
		text = 'How connect Internet?',
		rating = 3,
		author = u1,
	)
q15 = Question.objects.create(
		title = 'Computer',
		text = 'How connect Internet?',
		rating = 3,
		author = u1,
	)
q16 = Question.objects.create(
		title = 'Computer',
		text = 'How connect Internet?',
		rating = 3,
		author = u1,
	)
q17 = Question.objects.create(
		title = 'Computer',
		text = 'How connect Internet?',
		rating = 3,
		author = u1,
	)
q18 = Question.objects.create(
		title = 'Computer',
		text = 'How connect Internet?',
		rating = 3,
		author = u1,
	)
q19 = Question.objects.create(
		title = 'Computer',
		text = 'How connect Internet?',
		rating = 3,
		author = u1,
	)
q20 = Question.objects.create(
		title = 'Computer',
		text = 'How connect Internet?',
		rating = 3,
		author = u1,
	)
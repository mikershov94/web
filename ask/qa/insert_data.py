from qa.models import Question, Answer
from django.contrib.auth.models import User, UserManager

u1 = UserManager.create_user(John, email = 'john@qa.com', password = '')
u2 = UserManager.create_user(Bill, email = 'bill@qa.com', password = '')
u3 = UserManager.create_user(Jane, email = 'jane@qa.com', password = '')
u4 = UserManager.create_user(Helen, email = 'helen@qa.com', password = '')
u5 = UserManager.create_user(Patrick, email = 'pat@qa.com', password = '')

q1 = Question.objects.create(
		title = ,
		text = ,

	)
q2
q3
q4
q5
q6
q7
q8
q9
q10
q11
q12
q13
q14
q15
q16
q17
q18
q19
q20
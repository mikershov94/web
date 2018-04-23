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
		title = 'TV',
		text = 'How move TV?',
		rating = 3,
		author = u1,
	)
q3 = Question.objects.create(
		title = 'Sun',
		text = 'Where wake up sun?',
		rating = 3,
		author = u1,
	)
q4 = Question.objects.create(
		title = 'Water',
		text = 'How clean water?',
		rating = 3,
		author = u1,
	)
q5 = Question.objects.create(
		title = 'Clip',
		text = 'How create clip?',
		rating = 3,
		author = u1,
	)
q6 = Question.objects.create(
		title = 'YouTube',
		text = 'How log up to YouTube?',
		rating = 3,
		author = u1,
	)
q7 = Question.objects.create(
		title = 'Desert',
		text = 'Do you want desert?',
		rating = 3,
		author = u1,
	)
q8 = Question.objects.create(
		title = 'Video',
		text = 'How record video?',
		rating = 3,
		author = u1,
	)
q9 = Question.objects.create(
		title = 'Club',
		text = 'How input to club?',
		rating = 3,
		author = u1,
	)
q10 = Question.objects.create(
		title = 'Sound',
		text = 'How create cool sound?',
		rating = 3,
		author = u1,
	)
q11 = Question.objects.create(
		title = 'Games',
		text = 'Do you like videogames?',
		rating = 3,
		author = u1,
	)
q12 = Question.objects.create(
		title = 'Films',
		text = 'Do you like watch films?',
		rating = 3,
		author = u1,
	)
q13 = Question.objects.create(
		title = 'What films',
		text = 'What films you like??',
		rating = 3,
		author = u1,
	)
q14 = Question.objects.create(
		title = 'Guitar',
		text = 'How play on guitar?',
		rating = 3,
		author = u1,
	)
q15 = Question.objects.create(
		title = 'Accords',
		text = 'Accords - what is it?',
		rating = 3,
		author = u1,
	)
q16 = Question.objects.create(
		title = 'MIDI',
		text = 'How connect midi-keyboard to computer?',
		rating = 3,
		author = u1,
	)
q17 = Question.objects.create(
		title = 'Nadya Dorofeeva',
		text = 'Do you like Nadya Dorofeeva?',
		rating = 3,
		author = u1,
	)
q18 = Question.objects.create(
		title = 'Programmist',
		text = 'You programmist?',
		rating = 3,
		author = u1,
	)
q19 = Question.objects.create(
		title = 'Your names',
		text = 'What is your names?',
		rating = 3,
		author = u1,
	)
q20 = Question.objects.create(
		title = 'Tickets',
		text = 'Where buy tickets to concert?',
		rating = 3,
		author = u1,
	)
from django.contrib.auth.models import User
from qa.models import Session
import random

def do_login(login, password):
	try:
		user = User.objects.get(username=login)
	except User.DoesNotExist:
		return None

	if user.password != password:
		return None

	session = Session()
	session.session_key = random.randint()
	session.user = user
	session.expire_date = datetime.now()+timedelta(days=5)
	session.save()
	return session.session_key
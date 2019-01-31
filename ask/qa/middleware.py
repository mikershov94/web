from django.utils.deprecation import MiddlewareMixin
from django.contrib.sessions.models import Session
from datetime import datetime

class CheckSessionMiddleware(MiddlewareMixin):
	def process_request(self, request):
		try:
			sessid = request.COOKIES.get('sessid')
			session = Session.objects.get(
				key = sessid,
				expire_date__gt = datetime.now(),
				)
			request.session = session
			request.user = session.user
		except Session.DoesNotExist:
			request.session = None
			request.user = None

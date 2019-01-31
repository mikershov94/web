from django.utils.deprecation import MiddlewareMixin
from django.contrib.sessions.models import Session

class CheckSessionMiddleware(MiddlewareMixin):
	def process_request(self, request):
		try:
			sessid = request.COOKIE.get('sessid')
			session = Session.objects.get(
				key = sessid,
				expires__gt = datetime.now(),
				)
			request.session = session
			request.user = session.user
		except Session.DoesNotExist:
			request.session = None
			request.user = None

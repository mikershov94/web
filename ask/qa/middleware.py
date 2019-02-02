from django.utils.deprecation import MiddlewareMixin
from qa.models import Session
from datetime import datetime
from django.utils import timezone

class CheckSessionMiddleware(MiddlewareMixin):
	def process_request(self, request):
		try:
			sessid = request.COOKIES.get('sessid')
			session = Session.objects.get(
				session_key = sessid,
				expire_date__gt = datetime.now(tz=timezone.utc),
				)
			request.session = session
			request.user = session.user
		except Session.DoesNotExist:
			request.session = None
			request.user = None

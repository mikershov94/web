from django.conf.urls import url
from qa.views import test

urlpatterns = [
	url(r'^$', question_list_new),
	url(r'^login/$', test),
	url(r'^signup/$', test),
	url(r'^question/(\d+)/$', question_details),
	url(r'^ask/$', test),
	url(r'^popular/$', question_popular),
	url(r'^new/$', test),
]
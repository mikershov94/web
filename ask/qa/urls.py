from django.conf.urls import url
from qa.views import test, question_list_new, question_details, question_popular, question_add

urlpatterns = [
	url(r'^$', question_list_new),
	url(r'^login/$', test),
	url(r'^signup/$', test),
	url(r'^question/(?P<question_id>\d+)/$', question_details),
	url(r'^ask/$', question_add),
	url(r'^popular/', question_popular),
	url(r'^new/$', test),
]
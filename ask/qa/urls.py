from django.conf.urls import url

urlpatterns = [
	url(r'^$', 'qa.views.question_list_new', name='question_list_new'),
	url(r'^login/$', test),
	url(r'^signup/$', test),
	url(r'^question/(\d+)/$', 'qa.views.question_details', name='question_details'),
	url(r'^ask/$', test),
	url(r'^popular/$', 'qa.views.question_popular', name='question_popular'),
	url(r'^new/$', test),
]
from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'chat.views.index'),
	(r'^connected$', 'chat.views.connected'),
	(r'^disconnected$', 'chat.views.disconnected'),
	(r'^message$', 'chat.views.message'),
)


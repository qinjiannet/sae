#-*- coding: UTF-8 -*-
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response,redirect
from django.http import HttpResponse,Http404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect,csrf_exempt
import json
from sae import channel

@login_required
def index(request):
	url = ''
	name = 'test_channel'
	duration = 10
	url = channel.create_channel(name, duration)
	if request.method == 'POST':
		content = request.POST.get('content','')
		channel.send_message(name, str(content))
	return render_to_response('chat/index.html', {'url':url }, context_instance=RequestContext(request))

@csrf_exempt
def connected(request):
	res = request.POST
	print res
	return HttpResponse(json.dumps(res), mimetype="text/plain")
@csrf_exempt
def disconnected(request):
	res = request.POST
	print res
	return HttpResponse(json.dumps(res), mimetype="text/plain")
@csrf_exempt
def message(request):
	res = request.POST
	print res
	return HttpResponse(json.dumps(res), mimetype="text/plain")

from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
import os

def home(request):	
	current_date = datetime.datetime.now()
	return render_to_response('homepage.html', locals())

def ban_pick(request):
	os.environ['TZ'] = 'US/Eastern'
	current_date = datetime.datetime.now()
	return render_to_response('homepage.html', locals())
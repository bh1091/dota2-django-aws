from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def home(request):
	current_date = datetime.datetime.now()
	return render_to_response('current_date.html', locals())

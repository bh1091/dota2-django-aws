from django.shortcuts import render_to_response
import os
import urllib


def rank(request):
	# module_dir = os.path.dirname(__file__)  # get current directory
	# file_path = os.path.join(module_dir, 'apr.txt')
	# apr_file = open('http://s3.amazonaws.com/match-history/apr.txt','r')

	opener = urllib.URLopener()
	apr_file = opener.open('http://s3.amazonaws.com/match-history/apr.txt')
	aprs = apr_file.readlines()

	hero_list = []

	for apr in aprs:
		data = apr.split()
		hero_id = int(data[0])+1
		rate = "{0:.4f}".format(float(data[1]))
		rate = float(rate)*100
		apr_tuple = (hero_id, rate)
		if rate != 0.0:				
			hero_list.append(apr_tuple)

	hero_list.sort(key=lambda tup: -tup[1])

	return render_to_response('rank.html', locals())

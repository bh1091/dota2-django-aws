from django.shortcuts import render_to_response
import os
import urllib


def rank(request):
	# module_dir = os.path.dirname(__file__)  # get current directory
	# file_path = os.path.join(module_dir, 'apr.txt')
	# apr_file = open('http://s3.amazonaws.com/match-history/apr.txt','r')

	opener = urllib.URLopener()
	apr_file_0 = opener.open('http://s3.amazonaws.com/match-history/output/part-00000')
	aprs_0 = apr_file_0.readlines()
	apr_file_1 = opener.open('http://s3.amazonaws.com/match-history/output/part-00001')
	aprs_1 = apr_file_1.readlines()
	apr_file_2 = opener.open('http://s3.amazonaws.com/match-history/output/part-00002')
	aprs_2 = apr_file_2.readlines()

	aprs = []
	aprs.extend(aprs_0)
	aprs.extend(aprs_1)
	aprs.extend(aprs_2)
	hero_list = []

	app_sum = 0
	for apr in aprs:
		app_sum = app_sum + int(apr.split()[1])

	app_sum = float(app_sum/10)

	for apr in aprs:
		data = apr.split()
		hero_id = int(data[0])+1
		# rate = "{0:.4f}".format(float(data[1]))
		# rate = float(rate)*100
		rate = "{0:.4f}".format(float(data[1])/app_sum)
		rate = float(rate)*100
		apr_tuple = (hero_id, rate)
		if rate != 0.0:				
			hero_list.append(apr_tuple)

	hero_list.sort(key=lambda tup: -tup[1])

	return render_to_response('rank.html', locals())

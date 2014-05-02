from django.shortcuts import render_to_response
from models import News
from util import *

# Create your views here.
def news(request):
	all_news = News.objects.order_by('-post_date')
	all_page_news = []
	for news in all_news:
		all_page_news.append(db_to_obj(news))
	return render_to_response('news.html', locals())


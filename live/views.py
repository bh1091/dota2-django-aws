from django.shortcuts import render
import urllib2,json


class LiveInfo(object):
	def __init__(self,info):
		self.pic = info[0]
		self.url = info[1]
		self.name = info[2]
		self.display = info[3]
		self.viewers = info[4]
	def __repr__(self):
		return 'LiveInfo Object pic : %s, url : %s, name: %s, display_name: %s, viewers: %s' %(self.pic,self.url,self.name,self.display,self.viewers)
# Create your views here.

def present_live(request):
	streamers = urllib2.urlopen("https://api.twitch.tv/kraken/streams?game=Dota%202&embeddable=true&limit=10")
	streamers_data = json.loads(streamers.readlines()[0])
	infolist = [[stream['preview']['medium'],stream['channel']['url'],stream['channel']['name'],stream['channel']['display_name'],stream['viewers']] for stream in streamers_data['streams']]
	lives = []
	for  info in infolist:
		lives.append(LiveInfo(info))
	return render(request,'live.html',{'lives':lives})

def watch(request,name):
	return render(request,'watch.html',{'name':name})
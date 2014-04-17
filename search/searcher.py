import requests
import json

class player_searcher:
	def __init__(self):
		pass

	def get_steamid_by_name(self, name):
		url = 'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=D8023851199312FC130D5F896A60BD84&vanityurl=' + str(name)
		try:
			resp = requests.get(url)
			content = json.loads(resp.content)
			steamid = content['response']['steamid']
			return str(steamid)
		except Exception, e:
			print 'error when getting steamid : ' + str(e)

	def get_player_by_steamid(self, steamid):
		url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=D8023851199312FC130D5F896A60BD84&steamids=' + str(steamid)
		try:
			resp = requests.get(url)
			content = json.loads(resp.content)
			player = content['response']['players'][0]
			return player
		except Exception, e:
			print 'error when getting player : ' + str(e)

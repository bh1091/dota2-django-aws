import requests
import json

class match_info(object):
	def __init__(self, match_id):
		self.match_id = match_id
		self.players = []
		self.heros = []

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

	def get_match_by_steamid(self, steamid):
		url = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v001/?key=D8023851199312FC130D5F896A60BD84&account_id=' + str(steamid)
		try:
			resp = requests.get(url)
			content = json.loads(resp.content)
			match_list = content['result']['matches']
			match_list = match_list[:10]
			match_list_10 = []
			for match in match_list:
				match_tmp = match_info(match['match_id'])
				match_list_10.append(match_tmp)
			return match_list_10
		except Exception, e:
			print 'error when getting matches : ' + str(e)
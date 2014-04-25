import requests
import json

def get_steamid_by_name(name):
	url = 'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=D8023851199312FC130D5F896A60BD84&vanityurl=' + str(name)
	try:
		resp = requests.get(url)
		content = json.loads(resp.content)
		steamid = content['response']['steamid']
		return str(steamid)
	except Exception, e:
		print 'error when getting steamid : ' + str(e)

def get_player_by_steamid(steamid):
	url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=D8023851199312FC130D5F896A60BD84&steamids=' + str(steamid)
	try:
		resp = requests.get(url)
		content = json.loads(resp.content)
		player = content['response']['players'][0]
		return player
	except Exception, e:
		print 'error when getting player : ' + str(e)

def get_match_by_steamid(steamid):
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

def get_match_detail(match_id):
	url = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v001/?key=D8023851199312FC130D5F896A60BD84&match_id=' + str(match_id)
	match_detail = match_info(match_id)
	try:
		resp = requests.get(url)
		content = json.loads(resp.content)
		players = content['result']['players']
		for player in players:
			match_detail.players.append(player['account_id'])
			match_detail.heros.append(player['hero_id'])
			if int(player['player_slot']) < 5:
				match_detail.radiant_hero.append(player['hero_id'])
			else:
				match_detail.dire_hero.append(player['hero_id'])
			if content['result']['radiant_win']:
				match_detail.winner = 'Radiant'
			else:
				match_detail.winner = 'Dire'
	except Exception, e:
		print 'error when getting match_detail : ' + str(e)
	return match_detail
			

class match_info(object):
	def __init__(self, match_id):
		self.match_id = match_id
		self.players = []
		self.heros = []
		self.radiant_hero = []
		self.dire_hero = []
		self.winner = ''

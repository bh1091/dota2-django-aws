import json
import os.path
BASE = os.path.dirname(os.path.abspath(__file__))

def generate_image_resource(hero_list, suffix='.png'):
	url_list = []
	hero_id_list = hero_list.split()
	for hero_id in hero_id_list:
		url_list.append(get_hero_image_by_id(hero_id, suffix))
	return url_list

def get_hero_image_by_id(hero_id, suffix='.png'):
	base_url = '/static/img/potrait/'
	# hero_name = get_hero_name_by_id(hero_id)
	if hero_id is not None:
		return base_url + str(hero_id) + suffix
	else:
		return ''

def get_hero_name_by_id(hero_id):
	json_file = open(os.path.join(BASE,'heroes.txt'),'r')
	hero_list = json.loads(json_file.read())['result']['heroes']
	hero_id = int(hero_id)
	if hero_id > 0:
		return hero_list[hero_id-1]['name']
	else:
		return None

def generate_option_list(radiant_pick, radiant_ban, dire_pick, dire_ban):
	option_list = []
	for i in range(104):
		option_list.append(str(i+1))
	
	radiant_pick = radiant_pick.split()	
	radiant_ban = radiant_ban.split()
	dire_pick = dire_pick.split()
	dire_ban = dire_ban.split()

	option_list = [x for x in option_list if x not in radiant_pick]
	option_list = [x for x in option_list if x not in dire_pick]
	option_list = [x for x in option_list if x not in radiant_ban]
	option_list = [x for x in option_list if x not in dire_ban]
	# url_list = generate_image_resource(option_list[1:-1].replace(',',''))
	return option_list
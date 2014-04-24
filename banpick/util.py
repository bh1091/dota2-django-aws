import json
import os.path
BASE = os.path.dirname(os.path.abspath(__file__))

def generate_image_resource(hero_list, suffix='_sb.png'):
	url_list = []
	hero_id_list = hero_list.split()
	for hero_id in hero_id_list:
		url_list.append(get_hero_image_by_id(hero_id, suffix))
	return url_list

def get_hero_image_by_id(hero_id, suffix='_sb.png'):
	base_url = 'http://cdn.dota2.com/apps/dota2/images/heroes/'
	hero_name = get_hero_name_by_id(hero_id)
	if hero_name is not None:
		return base_url + str(hero_name).replace('npc_dota_hero_','') + suffix
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
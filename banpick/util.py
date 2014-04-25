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
	# option_list = []
	# for i in range(104):
	# 	option_list.append(str(i+1))

	strength_list = '2 7 14 16 18 19 23 28 29 38 42 49 51 54 57 59 60 65 69 71 73 77 78 81 83 85 91 96 97 98 99 100 102 103 104 107 110 '
	agility_list = '1 4 6 8 9 10 11 12 15 20 32 35 40 41 44 46 47 48 56 61 62 63 67 70 72 80 82 88 89 93 94 95 106 109 '
	intell_list = '3 5 13 17 21 22 25 26 27 30 31 33 34 36 37 39 43 45 50 52 53 55 58 64 66 68 74 75 76 79 84 86 87 90 92 101 '
	
	# option_list = strength_list + agility_list + intell_list
	# option_list = option_list.split()

	strength_list = strength_list.split()
	agility_list = agility_list.split()
	intell_list = intell_list.split()

	radiant_pick = radiant_pick.split()	
	radiant_ban = radiant_ban.split()
	dire_pick = dire_pick.split()
	dire_ban = dire_ban.split()

	strength_list = [x for x in strength_list if x not in radiant_pick]
	strength_list = [x for x in strength_list if x not in dire_pick]
	strength_list = [x for x in strength_list if x not in radiant_ban]
	strength_list = [x for x in strength_list if x not in dire_ban]

	agility_list = [x for x in agility_list if x not in radiant_pick]
	agility_list = [x for x in agility_list if x not in dire_pick]
	agility_list = [x for x in agility_list if x not in radiant_ban]
	agility_list = [x for x in agility_list if x not in dire_ban]

	intell_list = [x for x in intell_list if x not in radiant_pick]
	intell_list = [x for x in intell_list if x not in dire_pick]
	intell_list = [x for x in intell_list if x not in radiant_ban]
	intell_list = [x for x in intell_list if x not in dire_ban]

	option_list = [strength_list,agility_list,intell_list]

	# option_list = [x for x in option_list if x not in radiant_pick]
	# option_list = [x for x in option_list if x not in dire_pick]
	# option_list = [x for x in option_list if x not in radiant_ban]
	# option_list = [x for x in option_list if x not in dire_ban]
	# url_list = generate_image_resource(option_list[1:-1].replace(',',''))
	return option_list
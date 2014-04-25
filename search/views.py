from django.http import HttpResponse
from django.shortcuts import render_to_response
from searcher import *
from searcher import match_info

# Create your views here.
def search(request):
	if 'steam_id' in request.GET and request.GET['steam_id']:
		steam_id = request.GET['steam_id']		
		player = get_player_by_steamid(steam_id)
		player_name = player['personaname']
		player_avatar = player['avatarmedium']
		match_list_10 = get_match_by_steamid(steam_id)
		match_number = len(match_list_10)
		match_detail_list = []
		for match in match_list_10:
			match_detail_list.append(get_match_detail(match.match_id))

	return render_to_response('search_form.html', locals())
from django.http import HttpResponse
from django.shortcuts import render_to_response
from searcher import player_searcher

# Create your views here.
def search(request):
	if 'steam_id' in request.GET and request.GET['steam_id']:
		steam_id = request.GET['steam_id']
		user_searcher = player_searcher()
		player = user_searcher.get_player_by_steamid(steam_id)
		player_name = player['personaname']
		player_avatar = player['avatarmedium']
		match_list_10 = user_searcher.get_match_by_steamid(steam_id)
		match_number = len(match_list_10)

	return render_to_response('search_form.html', locals())
from django.shortcuts import render_to_response
from analysiser import analysis_winrate
from util import *

# Create your views here.
def banpick(request):
	# initiate	
	banpick_phase = 0
	banpick_side = ''
	ban_or_pick = ''
	radiant_ban = ''
	radiant_pick = ''
	dire_ban = ''
	dire_pick = ''
	change_side = [1,2,3,4,5,7,9,10,11,13,14,15,16,17,18,19,20]
	ban_phase = [1,2,3,4,9,10,11,12,17,18]
	pick_phase = [5,6,7,8,13,14,15,16,19,20]
	# process form
	if 'phase' in request.GET:
		banpick_phase = int(request.GET['phase'])
		radiant_ban = str(request.GET['radiant_ban'])		
		radiant_pick = str(request.GET['radiant_pick'])		
		dire_ban = str(request.GET['dire_ban'])		
		dire_pick = str(request.GET['dire_pick'])		
		if banpick_phase == 0:
			banpick_side = str(request.GET['choose_side'])
			ban_or_pick = 'ban'
			banpick_phase = banpick_phase+1
			option_list = generate_option_list(radiant_pick, radiant_ban, dire_pick, dire_ban)
		else:
			banpick_phase = int(request.GET['phase'])
			banpick_side = str(request.GET['side'])
			if 'hero_id' in request.GET:
				hero_id = request.GET['hero_id']
				if banpick_side == 'radiant' and banpick_phase in ban_phase:					
					radiant_ban = radiant_ban + str(hero_id) + ' '
				if banpick_side == 'radiant' and banpick_phase in pick_phase:					
					radiant_pick = radiant_pick + str(hero_id) + ' '
				if banpick_side == 'dire' and banpick_phase in ban_phase:					
					dire_ban = dire_ban + str(hero_id) + ' '
				if banpick_side == 'dire' and banpick_phase in pick_phase:					
					dire_pick = dire_pick + str(hero_id) + ' '
				option_list = generate_option_list(radiant_pick, radiant_ban, dire_pick, dire_ban)
				if banpick_phase in change_side:
					if banpick_side == 'radiant':
						banpick_side = 'dire'
					else:
						banpick_side = 'radiant'
				radiant_ban_image = generate_image_resource(radiant_ban)
				radiant_pick_image = generate_image_resource(radiant_pick)
				dire_ban_image = generate_image_resource(dire_ban)
				dire_pick_image = generate_image_resource(dire_pick)
				banpick_phase = int(banpick_phase) + 1
				if banpick_phase in ban_phase:
					ban_or_pick = 'ban'
				else:
					ban_or_pick = 'pick'
				if banpick_phase == 21:
					win_rate = analysis_winrate(radiant_ban, radiant_pick, dire_ban, dire_pick)
					radiant_winrate = win_rate
					dire_winrate = 1.0 - radiant_winrate
	

	return render_to_response('banpick.html', locals())
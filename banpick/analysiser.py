from sklearn.externals import joblib
import os
import numpy as np


def analysis_winrate(radiant_pick, dire_pick):
	bp_input = generate_numpy_list(radiant_pick, dire_pick)
	module_dir = os.path.dirname(__file__)
	file_path = os.path.join(module_dir, 'decision4.pkl')
	model = joblib.load(file_path)
	result = model.predict_proba(bp_input)
	winrate = float(result[:,1])*100
	return winrate

def generate_numpy_list(radiant_pick, dire_pick):
	radiant_pick = radiant_pick.split()
	dire_pick = dire_pick.split()
	np_list = np.zeros(224)
	for hero_id in radiant_pick:
		np_list[int(hero_id)-1] = 1
	for hero_id in dire_pick:
		np_list[int(hero_id)+111] = 1
	return np_list
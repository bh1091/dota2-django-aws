from models import News

def db_to_obj(news_db):
	news_page = news_info(news_db)
	if news_page.is_match:
		match_up = news_db.heroes
		news_page.winner = int(match_up.split()[0])
		heroes = match_up.split()[1].split(',')
		index = 0
		for hero in heroes:
			if index < 5:
				news_page.radiant_hero.append(hero)
			else:
				news_page.dire_hero.append(hero)
			index += 1
	return news_page


class news_info(object):
	def __init__(self, news_db):
		self.title = news_db.title
		self.is_match = news_db.is_match
		self.author = news_db.author
		self.source = news_db.source
		self.link = news_db.link
		self.content = news_db.content
		self.post_date = news_db.post_date
		self.radiant_hero = []
		self.dire_hero = []
		self.winner = ''
	
	
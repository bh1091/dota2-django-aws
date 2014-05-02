from django.db import models

class News(models.Model):
	serial_id = models.CharField(primary_key=True, max_length=100)
	title = models.TextField()
	is_match = models.BooleanField()
	author = models.CharField(blank=True, null=True, max_length=100)
	source = models.CharField(max_length=100)
	link = models.URLField()
	content = models.TextField()
	heroes = models.TextField(blank=True, null=True)
	post_date = models.DateTimeField()
	modify_date = models.DateTimeField(blank=True, null=True)

	def __unicode__(self):
		return self.title
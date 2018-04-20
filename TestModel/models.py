from django.db import models

# Create your models here.
class qiushi_joke(models.Model):
	username = models.CharField(max_length=128)
	content = models.CharField(max_length=1024)
	laugh_num = models.IntegerField()
	comment_num = models.IntegerField()
	imgurl = models.CharField(max_length=256)
	def __unicode__(self):
		return self.name
	class Meta:
		db_table = 'qiushi_joke'

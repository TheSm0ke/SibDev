from django.db import models

# Create your models here.
class SavedForm(models.Model):
    username = models.CharField(max_length=150)
    spent_money = models.IntegerField()
    gems = models.CharField(max_length=50)

    def __str__(self):
        return self.username

    def get_absolutle_url(self):
        return reverse('objects_detail_url', kwargs={'username': self.username})

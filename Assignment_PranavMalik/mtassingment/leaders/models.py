from django.db import models
from django.contrib.auth.models import User

class extendeduser(models.Model):
    email=models.EmailField( max_length=254)
    age=models.IntegerField()
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class user_score(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      score=models.IntegerField()
      medal=models.CharField(max_length=20)
    
class levels(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    medal=models.CharField(max_length=50)
    max_score=models.IntegerField()

class tests(models.Model):
    title=models.CharField( max_length=100)
    memo=models.TextField(blank=True)
    score=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    datecompleted=models.DateTimeField(null=True,blank=True)
    important=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    





from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    usertype=models.CharField(max_length=20)


class Registration(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    add=models.CharField(max_length=100)
    con=models.BigIntegerField()
    psw=models.CharField(max_length=20)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)

class Expert(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    add=models.CharField(max_length=100)
    con=models.BigIntegerField()
    lic=models.ImageField()
    psw=models.CharField(max_length=20)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)



class Videos(models.Model):
    title=models.CharField(max_length=20)
    file=models.FileField()

class Raw(models.Model):
    title=models.CharField(max_length=20)
    ing=models.CharField(max_length=500)
    link=models.URLField(null=True)

class Cooked(models.Model):
    title=models.CharField(max_length=20)
    ing=models.CharField(max_length=500)
    link=models.URLField(null=True)

class Request(models.Model):
    user=models.ForeignKey(Registration,on_delete=models.CASCADE)
    expert=models.ForeignKey(Expert,on_delete=models.CASCADE,null=True)
    bmi=models.CharField(max_length=200,null=True)
    healthstat=models.CharField(max_length=200,null=True)
    height=models.CharField(max_length=20,null=True)
    weight=models.CharField(max_length=20,null=True)
    breakfast=models.CharField(max_length=200,null=True)
    lunch=models.CharField(max_length=200,null=True)
    snack=models.CharField(max_length=200,null=True)
    dinner=models.CharField(max_length=200,null=True)
    esnack=models.CharField(max_length=200,null=True)
    status=models.CharField(max_length=500)

class Pyramid(models.Model):
    breakfast=models.CharField(max_length=200)
    bcal=models.CharField(max_length=200)
    lcal=models.CharField(max_length=200)
    dcal=models.CharField(max_length=200)
    lunch=models.CharField(max_length=200)
    dinner=models.CharField(max_length=200)
    user=models.ForeignKey(Registration,on_delete=models.CASCADE)
    req=models.ForeignKey(Request,on_delete=models.CASCADE,null=True)
    




class Foods(models.Model):
    r=models.ForeignKey(Request,on_delete=models.CASCADE)
    list=models.CharField(max_length=200)


class Chat(models.Model):
    sender=models.CharField(max_length=20)
    receiver=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    message=models.CharField(max_length=400)


class Feedback(models.Model):
    con=models.CharField(max_length=100)
    sender=models.ForeignKey(Registration,on_delete=models.CASCADE)
   
    date=models.DateField(auto_now_add=True)

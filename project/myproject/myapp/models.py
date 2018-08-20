from django.db import models

# Create your models here.
class Customer(models.Model):
    name        = models.CharField(max_length=99)
    lastname    = models.CharField(max_length=99)
    gender_choice = (
        ('M','Male'),
        ('F','Female'),
        ('N','None'),
    )
    gender      = models.CharField(max_length=1,choices=gender_choice,default='None')
    address     = models.TextField()
    tel         = models.CharField(max_length=13)
    def __str__(self):
        return "%s %s"%(self.name,self.lastname)

class Book(models.Model):
    name = models.CharField(max_length=99)
    def __str__(self):
        return self.name

class Rent(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    book    = models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
    time    = models.DateField(auto_now_add=True)

from django.db import models

class Pin_Num(models.Model):
    Customer= models.CharField(max_length=100)
    Pin= models.IntegerField(default=0)
    
# ATM/models.py

class profile(models.Model):
    name = models.CharField(max_length=100)
    Ifsc = models.CharField(max_length=20)  # Change from IntegerField to CharField

class account(models.Model):
    Customer= models.CharField(max_length=100)
    account_number= models.IntegerField(default=0)


    def __str__(self):
        return self.username




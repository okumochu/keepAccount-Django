from django.db import models

# Create your models here.

class account(models.Model):
    userName=models.CharField(max_length=128)
    disciption=models.CharField(max_length=128)
    money=models.IntegerField()
    date=models.DateField()
    type=models.IntegerField()

    def __str__(self):
        return f'{self.userName} spend {self.money} on {self.type}  {self.disciption} at {self.date}' 



    

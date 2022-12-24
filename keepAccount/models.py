from django.db import models
from django.contrib.auth.models import User
# Create your models here.

TYPE_CHOICES = (
    ("1", "食"),
    ("2", "衣"),
    ("3", "住"),
    ("4", "行"),
    ("5", "育"),
    ("6", "樂"),
)

class account(models.Model):
    user=models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)
    disciption=models.TextField(blank=True)
    money=models.IntegerField()
    date=models.DateTimeField()
    type=models.CharField(max_length = 20,choices = TYPE_CHOICES,default = '1')

    def __str__(self):
        return f'{self.user} spends {self.money} on {self.type}  {self.disciption} at {self.date}' 



    

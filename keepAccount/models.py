from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

TYPE_CHOICES = (
    ("食", "食"),
    ("衣", "衣"),
    ("住", "住"),
    ("行", "行"),
    ("育", "育"),
    ("樂", "樂"),
    ("收入","收入"),
    ("其他", "其他")
)


class account(models.Model):
    user=models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)
    description=models.TextField(blank=True)
    cost=models.IntegerField()
    date=models.DateField()
    type=models.CharField(max_length = 20,choices = TYPE_CHOICES,default = '1')


    def __str__(self):
        return f'{self.user} spends {self.cost} on {self.type}  {self.description} at {self.date}' 

class assets(models.Model):
    user=models.OneToOneField(User,blank=True,null=True, on_delete=models.CASCADE)
    asset=models.IntegerField(blank=True)
    expectedCost=models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.user} with asset{self.asset} and expectedCost{self.expectedCost} ' 


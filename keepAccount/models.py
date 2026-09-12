from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Stored category values remain unchanged; labels are displayed in English.

TYPE_CHOICES = (
    ("食", "Food"),
    ("衣", "Clothing"),
    ("住", "Housing"),
    ("行", "Transportation"),
    ("育", "Education"),
    ("樂", "Entertainment"),
    ("收入", "Income"),
    ("其他", "Other")
)


class account(models.Model):
    user=models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)
    description=models.TextField(blank=True)
    cost=models.IntegerField()
    date=models.DateField()
    type=models.CharField(max_length = 20,choices = TYPE_CHOICES,default = '1')


    def __str__(self):
        return f'{self.user} spends {self.cost} on {self.get_type_display()}  {self.description} at {self.date}' 

class assets(models.Model):
    user=models.OneToOneField(User,blank=True,null=True, on_delete=models.CASCADE)
    asset=models.IntegerField(blank=True)
    expectedCost=models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.user} with asset{self.asset} and expectedCost{self.expectedCost} ' 


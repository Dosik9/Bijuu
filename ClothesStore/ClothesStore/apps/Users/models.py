from django.db import models
from django.contrib.auth.models import AbstractUser

class SimpleUser(AbstractUser):
    user_name= models.CharField("Name", max_length=20,null=True, blank=True)
    user_surname = models.CharField("Surname", max_length=20,null=True, blank=True)
    user_email = models.EmailField('Email')
    user_phone_num = models.CharField('Country of User', max_length = 48, blank = True, null=True, default=None)
    user_avatar=models.ImageField(upload_to='users/', null=True, blank=True)
    user_birthdate=models.DateField(null=True, blank=True)

    def __str__(self):
        return (self.username)



class CreditCard(models.Model):
    user = models.ForeignKey(SimpleUser, on_delete=models.CASCADE)
    card_name=models.CharField("Card Name", max_length=15)
    card_number= models.IntegerField("Card number")
    # card_date=models.DateField("VALID THRU", widget=models.dat
    card_AS=models.IntegerField("Authorization Signature")

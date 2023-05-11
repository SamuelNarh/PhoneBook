from django.db import models

# Create your models here.
class PhoneBook(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30,)
    mobile_number = models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return f'firstname: {self.firstname} , lastname: {self.lastname} and Mobile No: {self.mobile_number}'
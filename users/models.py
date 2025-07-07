from django.db import models
from institutions.models import Institution
from api.enums import RoleEnum

#class User(models.Model):
   # username = models.CharField(max_length=50)
    #email = models.EmailField(unique=True)
    #password_hash = models.CharField(max_length=255)
    #role = models.CharField(max_length=10, choices=RoleEnum.choices)
    #institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    #created_at = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
        #return self.usernam

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    availability = models.JSONField()
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

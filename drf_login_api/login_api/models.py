from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    
    DROPSHIPPER = 'dropshipper'
    INFLUENCEUR = 'influenceur'
    AFFILIATION = 'affiliation'
    PRESTATAIRE = 'prestataire'
    OCCUPATION_CHOICES = [
        (DROPSHIPPER, 'dropshipper'),
        (INFLUENCEUR, 'influenceur'),
        (AFFILIATION, 'affiliation'),
        (PRESTATAIRE, 'prestataire')
    ] 
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    status = models.CharField(
        null=False,
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default=PRESTATAIRE
    )
    
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

# class Customer(models.Model):

#     DROPSHIPPER = 'dropshipper'
#     INFLUENCEUR = 'influenceur'
#     AFFILIATION = 'affiliation'
#     PRESTATAIRE = 'prestataire'
#     OCCUPATION_CHOICES = [
#         (DROPSHIPPER, 'dropshipper'),
#         (INFLUENCEUR, 'influenceur'),
#         (AFFILIATION, 'affiliation'),
#         (PRESTATAIRE, 'prestataire')
#     ]     
#     user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
#     surnom = models.CharField(max_length=200)
#     status = models.CharField(
#         null=False,
#         max_length=20,
#         choices=OCCUPATION_CHOICES,
#         default=PRESTATAIRE
#     )

#     def __str__(self):
#         return self.surnom
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    
    DROPSHIPPEUR = 'dropshippeur'
    INFLUENCEUR = 'influenceur'
    AFFILIATION = 'affiliation'
    PRESTATAIRE = 'prestataire'
    OCCUPATION_CHOICES = [
        (DROPSHIPPEUR, 'dropshippeur'),
        (INFLUENCEUR, 'influenceur'),
        (AFFILIATION, 'affiliation'),
        (PRESTATAIRE, 'prestataire')
    ]
    user = user = models.ForeignKey(User, verbose_name="Utilisateur associé", on_delete=models.CASCADE)
    username = models.CharField(max_length=200, unique=True, null=True)
    email = models.EmailField(max_length=254,unique=True, null=True)
    status = models.CharField(
        null=False,
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default=PRESTATAIRE
    )
    

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
from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,UserManager

# Create your models here.

class MyUser(models.Model):
    email = models.CharField(max_length=50, primary_key=True)
    first_name = models.CharField(max_length=30,default=None)
    last_name = models.CharField(max_length=30, default=None)
    gender = models.CharField(max_length=10,default=None)
    phone_number = models.CharField(max_length=12)
    REQUIRED_FIELDS = ['phone_number','first_name','gender']
    USERNAME_FIELD = 'email'

    objects = UserManager()
    class Meta:
        db_table = 'MyUser'

class country(models.Model):
    Code = models.CharField(max_length=3,primary_key=True,blank=None,default='')
    Name = models.CharField(max_length=52,default='',blank=False)
    CONTINENTCHOICE = (
        ('Asia','Asia'),
        ('Europe','Europe'),
        ('North America','North America'),
        ('Africa','Africa'),
        ('Oceania','Oceania'),
        ('Antartica','Antartica'),
        ('South America','South America'),

    )
    Continent = models.CharField(max_length=30,default='Asia',blank=False,choices=CONTINENTCHOICE)
    Region = models.CharField(max_length=26,default='',blank=False)
    SurfaceArea = models.FloatField(default=0.00,blank=False)
    IndepYear = models.SmallIntegerField(default=None,blank=True,null=True)
    Population = models.IntegerField(default=0,blank=False)
    LifeExpectancy = models.FloatField(default=None,blank=True,null=True)
    GNP = models.FloatField(default=None,blank=True,null=True)
    GNPOld =models.FloatField(default=None,blank=True,null=True)
    LocalName = models.CharField(max_length=45,default='',blank=False)
    GovernmentForm = models.CharField(max_length=45, default='',blank=False)
    HeadOfState = models.CharField(max_length=60,default=None,blank=True,null=True)
    Capital = models.IntegerField(default=None,null=True)
    Code2 = models.CharField(max_length=2,default='',blank=False)
    def __str__(self):
        return self.Name
    class Meta:
        db_table = 'country'


class city(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=35,default='',blank=False)
    CountryCode = models.ForeignKey(country,to_field='Code',db_column='CountryCode',blank=False,default='')
    District = models.CharField(max_length=20, default='', blank=False)
    Population = models.IntegerField(default=0,blank=False)
    def __str__(self):
        return self.Name
    class Meta:
        db_table = 'city'


class countrylanguage(models.Model):
    countrylanguage_id = models.AutoField(primary_key=True)
    CountryCode = models.ForeignKey(country, to_field='Code', db_column='CountryCode')
    Language = models.CharField(max_length=30, default='', blank=False)
    ISOFFICIALCHOICES = (
        ('T', 'true'),
        ('F', 'false'),
    )
    IsOfficial = models.CharField(max_length=1, default='F', blank=False, choices=ISOFFICIALCHOICES)
    Percentage = models.FloatField(default=0.0, blank=False)

    def __str__(self):
        return self.Language

    class Meta:
        db_table = 'countrylanguage'
        unique_together = (('CountryCode', 'Language'),)

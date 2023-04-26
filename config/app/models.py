
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
from django.contrib.auth.models import PermissionsMixin

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, null=True, blank=True, default=None)
    branch = models.CharField(max_length=100, null=True, blank=True, default=None)
    
    # leetcode_name = models.CharField(max_length=100, null=True, blank=True, default=None)    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    otp = models.CharField(max_length=7, null=True, blank=True, default=None)
    
    def get_short_name(self):
        # The user is identified by their email
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    
    def has_module_perms(self, app_label):
           return True
    
    def __str__(self):
        return self.email
    

class leetcode_acc(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='leetcode')
    username = models.CharField(max_length=100, null=False, blank=False, unique=True, default="")
    name = models.CharField(max_length=100, null=True, blank=True, default="Scraping..")
    rank= models.CharField(max_length=10, null=True, blank=True, default="Scraping..")
    photo_url = models.CharField(max_length=200, null=True, blank=True, default="Scarping..")
    number_of_questions = models.IntegerField(null=True, blank=True, default=0)
    last_solved = models.CharField(max_length=50, null=True, blank=True, default="Scraping..")
    
    def __str__(self):
        return self.username

class codechef_acc(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='codechef')
    username = models.CharField(max_length=100, null=False, blank=False, unique=True, default="")
    name = models.CharField(max_length=100, null=True, blank=True, default="Scraping..")
    global_rank= models.CharField(max_length=10, null=True, blank=True, default="Scraping..")
    country_rank= models.CharField(max_length=10, null=True, blank=True, default="Scraping..")    
    rating = models.IntegerField(null=True, blank=True, default=0)
    stars = models.CharField(max_length=10, null=True, blank=True)
    photo_url = models.CharField(max_length=100, null=True, blank=True, default="Scarping..")
    number_of_questions = models.CharField(max_length=10,null=True, blank=True, default='0')
    
    def __str__(self):
        return self.username
from django.db import models
import re

class userManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First Name must be at least 2 characters"        
        if not postData['first_name'].isalpha():
            errors['first_name_letterOnly'] ="Name must be alphabet characters only"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name must be at least 2 characters" 
        if not postData['last_name'].isalpha():
            errors['last_name_letterOnly'] ="Name must be alphabet characters only"
        user_id = Users.objects.filter(user_id=postData['user_id'])
        if len(postData['user_id']) < 6:
            errors['user_id_short'] = "ID must be at least 6 characters" 
        if len(user_id):
            if postData['user_id'] == user_id[0].user_id:
                errors['user_id'] = "user ID is not available"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    
            errors['email'] = ("Invalid email address format!")
        email = Users.objects.filter(email=postData['email'])
        if len(email):
            if postData['email'] == email[0].email:
                errors['duplicate_email'] = "The email is already registered"
        if len(postData['password']) < 8:
            errors['password'] = "Passwords, at least 8 chracters"
        if postData['password'] != postData['confirm']:
            errors['confirm'] = "Password does not match"
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to="profile/%Y/%m/%d", blank=True)
    user_id = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm = models.CharField(max_length=255)
    objects = userManager()

class DMs(models.Model):
    dm_to = models.ForeignKey(Users, related_name="dm", on_delete=models.CASCADE)
    dm_from_name = models.CharField(max_length=255)
    dm_from_email = models.CharField(max_length=255)
    if_check = models.CharField(max_length=10, default="no")
    dm_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
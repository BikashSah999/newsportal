from django.db import models
from django.utils import timezone
from django.contrib.auth.admin import User
from ckeditor.fields import RichTextField

# Create your models here.
class Categorylist(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=30)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return(self.category_name)
    
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    #cat_list = (('Technology','Technology'), ('Entertainment','Entertainment'), ('Sports','Sports'), ('Politics','Politics'))
    title = models.CharField(max_length=30)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='blogapp/blog/images')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    date = models.DateField(default=timezone.now)
    #category = models.CharField(choices=cat_list, max_length=20)
    categorylist = models.ForeignKey(Categorylist, on_delete=models.CASCADE, related_name='categorylist')
    views = models.IntegerField(default='0')
    likes = models.IntegerField(default='0')

    def __str__(self):
        return (self.title)

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank=False, null=False)
    date = models.DateField(default=timezone.now)
    message = models.CharField(max_length=1000)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return (self.first_name)
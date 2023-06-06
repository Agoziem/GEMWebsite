from django.db import models
from Home.models import Organization_detail
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Categorie(models.Model):
	Category_image=models.ImageField( upload_to="assets/Article/Category", blank=False)
	name=models.CharField(max_length=300,blank=False)
	description=models.TextField(blank=False)
    
	def __str__(self):
	    return str(self.name)
	
class Articles(models.Model):
	Category=models.ForeignKey(Categorie,related_name="Articles",on_delete=models.CASCADE)
	thumb=models.ImageField( upload_to="assets/Article/thumbnail", blank=False)
	title=models.CharField(max_length=300,blank=False)
	slug=models.CharField(max_length=300,blank=True)
	body=RichTextField()
	date_published=models.DateTimeField(auto_now_add=True)
	author=models.ForeignKey(User,related_name="Articles",on_delete=models.CASCADE)
	reading_time=models.CharField(max_length=300,blank=False)
	
	def __str__(self):
		return str(self.title)
	
	@property
	def picture(self):
		try:
			url= self.thumb.url
		except:
			url=""
		return url
	

class Comment(models.Model):
	Article=models.ForeignKey(Categorie,related_name="comments",on_delete=models.CASCADE)
	name=models.CharField(max_length=300,blank=False)
	email=models.EmailField(blank=False)
	message=models.TextField(blank=False)
    
	def __str__(self):
	    return f"{self.name} commented on - {self.Article}"
	    
	

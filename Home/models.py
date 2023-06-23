from django.db import models
from ckeditor.fields import RichTextField


class Organization_detail(models.Model):
	name=models.CharField(max_length=300,blank=False)
	Vision=models.TextField(blank=False)
	Mission=models.TextField(blank=False)
	About=models.TextField(blank=False)
    
	def __str__(self):
	    return str(self.name)

class Value(models.Model):
	S_N = models.IntegerField(blank=False,default=1)
	Organization_name=models.ForeignKey(Organization_detail,related_name="values",on_delete=models.CASCADE,blank=False)
	Value_heading=models.CharField(max_length=300,blank=False)
	Value=models.CharField(max_length=300,blank=False)
    
	def __str__(self):
	    return f"{self.Organization_name} Value - {self.Value_heading}"
	

class Photo(models.Model):
	S_N = models.IntegerField(blank=False,default=1)
	Picture=models.ImageField( upload_to="assets/Photogallery", blank=False)
	description=models.CharField( blank=True , max_length=300)

	def __str__(self):
		return str(self.description)
	
	@property
	def picture(self):
		try:
			url= self.Picture.url
		except:
			url=""
		return url


class Project(models.Model):
	S_N = models.IntegerField(blank=False,default=1)
	Title=models.CharField(max_length=300,blank=False)
	Picture=models.ImageField( upload_to="assets/Projects", blank=False)
	description=RichTextField(blank=False)
    
	def __str__(self):
		return str(self.Title)
	    
	@property
	def picture(self):
		try:
			url= self.Picture.url
		except:
			url=""
		return url
	
	
class Staff(models.Model):
	S_N = models.IntegerField(blank=False,default=1)
	Profileimage=models.ImageField( upload_to="assets/Profile", blank=False)
	Name=models.CharField(max_length=300,blank=False)
	Responsibility=models.CharField(max_length=300,blank=False)
	facebook=models.CharField(max_length=300,blank=True)
	whatsapp=models.CharField(max_length=300,blank=True)
	instagram=models.CharField(max_length=300,blank=True)
	twitter=models.CharField(max_length=300,blank=True)
    
	def __str__(self):
		return str(self.Name)
	
	@property
	def picture(self):
		try:
			url= self.Profileimage.url
		except:
			url=""
		return url

Arm_list=(
	("Bible Studies","Bible Studies"),
	("Revival Prayers","Revival Prayers"),
	("Foundation","Foundation"),
	("Women’s Hub","Women’s Hub"),
	("Partners","Partners")
	)
		
class Event(models.Model):
	S_N = models.IntegerField(blank=False,default=1)
	GEM_Arm=models.CharField(blank=False , default="None",choices=Arm_list,max_length=300)
	Event_Flier=models.ImageField( upload_to="assets/Events", blank=False)
	Title=models.CharField(max_length=300,blank=False)
	description=models.TextField(blank=False, max_length=300 , help_text="max_lenght of 300")
	Day=models.CharField(max_length=300,blank=False)
	Month=models.CharField(max_length=300,blank=False)
	Time=models.CharField(max_length=300,blank=False)
	Zoom_meeting=models.BooleanField(default=True, blank=False)
	Zoom_ID=models.CharField(max_length=300,blank=False)
	Zoom_Password=models.CharField(max_length=300,blank=False)
	Other_Venue=models.CharField(max_length=300,blank=True)
    
	def __str__(self):
		return str(self.Title)
	
	@property
	def picture(self):
		try:
			url= self.Event_Flier.url
		except:
			url=""
		return url
	

class Subscription(models.Model):
	Email=models.EmailField(max_length=300,blank=False)
    
	def __str__(self):
	    return str(self.Email)
	
class Contact(models.Model):
	name=models.CharField(max_length=300,blank=False)
	email=models.EmailField(max_length=300,blank=False)
	message=models.TextField(blank=False)
	
    
	def __str__(self):
	    return str(self.name)
	
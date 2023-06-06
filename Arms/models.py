from django.db import models
from Home.models import Organization_detail
from ckeditor.fields import RichTextField

class Arm(models.Model):
	Organization_name=models.ForeignKey(Organization_detail,related_name="Arms",on_delete=models.CASCADE)
	Arm_image=models.ImageField( upload_to="assets/Arms", blank=False)
	Arm=models.CharField(max_length=300,blank=False)
	sideline=models.CharField(max_length=300,blank=False)
	Vision=models.TextField(max_length=400,blank=False, help_text="max of 400 words")
	Mission=models.TextField(max_length=400,blank=True, help_text="max of 400 words")
	
	
	def __str__(self):
		return str(self.Arm)
	    
	@property
	def picture(self):
		try:
			url= self.Arm_image.url
		except:
			url=""
		return url
	
class Arm_detail(models.Model):
	Arm_name=models.ForeignKey(Arm,related_name="details",on_delete=models.CASCADE)
	image_beside=models.ImageField( upload_to="assets/Arms image beside", blank=False)
	heading=models.CharField(max_length=300,blank=False)
	sideline=models.CharField(max_length=300,blank=False)
	body=RichTextField()
 
	def __str__(self):
	    return f"{self.Arm_name} - {self.heading}"
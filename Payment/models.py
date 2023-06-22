from django.db import models
import secrets

Partnership_type=(
	("One Time","One Time"),
	("Monthly Recurrent","Monthly Recurrent"),
	)

class Donations_and_Support(models.Model):
    Name=models.CharField(max_length=300)
    Payment_description=models.CharField(max_length=300)
    ref=models.CharField(max_length=300)
    Email=models.CharField(max_length=300)
    Partnership_type=models.CharField(max_length=300 ,choices=Partnership_type,blank=False, default="None")
    verified=models.BooleanField()
    total_amount=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Date_Created=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-Date_Created',)
            
    @property
    def amount_value(self) -> int:
        return self.total_amount*100

    def save(self,*args,**kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(20)
            object_with_similar_ref=Donations_and_Support.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref=ref
            super().save(*args,**kwargs)
            

    def __str__(self):
        return str(self.Name)


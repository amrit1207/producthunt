from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=225)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='image/')
    icon = models.ImageField(upload_to='image/')
    url=models.TextField()
    votes=models.IntegerField(default=1)
    hunter=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
       return self.title


    def summary(self):
        return self.body[0:100]


    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
#title
#pub_date
#image
#icon
#body
#votes
#hunter user who access
#url

#pub_date_pretty


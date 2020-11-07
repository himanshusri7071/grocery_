from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    head0= models.CharField(max_length=500, default="")
    chead0 = models.CharField(max_length=5000, default="")
    head1 = models.CharField(max_length=500, default="")
    chead1 = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=500, default=True,null=True)
    chead2 = models.CharField(max_length=5000, default=True,null=True)

    pub_date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.title
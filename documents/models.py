from django.db import models
from django.contrib.auth.models import User




class DocumentModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=1000000,null=True,blank=True)
    document = models.FileField(upload_to='media')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} -> {self.title}"



from django.db import models

class AppDetails(models.Model) :
    app_name = models.CharField(max_length=255)
    version = models.CharField(max_length=25)
    description = models.TextField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta :
        ordering = ['-updated' , '-created']
    def __str__(self):
        return self.app_name
    

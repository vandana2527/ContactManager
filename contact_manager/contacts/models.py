from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    
    class Meta:
        app_label = 'contacts'

    def __str__(self):
        return self.name
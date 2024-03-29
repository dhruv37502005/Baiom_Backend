from django.db import models

class MaintenancePage(models.Model):
    name = models.CharField(max_length=200, unique=True)
    is_enabled = models.BooleanField(default=False)
    access_code = models.CharField(max_length=100, null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['name']

class GetInTouch(models.Model):
    phone_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number


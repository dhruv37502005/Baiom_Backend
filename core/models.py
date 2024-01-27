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

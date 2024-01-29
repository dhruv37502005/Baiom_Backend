from django.db import models
from django.utils.text import slugify
from django.utils import timezone
# import cv2
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# class Author(models.Model):
#     author_name = models.CharField(max_length=100, null=True)
#     about_author = models.CharField(max_length=100, null=True)
    
#     def __str__(self):
#         return self.author_name
    
# class Course(models.Model):
    
#     featured_image=models.ImageField(upload_to="Media/featured_image", null=True, blank=True)
#     title = models.CharField(max_length=200, null=True)
#     slug = models.SlugField(blank=True, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True, blank=True)
#     description = models.TextField(max_length=200, blank=True, null=True)
#     price=models.FloatField(null=True, blank=True)
#     discount= models.FloatField(null=True, blank=True)
    
#     def __str__(self):
#         return self.title
    

class CourseCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_itie = models.BooleanField(default=False)

 
    def __str__(self):
        return self.name

class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=50)
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    video = models.FileField(upload_to='course_videos/',null=True, blank=True)
    price=models.FloatField(null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    duration_field = models.DurationField(default=timezone.timedelta)
    watch_percent = models.FloatField(blank=True,null=True)
    brochure = models.FileField(upload_to='course_brochure/',null=True,blank=True)
    itie = models.BooleanField(default=False)
    status_choices = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('draft', 'Draft'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    carriculum_title = models.CharField(max_length=100, default=False)
    carriculum_desc =  models.TextField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
    
        super().save(*args, **kwargs)


@receiver(post_save, sender=CourseCategory)
def update_itie(sender, instance, **kwargs):
    courses = Course.objects.filter(category=instance)
    for course in courses:
        course.itie = instance.is_itie
        course.save()   



  #  def save(self, *args, **kwargs):
        # Call the function to calculate and update the duration
   
   #     self.calculate_and_update_duration()
    #    super().save(*args, **kwargs)
    

    #def calculate_and_update_duration(self):
        # Get the video file path
     #   video_path = self.video.path

        # Open the video file
      #  cap = cv2.VideoCapture(video_path)

        # Get the total number of frames and frames per second
       # total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
       # fps = int(cap.get(cv2.CAP_PROP_FPS))

        # Calculate the duration in seconds
      #  try: 
       #     duration_seconds = total_frames / fps
       # except: ZeroDivisionError

        # Convert seconds to a timedelta object
        #duration_timedelta = datetime.timedelta(seconds=duration_seconds)

        # Update the duration field in the model
   #     self.duration_field = duration_timedelta
    
    
    def __str__(self):
       return self.title



  



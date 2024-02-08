from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
Dashboard_User = get_user_model()
# import cv2
import datetime

# from userauths.models import Dashboard_User
# course/models.py



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
    brochure = models.FileField(upload_to='course_brochure/',null=True,blank=True)

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
    status_choices = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('draft', 'Draft'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    carriculum_title = models.CharField(max_length=100, default=False)
    carriculum_desc =  models.TextField(default=False)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Batch(models.Model):
    batch_name = models.CharField(max_length=100)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    # users = models.ManyToManyField(Dashboard_User)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.course.title} - Batch {self.id}"



class Purchase(models.Model):
    user = models.ForeignKey(Dashboard_User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Batch = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True, blank=True)
    purchase_date = models.DateField(auto_now_add=True)
    purchase_start_date = models.DateField()
    purchase_end_date = models.DateField()
    additional_access_date = models.DateField()

    
    def __str__(self):
        return f"{self.course.title} - Course"

    def is_course_access_valid(self):
        now = timezone.now()
        return self.start_date <= now <= self.end_date

    def can_access_recorded_videos(self):
        now = timezone.now()
        return self.end_date <= now <= self.additional_access_date

class Resource(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    notes = models.FileField(upload_to='course_notes/', null=True, blank=True)
    recorded_video_link = models.FileField(upload_to='course_recorded_lectures/',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.title} - {self.created_at}"

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
    
    
    # def __str__(self):
    #    return self.title



  



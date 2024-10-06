from django.db import models
from django.utils import timezone

# Create your models here.
class BlogPost(models.Model):
    SECTION_CHOICES = [
        ('travel', 'Travel'),
        ('food', 'Food'),
        ('fitness', 'Fitness'),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    section = models.CharField(max_length=7, choices=SECTION_CHOICES)
    event_date = models.DateField(default=timezone.now)
    head_image = models.ImageField(upload_to='blog_images/', null=True, blank=True)  # Main image for gallery
    other_images = models.ManyToManyField('BlogImage', blank=True)  # Other images for the post

    def __str__(self):
        return self.title
    
class BlogImage(models.Model):
    image = models.ImageField(upload_to='blog_images/')
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='blog_images')

    def __str__(self):
        return f"Image for {self.blog_post.title}"
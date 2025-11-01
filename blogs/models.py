
# Create your models here.
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError

def validate_image_size(image):
    max_size_mb = 3
    if image.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Image file size should not exceed {max_size_mb} MB.")

class Blog(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    summary = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', validators=[validate_image_size])
    slug = models.SlugField(unique=True, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def _str_(self):
        return self.title
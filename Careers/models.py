from django.db import models

# Create your models here.
from django.db import models

class Career(models.Model):
    WORK_MODE_CHOICES = [
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid'),
        ('On-site', 'On-site'),
    ]

    JOB_TYPE_CHOICES = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Internship', 'Internship'),
        ('Contract', 'Contract'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    work_mode = models.CharField(max_length=50, choices=WORK_MODE_CHOICES, default='Remote')
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES, default='Full-time')
    description = models.TextField()
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags like AI, Python, Research")
    details = models.TextField(help_text="Detailed job description for the View Role page")
    posted_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_on']
        verbose_name = "Career"
        verbose_name_plural = "Careers"

    def _str_(self):
        return self.title
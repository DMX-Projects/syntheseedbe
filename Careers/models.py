from django.db import models


# ✅ Existing Career model (no changes)
class Career(models.Model):
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    work_mode = models.CharField(max_length=50)
    job_type = models.CharField(max_length=50)
    description = models.TextField()
    tags = models.TextField(blank=True)
    details = models.TextField(blank=True)
    posted_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


# ✅ New JobApplication model (for "Apply Now" feature)
class JobApplication(models.Model):
    # Link the application to a specific career
    career = models.ForeignKey(
        Career,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    cover_letter = models.TextField(blank=True)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.career.title}"

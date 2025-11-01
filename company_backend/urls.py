from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # API Routes
    path('api/contact/', include('contact.urls')),     # Contact App
    path('api/blogs/', include('blogs.urls')),         # Blogs App
    path('api/careers/', include('Careers.urls')),     # Careers App
]

# ✅ Serve media files (resumes, images, etc.) during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

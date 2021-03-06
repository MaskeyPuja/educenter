"""educenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from eduapp.views import HomeView, AboutView, CourseView, EventView, BlogView, ContactView, NoticeView, ResearchView, ScholarshipView, TeacherView, CourseDetailView

from django.conf import settings
from django.views.static import serve

from django.conf.urls.static import static


urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('admin/', admin.site.urls),
    path('about', AboutView.as_view(), name = 'about'),
    path('course', CourseView.as_view(), name = 'course'),
    path('event', EventView.as_view(), name = 'event'),
    # path('blog', BlogView.as_view(), name = 'blog'),
    path('contact', ContactView.as_view(), name = 'contact'),
    path('notice', NoticeView.as_view(), name = 'notice'),
    path('research', ResearchView.as_view(), name = 'research'),
    path('scholarship', ScholarshipView.as_view(), name = 'scholarship'),
    path('teacher', TeacherView.as_view(), name = 'teacher'),
    path('course_detail', CourseDetailView.as_view(), name = 'course-detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
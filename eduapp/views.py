from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name = 'eduapp/index.html'


class CourseView(TemplateView):
	template_name = 'eduapp/courses.html'

class EventView(TemplateView):
	template_name = 'eduapp/events.html'

class BlogView(TemplateView):
	template_name = 'eduapp/blog.html'
from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name = 'eduapp/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['active'] = 'home'

		return context


class CourseView(TemplateView):
	template_name = 'eduapp/courses.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['active'] = 'course'

		return context

class EventView(TemplateView):
	template_name = 'eduapp/events.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['active'] = 'event'

		return context


class BlogView(TemplateView):
	template_name = 'eduapp/blog.html'

class ContactView(TemplateView):
	template_name = 'eduapp/contact.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['active'] = 'contact'

		return context


class NoticeView(TemplateView):
	template_name = 'eduapp/notice.html'



class ResearchView(TemplateView):
	template_name = 'eduapp/research.html'


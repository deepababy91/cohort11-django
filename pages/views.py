# pages/views.py
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'#spitting out json in case

class AboutPageView(TemplateView): # new
    template_name = 'about.html'

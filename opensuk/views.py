from django.views.generic import TemplateView

class Home(TemplateView):
    template_name='index.html'

class Privacy(TemplateView):
    template_name='privacy.html'
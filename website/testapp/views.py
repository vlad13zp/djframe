from django.views.generic.base import TemplateView
from testapp.actions import get_all_info


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['all'] = get_all_info()

        return context

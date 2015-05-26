from django.views.generic.base import TemplateView
from testapp.models import Author, Book


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        my_dict = {}

        for name in Author.objects.all():
            local_list = [
                book.name for book in Book.objects.filter(author=name)
            ]
            my_dict[name.first_name] = {str(local_list)}

        context['all'] = my_dict

        for name, books in context['all'].iteritems():
            print name + '/'
            for book in books:
                print book

        return context

from django.http import HttpResponse, Http404
import datetime

from testapp.models import Author

def hello(request, username):
	return HttpResponse('<html><head><title>Hello page</title></head>'
        '<body><h1>Hello, {0}!</h1></body>'
        '</html>'.format(
        username
    ));

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset,
    dt)
    return HttpResponse(html)

def home(request):
    authors = [
        author.first_name for author in Author.objects.all()
    ]
    authors = ', '.join(authors)

    return HttpResponse(
        '<html><head><title>Home page</title></head>'
        '<body><h1>Hello world!</h1>'
        '<p>Authors : <i>{0}</i></p>'
        '</body>'
        '</html>'.format(authors)
    )

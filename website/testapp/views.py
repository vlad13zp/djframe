from django.http import HttpResponse
from testapp.models import Author, Info_author


def home(request):
    authors = [
        author.first_name + ' / <a href="./user/' + str(author.id) +
        '">Read more...</a>' for author in Author.objects.all()
    ]

    authors = '<br/><hr>'.join(authors)

    return HttpResponse(
        '<html><head><title>Home page</title></head>'
        '<body><h1>Hello, my dear friend!</h1>'
        '<h5>I want to show you some information about famous people</h5>'
        '<p><i>{0}</i></p>'
        '</body>'
        '</html>'.format(authors)
    )


def info(request, id):
    authors = [
        info_author.info_author + '<br/><hr><h5>Date birth : ' +
        str(info_author.date_birth) + '</h5>'
        for info_author in Info_author.objects.filter(
            id_author=id)
    ]

    if (len(authors) == 0):
        authors = ['The information is empty. Please visit that page later']

    authors = '<br/>'.join(authors)

    return HttpResponse(
        '<html><head><title>Info page</title></head>'
        '<body><h1>Detail information</h1>'
        '<h5>I want to show you detail information about famous people</h5>'
        '<p><i>{0}</i></p>'
        '<a href="../">Back to the home page</a>'
        '</body>'
        '</html>'.format(authors)
    )

from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __unicode__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class Info_author(models.Model):
    id_author = models.IntegerField()
    info_author = models.TextField()
    date_birth = models.DateField()


class Book(models.Model):
    author = models.ForeignKey(Author)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return '{0} - {1}'.format(self.author.first_name, self.name)

from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()


class Info_author(models.Model):
    id_author = models.IntegerField()
    info_author = models.TextField()
    date_birth = models.DateField()

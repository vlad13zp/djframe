from testapp.models import Author, Book


def get_all_info():
    my_dict = {}

    for name in Author.objects.all():
        local_list = [
            book.name for book in Book.objects.filter(author=name)
        ]
        my_dict[name.first_name] = local_list

    return my_dict

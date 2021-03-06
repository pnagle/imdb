import os, json
# from models import  Movies, Genre
import sqlite3
from array import *


def populate():
    print ('here')
    connection = sqlite3.connect('/home/piyush/Experiments/FyndAssignment/imdb/db.sqlite3')
    with open('/home/piyush/Experiments/FyndAssignment/imdb.json') as imdb_file:
        with connection:
            cursor = connection.cursor()
            data = json.load(imdb_file)
            i = 0
            # print len(data[2]['name'])
            for i in range(0, len(data)):
                print(data[0])
                print ('''INSERT INTO imdb_api_movies VALUES''' +
                    str(tuple(list(data[i]['name']))))
                cursor.execute(
                    '''INSERT INTO imdb_api_movies VALUES''' +
                    str(tuple(data[i]['name'] + data[i]['director'])))
                # Movies.objects.get_or_create(name=data[i][name], title=title, url=url, views=views)[0]
#     # python_cat = add_cat('Python')
#     #
#     # add_page(cat=python_cat,
#     #     title="Official Python Tutorial",
#     #     url="http://docs.python.org/2/tutorial/")
#     #
#     # add_page(cat=python_cat,
#     #     title="How to Think like a Computer Scientist",
#     #     url="http://www.greenteapress.com/thinkpython/")
#     #
#     # add_page(cat=python_cat,
#     #     title="Learn Python in 10 Minutes",
#     #     url="http://www.korokithakis.net/tutorials/python/")
#     #
#     # django_cat = add_cat("Django")
#     #
#     # add_page(cat=django_cat,
#     #     title="Official Django Tutorial",
#     #     url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")
#     #
#     # add_page(cat=django_cat,
#     #     title="Django Rocks",
#     #     url="http://www.djangorocks.com/")
#     #
#     # add_page(cat=django_cat,
#     #     title="How to Tango with Django",
#     #     url="http://www.tangowithdjango.com/")
#     #
#     # frame_cat = add_cat("Other Frameworks")
#     #
#     # add_page(cat=frame_cat,
#     #     title="Bottle",
#     #     url="http://bottlepy.org/docs/dev/")
#     #
#     # add_page(cat=frame_cat,
#     #     title="Flask",
#     #     url="http://flask.pocoo.org")
#     #
#     # # Print out what we have added to the user.
#     # for c in Category.objects.all():
#     #     for p in Page.objects.filter(category=c):
#     #         print "- {0} - {1}".format(str(c), str(p))
#
# def add_page(cat, title, url, views=0):
#     p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
#     return p
#
# def add_cat(name):
#     c = Category.objects.get_or_create(name=name)[0]
#     return c

# Start execution here!
# if __name__ == '__main__':
#     print "Starting Movies population script..."
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imdb.settings')
#     from imdb_api.models import Movies, Genre
#     populate()


def isolate_city_codes():
    filename = '/home/piyush/Experiments/FyndAssignment/imdb.json'
    with open(filename, 'r') as f:
        contents = f.read()
    list_of_lines = [line.split('\t') for line in contents.split('\n')[1:]]
    # Latitude and longitude should be numbers
    for i in range(1, len(list_of_lines) - 1):
        list_of_lines[i][2] = float(list_of_lines[i][2])
        list_of_lines[i][3] = float(list_of_lines[i][3])
    return list_of_lines

populate()
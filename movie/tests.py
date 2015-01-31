from django.test import TestCase
from movie.models import *
from datetime import datetime

# Create your tests here.
class MovieTests(TestCase):
	def test_CreateMovie(self):
		Movie.objects.create(movie_name="Test", pub_date=datetime.now())
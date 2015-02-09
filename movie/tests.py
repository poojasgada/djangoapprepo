from django.test import TestCase
from movie.models import *
from datetime import datetime
from django.utils import timezone

# Create your tests here.
class MovieTests(TestCase):
	def test_CreateMovie(self):
		Movie.objects.create(movie_name="Test1", pub_date=timezone.now())
		Movie.objects.create(movie_name="Test2", pub_date=timezone.now())
		Movie.objects.create(movie_name="Test3", pub_date=timezone.now())

		movie_objs = Movie.objects.all()
		self.assertEqual(3, len(movie_objs))

		#Always nice to clearn up after tests
		Movie.objects.all().delete()

	def test_CreateLikeIT(self):
		movie_obj = Movie.objects.create(movie_name="Test1", pub_date=timezone.now())
		LikeIt.objects.create(movie=movie_obj, likeit_text="Love it!", upvote=1)
		LikeIt.objects.create(movie=movie_obj, likeit_text="Good!", upvote=1)

		likeit_objs = LikeIt.objects.all()
		self.assertEqual(2, len(likeit_objs))

		#Always nice to clean up after tests
		Movie.objects.all().delete()
		LikeIt.objects.all().delete()

	def test_LikeItUpvote(self):
		movie_obj = Movie.objects.create(movie_name="Test1", pub_date=timezone.now())
		LikeIt.objects.create(movie=movie_obj, likeit_text="Love it!", upvote=5)

		likeit_obj = LikeIt.objects.filter(movie=movie_obj)
		self.assertEqual(1, len(likeit_obj))

		likeit_obj = likeit_obj[0]
		likeit_obj.upvote = 10
		likeit_obj.save()

		likeit_obj_postsave = LikeIt.objects.filter(movie=movie_obj)[0]
		self.assertEqual(10, likeit_obj_postsave.upvote)

		#Always nice to clean up after tests
		Movie.objects.all().delete()
		LikeIt.objects.all().delete()

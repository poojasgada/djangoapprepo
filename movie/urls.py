from django.conf.urls import patterns, url

from movie import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<movie_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<movie_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/movie/
    url(r'^(?P<movie_id>\d+)/movie/$', views.movie, name='movie'),
)
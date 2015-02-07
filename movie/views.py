from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

from movie.models import Movie

def index(request):
    latest_movie_list = Movie.objects.order_by('-pub_date')[:5]
    context = {
        'latest_movie_list': latest_movie_list,
    }
    return render(request, 'movie/index.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie/detail.html', {'movie': movie})

def results(request, movie_id):
    response = "You're looking at the results of movie %s."
    return HttpResponse(response % movie_id)

def movie(request, movie_id):
    return HttpResponse("You're voting on movie %s." % movie_id)
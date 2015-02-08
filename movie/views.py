from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from movie.models import Movie, LikeIt

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
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie/results.html', {'movie': movie})

def movie(request, movie_id):
    p = get_object_or_404(Movie, pk=movie_id)
    try:
        selected_likeit = p.likeit_set.get(pk=request.POST['likeit'])
    except (KeyError, LikeIt.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'movie/detail.html', {
            'movie': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_likeit.upvote += 1
        selected_likeit.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('movie:results', args=(p.id,)))
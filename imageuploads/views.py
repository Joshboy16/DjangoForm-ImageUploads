from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from imageuploads.forms import UploadForm
from imageuploads.models import Movie


def home(request):
    movies = Movie.objects.all()
    if movies is not None:
        print(movies)
        return render(request, 'movies/movies.html', {'movie': movies})
    else:
        raise Http404('Movies does not exist')

def movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if movie is not None:
        return render(request, 'movies/movie.html', {'movie': movie})
    else:
        raise Http404('Movie does not exist')


def upload(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        return redirect(home)
    return render(request, 'movies/upload.html', {'form': UploadForm})

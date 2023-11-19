
from django.http import HttpResponse
from django.template import loader
from .models import Movies
from .forms import MovieForm,MovieSearchForm,MovieUpdateForm
from django.shortcuts import render, redirect,get_object_or_404
# Create your views here.
def movies(request):
    allmovies=Movies.objects.all().values()
    template=loader.get_template('movie.html')
    context={
        'allmovies':allmovies,
    }
    return HttpResponse(template.render(context,request))
def details(request,id):
    moviess=Movies.objects.get(id=id)
    template=loader.get_template('details.html')
    context={
        'moviess':moviess,
    }
    return HttpResponse(template.render(context,request))
# def addmovie(request):
#     if request.method=='POST':
#         form =MovieForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('movies')
#         else:
#             form=MovieForm()
#     return render(request,'add_movie.html', {'form': form})
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST,request.FILES)
        if form.is_valid():  
            form.save()
            return redirect('movieslist')  
    else:
        form = MovieForm()

    return render(request, 'add_movie.html', {'form': form})
def movies_list(request):
    form = MovieSearchForm(request.GET)
    movies = Movies.objects.all()
    languages = Movies.objects.values('language').distinct()
    language_counts = []

    for language in languages:
        count = Movies.objects.filter(language=language['language']).count()
        language_counts.append({'language': language['language'], 'count': count})

    if form.is_valid():
        query = form.cleaned_data.get('query')
        filter_by_name = form.cleaned_data.get('filter_by_name')
        filter_by_director = form.cleaned_data.get('filter_by_director')
        filter_by_release_year = form.cleaned_data.get('filter_by_release_year')
        filter_by_language = form.cleaned_data.get('filter_by_language')
        filter_by_rating = form.cleaned_data.get('filter_by_rating')

    if query:
        movies = movies.filter(moviename__icontains=query)

    if filter_by_name:
        movies = movies.order_by('moviename')

    if filter_by_director:
        movies = movies.order_by('direcname')

    if filter_by_release_year:
        movies = movies.order_by('year')

    if filter_by_language:
        movies = movies.order_by('language')

    if filter_by_rating:
        movies = movies.order_by('-rating')

    context = {
        'form': form,
        'movies': movies,
        'language_counts': language_counts,
    }

    return render(request, 'movies_list.html', context)
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)

    if request.method == 'POST':
        # If the user confirms the deletion
        movie.delete()
        return redirect('movieslist')

    return render(request, 'delete_movie.html', {'movie': movie})
def delete_list(request):
    form = MovieSearchForm(request.GET)
    movies = Movies.objects.all()
    template=loader.get_template('deletelist.html')
    context={
        'movies':movies,
    }
    return HttpResponse(template.render(context,request))
def update_movie(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)

    if request.method == 'POST':
        form = MovieUpdateForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movieslist')
    else:
        form = MovieUpdateForm(instance=movie)

    return render(request, 'update_movie.html', {'form': form, 'movie': movie})
def update_list(request):
    form = MovieSearchForm(request.GET)
    movies = Movies.objects.all()
    template=loader.get_template('updatelist.html')
    context={
        'movies':movies,
    }
    return HttpResponse(template.render(context,request))
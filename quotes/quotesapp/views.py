from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView
from django.contrib import messages

from .models import Quote, Author, Tag
from .forms import AddAuthorForm, AddQuoteForm

def quotes(request):
    quotes = Quote.objects.all()
    paginator = Paginator(quotes, 10)
    page_number = request.GET.get('page')
    quotes_page = paginator.get_page(page_number)
    
    return render(request, 'quotesapp/quotes.html', {'quotes_page': quotes_page})

def author_info(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'quotesapp/author.html', {'author': author})

#@login_required
def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotesapp:quotes')
    else:
        form = AddAuthorForm()

    return render(request, 'quotesapp/add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = AddQuoteForm(request.POST)
        if form.is_valid():
            quote_text = form.cleaned_data['quote']
            tags_name = [tag_name.strip() for tag_name in form.cleaned_data['tags'].split(',')]

            if form.cleaned_data['author'] is None:
                request.session['quote'] = form.cleaned_data['quote']
                request.session['tags'] = form.cleaned_data['tags']
                request.session['check_author_group'] = form.cleaned_data['check_author_group']
                request.session['author_input'] = form.cleaned_data['author_input']
                return redirect('quotes:new_author')

            quote = Quote(quote=quote_text, author=form.cleaned_data['author'])
            quote.save()

            for tag_name in tags_name:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                quote.tags.add(tag)
            return redirect('/')
    else:
        if 'author_input' in request.session:
            form = AddQuoteForm(initial={
                'quote': request.session['quote'],
                'tags': request.session['tags'],
                'author_input': request.session['author_input'],
                'check_author_group': request.session['check_author_group'],
            })
        else:
            # If there is no form data in the session, create a new empty form
            form = AddQuoteForm()
    return render(request, 'quotesapp/add_quote.html', {'form': form})

def quotes_by_tag(request, tag_name):
    quotes = Quote.objects.filter(tags__name=tag_name)
    paginator = Paginator(quotes, 10)  # показывать по 10 записей на странице.

    page_number = request.GET.get('page')
    quotes_page = paginator.get_page(page_number)

    tag = Tag.objects.get(name=tag_name)
    tag.popularity += 1
    tag.save()

    top_tags = Tag.objects.order_by('-popularity')[:5]

    return render(request, 'quotes/index.html', {'quotes_page': quotes_page, 'top_tags': top_tags})
    
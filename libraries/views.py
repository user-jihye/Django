from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    return render(request, 'libraries/home.html')


def recommend(request):
    API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
    API_KEY = 'ttbzkfkzktm1727001'
    params = {
        'ttbkey': API_KEY,
        'MaxResults' : 20,
        'start' : 1,
        'QueryType' : 'ItemNewAll',
        'SearchTarget' : 'Book',
        'Version' : '20131101',
        'output' : 'js',
    }
    response=requests.get(API_URL,params=params).json()
    items = response.get('item')
    books = []

    for item in items:
        books.append({
            'title' : item.get('title'),
            'author' : item.get('author')
        })
    context = {
        'books' : books
    }

    return render(request, 'libraries/recommend.html', context)


def bestseller(request):
    API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
    API_KEY = 'ttbzkfkzktm1727001'
    params = {
        'ttbkey': API_KEY,
        'MaxResults' : 20,
        'start' : 1,
        'QueryType' : 'Bestseller',
        'SearchTarget' : 'Book',
        'Version' : '20131101',
        'output' : 'js',
    }
    response=requests.get(API_URL,params=params).json()
    items = response.get('item')
    books = []

    for item in items:
        books.append({
            'title' : item.get('title'),
            'author' : item.get('author')
        })
    context = {
        'books' : books
    }
    return render(request, 'libraries/bestseller.html', context)
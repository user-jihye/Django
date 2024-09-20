from django.urls import path
from . import views

app_name = 'libraries'

urlpatterns = [
    # libraries/recommend/
    path('recommend/', views.recommend, name = 'recommend'),
    # libraries/bestseller
    path('bestseller/', views.bestseller, name='bestseller'),
]

# libraries:recommend >> libraries/recommend/
# libraries:bestseller >> libraries/bestseller/
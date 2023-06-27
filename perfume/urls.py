from django.urls import path

from perfume import views

# from product import views

app_name = 'perfume'

urlpatterns = [
    path('year90/', views.year_90, name='year90')
]
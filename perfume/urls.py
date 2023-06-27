from django.urls import path

from perfume import views

# from product import views

app_name = 'perfume'

urlpatterns = [
    path('year90/', views.list_memory, name='year90'),
    path('add_memory/', views.write_memory, name='write_memory'),
    path('detail/<int:pk>/', views.detail_memory, name='detail_memory')
    # path('year00/', views.year_90, name='year90'),
    # path('year10/', views.year_90, name='year90')
]


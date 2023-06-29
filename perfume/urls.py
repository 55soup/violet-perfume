from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from perfume import views

# from product import views

app_name = 'perfume'

urlpatterns = [
    path('year90/', views.list_memory90, name='year90'),
    path('year00/', views.list_memory00, name='year00'),
    path('year10/', views.list_memory10, name='year10'),
    path('add_memory/', views.write_memory, name='write_memory'),
    path('detail/<int:pk>/', views.detail_memory, name='detail_memory'),
    path('comment_write/<int:pk>/', views.comment_write, name="comment_write"),
    # path('comment/<int:pk>/', views.write_comments, name='write_comment'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


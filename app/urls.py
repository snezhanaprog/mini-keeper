from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.directory_list, name='directory_list'),
    path('directory/<int:pk>/', views.directory_detail, name='directory_detail'),
    path('directory/add/', views.add_directory, name='add_directory'),
    path('directory/<int:parent_id>/add/', views.add_directory, name='add_subdirectory'),
    path('directory/<int:directory_id>/add_record/', views.add_record, name='add_record'),
    path('directory/<int:directory_id>/record/<int:record_id>/delete/', views.del_record, name='del_record'),
    path('directory/<int:directory_id>/delete/', views.del_directory, name='del_directory'),
    path('directory/<int:directory_id>/record/<int:record_id>/change/', views.change_record, name='change_record'),
    path('directory/<int:directory_id>/change/', views.change_directory, name='change_directory'),
    path('directory/<int:parent_id>/change/<int:directory_id>', views.change_directory, name='change_subdirectory'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
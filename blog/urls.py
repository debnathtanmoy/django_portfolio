from django.urls import path
from . import views
app_name = 'blog' # use this specify the blog name and use it in the html 
urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.details, name='details'),
]
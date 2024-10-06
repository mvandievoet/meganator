from django.urls import path
from . import views

app_name = 'blog'  # This registers the 'blog' namespace

urlpatterns = [
    path('', views.index, name='index'),  # Homepage for blog posts
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # Individual blog post
    path('<str:section>/', views.section_view, name='section_view'), # Firlered blog post view
]
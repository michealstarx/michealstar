from django.urls import path

from .views import home_page, blog_home, blog_details, images

urlpatterns = [
    path('', home_page, name='home_page'),
    path('blog/', blog_home, name='blog_home'),
    path('blog/<int:id>/', blog_details, name='blog_details'),
    path('images', images, name='images')
]
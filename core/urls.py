from django.urls import path

from .views import index, user_login, register, detailedView,search, blog

app_name = 'core'
urlpatterns = [
    path("", index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog/<str:slug>', detailedView, name='detailed-blog'),
    path('search/', search, name='search'),
    path('login/', user_login, name='login'),
    path('sign-up/', register, name='signup'),
]
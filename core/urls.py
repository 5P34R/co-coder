from django.urls import path

from .views import index, user_login,logout_view, register, detailedView,search, blog, add_notes

app_name = 'core'
urlpatterns = [
    path("", index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog/<str:slug>', detailedView, name='detailed-blog'),
    path('search/', search, name='search'),
    path('login/', user_login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('sign-up/', register, name='signup'),

    path('add-notes/', add_notes, name="add-note")
]
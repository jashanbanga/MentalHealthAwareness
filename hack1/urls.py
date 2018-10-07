from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.post),
    path('post/new',views.newpost),
    path('signup/',views.signup),
    path('login/',views.login),
    path('logout/',views.logout),
    path('message',views.message),
    path('youth',views.youth),
    path('gay',views.gay),
    path('diaster',views.disaster),
    path('fact',views.fact),
    path('faq',views.faq),
    path('login/index',views.post),
    path('signup/index',views.post),
]

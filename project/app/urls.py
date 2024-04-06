from django.contrib import admin
from django.urls import path
from app.views import RegisterView, login_view, logout_view, AbouMeViews
from django.contrib.auth.views import LoginView

app_name = 'app'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='registration'),
    path('login/', LoginView.as_view(template_name='app/logon.html', redirect_authenticated_user=True), name='login'),
    path('logout/', logout_view, name='logout'),
    path("about-me/", AbouMeViews.as_view(), name="about-me"),
]
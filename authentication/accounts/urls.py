from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.signup,name="signup"),
    path('login',LoginView.as_view(),name="login"),
    path('logout',LogoutView.as_view(next_page="home"),name="logout"),
    path('accounts/profile/',views.profile,name="profile"),
    path('edit_profile',views.EditProfile,name="edit_profile"),
]
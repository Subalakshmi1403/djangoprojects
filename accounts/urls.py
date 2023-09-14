from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView

urlpatterns = [
    path('',views.index, name="index"),
    path('register',views.register, name="register"),
    path('profile',views.profile,name="profile"),
    path('login',LoginView.as_view(),name="login"),
    path('logout',LogoutView.as_view(next_page='index'),name="logout"),
    path('password_reset/',PasswordResetView.as_view(),name="password_reset"),
    path('password_reset_confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('password_reset/done',PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('password_reset/complete',PasswordResetCompleteView.as_view(),name="password_reset_complete"),

    
]
    
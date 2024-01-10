from django.urls import path
from userauths.views import signup, login_view, logout_view, activate
from userauths.views import ResetPasswordView
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetCompleteView, CustomPasswordResetConfirmView

app_name = 'userauths'

urlpatterns = [
    path("signup/", signup, name='signup'),
    path("login/", login_view, name='login'),
    path("logout/", logout_view, name='logout'),
    path('activate/<str:uidb64>/<str:token>/', activate, name='activate'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         CustomPasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         CustomPasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
]

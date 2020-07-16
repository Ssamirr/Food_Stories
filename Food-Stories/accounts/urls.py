from django.urls import path , re_path
from accounts.views import UserProfile , CreateRegisterView , RegisterUpdateView , CustomLoginView , activate ,\
    CustomPasswordChangeView , ForgetPasswordView , CustomPasswordResetConfirmView
from django.contrib.auth.views import LogoutView

# app_name = "accounts"


urlpatterns = [
    path('user-profile/',UserProfile.as_view(),name = 'user_profile'),
    path('register/', CreateRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    re_path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate, name='activation'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit_profile/<str:slug>', RegisterUpdateView.as_view(), name='edit_profile'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('forget-password/', ForgetPasswordView.as_view(), name='forget_password'),
    re_path(r'password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
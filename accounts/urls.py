from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path("signup/",views.Signup.as_view(),name='signup'),
    path("login/", auth_views.LoginView.as_view(), name='login'),
#     path("accounts/password_change /",
#          auth_views.PasswordChangeView.as_view(), name='password_change'),
#     path("accounts/password_change/done / ",
#          auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
#     path("accounts/password_reset / ",
#          auth_views.PasswordResetView.as_view(), name='password_reset'),
#     path("accounts/password_reset/done / ",
#          auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     path("accounts/reset/<uidb64 > / < token > /  ",
#          auth_views.PasswordResetDoneView.as_view(), name='password_reset_confirm'),
#     path("accounts/reset/done /  ",
#          auth_views.PasswordResetDoneView.as_view(), name='password_reset_complete'),
#     #path("logout/",auth_views.LogoutView.as_view(),name='logout'),

]

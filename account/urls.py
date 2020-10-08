from django.urls import path, include
from .views import user_login, dashboard, register, edit
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('login/', user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', dashboard, name='dashboard'),

    path('', include('django.contrib.auth.urls')),

    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),

    # # change password urls
    # path('password_change/',
    #      auth_views.PasswordChangeView.as_view(),
    #      name='password_change'),
    # path('password_change/done/',
    #      auth_views.PasswordChangeDoneView.as_view(),
    #      name='password_change_done'),
    #
    # # rest password
    # path('pssword_reset/',
    #      auth_views.PasswordResetView.as_view(),
    #      name='password_reset'),
    # path('pssword_reset/done/',
    #      auth_views.PasswordResetDoneView.as_view(),
    #      name='password_reset_done'),
    # path('rest/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(),
    #      name='password_reset_confirm'),
    # path('reset/done/',
    #      auth_views.PasswordResetCompleteView.as_view(),
    #      name='password_reset_complete'),
]

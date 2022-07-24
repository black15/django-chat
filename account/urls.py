from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path("profile/<user_id>/", account_view , name="profile"),
    path("profile/<user_id>/edit/", edit , name="edit"),
    path("profile/<user_id>/friends/", list_friends , name="list-friends"),
    path("profile/<user_id>/frequest/", list_friend_requests , name="list-friend-requests"),
    path("profile/<id>/add/", send_friend_request , name="add-friend"),
    path("profile/<id>/accept/", accept_friend_request , name="accept-friend"),
    path("profile/<user_id>/remove/", remove_friend , name="remove-friend"),
    path('register/', register, name="register"),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
     name='password_reset_complete'),
]
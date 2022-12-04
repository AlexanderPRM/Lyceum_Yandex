from users.forms import (UserLoginForm, PasswordChangeForm,
                         CustomPasswordResetForm,
                         CustomPasswordResetConfirmForm)
from django.urls import path
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView,
                                       PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)
from users.views import profile, register, users_list, user_detail


app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(
                                    template_name='pages/users/login.html',
                                    authentication_form=UserLoginForm
                                    ), name='login'),
    path('logout/', LogoutView.as_view(
                                template_name='pages/users/logged_out.html',
                                ), name='logout'),
    path('password_change/', PasswordChangeView.as_view(
                                template_name='pages/users/'
                                              'password_change.html',
                                form_class=PasswordChangeForm
                                ), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(
                            template_name='pages/users/'
                                          'password_change_done.html'
                            ), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(
                                template_name='pages/users/'
                                              'password_reset.html',
                                form_class=CustomPasswordResetForm
                                ), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
                                template_name='pages/users/'
                                              'password_reset_done.html',
                                ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
                                template_name='pages/users/'
                                              'password_reset_confirm.html',
                                form_class=CustomPasswordResetConfirmForm
                                ), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
                            template_name='pages/users/'
                                          'password_reset_complete.html'
                            ), name='password_reset_complete'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('users_list/', users_list, name='users_list'),
    path('user_detail/<pk>', user_detail, name='user_detail')
]

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.http import Http404

from users.forms import UserUpdateForm, CustomUserCreationForm
from users.models import User


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    login_url = reverse_lazy("users:login")
    template_name = "pages/users/profile.html"

    def get_success_url(self) -> str:
        success_url = reverse_lazy("users:profile", kwargs={"pk": self.request.user.id})
        return success_url

    def get(self, request, *args: str, **kwargs):

        if request.user.id == int(kwargs["pk"]) or request.user.is_superuser:
            return super().get(request, *args, **kwargs)
        raise Http404


class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "pages/users/register.html"

    def get_success_url(self) -> str:
        success_url = reverse_lazy("users:login")
        return success_url


class UsersList(ListView):
    model = User
    template_name = "pages/users/users_list.html"
    context_object_name = "users"

    def get_queryset(self):
        return User.objects.filter(is_active=True)


class UserDetail(DetailView):
    model = User
    template_name = "pages/users/user_detail.html"
    context_object_name = "user"

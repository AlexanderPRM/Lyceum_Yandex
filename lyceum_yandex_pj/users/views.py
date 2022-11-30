from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.forms import UserUpdateForm, CustomUserCreationForm
# from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from users.models import User


@login_required
def profile(request):
    user_form = UserUpdateForm(request.POST or None, instance=request.user)
    context = {
            'form': user_form,
            'user': request.user
        }
    if user_form.is_valid():
        user_form.save()
        # messages.success(request, f'Your account has been updated!')
        return redirect('users:profile')
    return render(request, 'pages/users/profile.html', context)


def register(request):
    form = CustomUserCreationForm(request.POST or None)
    context = {
            'form': form
        }
    if form.is_valid():
        form.save()
        # username = form.cleaned_data.get('username')
        # messages.success(request, f'Создан аккаунт {username}!')
        return redirect('users:profile')
    return render(request, 'pages/users/register.html', context=context)


def users_list(request):
    users_list = User.objects.filter(is_active=True)
    context = {
        'users': users_list
    }
    return render(request, 'pages/users/users_list.html', context=context)


def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    context = {
        'user': user
    }
    return render(request, 'pages/users/user_detail.html', context=context)

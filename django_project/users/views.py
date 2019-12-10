from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# A form that django already made, just needs to be imported.
from django.contrib import messages
from .forms import UserRegisterForm

# messages example:
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.errar


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created For {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})

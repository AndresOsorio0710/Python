from beauty_public_area_app.forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


class RegisterUserView():
    def beauty_public_register_user(request):
        is_redirect = False
        template = 'registration/register_user.html'
        data = {
            'form' : CustomUserCreationForm()
        }
        if request.method == 'POST':
            form = CustomUserCreationForm(data=request.POST)
            if form.is_valid():
                user = User()
                user.username = form.cleaned_data["username"]
                user.first_name = form.cleaned_data["first_name"]
                user.last_name = form.cleaned_data["last_name"]
                user.email = form.cleaned_data["email"]
                user.set_password(form.changed_data["password1"])
                user.save()
                messages.success(request, "Invalid data.")
                is_redirect = True
                template = 'beauty_public_home'
            else:
                data["form"] = form
                messages.warning(request, "Invalid data.")
        if is_redirect:
            return redirect(to = template)
        return render(request, template, data)
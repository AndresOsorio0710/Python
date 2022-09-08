from beauty_person_app.forms import PersonForm
from beauty_person_app.models import Person
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

class PersonView():
    def person_register(request):
        is_redirect = False
        template = 'registration/register_user.html'
        data = {'form': PersonForm}
        if request.method == 'POST':
            form = PersonForm(data=request.POST)
            try:
                existe = Person.objects.get(phone_number=form.data['phone_number'], email=form.data['email'])
                messages.warning(request, "Invalid data, phone number or email is already in use.")
                data["form"] = form
            except:
                if form.is_valid():
                    person = Person()
                    person.first_name = form.cleaned_data["first_name"].upper()
                    person.last_name = form.cleaned_data["last_name"].upper()
                    person.email = form.cleaned_data["email"].upper()
                    person.phone_number = form.cleaned_data["phone_number"]
                    person.date_of_birth = form.cleaned_data["date_of_birth"]
                    person.gender = form.cleaned_data["gender"].upper()
                    person.save()
                    user = User()
                    user.username = person.phone_number
                    user.first_name = person.first_name
                    user.last_name = person.last_name
                    user.email = person.email
                    user.set_password(person.phone_number)
                    user.save()
                    messages.success(request, "Seuccessfully registered user.")
                    is_redirect = True
                    datemplate = 'beauty_public_home'
                else:
                    data["form"] = form
                    messages.warning(request, "Invalid data.")
        if is_redirect:
            return redirect(to = template)
        return render(request, template, data)





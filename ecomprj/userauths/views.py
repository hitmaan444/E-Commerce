from django.shortcuts import render, redirect
from userauths.forms import UserRegisterFrom
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import logout

User = settings.AUTH_USER_MODEL


def register_view(request):
    if request.method == "POST":
        form = UserRegisterFrom(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"hey {username}, your account was created succsesfuly.")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1']
                                    )
            login(request, new_user)
            return redirect("core:index")




    else:

        form = UserRegisterFrom()

    context = {
        'form': form

    }

    return render(request, "userauths/sign-up.html", context)



def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"hey you are already logged in")
        return redirect("core:index")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # try:
        #     user = User.objects.get(email=email)


        # except:
        #     messages.warning(request, f"User with {email} does not excist")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request,user)
            messages.success(request, "you are logged in")
            return redirect("core:index")
        else:
            messages.warning(request, "user does not excist")

    context = {

    }

    return render(request, "userauths/sign-in.html", context)



def logout_view(request):
    logout(request)
    messages.success(request,"you logged out")
    return redirect("core:index")





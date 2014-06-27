from django.shortcuts import render,redirect, get_object_or_404
from django.utils.translation import ugettext as _
from forms import SignupForm,LoginForm, ProfileForm
from django.views.generic import ListView
from models import UserProfile
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.messages import info, error


class CompanyList(ListView):
    model = UserProfile
    template_name = 'company_list.html'
    context_object_name = 'companies'


# Create your views here.
def login(request, template="accounts/account_login.html"):
    """
    Login form.
    """
    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        authenticated_user = form.save()
        if authenticated_user is not None:
            if authenticated_user.is_active:
                auth_login(request, authenticated_user)
                # Redirect to a success page.
                return  redirect('core.dashboard')
            else:
                return  redirect('core.dashboard')

    context = {"form": form, "title": _("Log in")}
    return render(request, template, context)


def signup(request, template="accounts/account_signup.html"):
    """
    Signup form.
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            #if not new_user.is_active:
            #    if settings.ACCOUNTS_APPROVAL_REQUIRED:
            #        send_approve_mail(request, new_user)
            #        info(request, _("Thanks for signing up! You'll receive "
            #                        "an email when your account is activated."))
            #    else:
            #        send_verification_mail(request, new_user, "signup_verify")
            #        info(request, _("A verification email has been sent with "
            #                        "a link for activating your account."))
            #    return redirect(next_url(request) or "/")
            #else:
            #    info(request, _("Successfully signed up"))
            #    auth_login(request, new_user)
            #    return login_redirect(request)
    else:
        form = SignupForm()

    context = {"form": form, "title": _("Sign up")}
    return render(request, template, context)


def logout(request):
    auth_logout(request)
    return redirect('login')


def profile(request, template ='accounts/account_profile.html'):
    p = get_object_or_404(UserProfile, user_id=request.user.pk)
    #load form initial value from models
    form = ProfileForm(request.POST or None,initial={'company':p.company})
    #print p
    #print p.company
    if request.method == "POST" and form.is_valid():
        company = form.cleaned_data.get("company")
        p.company = company
        p.save()
        info(request, _("Profile updated"))

    context = {"form": form, "title": _("Update Profile"), "profile":p}
    return render(request, template, context)

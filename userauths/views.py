from django.shortcuts import redirect, render

from userauths.models import Dashboard_User
from .form import UseRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from .models import Dashboard_User

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetConfirmView

User = settings.AUTH_USER_MODEL


# email verfication
class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + str(timestamp) + str(user.is_active)


account_activation_token = AccountActivationTokenGenerator()


def signup(request):
    new_user = None
    if request.method == 'POST':
        form = UseRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_active = False
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hey {username}, your account was created successfully.")

            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('acc_active_email.html', {
                'user': new_user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                'token': account_activation_token.make_token(new_user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.content_subtype = 'html'
            email.send()
            messages.success(request,f"Please confirm your email address to complete the registration.<a href='{('https://mail.google.com/')}'>Click here</a> to go to Gmail.")
            return redirect('userauths:signup')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
            return render(request, 'signup.html', {'form': form})
    else:
        form = UseRegisterForm()
    context = {'form': form}
    return render(request, 'signup.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            request.session['username'] = user.username
            return redirect('core:index')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('userauths:login')
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")

    return redirect("core:index")


def home(request):
    return render(request, "home.html")


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        # Activate the user account
        user.is_active = True
        user.save()
        new = Dashboard_User(user=user)
        new.save()
        # Redirect to the login page
        return redirect('userauths:login')
    else:
        return HttpResponse('Activation link is invalid!')


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    # subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the addre ss you registered with, and check your spam folder."
    success_url = reverse_lazy('userauths:login')


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'  # Set your custom template name
    # Override success_url attribute
    success_url = reverse_lazy('userauths:password_reset_complete')


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'  # Set your custom template name
    # Override success_url attribute
    success_url = 'userauths:login'

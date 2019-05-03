from django.shortcuts import render, redirect , get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.core.mail import EmailMessage
from .models import User
from .forms import EditProfileForm
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash


# Create your views here.

def index(request):
    Hotels = request.user 
    return render(request, 'index.html', {'hotel_images' : Hotels}) 

    # return HttpResponse("Hello, world. You're at the polls index.")




# class SignUp(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        return render_to_response('activation_done.html')
    else:
        return HttpResponse('Activation link is invalid!')

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES , instance=request.user)

        if form.is_valid():
            form.save()
            args = {'form': form}
            return redirect('view_profile_with_pk')
            # return render(request, 'edit_profile.html', args)
        # else:
        #     return HttpResponse(form.errors)
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)
    form = EditProfileForm(instance=request.user)
    args = {'form': form}
    return render(request, 'edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('view_profile_with_pk')
        else:
            return redirect('change_password')
            
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'change_password.html', args)


def user_delete(request ):
    user = request.user
    obj = get_object_or_404(User, id=user.id)
    print (obj)
    if request.method == 'POST':
        # obj.delete()
        user.is_active = False
        user.save()
        # messages.success( request , "This has been deleted.")
        return redirect("home")
    context = {
        "object": obj
    }
    return render(request,"confirm_delete.html",context)
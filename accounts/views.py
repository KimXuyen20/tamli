from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from accounts.forms import RegistrationForm, UserForm, UserProfileForm
from accounts.models import Account, UserProfile
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from django.contrib.auth.views import redirect_to_login


from doctor.forms import DoctorForm

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('profile')
    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            # username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
               
                email=email,
                password=password
            )
            user.role = Account.CUSTOMER
            user.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')  # Thêm chuyển hướng sau khi đăng ký thành công
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('home')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.info(request, 'You are logged out.')
    return redirect('login')



from django.shortcuts import render

# Create your views here.


def registerDoctor(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        d_form = DoctorForm(request.POST, request.FILES)
        
        # Kiểm tra cả hai form
        if form.is_valid() and d_form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]  # Lấy phần đầu của email làm username
            
            # Tạo đối tượng User
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.role = Account.DOCTOR
            user.save()
            
            # Tạo đối tượng Doctor từ d_form
            doctor = d_form.save(commit=False)
            doctor.user = user
            doctor_name = d_form.cleaned_data['doctor_name']
            doctor.doctor_slug = slugify(doctor_name)+'-'+str(user.id)
            user_profile = UserProfile.objects.get(user=user)
            doctor.user_profile = user_profile
            doctor.save()
            
            messages.success(request, 'Your account has been registered sucessfully! Please wait for the approval.')
            return redirect('login')
        else:
            # In lỗi từ cả hai form
            print('Invalid form:')
            print(form.errors)
            
    else:        
        form = UserForm()
        d_form = DoctorForm()

    context = {
        'form': form,
        'd_form': d_form,
    }
    
    return render(request, 'accounts/registerDoctor.html', context)



@login_required
def edit(request):
    userprofile = get_object_or_404(UserProfile, user= request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect('edit')
    else:
        user_form = UserForm(instance=request.user)
        profile_form= UserProfileForm(instance=userprofile)
    context ={
        'user_form': user_form,
        'profile_form': profile_form,
    }        
    return render(request,'accounts/profile_edit.html',context)

def profile_view(request, email=None):
    if email:
        profile = get_object_or_404(Account, email=email).profile
    else:
        try:
            profile = request.user.profile
        except:
            return redirect_to_login(request.get_full_path())
    return render(request, 'accounts/profile.html', {'profile':profile})


@login_required
def profile_settings_view(request):
    return render(request, 'accounts/profile_settings.html')




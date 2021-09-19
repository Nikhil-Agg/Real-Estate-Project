import contacts
from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check password
        if password == password2:

            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'User with this email already registered')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email,
                     first_name=first_name, last_name=last_name)

                    # login after success
                    # auth.login(request, user)
                    # messages.success(request, 'You are siccessfully logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You are successfully registered and can Log In')
                    return redirect('login')

        else:
            messages.error(request, 'Passwords did not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):

    if request.method == 'POST':
        # Login
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are successfully logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):

    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are succesfully logged out')
        return redirect('index')

def dashboard(request):

    contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': contacts
    }
    return render(request, 'accounts/dashboard.html', context)
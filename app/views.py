from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponseRedirect, HttpResponseRedirect
from django.contrib import messages
from .models import Contact ,  Picture
from .forms import ContactForm,PictureForm
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django import forms



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q 
from django.contrib import messages





def index(request):
     if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact.name=name
        contact.phone=phone
        contact.subject=subject
        contact.message=message
        contact.save()

        messages.success(request, 'Your form was submitted successfully!')
     return render(request,'index.html')



def adminclick_view(request):
    if request.user.is_authenticated:
        return redirect('admin-dashboard')
    return redirect('adminlogin')

def afterlogin_view(request):
        return redirect('admin-dashboard')
 
@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    return render(request,'admin/dashboard.html')

def admin_404(request):
    return HttpResponseNotFound('<h1>Page not found</h1>')


@login_required(login_url='adminlogin')
def admin_contact_view(request):
   contact_list = Contact.objects.all()
   paginator = Paginator(contact_list, 5) # Change the number of contacts per page here
   page_number = request.GET.get('page')
   contacts = paginator.get_page(page_number)
   context = {'contacts': contacts}
   return render(request, 'admin/contact.html', context)



@user_passes_test(lambda u: u.is_authenticated and u.is_staff)
@login_required(login_url='adminlogin')
def admin_edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact updated successfully')
            return redirect('admin-contact')
    else:
        form = ContactForm(instance=contact)

    context = {'form': form, 'contact_id': contact_id}
    return render(request, 'admin/edit_contact.html', context)


@login_required(login_url='adminlogin')
def admin_delete_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
       
    return redirect('admin-contact')



@login_required(login_url='adminlogin')
def upload_picture(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
    else:
        form = PictureForm()
    return render(request, 'admin/admin-upload.html', {'form': form})

def view_pictures(request):
    pictures = Picture.objects.all()
    return render(request, 'view_pictures.html', {'pictures': pictures})






def admin_password_reset(request):
    if request.method == 'POST':
        username_or_email = request.POST['username_or_email']
        new_password = request.POST['new_password']

        try:
            # Check if the username_or_email exists in the User model (you can customize this to your actual user model)
            user = User.objects.get(Q(username=username_or_email) | Q(email=username_or_email))
        except User.DoesNotExist:
            # If the user is not found, show an error message
            messages.error(request, 'Admin not found with the provided username or email.')
            return redirect('admin_password_reset')

        # Update the user's password
        user.set_password(new_password)
        user.save()

        messages.success(request, 'Password reset successful.')
        return redirect('adminlogin')  # Redirect to login page or any other appropriate page

    return render(request, 'admin/admin_password_reset.html')
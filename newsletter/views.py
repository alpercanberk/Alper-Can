from django.conf import settings
from django.shortcuts import render
from .forms import ContactForm,SignUpForm
from django.core.mail import send_mail
# Create your views here.
def home(request):
	title="Welcome"
	form=SignUpForm(request.POST or None)
	context = {
		"template_title":title,
		"form":form,
	}

	if form.is_valid():
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name :
			full_name = "New full name"
		instance.full_name=full_name
		instance.save()
		context = {

		"template_title":"Thank you",
		
					


		}
	return render(request,"home.html",context)
def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email=form.cleaned_data.get("email")
		form_message=form.cleaned_data.get("message")
		form_full_name=form.cleaned_data.get("full_name")
		
		subject='Site Contact Form'
		from_email =settings.EMAIL_HOST_USER
		to_email = [from_email,'alper.nova.ac@gmail.com']
		contact_message="%s: %s via %s"%(form_full_name,form_message,form_email)




		send_mail(subject,contact_message,from_email,to_email,fail_silently=True)
	context={

		"form":form

	}
	return render(request,"forms.html",context)
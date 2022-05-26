from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf

from .models import Feedback
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    c ={}
    c.update(csrf(request))
    return render_to_response('contact/contact.html', c)


def submit(request):
    cust_name = request.POST.get('cname', '')
    cust_email = request.POST.get('cemail', '')
    query = request.POST.get('query', '')
    cust_id = request.POST.get('cid', '')
    f = Feedback(query=query, cust_id=cust_id, cust_name=cust_name, cust_email=cust_email)
    f.save()
    subject = "Thank You for Submiting Feedback"
    message = "\n\nThank you for contacting us. we will reply to your query soon.\n\n-Exam Hub.\n"
    from_email = settings.EMAIL_HOST_USER
    to_list = [cust_email]
    send_mail(subject, message, from_email, to_list, fail_silently=True)
    return HttpResponseRedirect('/contact/complete/')

def Complete(request):
    return render_to_response('contact/complete.html')
from django.shortcuts import render, redirect
from .forms import ComplaintForm
from .models import Complaint
from datetime import datetime
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email="testprojectdjango17@gmail.com"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, "srlgpuotsivzmcqm")
print("logged in")

def send_email(sender_email, text_to_send, receiver_email):

    # Create a MIME object
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Agent Complaint Response"

    # Attach the text to the email
    body = MIMEText(text_to_send, "plain")
    message.attach(body)

    try:
        # Establish a connection to the SMTP server
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
        

def first(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
            "complaints_group",
            {
                "type": "complaint_update",
                "message": "New complaint data available",
            },
        )
            return redirect('success')
    else:
        form = ComplaintForm()
    
    types = ['Electronics','Clothing','Furniture','Shoes','Phones','Appliances','TV & Laptop']
    return render(request, 'customer.html', {'form': form, 'products' : types})

def success(request):
    return render(request, 'success.html')

from django.shortcuts import render
from datetime import datetime

def admin_dashboard(request):
    current_hour = datetime.now().hour
    START_TIME = 9 #OFFICE START TIME
    END_TIME = 23 #OFFICE END TIME
    if START_TIME <= current_hour < END_TIME:
        print("Sending WebSocket update...")
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "complaints_group",
            {
                "type": "complaint_update",
                "message": "New complaint data available",
            },
        )
        if request.method == 'POST':
            for key, value in request.POST.items():
                if key != 'csrfmiddlewaretoken':
                    complaint = Complaint.objects.get(phone_number=key)
                    if complaint.feedback != value:  # Check if the feedback has changed
                        complaint.feedback = value
                        complaint.save()
                        print("Email: ", complaint.email)  # Print the email
                        send_email(sender_email,complaint.feedback,complaint.email)
            return redirect('admin_dashboard')
        else:
            complaints = Complaint.objects.all()
            return render(request, 'admin_dashboard.html', {'complaints': complaints})
    else:
        return render(request, 'countdown.html', {'start_time': START_TIME})

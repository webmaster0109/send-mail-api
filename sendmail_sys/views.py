from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
import json
from .utils import send_mail_func
import re
from django.utils.html import strip_tags

def login_attempt(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return JsonResponse({'status': 'error', 'message': 'All fields are required'}, status=400)
        
        user_obj = authenticate(request, username=username, password=password)

        if user_obj:
            login(request, user_obj)
            return JsonResponse({'status': 'success', 'message': 'login successfully'}, status=200)
        
        return JsonResponse({'status': 'error', 'message': 'Invalid credentials'}, status=401)
    
    if request.user.is_authenticated:
        return redirect('mail_sys')
    
    return render(request, template_name="login.html")

def logout_attempt(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/account/login/')
def homepage(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Parse JSON payload
            emails = data.get('emails')
            subject = data.get('subject')
            content = data.get('textareaData')

            if not emails or not content:
                return JsonResponse({'status': 'error', 'message': 'All fields are required'}, status=400)
            
            plain_text_content = re.sub(r'</p>\s*', '\n', content)  
            plain_text_content = strip_tags(plain_text_content).strip()

            email_list = [email.strip() for email in emails.split(',') if email.strip()]
            text_content = plain_text_content
            template_path = "mail_template.html"

            context = {
                'content': content
            }

            
            send_mail_func(subject, text_content, template_path, context, email_list)

            return JsonResponse({'status': 'success', 'message': 'Send mail successfully'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON payload'}, status=400)
        
    return render(request, template_name="index.html")
    
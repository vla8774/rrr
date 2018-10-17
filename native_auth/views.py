
import io, base64, json, mimetypes, string, random, re, uuid, os
import cv2
import numpy as np
import requests
import django
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth import login,  authenticate
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.decorators import method_decorator
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

#############################################################################
# Sign in

@csrf_exempt
def signin(request):

    template = loader.get_template("auth/log-in.html")
    response = HttpResponse(template.render({}, request))
    
    return response

@csrf_exempt
def do_signin(request):
    
    if request.method == "POST":
        
        _login = request.POST["e-mail"]
        password = request.POST.get("password")
        img = request.POST["photo"]

        user = authenticate(username = _login, password = password)

        if user is None:

            return JsonResponse({ "error" : "Bad login, password or person id", "info" : response }, status = 500)

        else:
            
            if user.is_active:
                
                login(request, user)
                
                return JsonResponse({ "info" : response })

            return JsonResponse({ "error" : "Account not activated", "info" : response }, status = 500)
            
    return JsonResponse({ "error" : "Please, sign in", "info" : response }, status = 500)

#############################################################################
# Sign up

@csrf_exempt
def signup(request):

    template = loader.get_template("auth/sign-up.html")
    response = HttpResponse(template.render({}, request))
    
    return response

@csrf_exempt
def signup_done(request):

    template = loader.get_template("auth/thank-you.html")
    response = HttpResponse(template.render({}, request))
    
    return response

@csrf_exempt
def do_signup(request):

    email = request.POST["e-mail"]
    password = request.POST["password"]
    img = request.POST.get("face_video")

    # print("--->", email, raw_video)
    
    if raw_video is None:

        person_id = ""

    else:

        person_id, response = create_person_id(raw_video, email)

        if person_id is None:

            return JsonResponse({ "error" : "Unable to create person id (%s)" % response }, status = 500)

    model = get_user_model()
    data = \
    {
        model.USERNAME_FIELD : email,
        model.EMAIL_FIELD : email,
        "password" : password,
        "person_id" : person_id
    }

    try:

        model._default_manager.db_manager("default").create_user(**data)
            
        return JsonResponse({ "login" : email, "password" : password, "person_id" : person_id })

    except django.db.utils.IntegrityError:

        return JsonResponse({ "error" : "User exists" }, status = 500)


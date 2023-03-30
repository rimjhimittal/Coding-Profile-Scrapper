from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
import requests

from .models import User,leetcode_acc

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from .models import User

class register(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        leetcode_name=request.data.get('leetcode_name')
        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'},
                            status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(email,password)
        user.save()
        if leetcode_name is not None or leetcode_name=='':
            account = leetcode_acc.objects.create(user=user,username=leetcode_name)
            account.save()
        return Response({'status':'success'},status=status.HTTP_201_CREATED)
    
class register_leetcode(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        user=request.user
        if (leetcode_acc.objects.filter(user=user).exists()):
            return Response({'error': 'leetcode account for this user already exists'},status=status.HTTP_400_BAD_REQUEST)
        leetcode_name = request.data.get('leetcode_name')
        if leetcode_name is None or leetcode_name=='':
            return Response({'error': 'Please provide leetcode name'},
                            status=status.HTTP_400_BAD_REQUEST)
        leetcode_acc.objects.create(user=user,username=leetcode_name)
        
        
        return Response({'status':'success'},status=status.HTTP_201_CREATED)
    
class login(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
       
        print(email,password)
        print()
        
        user = authenticate(request, email=email, password=password)

        if user is None:
            print("lol")
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
        token = Token.objects.get_or_create(user=user)

        data = {
            'key': token[0].key,
            'email': user.email,
        }

        return Response(data, status=status.HTTP_200_OK)
    
    
class getLeetcodeInfo(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        user=request.user
        if (leetcode_acc.objects.filter(user=user).exists()):
            account=leetcode_acc.objects.filter(user=user).first()
            d={
                'username':account.username,
                'name':account.name,
                'rank':account.rank,
                'photo_url':account.photo_url,
                'number_of_questions':account.number_of_questions,
                'last_solved':account.last_solved
            }
            return Response(d,status=status.HTTP_200_OK)
        else:
            return Response({'error':'leetcode account for this user does not exist'},status=status.HTTP_400_BAD_REQUEST)
    


from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
import requests

from .models import User,leetcode_acc,codechef_acc

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *

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
        if (codechef_acc.objects.filter(user=user).exists()):
            return Response({'error': 'leetcode account for this user already exists'},status=status.HTTP_400_BAD_REQUEST)
        leetcode_name = request.data.get('leetcode_name')
        if leetcode_name is None or leetcode_name=='':
            return Response({'error': 'Please provide leetcode name'},
                            status=status.HTTP_400_BAD_REQUEST)
        leetcode_acc.objects.create(user=user,username=leetcode_name)
        
        
        return Response({'status':'success'},status=status.HTTP_201_CREATED)

class register_codechef(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        user=request.user
        if (codechef_acc.objects.filter(user=user).exists()):
            return Response({'error': 'Codechef account for this user already exists'},status=status.HTTP_400_BAD_REQUEST)
        codechef_name = request.data.get('codechef_name')
        if codechef_name is None or codechef_name=='':
            return Response({'error': 'Please provide leetcode name'},
                            status=status.HTTP_400_BAD_REQUEST)
        codechef_acc.objects.create(user=user,username=codechef_name)
        
        
        return Response({'status':'success'},status=status.HTTP_201_CREATED)
    
class getUserInfo(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self,request):
        user=request.user
        data={}
        data['email']=user.email
        data['name']=user.name
        data['branch']=user.branch
        
        leetcode=leetcode_acc.objects.filter(user=user).first()
        if leetcode is not None:
            d={}
            d['username']=leetcode.username
            d['rank']=leetcode.rank
            d['photo_url']=leetcode.photo_url
            d['number_of_questions']=leetcode.number_of_questions
            d['last_solved']=leetcode.last_solved
            data['leetcode']=d
        
        codechef=codechef_acc.objects.filter(user=user).first()
        if codechef is not None:
            d={}
            d['username']=codechef.username
            d['global_rank']=codechef.global_rank
            d['country_rank']=codechef.country_rank
            d['rating']=codechef.rating
            d['stars']=codechef.stars
            d['photo_url']=codechef.photo_url
            d['number_of_questions']=codechef.number_of_questions
            data['codechef']=d
        return Response(data,status=status.HTTP_200_OK)
    
class login(APIView):
    
    def post(self, request):
        
        try:
            data=request.data
            serializer = LoginSerializer(data=data)
            if (serializer.is_valid()):
                email = serializer.data.get('email')
                password = serializer.data.get('password')
                user = authenticate(email=email, password=password)
                if user is None:
                    return Response({'error':'Invalid Credentials'},status=status.HTTP_400_BAD_REQUEST)
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
                
            return Response({'status':'400','data':serializer.errors})
        
        except Exception as e:
            print(e)



# class login(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')
       
#         print(email,password)
#         print()
        
#         user = authenticate(request, email=email, password=password)

#         if user is None:
#             print("lol")
#             return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
#         token = Token.objects.get_or_create(user=user)
#         print('done')
#         data = {
#             'key': token[0].key,
#             'email': user.email,
#         }

#         return Response(data, status=status.HTTP_200_OK)


# class TokenObtainPairWithEmailView(TokenObtainPairView):
    

#     def post(self, request, *args, **kwargs):
#         # print((request.data['email']))
#         data={}
#         data['email']=request.data['email']
#         data['password']=request.data['password']
#         serializer = UserSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
#         token = serializer.validated_data.get('access')
#         print("token",token)
#         response = super().post(request, *args, **kwargs)
#         response.data['email'] = user.email
#         return response


    
class getLeetcodeInfo(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        # user=request.user
        # if (leetcode_acc.objects.filter(user=user).exists()):
        #     account=leetcode_acc.objects.filter(user=user).first()
        result =[]
        accounts = leetcode_acc.objects.all().order_by('-number_of_questions')
        n=1
        for account in accounts:
            d={
                'serialNumber':n,
                'username':account.username,
                'name':account.name,
                'rank':account.rank,
                'photo_url':account.photo_url,
                'number_of_questions':account.number_of_questions,
                'last_solved':account.last_solved
            }
            result.append(d)
            n+=1
        return Response(result,status=status.HTTP_200_OK)

class getCodechefInfo(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        # user=request.user
        # if (leetcode_acc.objects.filter(user=user).exists()):
        #     account=leetcode_acc.objects.filter(user=user).first()
        result =[]
        accounts = codechef_acc.objects.all().order_by('-rating')
        n=1
        for account in accounts:
            d={
                'serialNumber':n,
                'username':account.username,
                'name':account.name,
                'rating':account.rating,
                'global_rank':account.global_rank,
                'country_rank':account.country_rank,
                'stars':account.stars,
                'photo_url':account.photo_url,
                'number_of_questions':account.number_of_questions,
            }
            result.append(d)
            n+=1
        return Response(result,status=status.HTTP_200_OK)
        
    

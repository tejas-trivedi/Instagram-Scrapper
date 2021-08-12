from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from django.utils import timezone
from django.db import models
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, mixins, serializers, status
from rest_framework.generics import CreateAPIView
from django.shortcuts import get_object_or_404
from decimal import Decimal
import cv2
import datetime

from .serializers import *
import json
import os


class InstaScrapeView(APIView):

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):

        username = request.data.get("username")

        os.system("instagram-scraper {} --media-metadata --media-types none -u _._an_._007 -p CSE001tt".format(username))

        with open("{}/{}.json".format(username, username)) as fp:
            v = fp.read()
            v = json.loads(v)

        insta_data = v

        data = {
            "username": username,
            "data": insta_data
        }

        serializer = InstaScrapeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "data": insta_data
            }

            return Response(response, status=status.HTTP_201_CREATED)

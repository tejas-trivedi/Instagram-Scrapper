from django.contrib.auth import authenticate, user_logged_in, user_login_failed
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
from django.contrib.auth.models import Group
from django.utils import timezone
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.core.validators import EmailValidator

from scrape.models import *

class InstaScrapeSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstaData
        fields = [
            "username",
            "data",
        ]



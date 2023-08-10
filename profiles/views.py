from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        # this takes the objects in profiles and runs it through the
        # ProfileSerializer defined in serializers.py
        # it takes this data, then takes the `Profile` model as a reference
        # and then renders the specified fields within the passed-in
        # dataset into JSON data
        return Response(serializer.data)


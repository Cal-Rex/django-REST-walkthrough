from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class ProfileList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(
            profiles,
            many=True,
            context={'request': request}
        )
        # this takes the objects in profiles and runs it through the
        # ProfileSerializer defined in serializers.py
        # it takes this data, then takes the `Profile` model as a reference
        # and then renders the specified fields within the passed-in
        # dataset into JSON data
        return Response(serializer.data)


class ProfileDetail(APIView):
    # establish the form structure for the data
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        """
        the function that checks the validity
        of a profile request, returns an error if
        invalid
        """
        try:
            profile = Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        """
        uses the function above to get a profile by id
        serializes it using the ProfileSerializer
        """
        profile = self.get_object(pk)
        serializer = ProfileSerializer(
            profile,
            context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        """
        updates a retreived profile with data receieved
        from a request via a form contextualised by
        serializer_class at the top of this view
        handles BAD_REQUEST errors too
        """
        profile = self.get_object(pk)
        serializer = ProfileSerializer(
            profile,
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
            serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):  # step 13
    permission_classes = [IsOwnerOrReadOnly]  # step 14
    serializer_class = LikeSerializer  # step 15
    queryset = Like.objects.all()  # step 16
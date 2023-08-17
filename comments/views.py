from django.shortcuts import render
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):  # step 3
        serializer_class = CommentSerializer  # step 4
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # step 5
        queryset = Comment.objects.all()  # step 6

        def perform_create(self, serializer):  # step 7
                serializer.save(owner=self.request.user)  #step 8


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):  # step 13
    permission_classes = [IsOwnerOrReadOnly]  # step 14
    serializer_class = CommentDetailSerializer  # step 15
    queryset = Comment.objects.all()  # step 16


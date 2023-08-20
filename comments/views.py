from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):  # step 3
        serializer_class = CommentSerializer  # step 4
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # step 5
        queryset = Comment.objects.all()  # step 6
        filter_backends = [
        DjangoFilterBackend,  #  new filter added here
        ]
        filterset_fields = [  # new field here
        'post',
    ]


        def perform_create(self, serializer):  # step 7
                serializer.save(owner=self.request.user)  #step 8


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):  # step 13
    permission_classes = [IsOwnerOrReadOnly]  # step 14
    serializer_class = CommentDetailSerializer  # step 15
    queryset = Comment.objects.all()  # step 16


from rest_framework import serializers
from .models import Post
from likes.models import Like


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.id')
    profile_image = serializers.ReadOnlyField(source='owner.image.url')
    is_owner = serializers.SerializerMethodField()
        # this variable above is used to house 
        # the requisite serializer it is called 
        # as a function below by prefixing the variable's 
        # name with 'get_'
    like_id = serializers.SerializerMethodField()
    
    def get_is_owner(self, obj):
        """
        passes the request of a user into the serializer
        from views.py
        to check if the user is the owner of a record
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            liked = Like.objects.filter(owner=user, post=obj).first()
            print(liked)
            return liked.id if liked else None
        return None
    
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image wider than 4096 pixels!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image taller than 4096 pixels!'
            )
        return value

    class Meta:
        model = Post
        fields = [
            'id',
            'owner',
            'profile_id',
            'profile_image',
            'created_at',
            'updated_at',
            'title',
            'content',
            'image',
            'image_filter',
            'is_owner',
            'like_id',
        ]
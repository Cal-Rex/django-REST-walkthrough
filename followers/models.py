from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User
from profiles.models import Profile

# Create your models here.

class Follower(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [UniqueConstraint(fields=['owner', 'followed'], name='unique_follow')]

    def __str__(self):
        return f"{self.owner} {self.followed}"
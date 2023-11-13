from django.db import models
from souls_of_stockholm.user.models import CustomUser


class Tag(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Posts(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    content = models.TextField(max_length=8000)

    def __str__(self):
        return self.name


class Comments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

from rest_framework import serializers
from souls_of_stockholm.posts.models import Posts, Comments
from souls_of_stockholm.user.models import CustomUser
from souls_of_stockholm.posts.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ["id", "name", "content", "user"]



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class AnyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'age', 'gender', 'country']


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
        fields = ("id", "content", "post", "create_at", "user")


class PostSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = ["id", "name", "content", "user"]

    def get_user(self, obj):
        user = obj.author
        return {
            'id': user.id,
            'username': user.username
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class AnyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'age', 'gender', 'country', "is_staff", "is_superuser"]

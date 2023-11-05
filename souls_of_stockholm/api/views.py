from rest_framework import generics
from souls_of_stockholm.posts.models import Posts, Comments
from souls_of_stockholm.user.models import CustomUser
from souls_of_stockholm.api.serializers import (PostSerializer,
                                                UserSerializer,
                                                AddCommentSerializer,
                                                AnyUserSerializer,
                                                TagSerializer,
                                                CommentSerializer,
                                                AddPostSerializer)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response


class PostsListView(generics.ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class PersonalUserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)


class ShowUserListView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = AnyUserSerializer
    lookup_field = 'id'


class OnePostListView(generics.RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        post_serializer = self.get_serializer(instance)
        comments = Comments.objects.filter(post=instance)
        comment_serializer = CommentSerializer(comments, many=True)
        tags = instance.tag.all()
        tag_serializer = TagSerializer(tags, many=True)

        response_data = {
            'post': post_serializer.data,
            'comments': comment_serializer.data,
            'tags': tag_serializer.data
        }
        return Response(response_data)


class CommentCreateView(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = AddCommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class PostCreateView(generics.CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = AddPostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


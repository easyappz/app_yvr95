from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from drf_spectacular.utils import extend_schema
from .serializers import MemberSerializer, PostSerializer, LikeSerializer, CommentSerializer
from .models import Member, Post, Like, Comment


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        request=MemberSerializer,
        responses={201: MemberSerializer},
        description="Register a new user"
    )
    def post(self, request):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "username": {"type": "string"},
                    "password": {"type": "string"}
                },
                "required": ["username", "password"]
            }
        },
        responses={200: {"description": "Login successful"}},
        description="Login user"
    )
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        responses={200: {"description": "Logout successful"}},
        description="Logout user"
    )
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        responses={200: MemberSerializer, 200: MemberSerializer},
        description="Get or update user profile"
    )
    def get(self, request):
        serializer = MemberSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = MemberSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=PostSerializer,
        responses={201: PostSerializer},
        description="List or create posts"
    )
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.initial_data['author'] = request.user.id
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        responses={200: PostSerializer, 200: PostSerializer, 204: {"description": "Post deleted"}},
        description="Retrieve, update or delete a post"
    )
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk=None):
        post = self.get_object(pk)
        if post.author != request.user:
            return Response({"error": "You don't have permission to edit this post"}, status=status.HTTP_403_FORBIDDEN)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        post = self.get_object(pk)
        if post.author != request.user:
            return Response({"error": "You don't have permission to delete this post"}, status=status.HTTP_403_FORBIDDEN)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "post_id": {"type": "integer"}
                },
                "required": ["post_id"]
            }
        },
        responses={201: LikeSerializer, 204: {"description": "Like removed"}},
        description="Like or unlike a post"
    )
    def post(self, request):
        post_id = request.data.get('post_id')
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=CommentSerializer,
        responses={201: CommentSerializer},
        description="List or create comments"
    )
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.initial_data['user'] = request.user.id
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentRetrieveUpdateDestroyView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        responses={200: CommentSerializer, 200: CommentSerializer, 204: {"description": "Comment deleted"}},
        description="Retrieve, update or delete a comment"
    )
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk=None):
        comment = self.get_object(pk)
        if comment.user != request.user:
            return Response({"error": "You don't have permission to edit this comment"}, status=status.HTTP_403_FORBIDDEN)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        comment = self.get_object(pk)
        if comment.user != request.user:
            return Response({"error": "You don't have permission to delete this comment"}, status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

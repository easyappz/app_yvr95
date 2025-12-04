from rest_framework import serializers
from .models import Member, Post, Like, Comment


class MemberSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Member
        fields = ('id', 'username', 'first_name', 'last_name', 'about_me', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        if password is None:
            raise serializers.ValidationError({"password": "This field is required."}) 
        user = Member(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)


class PostSerializer(serializers.ModelSerializer):
    author = MemberSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'content', 'created_at', 'updated_at')


class LikeSerializer(serializers.ModelSerializer):
    user = MemberSerializer(read_only=True)
    post = PostSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ('id', 'user', 'post', 'created_at')


class CommentSerializer(serializers.ModelSerializer):
    user = MemberSerializer(read_only=True)
    post = PostSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'post', 'content', 'created_at')

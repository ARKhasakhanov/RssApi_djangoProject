from rest_framework import serializers

from ForumApp.models import Message, Section, Thread, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'login', 'password')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'thread', 'user', 'message_text', 'date')


class MessageSerializerExpand(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'thread_id', 'thread', 'user_id', 'user', 'message_text', 'date')
        depth = 1


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'section_name', 'parent')


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ('id', 'section_id', 'header', 'user_id', 'tread_text', 'date')


class ThreadSerializerExpand(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ('id', 'section_id', 'section', 'header', 'user_id', 'user', 'tread_text', 'date')
        depth = 1







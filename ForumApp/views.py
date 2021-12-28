from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ForumApp.models import Message, Section, Thread, User
from ForumApp.serializers import MessageSerializer,MessageSerializerExpand, SectionSerializer, ThreadSerializer, UserSerializer, ThreadSerializerExpand


class MessageItemList(APIView):

    def get(self, request):
        rss_items = Message.objects.all()
        thread = self.request.query_params.get('thread')
        user = self.request.query_params.get('user')
        message_text = self.request.query_params.get('message_text')
        date = self.request.query_params.get('date')
        expand = self.request.query_params.get('expand')

        if thread is not None:
            rss_items = rss_items.filter(thread=thread)
        if user is not None:
            rss_items = rss_items.filter(user=user)
        elif message_text is not None:
            rss_items = rss_items.filter(message_text=message_text)
        elif date is not None:
            rss_items = rss_items.filter(date=date)
        if expand is not None:
            rss_items_serializer = MessageSerializerExpand(instance=rss_items, many=True)
        else:
            rss_items_serializer = MessageSerializer(instance=rss_items, many=True)

        return Response(rss_items_serializer.data)

    def post(self, request):
        rss_item_serializer = MessageSerializer(data=request.data)
        if rss_item_serializer.is_valid():
            rss_item_serializer.save()
        return Response(rss_item_serializer.data)


class MessageItemDetail(APIView):

    def get(self, request, pk):
        try:
            rss_item = Message.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        rss_item_serializer = MessageSerializer(instance=rss_item)
        return Response(rss_item_serializer.data)

    def put(self, request, pk):
        try:
            rss_item = Message.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        rss_item_serializer = MessageSerializer(instance=rss_item, data=request.data, partial=True)
        if rss_item_serializer.is_valid():
            rss_item_serializer.save()
        return Response(rss_item_serializer.data)

    def delete(self, request, pk):
        try:
            rss_item = Message.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        rss_item_serializer = MessageSerializer(instance=rss_item)
        rss_item.delete()
        return Response(rss_item_serializer.data)


class SectionItemList(APIView):

    def get(self, request):
        rss_items = Section.objects.all()
        section_name = self.request.query_params.get('section_name')
        parent = self.request.query_params.get('parent')

        if section_name is not None:
            rss_items = rss_items.filter(section_name=section_name)
        if section_name is not None:
            rss_items = rss_items.filter(parent=parent)

        rss_items_serializer = SectionSerializer(instance=rss_items, many=True)
        return Response(rss_items_serializer.data)

    def post(self, request):
        rss_item_serializer = SectionSerializer(data=request.data)
        if rss_item_serializer.is_valid():
            rss_item_serializer.save()
        return Response(rss_item_serializer.data)


class SectionItemDetail(APIView):

    def get(self, request, pk):
        try:
            rss_item = Section.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        rss_item_serializer = SectionSerializer(instance=rss_item)
        return Response(rss_item_serializer.data)

    def put(self, request, pk):
        try:
            rss_item = Section.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        rss_item_serializer = SectionSerializer(instance=rss_item, data=request.data, partial=True)
        if rss_item_serializer.is_valid():
            rss_item_serializer.save()
        return Response(rss_item_serializer.data)

    def delete(self, request, pk):
        try:
            rss_item = Section.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        rss_item_serializer = SectionSerializer(instance=rss_item)
        rss_item.delete()
        return Response(rss_item_serializer.data)


class ThreadItemList(APIView):

    def get(self, request):
        rss_items = Thread.objects.all()
        section = self.request.query_params.get('section')
        header = self.request.query_params.get('header')
        user = self.request.query_params.get('user')
        thread_text = self.request.query_params.get('thread_text')
        date = self.request.query_params.get('date')
        expand = self.request.query_params.get('expand')

        if section is not None:
            rss_items = rss_items.filter(section=section)

        if header is not None:
            rss_items = rss_items.filter(header=header)

        if user is not None:
            rss_items = rss_items.filter(user=user)

        if thread_text is not None:
            rss_items = rss_items.filter(thread_text=thread_text)

        if date is not None:
            rss_items = rss_items.filter(date=date)

        if expand is not None:
            rss_items_serializer = ThreadSerializerExpand(instance=rss_items, many=True)
        else:
            rss_items_serializer = ThreadSerializer(instance=rss_items, many=True)

        return Response(rss_items_serializer.data)

    def post(self, request):
        rss_item_serializer = ThreadSerializer(data=request.data)
        if rss_item_serializer.is_valid():
            rss_item_serializer.save()
        return Response(rss_item_serializer.data)


class ThreadItemDetail(APIView):

    def get(self, request, pk):
        try:
            rss_item = Thread.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        rss_item_serializer = ThreadSerializer(instance=rss_item)
        return Response(rss_item_serializer.data)

    def put(self, request, pk):
        try:
            rss_item = Thread.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        rss_item_serializer = ThreadSerializer(instance=rss_item, data=request.data, partial=True)
        if rss_item_serializer.is_valid():
            rss_item_serializer.save()
        return Response(rss_item_serializer.data)

    def delete(self, request, pk):
        try:
            rss_item = Thread.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        rss_item_serializer = ThreadSerializer(instance=rss_item)
        rss_item.delete()
        return Response(rss_item_serializer.data)


class UserItemList(APIView):

    def get(self, request):
        rss_items = User.objects.all()
        login = self.request.query_params.get('login')
        password = self.request.query_params.get('password')

        if login is not None:
            rss_items = rss_items.filter(login=login)
        if password is not None:
            rss_items = rss_items.filter(password=password)

        rss_items_serializer = UserSerializer(instance=rss_items, many=True)
        return Response(rss_items_serializer.data)

    def post(self, request):
        rss_item_serializer = UserSerializer(data=request.data)
        if rss_item_serializer.is_valid():
            rss_item_serializer.save()
        return Response(rss_item_serializer.data)


class UserItemDetail(APIView):

    def get(self, request, pk):
        try:
            rss_item = User.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        rss_item_serializer = UserSerializer(instance=rss_item)
        return Response(rss_item_serializer.data)

    def put(self, request, pk):
        try:
            rss_item = User.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        rss_item_serializer = UserSerializer(instance=rss_item, data=request.data, partial=True)
        if rss_item_serializer.is_valid():
            rss_item_serializer.save()
        return Response(rss_item_serializer.data)

    def delete(self, request, pk):
        try:
            rss_item = User.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        rss_item_serializer = UserSerializer(instance=rss_item)
        rss_item.delete()
        return Response(rss_item_serializer.data)

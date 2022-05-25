import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from api.serializers import UserSerializer, LaundrySerializer, LaundryEntrySerializer, RoomsSerializer, RoomEntrySerializer
from users.models import User
from laundry.models import Laundry, LaundryEntry
from rooms.models import Rooms, RoomEntry


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names= ['get', 'post', 'put', 'delete']


class LaundryViewSet(ModelViewSet):
    queryset = Laundry.objects.all()
    serializer_class = LaundrySerializer
    http_method_names= ['get', 'post', 'put', 'delete']


class LaundryEntryViewSet(ModelViewSet):
    queryset = LaundryEntry.objects.all()
    serializer_class = LaundryEntrySerializer
    http_method_names= ['get', 'post', 'put', 'delete']


class RoomsViewSet(ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    http_method_names= ['get', 'post', 'put', 'delete']


class RoomEntryViewSet(ModelViewSet):
    queryset = RoomEntry.objects.all()
    serializer_class = RoomEntrySerializer
    http_method_names= ['get', 'post', 'put', 'delete']


@api_view(['GET', 'POST'])
def room_entry_for_day_list(request, year, month, day, format=None):
    try:
        enrties = RoomEntry.objects.get(start_time=datetime.date(year, month, day))
    except RoomEntry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = RoomEntrySerializer(enrties)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RoomEntrySerializer(enrties, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def laundry_entry_for_day_list(request, year, month, day, format=None):
    try:
        enrties = LaundryEntry.objects.get(start_time=datetime.date(year, month, day))
    except LaundryEntry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = LaundryEntry(enrties)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LaundryEntry(enrties, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''class UserListView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)'''


'''@api_view(['GET', 'POST'])
def users_list(request, format=None):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''

'''@api_view(['GET', 'PUT', 'DELETE'])
def users_detail(request, pk, format=None):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''


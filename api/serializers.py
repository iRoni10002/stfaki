from rest_framework.serializers import IntegerField, CharField, Serializer, ModelSerializer, SlugRelatedField, DateTimeField, BooleanField
from users.models import User
from laundry.models import Laundry, LaundryEntry
from rooms.models import Rooms, RoomEntry


'''class UserSerializer(Serializer):
    id = IntegerField(read_only=True)
    name = CharField(required=True, max_length=250)
    email = CharField(required=False, max_length=250)
    money = IntegerField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.money = validated_data.get('money', instance.money)
        instance.save()
        return instance'''


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LaundrySerializer(ModelSerializer):
    user = SlugRelatedField(
        many=False, 
        read_only=True,
        slug_field="name"
    )
    class Meta:
        model = RoomEntry
        fields = '__all__'


class LaundryEntrySerializer(ModelSerializer):
    class Meta:
        model = LaundryEntry
        fields = '__all__'


class RoomsSerializer(ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'


class RoomEntrySerializer(ModelSerializer):
    room = SlugRelatedField(
        many=False, 
        read_only=True,
        slug_field="name"
    )
    user = SlugRelatedField(
        many=False, 
        read_only=True,
        slug_field="name"
    )
    class Meta:
        model = RoomEntry
        fields = '__all__'


'''class RoomEntrySerializer(Serializer):
    id = IntegerField(read_only=True)
    start_time = DateTimeField(read_only=True)
    end_time = DateTimeField(read_only=True)
    color = CharField()
    type = BooleanField()
    room = SlugRelatedField(
        many=False, 
        read_only=True,
        slug_field="name"
    )

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.color = validated_data.get('color', instance.color)
        instance.type = validated_data.get('type', instance.type)
        instance.room = validated_data.get('room', instance.room)
        instance.save()
        return instance'''

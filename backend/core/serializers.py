from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from .models import Guestprofile, Booking, Room, Dining

UserModel = get_user_model()


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class GetBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class BookingSerializer(serializers.Serializer):
    room_number = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
    room_type = serializers.CharField()
    # room_count = serializers.IntegerField()
    adults_count = serializers.IntegerField()
    children_count = serializers.IntegerField()
    check_in = serializers.DateField()
    check_out = serializers.DateField()
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        # Extract validated data
        room_number = validated_data.get("room_number")
        room_type = validated_data["room_type"]
        # room_count = validated_data["room_count"]
        adults_count = validated_data["adults_count"]
        children_count = validated_data["children_count"]
        check_in = validated_data["check_in"]
        check_out = validated_data["check_out"]
        total_price = validated_data["total_price"]
        print("total : ", total_price)
        # Get user from request (assuming token authentication)
        user = self.context["request"].user
        guest_data = Guestprofile.objects.get(user=user)
        print(guest_data)
        return Booking.objects.create(
            guest=guest_data.user,
            room_number=room_number,
            room_type=room_type,
            # room_count=room_count,
            adults_count=adults_count,
            children_count=children_count,
            total_price=total_price,
            check_in=check_in,
            check_out=check_out,
        )


from datetime import datetime


class DiningSerializer(serializers.Serializer):

    dine_type = serializers.CharField()
    # room_count = serializers.IntegerField()
    refer_number = serializers.IntegerField()
    people_count = serializers.IntegerField()

    date_time = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        # Extract validated data
        dine_type = validated_data["dine_type"]
        refer_number = validated_data["refer_number"]
        # room_count = validated_data["room_count"]
        people_count = validated_data["people_count"]
        date_t = self.context["request"].data.get("date")
        time_t = self.context["request"].data.get("time")
        date = datetime.strptime(date_t, "%Y-%m-%d").date()
        time = datetime.strptime(time_t, "%H:%M:%S").time()

        # Combine date and time into a single datetime object
        date_time = datetime.combine(date, time)
        # Combine date and time into a single datetime object
        date_time = datetime.combine(date, time)

        # data = {

        #     "refer_number": validated_data.get("refer_number"),
        #     "dine_type": validated_data.get("dine_type"),
        #     "people_count": validated_data.get("people_count"),
        # }
        # Get user from request (assuming token authentication)
        user = self.context["request"].user
        guest_data = Guestprofile.objects.get(user=user)

        return Dining.objects.create(
            guest=guest_data.user,
            dine_type=dine_type,
            refer_number=refer_number,
            # room_count=room_count,
            people_count=people_count,
            date_time=date_time,
        )


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

    def create(self, clean_data):

        user_obj = UserModel.objects.create_user(
            username=clean_data["username"],
            password=clean_data["password"],
        )

        user_obj.first_name = clean_data["first_name"]
        user_obj.last_name = clean_data["last_name"]
        user_obj.email = clean_data["email"]
        user_obj.save()
        return user_obj


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    ##
    def check_user(self, clean_data):
        user = authenticate(
            username=clean_data["username"], password=clean_data["password"]
        )
        print(user)
        if not user:
            raise ValidationError("user not found")
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("id", "username", "email")

import datetime
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token


from .models import Guestprofile, Booking, Room, Staff
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    UserSerializer,
    BookingSerializer,
    GetBookingSerializer,
    RoomSerializer,
    DiningSerializer,
)
from .validations import (
    custom_validation,
    validate_username,
    validate_password,
    validate_email,
)
from django.contrib.auth.hashers import identify_hasher

# from .forms import UserProfileInfo,BookingInfo
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .forms import BookingForm


def booking_update(request, pk):
    booking = Booking.objects.get(pk=pk)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect("booking_detail", pk=booking.pk)
    else:
        form = BookingForm(instance=booking)
    return render(request, "booking/booking_form.html", {"form": form})


class Profile(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (
        SessionAuthentication,
        TokenAuthentication,
    )

    def put(self, request):
        user = request.user
        guest_data = Guestprofile.objects.get(user=user)

        # Update username
        if "username" in request.data:
            new_username = request.data["username"]
            user.username = new_username

        # Update password
        if "password" in request.data:
            new_password = request.data["password"]
            user.set_password(new_password)

        # Update location
        if "location" in request.data:
            new_location = request.data["location"]
            guest_data.location = new_location

        if "contact" in request.data:
            new_contact = request.data["contact"]
            guest_data.contact = new_contact
        # Update picture
        if "picture" in request.data:
            new_picture = request.data["picture"]
            guest_data.picture = new_picture

        user.save()
        guest_data.save()

        return Response(status=status.HTTP_200_OK)

    def get(self, request):

        authorization_header = request.headers.get("Authorization")
        # Print the Authorization header value
        print("Profile Auth: ", authorization_header)

        token_auth = str(authorization_header).replace("Token", "").strip()
        token_obj = Token.objects.get(key=token_auth)
        user = token_obj.user
        guest_data = Guestprofile.objects.get(user=user)
        pic = guest_data.picture.url
        abs_pic_url = request.build_absolute_uri(pic)

        # Retrieve the original form of user password

        # Retrieve the original form of user password not the encrypted

        user_data = {
            "username": user.username,
            "email": guest_data.email,
            "first_name": guest_data.first_name,
            "last_name": guest_data.last_name,
            "location": guest_data.location,
            "contact": guest_data.contact,
            "password": user.password,
            "picture": abs_pic_url,
            # Add other fields as needed
        }
        return Response(user_data)


class RoomAvailability(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):

        rooms = Room.objects.all()
        print(rooms)
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        data = request.data
        availability = data["availability"]

        print("Value:", availability)
        room_availability = (
            Room.objects.filter(availability=availability)
            if availability is not None
            else Room.objects.all()
        )
        # Filter rooms based on availability
        room_availability_data = RoomSerializer(room_availability, many=True).data

        return Response(room_availability_data, status=status.HTTP_200_OK)


class SaveDining(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        # room = Room.objects.get(room_number=request.data["room_number"])

        # # Create a new dictionary with the request data and the Room object
        # data = request.data
        # data["room_number"] = room.room_number
        # print(data["room_number"])
        
        
        serializer = DiningSerializer(data=request.data, context={"request": request})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        dining = serializer.save()
        return Response(DiningSerializer(dining).data, status=status.HTTP_201_CREATED)


class SaveBooking(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        # room = Room.objects.get(room_number=request.data["room_number"])

        # # Create a new dictionary with the request data and the Room object
        # data = request.data
        # data["room_number"] = room.room_number
        # print(data["room_number"])

        serializer = BookingSerializer(data=request.data, context={"request": request})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        booking = serializer.save()
        return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        authorization_header = request.headers.get("Authorization")
        # Print the Authorization header value
        print("Booking Auth: ", authorization_header)

        token_auth = str(authorization_header).replace("Token", "").strip()
        token_obj = Token.objects.get(key=token_auth)
        user = token_obj.user
        get_all_bookings = Booking.objects.filter(guest=user)

        serializer = GetBookingSerializer(get_all_bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)






import pyotp
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.core.mail import send_mail
from datetime import datetime


class OTPView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        otp = self.generate_otp()
        OTPView.otp = otp
        return Response({"otp": otp}, status=status.HTTP_200_OK)

    def generate_otp(self):
        user_secret = pyotp.random_base32()
        return pyotp.TOTP(user_secret).now()


# from my_module import (
#     verify_otp,
# )  # Import the verify_otp function from the appropriate module


class VerifyOTP(APIView):

    def post(self, request):
        data = request.data
        otp = data.get("otp")
        print("OTP: ", otp)
        print("OTPView.otp: ", OTPView.otp)
        if OTPView.otp == otp:
            # Use the verify_otp function to check the OTP validity
            return Response({"isOtpValid": True}, status=status.HTTP_200_OK)
        else:
            return Response({"isOtpValid": False}, status=status.HTTP_400_BAD_REQUEST)



class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (
        SessionAuthentication,
        TokenAuthentication,
    )

    ##
    def get(self, request):
        authorization_header = request.headers.get("Authorization")
        # Print the Authorization header value
        print("Header Auth: ", authorization_header)

        UserView.token_auth = str(authorization_header).replace("Token", "").strip()
        serializer = UserSerializer(request.user)

        # session_id = request.session.session_key
        # print("Session ID:", session_id)
        return Response({"user": serializer.data}, status=status.HTTP_200_OK)


class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        first_name = data["first_name"].strip()
        last_name = data["last_name"].strip()
        location = data["location"].strip()
        contact = data["contact"].strip()
        email = data["email"].strip()

        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            if user := serializer.create(clean_data):
                Guestprofile.objects.create(
                    user=user,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    contact=contact,
                    location=location,
                    #  # Assuming you want to associate the GuestProfile with the created user
                )
                login(request, user)

                the_user = User.objects.get(username=data["username"].strip())

                print(the_user)
                token = Token.objects.create(user=the_user)

                # return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response({"token": token.key, "user": serializer.data})
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data
        assert validate_username(data)
        assert validate_password(data)

        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            # username = serializer.validated_data["username"]
            # password = serializer.validated_data["password"]
            user = serializer.check_user(data)
            # User is already authenticated, return appropriate response
            login(request, user)
            # session_id = request.session.session_key
            token, create = Token.objects.get_or_create(user=user)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)  
        


class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        
        # get_token = UserView.token_auth
        # print("Logout Token: ", get_token.replace("Token", "").strip())
        # del_token = Token.objects.get(key=get_token)
        # del_token.delete()
        logout(request)

        return Response(status=status.HTTP_200_OK)




# class StaffView(APIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     authentication_classes = (
#         SessionAuthentication,
#         TokenAuthentication,
#     )
#     ##

#     def get(self, request):
#         authorization_header = request.headers.get("Authorization")
#         # Print the Authorization header value
#         print("check Auth: ", authorization_header)
#         StaffView.token_auth = str(authorization_header).replace("Token", "").strip()
#         serializer = UserSerializer(request.user)
#         # session_id = request.session.session_key
#         # print("Session ID:", session_id)
#         return Response({"admin": serializer.data}, status=status.HTTP_200_OK)


# class GetStaffLogin(APIView):
#     permission_classes = (permissions.AllowAny,)
#     authentication_classes = (SessionAuthentication,)

#     def post(self, request):
#         data = request.data
#         assert validate_username(data)
#         assert validate_password(data)

#         def get_or_create_token(user):
#             token, create = Token.objects.get_or_create(user=user)
#             return token

#         serializer = UserLoginSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             user = serializer.check_user(data)
#             token = get_or_create_token(user)
#             staff_position = Staff.objects.get(account=user)
#             staff_position = staff_position.position
#             login(request, user)
#             return Response({"token": token.key, "user": serializer.data,"position":staff_position,})
#         else:
#             return Response(
#             {"error": "Invalid credentials"},
#             status=status.HTTP_401_UNAUTHORIZED,
#         )


# class LeaveStaff(APIView):
#     permission_classes = (permissions.AllowAny,)
#     authentication_classes = ()

#     def post(self, request):
#         # data = request.data
#         # authorization_header = request.headers.get("Authorization")
#         get_token = StaffView.token_auth
#         # Print the Authorization header value
#         print("Header Logout: ", get_token)
#         # get_token = str(authorization_header).replace("Token", "").strip()
#         # get_token = StaffView.token_auth
#         print("Logout Token: ", get_token.replace("Token", "").strip())
#         del_token = Token.objects.get(key=get_token)
#         print("Logout User: ", del_token.user)

#         if del_token.user in Staff.objects.all():
#             del_token.delete()

#         logout(request)

#         return Response(status=status.HTTP_200_OK)
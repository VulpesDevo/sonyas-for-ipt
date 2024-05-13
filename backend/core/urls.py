from django.urls import path, re_path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # re_path("book", views.Accomodate, name="book"),
    re_path("user", views.UserView.as_view(), name="user"),
    # re_path("sonyasstaff", views.StaffView.as_view(), name="sonyasstaff"),
    # re_path("stafflogin", views.GetStaffLogin.as_view(), name="stafflogin"),
    # re_path("leave", views.LeaveStaff.as_view(), name="leave"),
    re_path("register", views.UserRegister.as_view(), name="register"),
    re_path("login", views.UserLogin.as_view(), name="login"),
    re_path("logout", views.UserLogout.as_view(), name="logout"),
    re_path("profile", views.Profile.as_view(), name="profile"),
    re_path("submitbooking", views.SaveBooking.as_view(), name="save-booking"),
    re_path("checkrooms", views.RoomAvailability.as_view(), name="check"),
    re_path("add-dining", views.SaveDining.as_view(), name="add-dining"),
    re_path("send-otp", views.OTPView.as_view(), name="send-otp"),
    re_path("verify-otp", views.VerifyOTP.as_view(), name="verify-otp"),
    # path(
    #     "change-password/<int:user_id>/",
    #     views.ChangeUserPasswordView.as_view(),
    #     name="change_password",
    # ),
    # path("user", views.UserView.as_view(), name="user"),
]

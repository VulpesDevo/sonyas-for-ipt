# from django import forms
# from django.contrib.auth.forms import SetPasswordForm


# class CustomSetPasswordForm(SetPasswordForm):
#     def save(self, commit=True):
#         password = self.cleaned_data["new_password1"]
#         self.user.set_password(password)
#         if commit:
#             self.user.save()
#         return self.user
# from django import forms
# from .models import Booking


# class BookingAdminForm(forms.ModelForm):
#     check_in = forms.DateField(widget=forms.SelectDateWidget(), required=False)
#     check_out = forms.DateField(widget=forms.SelectDateWidget(), required=False)

#     class Meta:
#         model = Booking
#         fields = "__all__"
from django import forms
from .models import Booking, Room


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "guest",
            "room_number",
            "room_type",
            # "room_count",
            "adults_count",
            "children_count",
            "total_price",
            "check_in",
            "check_out",
        ]


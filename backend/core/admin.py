from django.contrib import admin
from django.forms import BaseInlineFormSet
from .models import Guestprofile, Booking, Staff, Room, Dining

from django.utils.dateparse import parse_date
from django.db.models import Q


class BookingColumn(admin.ModelAdmin):

    list_display = (
        "booking_id",
        "guest",
        "room_type",
        "room_number",
        "adults_count",
        "children_count",
        "total_price",
        "check_in",
        "check_out",
        "status",
        "created_at",
    )

    def booking_info(self, obj):
        return obj.description


class DiningInormation(admin.ModelAdmin):
    search_fields = ("refer_number",)
    list_display = (
        "guest",
        "refer_number",
        "dine_type",
        "people_count",
        "date_time",
        "status",
    )
    list_filter = ("dine_type",)

    def dining_info(self, obj):
        return obj.description





class Guests(admin.ModelAdmin):
    list_display = (
        "user",
        "first_name",
        "last_name",
        "location",
        "email",
        "contact",
        "picture",
        "active",
    )
    #inlines = [GuestBookingInline, GuestDiningInline]

    def guest_info(self, obj):
        return obj.description


class StaffInformation(admin.ModelAdmin):
    list_display = (
        "employee_id",
        "account",
        "first_name",
        "last_name",
        "picture",
        "position",
        "tin_no",
        "gender",
        "date_of_birth",
        "contact_no",
        "email",
        "address",
        "hiring_date",
        "salary",
    )

    def staff_info(self, obj):
        return obj.description


class BookingInline(admin.TabularInline):  # or admin.StackedInline
    model = Booking
    extra = 0

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.status == "completed":
            room = obj.room
            room.booking_id = None
            # room.booking_details = None
            room.availability = True
            room.save()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.exclude(status="completed")


class RoomInformation(admin.ModelAdmin):

    list_filter = (
        "room_type",
        "availability",
    )
    list_display = (
        "room_number",
        "room_type",
        "availability",
    )
    # Add this line
    inlines = [BookingInline]

    def room_info(self, obj):
        return obj.description


admin.site.register(Dining, DiningInormation)
admin.site.register(Room, RoomInformation)
admin.site.register(Staff, StaffInformation)
admin.site.register(Guestprofile, Guests)
admin.site.register(Booking, BookingColumn)

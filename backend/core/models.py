import uuid
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Guestprofile(models.Model):
    """
    Model representing a guest profile.
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="guest",
        blank=True,
        null=True,
        limit_choices_to={"is_staff": False, "is_superuser": False},
    )
    first_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField()
    contact = models.IntegerField(blank=True, null=True)
    picture = models.ImageField(blank=True, null=True, default="default_image.jpg")

    active = models.BooleanField(default=True)


from django.utils.html import format_html


class Room(models.Model):
    """
    Model representing a room.
    """

    ROOM_TYPES = [
        ("Lover's Suite", "Lover's Suite"),
        ("Business Suite", "Business Suite"),
        ("Family Suite", "Family Suite"),
    ]

    room_number = models.AutoField(primary_key=True)

    room_type = models.CharField(max_length=120, choices=ROOM_TYPES)
    availability = models.BooleanField(default=True)


class Booking(models.Model):
    """
    Model representing a booking.
    """

    booking_id = models.AutoField(primary_key=True, editable=False, unique=True)
    guest = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking", null=True
    )
    room_number = models.ForeignKey(
        Room,
        on_delete=models.SET_NULL,
        related_name="booking",
        null=True,
        limit_choices_to={"availability": True},
    )

    def save(self, *args, **kwargs):
        if self.room_number is not None:
            room = self.room_number  # Get the Room instance
            room.availability = room.availability != True
            room.booking_details = "No booking details"
            room.save()
        super().save(*args, **kwargs)

    room_type = models.CharField(max_length=120, verbose_name="Room Type")

    # room_count = models.IntegerField(verbose_name="Room Count")
    adults_count = models.IntegerField(verbose_name="Adults Count")
    children_count = models.IntegerField(verbose_name="Children Count")
    total_price = models.FloatField(verbose_name="Total Price")
    check_in = models.DateField(verbose_name="Check-in Date")
    check_out = models.DateField(verbose_name="Check-out Date")

    status = models.CharField(
        max_length=20,
        choices=[("completed", "Completed"), ("ongoing", "Ongoing")],
        default="ongoing",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    # def save(self, *args, **kwargs):
    #     if self.status == 'completed':
    #         room = (
    #             self.room_number
    #         )  # Assuming 'room' is the related name for the Room model
    #         room.booking_details = None
    #         room.availability = True
    #         room.save()
    #     super().save(*args, **kwargs)


class Dining(models.Model):
    """
    Model representing a dining reservation.
    """

    guest = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="dining", null=True
    )
    dine_type = models.CharField(max_length=120)
    refer_number = models.IntegerField(
        verbose_name="refer_number", unique=True, blank=True, null=True
    )
    people_count = models.IntegerField()
    date_time = models.DateTimeField()
    status = models.BooleanField(default=True)


class Staff(models.Model):
    """
    Model representing a staff member.
    """

    employee_id = models.AutoField(primary_key=True, unique=True)
    account = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="staff",
        null=True,
        limit_choices_to={"is_staff": True, "is_superuser": False},
    )
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=255)
    picture = models.ImageField(blank=True, null=True, default="default_image.jpg")
    position = models.CharField(
        max_length=120,
        choices=[("Manager", "Manager"), ("Regular Staff", "Regular Staff")],
    )
    tin_no = models.CharField(max_length=20)
    gender = models.CharField(
        max_length=10, choices=[("male", "Male"), ("female", "Female")]
    )
    date_of_birth = models.DateField()
    contact_no = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    hiring_date = models.DateField()
    salary = models.FloatField()

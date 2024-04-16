from rest_framework import serializers

from .models import Book, Member, Reservation


class BookSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class MemberSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"


class ReservationSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

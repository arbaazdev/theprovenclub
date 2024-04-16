from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ValidationError

from .models import Book, Member, Reservation
from .serializers import BookSeralizer, MemberSeralizer, ReservationSeralizer

class BookViewSet(ModelViewSet):
    serializer_class = BookSeralizer
    queryset = Book.objects.all()

    @action(detail=True, methods=["get"])
    def checkout(self, request, pk=None):
        book = self.get_object()
        if book.number_of_copies == 0:
            raise ValidationError("No more copies available.")
        book.number_of_copies -= 1
        book.save()
        serializer = self.get_serializer(book)
        return Response(data=serializer.data)

    @action(detail=True, methods=["get"])
    def returned(self, request, pk=None):
        book = self.get_object()
        book.number_of_copies += 1
        book.save()
        serializer = self.get_serializer(book)
        return Response(data=serializer.data)


class MemberViewSet(ModelViewSet):
    serializer_class = MemberSeralizer
    queryset = Member.objects.all()


class ReservationViewSet(ModelViewSet):
    serializer_class = ReservationSeralizer
    queryset = Reservation.objects.all().select_related("book", "member")

from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField(max_length=255)
    number_of_copies = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['name',]),
        ]

    def __str__(self) -> str:
        return self.name


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    reserve = models.BooleanField(default=False)
    fulfill = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.book.name} {self.user.name}"

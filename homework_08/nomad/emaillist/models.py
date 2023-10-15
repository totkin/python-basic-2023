from django.db import models
from django.urls import reverse

# Create your models here.

REGULAR_NVARCHAR_LENGTH = 255
SHORT_NVARCHAR_LENGTH = 50


class Title(models.Model):
    """Должность"""
    short_name = models.CharField(
        max_length=SHORT_NVARCHAR_LENGTH,
        help_text="Краткое название должности",
        verbose_name="Должность кратко"
    )
    name = models.CharField(
        max_length=REGULAR_NVARCHAR_LENGTH,
        help_text="Должность",
        verbose_name="Должность"
    )

    def __str__(self):
        return f"{self.name} ({self.short_name})"

    def get_queryset(self):
        return Title.objects.all()

    def get_absolute_url(self):
        return reverse("title-detail", args=[str(self.id)])


class Department(models.Model):
    """Отдел"""
    short_name = models.CharField(max_length=SHORT_NVARCHAR_LENGTH,
                                  help_text="Отдел кратко",
                                  verbose_name="Отдел кратко")

    name = models.CharField(max_length=REGULAR_NVARCHAR_LENGTH,
                            help_text="Название отдела",
                            verbose_name="Отдел")

    additional_info = models.CharField(max_length=REGULAR_NVARCHAR_LENGTH,
                                       help_text="Дополнительная информация по отделу",
                                       verbose_name="Доп информация",
                                       blank=True)

    def get_absolute_url(self):
        return reverse("department-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.short_name}"


    def get_queryset(self):
        return Department.objects.all()


class Subscription(models.Model):
    """Должность"""

    SUBSCRIPTION_STATUS = (
        ("+", "Включена"),
        ("-", "Отключена"),
        ("X", "Неактивна"),
    )

    SUBSCRIPTION_FREQUENCY = (
        ("D", "1 раз в день"),
        ("DD", "Несколько раз в день"),
        ("W", "1 раз в неделю"),
        ("O", "Однократно"),
    )

    name = models.CharField(max_length=REGULAR_NVARCHAR_LENGTH, help_text="Рассылка", verbose_name="Название")
    status = models.CharField(max_length=1, choices=SUBSCRIPTION_STATUS, default="+", null=False, verbose_name="Статус")
    frequency = models.CharField(max_length=2, choices=SUBSCRIPTION_FREQUENCY, default="D", null=False,
                                 verbose_name="Частота")

    def __str__(self):
        return f"{self.name} - {self.frequency}"


class Manager(models.Model):
    """Сотрудник"""
    GENDER_CHOICES = [
        ("М", "Мужчина"),
        ("Ж", "Женщина"),
        ("-", "Не указано"),
    ]

    MANAGER_STATUS = (
        ("+", "Работает"),
        ("-", "Уволен"),
        ("X", "Удалить из рассылки"),
    )

    first_name = models.CharField(max_length=SHORT_NVARCHAR_LENGTH, verbose_name="Имя")
    last_name = models.CharField(max_length=SHORT_NVARCHAR_LENGTH, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=SHORT_NVARCHAR_LENGTH, verbose_name="Отчество", blank=True)
    title = models.ForeignKey("Title", on_delete=models.SET_NULL, verbose_name="Должность", null=True)
    department = models.ForeignKey("Department", on_delete=models.SET_NULL, verbose_name="Отдел", null=True)
    email = models.EmailField(null=False)
    system_name = models.CharField(max_length=SHORT_NVARCHAR_LENGTH,
                                   verbose_name="Название в системе", null=False)
    subscription = models.ManyToManyField(Subscription, help_text="Выберите подписки", verbose_name="Подписки",
                                          blank=True)
    status = models.CharField(max_length=1, choices=MANAGER_STATUS, verbose_name="Статус", default="+", null=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Пол", default="М", null=True)
    birthday = models.DateField(null=True, verbose_name="День рождения", blank=True)

    class Meta:
        ordering = ["department", "status", "title", "last_name", "first_name"]

    def display_subcriptions(self):
        return ', '.join([subscription.name for subscription in self.subscription.all()[:3]])

    display_subcriptions.short_description = "Подписки"

    def full_name(self):
        """Creates a string"""
        return " ".join((self.last_name, self.first_name, self.middle_name))

    def get_absolute_url(self):
        return reverse("manager-detail", args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return " ".join((self.first_name, self.middle_name, self.last_name, f"({self.status})"))



# import uuid  # Required for unique book instances
# from datetime import date
#
# from django.contrib.auth.models import User  # Required to assign User as a borrower

#
# class SubscriptionInstance(models.Model):
#     """Model representing a specific Subscription"""
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4,
#                           help_text="Unique ID for this particular book across whole library")
#     book = models.ForeignKey("Book", on_delete=models.RESTRICT, null=True)
#     imprint = models.CharField(max_length=200)
#     due_back = models.DateField(null=True, blank=True)
#     borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#
#     @property
#     def is_overdue(self):
#         """Determines if the book is overdue based on due date and current date."""
#         return bool(self.due_back and date.today() > self.due_back)
#
#     LOAN_STATUS = (
#         ("d", "Maintenance"),
#         ("o", "On loan"),
#         ("a", "Available"),
#         ("r", "Reserved"),
#     )
#
#     status = models.CharField(
#         max_length=1,
#         choices=LOAN_STATUS,
#         blank=True,
#         default="d",
#         help_text="Book availability")
#
#     class Meta:
#         ordering = ["due_back"]
#         permissions = (("can_mark_returned", "Set book as returned"),)
#
#     def __str__(self):
#         """String for representing the Model object."""
#         return "{0} ({1})".format(self.id, self.book.title)

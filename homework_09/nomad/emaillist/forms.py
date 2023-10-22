from django import forms

from django.core.exceptions import ValidationError
import datetime  # for checking renewal date range.

from django.forms import ModelForm

from .models import Manager


def match(text):
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    return not alphabet.isdisjoint(text.lower())


# class RenewManagerForm(forms.Form):
# # renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
# first_name = forms.CharField(help_text="Имя", validators=[match])
# middle_name = forms.CharField(help_text="Отчество", validators=[match])
# last_name = forms.CharField(help_text="Фамилия", validators=[match])
#
# def clean_renewal_date(self):
#     data_first_name = self.cleaned_data['first_name']
#     data_middle_name = self.cleaned_data['middle_name']
#     data_last_name = self.cleaned_data['last_name']
#     alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
#     # data_birthday= self.cleaned_data['birthday']
#
#     # Проверка того, что имя содержит кириллические символы
#     # if alphabet.isdisjoint(data_first_name.lower()):
#     #     raise ValidationError('Имя должно содержать только криллические символы')
#     # if alphabet.isdisjoint(data_middle_name.lower()):
#     #     raise ValidationError('Отчество должно содержать только криллические символы')
#     # if alphabet.isdisjoint(data_last_name.lower()):
#     #     raise ValidationError('Фамилия должна содержать только криллические символы')
#
#     # Проверка того, что день рождения в будующем.
#     # if data_birthday > datetime.date.today() + datetime.timedelta(weeks=4):
#     #     raise ValidationError('Invalid date - renewal more than 4 weeks ahead')
#
#     # Помните, что всегда надо возвращать "очищенные" данные.
#     return data_first_name, data_middle_name, data_last_name
class RenewManagerForm(ModelForm):
    class Meta:
        model = Manager
        fields = ['first_name',
                  'middle_name',
                  'last_name', ]

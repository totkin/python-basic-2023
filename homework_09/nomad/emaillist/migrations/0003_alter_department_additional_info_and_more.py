# Generated by Django 4.2.6 on 2023-10-09 11:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("emaillist", "0002_alter_department_additional_info_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="department",
            name="additional_info",
            field=models.CharField(
                blank=True,
                help_text="Дополнительная информация по отделу",
                max_length=255,
                verbose_name="Доп информация",
            ),
        ),
        migrations.AlterField(
            model_name="manager",
            name="last_name",
            field=models.CharField(max_length=50, verbose_name="Фамилия"),
        ),
        migrations.AlterField(
            model_name="manager",
            name="middle_name",
            field=models.CharField(blank=True, max_length=50, verbose_name="Отчество"),
        ),
    ]
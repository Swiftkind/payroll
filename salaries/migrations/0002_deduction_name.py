# Generated by Django 2.2.6 on 2019-10-29 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salaries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deduction',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
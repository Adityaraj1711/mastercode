# Generated by Django 2.2.3 on 2019-07-13 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specs', '0003_auto_20190713_1838'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaintform',
            old_name='deliver_address',
            new_name='delivery_address',
        ),
        migrations.RemoveField(
            model_name='complaintform',
            name='model',
        ),
    ]

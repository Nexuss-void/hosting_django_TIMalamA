# Generated by Django 5.2 on 2025-06-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layananhotel_app', '0003_user_is_cashier'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='code',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]

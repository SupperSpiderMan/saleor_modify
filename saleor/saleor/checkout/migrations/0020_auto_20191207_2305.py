# Generated by Django 2.2.3 on 2019-12-08 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0019_checkout_gift_cards'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutline',
            name='param_file',
            field=models.FileField(blank=True, null=True, upload_to='saved_files/param_files'),
        ),
        migrations.AddField(
            model_name='checkoutline',
            name='user_upload_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

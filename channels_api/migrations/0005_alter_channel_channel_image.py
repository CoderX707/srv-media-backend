# Generated by Django 4.0.2 on 2022-02-07 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channels_api', '0004_alter_channel_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='channel_image',
            field=models.ImageField(default='not_found.jpg', upload_to='channelImages'),
        ),
    ]

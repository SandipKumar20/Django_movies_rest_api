# Generated by Django 5.0.4 on 2024-04-23 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviedata_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='image',
            field=models.ImageField(default='Images/None/Noimg.jpg', upload_to='Images/'),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-20 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0002_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="image_url",
            field=models.CharField(
                default="https://www.billboard.com/wp-content/uploads/2021/07/rick-astley-villa-maria-2020-billboard-1548-1627575428.jpg",
                max_length=2083,
            ),
        ),
    ]

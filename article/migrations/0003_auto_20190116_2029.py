# Generated by Django 2.1.5 on 2019-01-16 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20190116_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='published_date',
            field=models.DateField(auto_now=True),
        ),
    ]
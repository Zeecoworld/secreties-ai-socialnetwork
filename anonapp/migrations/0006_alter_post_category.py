# Generated by Django 3.2.9 on 2021-12-26 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anonapp', '0005_auto_20211221_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Davido', 'Davido'), ('Wizkid', 'Wizkid'), ('Drake', 'Drake'), ('JBeiber', 'JBeiber'), ('Cardib', 'Cardib')], max_length=128, verbose_name='category'),
        ),
    ]
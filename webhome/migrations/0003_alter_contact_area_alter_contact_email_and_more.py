# Generated by Django 5.1.4 on 2025-01-02 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhome', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='area',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='marriageDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]

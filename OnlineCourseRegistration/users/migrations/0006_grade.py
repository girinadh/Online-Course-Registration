# Generated by Django 2.1.2 on 2018-10-25 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20181019_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=20)),
                ('grade_point', models.CharField(max_length=20)),
            ],
        ),
    ]
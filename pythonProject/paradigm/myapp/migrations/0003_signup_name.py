# Generated by Django 4.0.5 on 2022-06-25 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_signup_name_signup_mid_alter_signup_myprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]

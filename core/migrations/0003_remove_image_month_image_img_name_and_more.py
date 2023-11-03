# Generated by Django 4.2.6 on 2023-11-02 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_image_month'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='month',
        ),
        migrations.AddField(
            model_name='image',
            name='img_name',
            field=models.CharField(default='Image from Ap Assets', max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='img_type',
            field=models.CharField(choices=[('BACKGROUND', 'background'), ('LOGO', 'logo'), ('GAME', 'game'), ('VFX', 'vfx')], default='BACKGROUND', max_length=10),
        ),
    ]
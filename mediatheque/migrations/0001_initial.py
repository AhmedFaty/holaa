# Generated by Django 4.2.4 on 2023-09-14 19:48

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('contenu', models.TextField()),
                ('image', models.ImageField(default='first_page1.jpg', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', embed_video.fields.EmbedVideoField()),
                ('titre', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=250)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

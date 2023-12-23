# Generated by Django 4.2.4 on 2023-10-30 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enseignement', '0004_bibliondaguasarr_headerndaguasarr_videondaguasarr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('contenu', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
            ],
        ),
    ]

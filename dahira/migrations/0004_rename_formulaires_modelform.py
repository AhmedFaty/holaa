# Generated by Django 4.2.4 on 2023-12-02 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dahira', '0003_rename_adresse_formulaires_adresse_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Formulaires',
            new_name='ModelForm',
        ),
    ]
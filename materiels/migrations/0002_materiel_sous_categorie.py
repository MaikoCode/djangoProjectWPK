# Generated by Django 4.2.3 on 2023-07-14 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materiels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materiel',
            name='sous_categorie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='materiels.souscategorie'),
        ),
    ]
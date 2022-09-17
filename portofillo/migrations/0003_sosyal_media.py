# Generated by Django 3.2.4 on 2022-09-17 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofillo', '0002_auto_20220915_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sosyal_Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='facebook')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='instagram')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='twitter')),
            ],
        ),
    ]
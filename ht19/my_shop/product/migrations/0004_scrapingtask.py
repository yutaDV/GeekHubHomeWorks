# Generated by Django 4.1.5 on 2023-01-20 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_id_product_product_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapingTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_text', models.TextField(default='Enter product ID to search separated by commas.', max_length=500)),
            ],
        ),
    ]

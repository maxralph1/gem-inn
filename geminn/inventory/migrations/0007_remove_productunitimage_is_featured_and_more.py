# Generated by Django 4.1.7 on 2023-04-10 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_remove_productunit_is_featured_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productunitimage',
            name='is_featured',
        ),
        migrations.AddField(
            model_name='productunitimage',
            name='is_product_unit_default',
            field=models.BooleanField(default=False, help_text='Change as default image of product unit', verbose_name='Product unit default image'),
        ),
    ]
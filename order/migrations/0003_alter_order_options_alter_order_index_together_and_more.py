# Generated by Django 4.1.2 on 2023-01-23 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterIndexTogether(
            name='order',
            index_together=set(),
        ),
        migrations.AddField(
            model_name='order',
            name='cep',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]

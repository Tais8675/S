# Generated by Django 3.2.12 on 2023-04-12 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0002_auto_20230412_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaCompras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batata', models.BooleanField(default=False)),
                ('cenoura', models.BooleanField(default=False)),
                ('brocolis', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='lista',
            name='compras',
            field=models.CharField(max_length=64),
        ),
        migrations.DeleteModel(
            name='dia',
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-30 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='emotion',
            field=models.IntegerField(choices=[(1, '😍행복해요'), (2, '🙃보통이에요'), (3, '😑별로에요'), (4, '😭슬퍼요'), (5, '😡화나요')], default=2),
        ),
    ]

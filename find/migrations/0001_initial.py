# Generated by Django 2.2.10 on 2020-05-28 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('zone', models.IntegerField(choices=[(1, '서울'), (2, '경기,인천'), (3, '강원'), (4, '충청'), (5, '경상'), (6, '제주')], default=0)),
                ('info', models.TextField()),
                ('site_url', models.URLField()),
                ('address', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=15)),
                ('img', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], default=5)),
                ('content', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('Hospital_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='find.Hospital')),
            ],
        ),
    ]

# Generated by Django 4.0.6 on 2023-02-13 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('rate', models.ManyToManyField(blank=True, null=True, to='rating.rating')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]

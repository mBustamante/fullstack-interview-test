# Generated by Django 3.2.9 on 2022-01-24 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PullRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=64)),
                ('target', models.CharField(max_length=64)),
                ('author_name', models.CharField(max_length=64)),
                ('author_email', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('OPEN', 'OPEN'), ('MERGED', 'MERGED'), ('CLOSED', 'CLOSED')], max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

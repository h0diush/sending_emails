# Generated by Django 4.1.4 on 2022-12-06 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailForSending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=35, verbose_name='Электронная почта')),
                ('owner', models.CharField(blank=True, max_length=155, null=True, verbose_name='Владелец почты')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Электронная почта',
                'verbose_name_plural': 'Электронные почты',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='GroupEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Группа для электронной почты',
                'verbose_name_plural': 'Группы для электронной почты',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('email', models.ManyToManyField(related_name='emails', to='sending_emails.emailforsending', verbose_name='Электронные почты')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщении',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='emailforsending',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sending_emails.groupemail', verbose_name='Группа'),
        ),
    ]

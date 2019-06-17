# Generated by Django 2.1 on 2019-06-16 19:55

from django.db import migrations, models
import django.db.models.deletion
import payment.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentSumm', models.IntegerField()),
                ('userLogin', models.TextField()),
                ('userEmail', models.EmailField(max_length=254)),
                ('inputTime', models.DateTimeField(auto_now_add=True)),
                ('confirm', models.BooleanField()),
                ('description', models.TextField()),
                ('confirmTime', models.DateTimeField(default=payment.models.get_delta)),
            ],
        ),
        migrations.CreateModel(
            name='ReturnPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='payment.Payment')),
            ],
        ),
    ]

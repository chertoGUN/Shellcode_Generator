# Generated by Django 3.1.1 on 2020-09-21 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrivEnc', '0002_ip_port_sleep'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payload_type', models.CharField(choices=[('meterpreter/bind_tcp', 'meterpreter/bind_tcp'), ('meterpreter/reverse_tcp', 'meterpreter/reverse_tcp')], max_length=100)),
            ],
        ),
    ]
# Generated by Django 2.0 on 2019-06-01 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('warehouse', '0014_auto_20190601_2206'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_name', models.CharField(max_length=100, verbose_name='品名')),
                ('good_version', models.CharField(max_length=100, verbose_name='型号')),
                ('good_num', models.IntegerField(verbose_name='数量')),
                ('apply_date', models.DateField(auto_now_add=True, verbose_name='申请日期')),
                ('sanction_date', models.DateField(auto_now=True, verbose_name='批准日期')),
                ('price', models.BigIntegerField(verbose_name='单价')),
                ('total_price', models.BigIntegerField(verbose_name='总价')),
                ('buyer_date', models.DateField(auto_now=True, verbose_name='采购日期')),
                ('apply_staff_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_a', to=settings.AUTH_USER_MODEL, verbose_name='申请人')),
                ('buyer_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='purchase_c', to=settings.AUTH_USER_MODEL, verbose_name='采购员')),
                ('sanction_staff_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_b', to=settings.AUTH_USER_MODEL, verbose_name='批准人')),
            ],
        ),
    ]

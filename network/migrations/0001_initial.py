# Generated by Django 4.1.7 on 2023-02-19 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('level', models.PositiveSmallIntegerField(choices=[(1, 'Завод'), (2, 'Розничная сеть'), (3, 'Индивидуальный предприниматель')], verbose_name='Вид звена')),
                ('debt', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Задолженность')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('country', models.CharField(max_length=30, verbose_name='Страна')),
                ('city', models.CharField(max_length=30, verbose_name='Город')),
                ('street', models.CharField(max_length=30, verbose_name='Улица')),
                ('home_number', models.IntegerField(verbose_name='Номер дома')),
            ],
            options={
                'verbose_name': 'Звено сети',
                'verbose_name_plural': 'Звенья сети',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('type', models.CharField(max_length=50, verbose_name='Модель')),
                ('date_issue', models.DateTimeField(verbose_name='Дата выхода продукта на рынок')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='LinkProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.link')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.products')),
            ],
        ),
        migrations.AddField(
            model_name='link',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='network.products'),
        ),
        migrations.AddField(
            model_name='link',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='network.link', verbose_name='Поставщик'),
        ),
    ]

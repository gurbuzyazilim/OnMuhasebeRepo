# Generated by Django 2.2.2 on 2019-07-21 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kasa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KasaKodu', models.CharField(max_length=10)),
                ('KasaAdi', models.CharField(max_length=50)),
                ('KasaAcilisBakiyesi', models.DecimalField(decimal_places=2, max_digits=10)),
                ('KasaBorc', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('KasaAlacak', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('KasaAcilisTarihi', models.DateField()),
                ('KasaKaydiOlusturan', models.CharField(max_length=50, null=True)),
                ('KasaDuzenlemeTarihi', models.DateField(null=True)),
                ('KasaKaydıDuzenleyen', models.CharField(max_length=50, null=True)),
                ('Aciklama', models.CharField(max_length=250, null=True)),
                ('IsSaved', models.BooleanField(default=False)),
                ('IsVerified', models.BooleanField(default=False)),
                ('IsDeleted', models.BooleanField(default=False)),
                ('IsCanceled', models.BooleanField(default=False)),
                ('IsTransferred', models.BooleanField(default=False)),
                ('IsTransferCache', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='KasaHareketleri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KasaKodu', models.CharField(max_length=10)),
                ('KasaBorc', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('KasaAlacak', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('Makbuz', models.CharField(max_length=50)),
                ('MakbuzNo', models.CharField(max_length=10)),
                ('MakbuzTarihi', models.DateField()),
                ('Aciklama', models.CharField(max_length=250, null=True)),
                ('CariKodu', models.CharField(max_length=10)),
                ('IsSaved', models.BooleanField(default=False)),
                ('IsVerified', models.BooleanField(default=False)),
                ('IsDeleted', models.BooleanField(default=False)),
                ('IsCanceled', models.BooleanField(default=False)),
                ('IsTransferred', models.BooleanField(default=False)),
                ('IsTransferCache', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MakbuzNo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KasaKodu', models.CharField(max_length=10)),
                ('TahsilatMakbuzuNo', models.CharField(max_length=10, null=True)),
                ('TediyeMakbuzuNo', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]

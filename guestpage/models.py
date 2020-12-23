from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class Wajibpajak(models.Model):
    nik = models.CharField(max_length=16)
    nama = models.CharField(max_length=64)
    jenis_kelamin = models.CharField(max_length=16)
    tempat_lahir = models.CharField(max_length=64)
    tanggal_lahir = models.DateField()
    alamat = models.TextField()


class Sppt(models.Model):
    nop = models.CharField(max_length=18)
    tahun_pajak = models.IntegerField()
    letak_objek_pajak = models.TextField()
    id_wp = models.IntegerField()
    op_bumi_njop = models.IntegerField()
    op_bangunan_njop = models.IntegerField()
    pbb_terhutang = models.IntegerField()
    tgl_jatuh_tempo = models.DateField()
    status = models.CharField(max_length=16)


class Transaksi(models.Model):
    id_pajak = models.IntegerField()
    waktu_bayar = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=16)

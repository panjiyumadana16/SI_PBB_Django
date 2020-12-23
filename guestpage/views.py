from django.shortcuts import render, redirect, get_object_or_404
from .models import Wajibpajak, Sppt, Transaksi
from django.urls import reverse_lazy
from .utils import Render

# Create your views here.
var = {}


def index(self):
    return render(self, 'guestpage/index.html')


def wpindex(self):
    var['wajibpajak'] = Wajibpajak.objects.values('id', 'nik', 'nama', 'jenis_kelamin', 'tempat_lahir', 'tanggal_lahir', 'alamat').\
        order_by('id')
    return render(self, 'guestpage/wp/index.html', context=var)


def wpInsertPage(self):
    return render(self, 'guestpage/wp/insert.html')


def wpCreate(self):
    if self.method == 'POST':
        wp = Wajibpajak()
        wp.nik = self.POST.get('nik')
        wp.nama = self.POST.get('nama')
        wp.jenis_kelamin = self.POST.get('jenis_kelamin')
        wp.tempat_lahir = self.POST.get('tempat_lahir')
        wp.tanggal_lahir = self.POST.get('tanggal_lahir')
        wp.alamat = self.POST.get('alamat')
        wp.save()

        return redirect('/wp/')

    else:
        return redirect('/wp/insert')


def wpEditPage(self, pk):
    wp = {}
    wp['wajibpajak'] = Wajibpajak.objects.filter(pk=pk)
    return render(self, 'guestpage/wp/edit.html', wp)


def wpUpdate(self, pk):
    if self.method == 'POST':
        wp = Wajibpajak.objects.get(pk=pk)
        wp.nik = self.POST.get('nik')
        wp.nama = self.POST.get('nama')
        wp.jenis_kelamin = self.POST.get('jenis_kelamin')
        wp.tempat_lahir = self.POST.get('tempat_lahir')
        wp.tanggal_lahir = self.POST.get('tanggal_lahir')
        wp.alamat = self.POST.get('alamat')
        wp.save()

        return redirect('/wp/')

    else:
        return redirect('/wp/edit/int:<pk>')


def wpDelete(self, pk):
    wp = Wajibpajak.objects.get(pk=pk)
    wp.delete()

    return redirect('/wp/')


def wpGetReportPDF(self):
    wp = {}
    wp['wajibpajak'] = Wajibpajak.objects.values('id', 'nik', 'nama', 'jenis_kelamin', 'tempat_lahir', 'tanggal_lahir', 'alamat').\
        order_by('id')
    return Render.to_pdf(self, 'guestpage/wp/reportPDF.html', context=wp)


def spptindex(self):
    sppt = {}
    sppt['sppt'] = Sppt.objects.all()
    return render(self, 'guestpage/sppt/index.html', context=sppt)


def spptInsertPage(self):
    wp = {}
    wp['wajibpajak'] = Wajibpajak.objects.all()
    return render(self, 'guestpage/sppt/insert.html', context=wp)


def spptCreate(self):
    if self.method == 'POST':
        sp = Sppt()
        sp.nop = self.POST.get('nop')
        sp.tahun_pajak = self.POST.get('tahun_pajak')
        sp.letak_objek_pajak = self.POST.get('letak_objek_pajak')
        sp.id_wp = self.POST.get('id_wp')
        sp.op_bumi_njop = self.POST.get('op_bumi_njop')
        sp.op_bangunan_njop = self.POST.get('op_bangunan_njop')
        sp.tgl_jatuh_tempo = self.POST.get('tgl_jatuh_tempo')
        sp.status = 'Belum Lunas'
        pbb = 0.005 * (int(sp.op_bangunan_njop) +
                       int(sp.op_bumi_njop) - 10000000)
        if pbb < 0:
            sp.pbb_terhutang = 2000
        else:
            sp.pbb_terhutang = pbb
        sp.save()

        return redirect('/sppt/')

    else:
        return redirect('/sppt/insert')


def spptEditPage(self, pk):
    sppt = {}
    wp = {}
    sppt = Sppt.objects.filter(pk=pk)
    wp = Wajibpajak.objects.all()
    return render(self, 'guestpage/sppt/edit.html', {'sppt': sppt, 'wajibpajak': wp})


def spptUpdate(self, pk):
    if self.method == 'POST':
        sp = Sppt.objects.get(pk=pk)
        sp.nop = self.POST.get('nop')
        sp.tahun_pajak = self.POST.get('tahun_pajak')
        sp.letak_objek_pajak = self.POST.get('letak_objek_pajak')
        sp.id_wp = self.POST.get('id_wp')
        sp.op_bumi_njop = self.POST.get('op_bumi_njop')
        sp.op_bangunan_njop = self.POST.get('op_bangunan_njop')
        sp.tgl_jatuh_tempo = self.POST.get('tgl_jatuh_tempo')
        pbb = 0.005 * (int(sp.op_bangunan_njop) +
                       int(sp.op_bumi_njop) - 10000000)
        if pbb < 0:
            sp.pbb_terhutang = 2000
        else:
            sp.pbb_terhutang = pbb
        sp.save()

        return redirect('/sppt/')

    else:
        return redirect('/sppt/edit/<int:pk>/')


def spptDelete(self, pk):
    sp = Sppt.objects.get(pk=pk)
    sp.delete()

    return redirect('/sppt/')


def trxindex(self):
    trx = {}
    trx['transaksi'] = Transaksi.objects.all()
    return render(self, 'guestpage/transaksi/index.html', context=trx)


def trxInsert(self):
    sppt = {}
    sppt['sppt'] = Sppt.objects.all()
    return render(self, 'guestpage/transaksi/insert.html', context=sppt)


def trxCreate(self):
    if self.method == 'POST':
        trx = Transaksi()
        trx.id_pajak = self.POST.get('id_pajak')
        trx.status = 'Lunas'
        trx.save()

        sppt = Sppt.objects.get(pk=int(self.POST.get('id_pajak')))
        sppt.status = 'Lunas'
        sppt.save()

        return redirect('/trx/')

    else:
        return redirect('/trx/insert')

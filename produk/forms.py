from django import forms
from .models import Produk

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama_produk', 'harga', 'kategori', 'status']

    def clean_nama_produk(self):
        nama_produk = self.cleaned_data.get('nama_produk')
        if not nama_produk:
            raise forms.ValidationError("Nama produk harus diisi!")
        return nama_produk

    def clean_harga(self):
        harga = self.cleaned_data.get('harga')
        try:
            harga = int(float(harga))
            if harga < 0:
                raise forms.ValidationError("Harga harus berupa angka bulat positif!")
            return harga
        except (TypeError, ValueError):
            raise forms.ValidationError("Harga harus berupa angka bulat positif!")

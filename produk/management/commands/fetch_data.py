import requests
from django.core.management.base import BaseCommand
from produk.models import Produk, Kategori, Status

class Command(BaseCommand):
    help = 'Fetch products dari API dan simpan ke database'

    def handle(self, *args, **kwargs):
        url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
        response = requests.post(url, data={"username": "tesprogrammer110125C12", "password": "4ac0087b411a38bad7c428dd1add9a8b"})
        data = response.json()

        for item in data['data']:
            kategori, _ = Kategori.objects.get_or_create(nama_kategori=item['kategori'])
            status, _ = Status.objects.get_or_create(nama_status=item['status'])

            Produk.objects.update_or_create(
                nama_produk=item['nama_produk'],
                defaults={
                    'harga': item['harga'],
                    'kategori': kategori,
                    'status': status
                }
            )

        self.stdout.write("Data berhasil disimpan.")
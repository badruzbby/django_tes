from django.shortcuts import render
from rest_framework import viewsets
from .models import Produk
from .serializers import ProdukSerializer
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produk
from .forms import ProdukForm
# Create your views here.

class ProdukViewSet(viewsets.ModelViewSet):
    queryset = Produk.objects.filter(status__nama_status='bisa dijual')
    serializer_class = ProdukSerializer

def produk_list(request):
    produk_list = Produk.objects.filter(status__nama_status="bisa dijual")
    return render(request, 'produk_list.html', {'produk_list': produk_list})

def produk_tambah(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produk_list')
    else:
        form = ProdukForm()
    return render(request, 'produk_form.html', {'form': form})

def produk_edit(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            return redirect('produk_list')
    else:
        form = ProdukForm(instance=produk)
    return render(request, 'produk_form.html', {'form': form, 'produk': produk})

def produk_hapus(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    if request.method == 'POST':
        produk.delete()
        return redirect('produk_list')
    return render(request, 'produk_confirm_delete.html', {'produk': produk})

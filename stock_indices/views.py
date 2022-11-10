from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import IndexVolume

def get(request, pk):
    index_volume = IndexVolume.objects.get(id=pk)
    print(index_volume.stock_id)
    print(index_volume.date)
    print(index_volume.index)

    return JsonResponse({
        'date': index_volume.date,
        'stock_id': index_volume.stock_id,
        'index': index_volume.index,
    }, safe=False)
    # return render(request, 'expenses/index.html', context)
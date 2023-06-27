from django.shortcuts import render, redirect
from perfume.forms import MemoryCreationForm
from perfume.models import Memory


def list_perfume(request):
    # product_list = Product.objects.all() #DB에 있는 product 전체 가져오자
    # context = {'product_list' : product_list} #product_list라는 키로 놓자
    # #product/product_list.html에 보내자
    # return render(request, 'product/product_list.html', context)
    return render(request, 'perfume/index.html')


# def year_90(request):
#     return render(request, 'perfume/year90.html')

def list_memory(request):
    memory_list = Memory.objects.all()
    context = {'memory_list' : memory_list}
    return render(request, 'perfume/year90.html', context)

def write_memory(request):
    if request.method == 'POST':
        form = MemoryCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('perfume:year90')
    else:
        form = MemoryCreationForm()
    return render(request, 'perfume/memory_create.html', {'form' : form })


def detail_memory(request, pk):
    memory_detail = Memory.objects.get(pk=pk)
    context = {'memory' : memory_detail}
    return render(request, 'perfume/memory_detail.html', context)
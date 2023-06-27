from django.shortcuts import render

def list_perfume(request):
    # product_list = Product.objects.all() #DB에 있는 product 전체 가져오자
    # context = {'product_list' : product_list} #product_list라는 키로 놓자
    # #product/product_list.html에 보내자
    # return render(request, 'product/product_list.html', context)
    return render(request, 'perfume/index.html')


def year_90(request):
    return render(request, 'perfume/year90.html')

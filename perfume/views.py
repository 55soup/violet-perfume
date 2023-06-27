from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from perfume.forms import MemoryCreationForm, CommentCreationsForm
from perfume.models import Memory, Comments


def list_perfume(request):
    # product_list = Product.objects.all() #DB에 있는 product 전체 가져오자
    # context = {'product_list' : product_list} #product_list라는 키로 놓자
    # #product/product_list.html에 보내자
    # return render(request, 'product/product_list.html', context)
    return render(request, 'perfume/index.html')


# def year_90(request):
#     return render(request, 'perfume/year90.html')

def list_memory90(request):
    memory_list = Memory.objects.filter(year__contains="90")
    context = {'memory_list' : memory_list}
    return render(request, 'perfume/year90.html', context)

def list_memory00(request):
    memory_list = Memory.objects.filter(year__contains="00")
    context = {'memory_list' : memory_list}
    return render(request, 'perfume/year00.html', context)

def list_memory10(request):
    memory_list = Memory.objects.filter(year__contains="10")
    context = {'memory_list' : memory_list}
    return render(request, 'perfume/year10.html', context)

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
    comment_form = CommentCreationsForm()
    list_comments = Comments.objects.filter(memory=pk) # memory 각 id에 맞는 댓글 가져옴

    post_detail = get_object_or_404(Memory, pk=pk)
    if request.method == "POST": #댓글작성
        comment = Comments()
        comment.memory = memory_detail
        comment.user = request.POST['user']
        comment.comment = request.POST['comment']
        comment.image = request.POST['image']
        # comment.parent_comment =
        comment.date = timezone.now()
        comment.save()
    context = {
        'memory' : memory_detail,
        'comment_form' : comment_form,
        'list_comments' : list_comments
    }
    return render(request, 'perfume/memory_detail.html', context)

def comment_write(request, pk): # 작성댓글 저장
    if request.method == 'POST':
        comment_write = CommentCreationsForm(request.POST)
        if comment_write.is_valid():
            # 어떤 게시글의 댓글인지 저장
            finished_form = comment_write.save(commit=False)
            finished_form.memory = get_object_or_404(Memory, pk=pk)
            finished_form.save()
            return redirect('perfume:detail_memory', pk)
        else:
            comment_write = CommentCreationsForm()
        return redirect(request, 'perfume:detail_memory', {'form' : comment_write})
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TableForm
from .models import Table


def create(request):
    context = {"tag_var": 'tag_var'}
    return render(request, "blog_posts/post_view.html", context)


# Create your views here.

def table_list(request, template="blog_posts/post_list.html"):
    table = Table.objects.all()
    context = {"object_list": table}
    print(table)
    return render(request, template, context)


def table_view(request, pk, template='blog_posts/post_view.html'):
    table = get_object_or_404(Table, pk=pk)
    context = {'table_o': table}
    return render(request, template, context)


def table_create(request, template='blog_posts/post_form.html'):
    table_f = TableForm(request.POST or None)
    if table_f.is_valid():
        table_f.save()
        return redirect('list')
    context = {'table_f': table_f}
    return render(request, template, context)


def table_update(request, pk, template='blog_posts/post_form.html'):
    table = get_object_or_404(Table, pk=pk)
    table_f = TableForm(request.POST or None, instance=table)
    if table_f.is_valid():
        table_f.save()
        return redirect('list')
    context = {'table_f': table_f}
    return render(request, template, context)


def table_delete(request, pk, template='blog_posts/post_delete.html'):
    table = get_object_or_404(Table, pk=pk)
    if request.method == 'POST':
        table.delete()
        return redirect('list')
    context = {'table_o': table}
    return render(request, template, context)

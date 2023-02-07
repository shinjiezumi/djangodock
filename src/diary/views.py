from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from .forms import DayCreateForm
from .models import Day


def index(request):
    context = {
        'day_list': Day.objects.all()
    }
    return render(request, 'diary/day_list.html', context)


def add(request):
    # 送信内容を元にフォームを作る
    form = DayCreateForm(request.POST or None)

    # フォーム送信で入力内容に問題なければ保存
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')

    print(timezone.now())
    print(timezone.localtime(timezone.now()))
    # 通常遷移時や入力に誤りがあればページを表示
    context = {
        'form': form
    }
    return render(request, 'diary/day_form.html', context)


def update(request, pk):
    # pkを元に日記を取得
    day = get_object_or_404(Day, pk=pk)

    # フォームに反映
    form = DayCreateForm(request.POST or None, instance=day)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')

    context = {
        'form': form
    }
    return render(request, 'diary/day_form.html', context)


def delete(request, pk):
    # pkを元に日記を取得
    day = get_object_or_404(Day, pk=pk)

    if request.method == 'POST':
        day.delete()
        return redirect('diary:index')

    context = {
        'day': day
    }
    return render(request, 'diary/day_confirm_delete.html', context)


def detail(request, pk):
    # pkを元に日記を取得
    day = get_object_or_404(Day, pk=pk)

    context = {
        'day': day
    }
    return render(request, 'diary/day_detail.html', context)


# クラスビュー版
class IndexView(generic.ListView):
    model = Day


class AddView(generic.CreateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:class_view_index')


class UpdateView(generic.UpdateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:class_view_index')


class DeleteView(generic.DeleteView):
    model = Day
    success_url = reverse_lazy('diary:class_view_index')


class DetailView(generic.DetailView):
    model = Day

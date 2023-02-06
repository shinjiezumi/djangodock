from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import DayCreateForm
from .models import Day


def index(request):
    context = {
        'day_list': Day.objects.all()
    }
    return render(request, 'diary/list.html', context)


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

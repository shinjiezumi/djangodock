from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import DayCreateForm


def index(request):
    return render(request, 'diary/list.html')


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

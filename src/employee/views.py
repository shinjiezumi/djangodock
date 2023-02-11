from django.views import generic

from .form import SearchForm
from .models import Employee


class IndexView(generic.ListView):
    model = Employee

    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = SearchForm(self.request.GET)  # 検索内容を引き継ぐ
        return context

    def get_queryset(self):
        # テンプレートへ渡す「employee_list」を作成する
        form = SearchForm(self.request.GET)
        form.is_valid()  # cleaned_dataの取得に必要

        # 全社員を取得
        queryset = super().get_queryset()

        # 部署の選択があれば絞り込み
        department = form.cleaned_data['department']
        if department:
            queryset = queryset.filter(department=department)

        # サークルの選択があればサークルで絞り込み
        club = form.cleaned_data['club']
        if club:
            queryset = queryset.filter(club=club)

        return queryset

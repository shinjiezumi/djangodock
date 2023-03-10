from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views import generic

from .form import CommentCreateForm
from .models import Post, Comment


class IndexView(generic.ListView):
    model = Post
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.order_by('-created_at')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)  # ブログ名、本文の部分一致
            )
        return queryset


class CategoryView(generic.ListView):
    model = Post
    paginate_by = 10

    """ 書き方1 """
    #     def get_queryset(self):
    #         category = get_object_or_404(Category, pk=self.kwargs['pk'])  # 指定されたカテゴリオブジェクトを取得
    #         queryset = Post.objects.order_by('-created_at').filter(category=category)  # 絞り込み
    #         return queryset

    """
    書き方2
    """

    def get_queryset(self):
        category_pk = self.kwargs['pk']  # 指定されたカテゴリID取得
        queryset = Post.objects.order_by('-created_at').filter(category__pk=category_pk)  # 絞り込み
        return queryset


class DetailView(generic.DetailView):
    model = Post


class CommentView(generic.CreateView):
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        post_pk = self.kwargs['post_pk']
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=post_pk)
        comment.save()
        return redirect('blog:detail', pk=post_pk)

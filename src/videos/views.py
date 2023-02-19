from django.urls import reverse_lazy
from django.views import generic

from .form import VideoCreateForm
from .models import Video


class IndexView(generic.ListView):
    """ 動画一覧画面 """
    model = Video


class CreateView(generic.CreateView):
    """ 動画アップロード画面 """
    model = Video
    form_class = VideoCreateForm
    success_url = reverse_lazy('videos:index')


class PlayView(generic.DetailView):
    """ 動画再生画面 """
    model = Video

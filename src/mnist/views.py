import base64
from io import BytesIO

import numpy as np
from PIL import Image
from django.shortcuts import render
from django.views import generic

from .forms import ImageUploadForm
from .lib import predict


class UploadView(generic.FormView):
    template_name = 'mnist/upload.html'
    form_class = ImageUploadForm

    def form_valid(self, form):
        # アップロードファイル本体を取得
        file = form.cleaned_data['file']
        # ファイルを28x28にリサイズし、グレースケール(モノクロ画像)にする
        img = Image.open(file).resize((28, 28)).convert('L')

        # 学習時と同じ形に画像データを変換する
        img_array = np.asarray(img) / 255
        img_array = img_array.reshape(1, 784)

        # 推論した結果をテンプレートへ渡して表示
        context = {
            'result': predict(img_array)
        }
        return render(self.request, 'mnist/result.html', context)


class PaintView(generic.TemplateView):
    template_name = 'mnist/paint.html'

    def post(self, request):
        base_64_string = request.POST['img-src'].replace(
            'data:image/png;base64,', ''
        )
        file = BytesIO(base64.b64decode(base_64_string))

        # ファイルを28x28にリサイズし、グレースケールにする
        img = Image.open(file).resize((28, 28)).convert('L')

        # 学習時と同じ形に画像データを変換する
        img_array = np.asarray(img) / 255
        img_array = img_array.reshape(1, 784)

        # 推論した結果をテンプレートへ渡して表示
        context = {
            'result': predict(img_array)
        }
        return render(self.request, 'mnist/result.html', context)

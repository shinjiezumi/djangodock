from django.db import models


class Video(models.Model):
    """ 動画モデル """
    title = models.CharField('動画タイトル', max_length=255)
    description = models.TextField('説明(空欄可)', blank=True)
    thumbnail = models.ImageField('サムネイル(空欄可)', upload_to='thumbnails/', null=True, blank=True)
    upload = models.FileField('ファイル', upload_to='uploads/%Y/%m/%d/')
    created_at = models.DateTimeField('作成日', auto_now_add=True)  # default=timezone.now と異なり、編集不可になる（入力欄が表示されない）
    updated_at = models.DateTimeField('更新日', auto_now=True)  # 更新するたびに日時が更新される

    def __str__(self):
        return self.title

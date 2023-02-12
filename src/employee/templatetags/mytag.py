from django import template

register = template.Library()

'''
標準のページネーション機能だと検索パラメータを引き継ぐことができない。
独自のタグで書き足す
'''


@register.simple_tag
def url_replace(request, field, value):
    # GETパラメータを書き換える
    url_dict = request.GET.copy()
    url_dict[field] = value
    return url_dict.urlencode()

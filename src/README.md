# Djangoとは

- PythonのWebフレームワークの中で人気のあるフレームワークの一つ
- 中規模〜大規模なWeb開発にも対応ができる
- ルーティング、テンプレート、O/Rマッパー等、豊富な機能を標準で用意しているフルスタックフレームワーク

# コマンド

## アプリを作成

```shell
python manage.py startapp myapp
```

## モデル作成・マイグレーション実行

```shell
python manage.py makemigrations diary
python manage.py migrate
```

# ソース説明

## manage.py

開発サーバの起動、DBへの反映といったDjangoを管理するためのファイル

## config/__init__.py

パッケージを読み込んだ際の初期化用ファイル

## config/wsgl.py

DjangoをWebサーバ上で動かすために必要なファイル

## config/urls.py

ルーティング

## config/settings.py

Djangoプロジェクト全体の設定を定義する

## アプリ名/migrations

マイグレーション。フレームワーク側で生成

## アプリ名/admin.py

管理画面の設定

## アプリ名/apps.py

アプリケーション自体の設定

## アプリ名/models.py

モデル

## アプリ名/tests.py

テストコード

## アプリ名/views.py

`urls.py`で定義した処理を実際に記載する

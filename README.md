# Ramen_Record_APP

簡単な登録が行えるラーメン店舗記録アプリです。 モデル(app/models.py)の編集とマイグレーション、データ表示の変更だけで自分用に使用することができます。


# Requirement

* Python 3.8.9
* Django 4.2

# Installation

Requirementで列挙したライブラリなどのインストール方法を説明する

```bash
pip install huga_package
```

# Usage

* 1.このプロジェクトを Git クローンで作成します
* 2.コマンドラインでフォルダ先のパスにアクセスしmekemigrationsを行う。
    python3 manage.py makemigrations
* 3.コマンドラインでフォルダ先のパスにアクセスしmigrateを行う。
* 
    python3 manage.py migrate
* 4.コマンドラインでユーザー作成を行う
* 
 　   python3 manage.py createsuperuser
    Username: name
    Password: password
* 5.コマンドラインでサーバーを立ち上げることで、アプリケーションを立ち上げることができる
* 
  　 　python3 manage.py runserver



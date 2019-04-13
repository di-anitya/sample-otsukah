# Sample Application for Anitya
![snapshot](https://user-images.githubusercontent.com/6835793/55947362-463a1f80-5c89-11e9-813a-988e21b1f5af.png)
## インストール方法
1. Python3 をインストール
2. `./install.sh` を実行

## 実行方法
1. `./start_app.sh` を実行
2. Web ブラウザから http://127.0.0.1:8000/ にアクセス
3. 以下のユーザ名/パスワードでログイン
  - user1/password  (is_superuser: true,  is_staff: true,  is_active: true)
  - user2/password  (is_superuser: false, is_staff: true,  is_active: true)
  - user3/password  (is_superuser: true,  is_staff: false, is_active: true)
  - user4/password  (is_superuser: false, is_staff: false, is_active: true)

## メンテナンス
### DB(SQLite) への接続
`./connect_db.sh` を実行

### DB(SQLite) の初期化
`./initialize.sh` を実行

### 特権ユーザの作成
```bash
$ python manage.py createsuperuser
$ python manage.py dumpdata auth.User --indent 4 > users.json
```

### accounts fixtures に設定する暗号化されたパスワード文字列を取得
```bash
./manage.py shell

>>> from django.contrib.auth.hashers import make_password
>>> make_password('Passw0rd')
'pbkdf2_sha256$120000$lzlM64gdQVTB$BpS/OFZH+d52DJa8EYBqiL+6gzt3zNzj0VErFbXOoQw='
```
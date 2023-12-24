# ur_name
CNNモデルでUSB差込口の規格を判定するDjango製Webアプリ。Tech-Baseインターンでの成果物。<br>
とりあえずアップロードした程度のものです。

#依存関係
<li>django</li>
<li>tensorflow (>2.0)</li>
<li>Pillow</li>
<li>numpy</li>

#事前準備
SECRET_KEYをur_name/usb_hanbetsu/usb_hanbetsu/local_setting/local_settings.pyに設定する
```
SECRET_KEY = 'your_secret_key'
```
SECRET_KEYは以下のようにして生成可能
```
user@userpc: python3
Python 3.11.5 (main, Sep 11 2023, 13:23:44) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
'*u^6bvxcxz-uur&d3m+*48(4w6-gk_meygd8=6kwb+z9e21ry@' #SECRET_KEY
>>> 
```
#起動
ur_name/usb_hanbetsuディレクトリに移動し以下を実行
```
python3 manage.py runserver
```
正常に起動すれば最後の方に以下のメッセージが表示されるはず
```
System check identified no issues (0 silenced).
December 25, 2023 - 01:33:27
Django version 4.1, using settings 'usb_hanbetsu.settings'
Starting development server at http://127.0.0.1:8000/
```
以下のURLをWebブラウザに打つと起動する
```
http://127.0.0.1:8000/usbai/
```

#ToDo
<li>機械学習モデル実装コードと精度検証の結果公開</li>
<li>ドキュメント(このページ)の整理・充実</li>
<li>Webアプリの使い勝手向上</li>

#参考
SECRET_KEYの作成: https://blog.kyanny.me/entry/2021/01/27/033507
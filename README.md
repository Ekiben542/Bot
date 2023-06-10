# Bot
N4Botであーる。

# N4Botってなに？

N4Botとは、「みんなの教室」サーバー専属のBotのことである。  


ちなみにBotを動かすのにRenderを使っています。

## 処理（開発者向け）
```py
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
``` 
このコードを使ってサーバーを常時動かしています.（Flaskであーだこーだーする）
処理の方はmain.pyにあるので、壊さない限りはいじっても大丈夫です.

### 余談
~~これ作るのに１週間もかかった.Discord.py勉強します.~~

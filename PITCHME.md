---?color=#E58537
@snap[north-west]
#### **拡張の方向性、方法は自由！**
@snapend
@snap[west span-100]
@ul[text-white](false)
- 今回紹介したプログラムの機能拡張をする
- GUIで操作できるようにする
- DBに対応する
- @color[cyan](***データの取得方法を工夫する（Webスクレイピング）***)
- Web APIに対応する
- @color[cyan](***形態素解析を用いた自然言語処理***)
- word2vecの学習モデルの精度や対応する単語を増やす
@ulend
@snapend

---?color=#E58537
@snap[north-west]
#### **データの収集自動化（静的サイトのWebスクレイピング）**
ブラウザでサイトが開かれるまでの簡略図
![WEB Flow](assets/img/static_website.flow.png)
assets/img
@snapend

---?color=#E58537
#### **HTMLの描画例**
@snap[west span-40]
@code[html zoom-07](hoge.html)
@snapend

---?color=#E58537
@snap[north-west]
#### **pythonでWebスクレイピング（静的なサイト）**
@snapend
```python
from bs4 import BeautifulSoup
import requests

url = "https://www.e-hon.ne.jp/bec/SE/Genre?ccode=99&dcode=06"
response = requests.get(url)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text,"html.parser")

# 本のタイトルを取得
books = [a.text for a in soup.select("div.rankInner a")]
```
---?color=#E58537
@snap[north-west]
#### **データの収集自動化（動的サイトのWebスクレイピング）**
@snapend

---?color=#E58537
@snap[north-west]
#### **先程の本のランキングサイトが動的サイトの場合**
@snapend

---?color=#E58537
@snap[north-west]
##### **PythonでWebスクレイピング（動的なサイト）**
@snapend
```python
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = "https://www.amazon.co.jp/gp/bestsellers/books/ref=zg_bs_books_pg_1?ie=UTF8&pg=1"
browser = webdriver.PhantomJS()
browser.implicitly_wait(3)
browser.get(url)
html_source = browser.page_source
bs_obj = BeautifulSoup(html_source)
books = [a.text for a in bs_obj.select("div.a-fixed-left-grid-col div.p13n-sc-truncated")]
```

---?color=#E58537
@snap[north-west]
##### **形態素解析を用いた自然言語処理（mecab）**
@snapend
```python
tokenized_text = mecab.parse('ハリーポッターと賢者の石').split('\n')[0:-2]
surfaces = [t.split('\t')[0] for t in tokenized_text]
poses = [t.split('\t')[3].split('-')[0] for t in tokenized_text]
morphs = [{"surface":s, "pos":p} for (s,p) in zip(surfaces,poses)]
for m in morphs:
  print(m)

# {'surface': 'ハリーポッター', 'pos': '名詞'}
# {'surface': 'と', 'pos': '助詞'}
# {'surface': '賢者', 'pos': '名詞'}
# {'surface': 'の', 'pos': '助詞'}
# {'surface': '石', 'pos': '名詞'}
```
---


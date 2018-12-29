# Let's Get Started

---
## Add Some Slide Candy
![](assets/img/presentation.png)

---?color=#E58537
@snap[north-west]
#### **拡張の方向性、方法は自由！**
@snapend
@snap[west span-100]
@ul[text-white]
- 今回紹介したプログラムの機能拡張をする
- GUIで操作できるようにする
- DBに対応する
- @color[cyan](***データの取得方法を工夫する（Webスクレイピング）***)
- Web APIに対応する
- @color[cyan](***形態素解析を用いた自然言語処理***)
- word2vecの学習モデルの精度や対応する単語を増やす
@ulend
@snapend
---
@snap[north-west]
#### **データの収集自動化（静的サイトのWebスクレイピング）**
ブラウザでサイトが開かれるまでの簡略図
@snapend
---
@snap[north-west]
#### **pythonでWebスクレイピング（静的なサイト）**
@snapend
---
@snap[north-west]
#### **データの収集自動化（動的サイトのWebスクレイピング）**
@snapend
---
@snap[north-west]
#### **先程の本のランキングサイトが動的サイトの場合**
@snapend
---
@snap[north-west]
##### **PythonでWebスクレイピング（動的なサイト）**
@snapend

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


### グラフやチャートの表示


<canvas data-chart="radar">
    Month, 1月, 2月, 3月, 4月, 5月, 6月, 7月
    1980, 65, 59, 80, 81, 56, 55, 40
    2017, 28, 48, 40, 19, 86, 27, 90
</canvas>
---
<canvas data-chart="line">
<!-- 
{
 "data": {
  "labels": ["January"," February"," March"," April"," May"," June"," July"],
  "datasets": [
   {
    "data":[65,59,80,81,56,55,40],
    "label":"My first dataset","backgroundColor":"rgba(20,220,220,.8)"
   },
   {
    "data":[28,48,40,19,86,27,90],
    "label":"My second dataset","backgroundColor":"rgba(220,120,120,.8)"
   }
  ]
 }, 
 "options": { "responsive": "true" }
}
-->
</canvas>
---
@title[Customize Slide Layout]


@snap[west span-50]
## Customize Slide Content Layout
@snapend

@snap[east span-50]
![](assets/img/presentation.png)
@snapend

---?color=#E58537
@title[Add A Little Imagination]

@snap[north-west]
#### Add a splash of @color[cyan](**color**) and you are ready to start presenting...
@snapend
@snap[west span-55]
@ul[spaced text-white]
- You will be @color[cyan](**amazed**)
- What you can achieve
- *With a little imagination...*
- And **GitPitch Markdown**
@ulend
@snapend

@snap[east span-45]
@img[shadow](assets/img/conference.png)
@snapend

---?image=assets/img/presenter.jpg
@[1]
@[2]
@[3]

@snap[north span-100 headline]
## Now It's Your Turn
@snapend

@snap[south span-100 text-06]
[Click here to jump straight into the interactive feature guides in the GitPitch Docs @fa[external-link]](https://gitpitch.com/docs/getting-started/tutorial/)
@snapend

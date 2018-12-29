import MeCab
mecab = MeCab.Tagger('-Ochasen')
mecab.parse('ハリーポッターと賢者の石').split('\n')

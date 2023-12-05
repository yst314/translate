Yog Sothoth's Yardが読めなすぎる

OCR(Tesseract) => 翻訳(Deepl or Gpt)

## Install
### pip
```shell
pip install -r requirements.txt
```
### deeplのapiキーの設定

`.env`ファイルを作成して`DEEPL_API_KEY=${deeplのapiキー}`を書く

### Tesseract(ocr)をインストールする
- [windows 版のインストール](https://github.com/UB-Mannheim/tesseract/wiki)

- 環境変数のPathに`C:\Program Files\Tesseract-OCR`の Path を通す

### 実行

`python test.py`で実行。

`config.yml`の`hotkey`で設定されてるキーを二回押すとその範囲でスクショして翻訳

## 実行時間

- ocr(tesseract): 0.917316198348999 (689 x 408 jpg)
- translate(deepl): 1.2258949279785156 (1375 文字)



## Unity直翻訳よりいいところ
- 原文見ながらできるので英語勉強できる。（知らんけど）
- Unityじゃなくても翻訳できる。

## メモ
中国語は一文字の情報量が多い(?)から中国語を翻訳する方が api の文字数の節約になる。(知らんけど)
# translatorについて
Configファイルの設定値にしたがって文字列を表示するスクリプトです。

# 使い方
## インストール
以下のコマンドでリポジトリをクローンします。
```
git clone https://github.com/K0j1-y/translator.git
```
## 事前準備
1. importを追加する  
    パスは環境に応じて変更してください。
    ```python
    from translator import Translator
    from lang_type import LangType
    ```
1. Translatorクラスの初期化  
    必要に応じて引数を変更してください。  
    翻訳ファイルのディレクトリ、Configファイル名の共通パート、デフォルトの言語を指定できます。
    ```python
    self._tr = Translator()
    ```
1. 翻訳処理を追加します。
    ```python
    print(self._tr.tr("00-000"))
    ```

## 言語の変更方法
以下のコードを実行してください。
引数は言語のタイプです。
```python
self._tr.change_lang(LangType.JP)
```

# 構成

## Configファイルの設定
Configファイルは`src/lib`ディレクトリに格納されています。

### Configファイルの命名規則
コンフィグファイル名は共通パートと言語の名前パートで構成されます。
デフォルトではそれぞれ"translation"と"EN"となります。

### Configファイルの内容について
Configファイルの構成は以下の通りです。
```json
{
    "keyword": "translation word",
    ...
}
```
キーワードはstr型でユーザはすべての言語で同じキーワードを設定しなければなりません。

### 言語ファイルの追加
他の翻訳用jsonファイルと同じディレクトリに`translation_[一意の文字列].json`というファイルを作成します。
jsonファイルの構成は他の言語ファイルと同じにします。

1. 言語種別をsrc/lang_type.pyに追加します。


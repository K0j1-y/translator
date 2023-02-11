# translator
Translate multi langage word with config files.

日本語版は[こちら](README_JP.md)

# How to use
## Installation
Clone this repository with below command.
```
git clone https://github.com/K0j1-y/translator.git
```
## Preparation
1. Add import part.  
    Please change path part with your environment.
    ```python
    from translator import Translator
    from lang_type import LangType
    ```
1. Initialize Translator class.  
    If you need, please change arguments.  
    Translation file direcotry, a part of file name, default language.
    ```python
    self._tr = Translator()
    ```
1. Add translation part
    Argment is json file's keyword.
    ```python
    print(self._tr.tr("00-000"))
    ```

## How to change language
Run this code in your script.  
Arguments is language type from LangType.
```python
self._tr.change_lang(LangType.JP)
```

# Configuration

## Set up config file
Config file stored src/lib directory.

## About config file name rule
The config file consists of a common part and a language name part.  
The default is "translation" and "EN".

## About confing file containts
The config file structure is below.
```json
{
    "keyword": "translation word",
    ...
}
```
The keyword type is str and user must set same word in all languages.

## Add new language file.
1. Create a file named `translation_[unique string].json` in the same directory as the other translation json files.  
That file structure is same as other traslation file. and same keywords.

1. Add language type in src/lang_type.py.


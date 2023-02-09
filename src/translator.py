from pathlib import Path
import json

from lang_type import LangType

class translator:
    def __init__(self, tr_dir: str = "tr", file_name: str = "translation", lang: LangType = LangType.EN) -> None:
        """ Load and set translate file.
        Parameters:
            tr_dir: Translation file stored direcotry.
            file_name: Translation files common part.
            lang: Language type.
        """
        self._tr_dir = Path(tr_dir)
        if not self._tr_dir.exists():
            raise ValueError(f"translation file directory is not found. forlder path:{tr_dir}")
        self._file_name = file_name
        self._create_file_name(lang)

    def tr(self, tr_key: str, default_value: str = "") -> str:
        """ Run translation.
        Parameters:
            tr_key: Translation keyword that search in translation file.
            default_value: When keyword is missing, display this word.
        Returns:
            Display word.
        """
        return self._tr_dict.get(tr_key, default_value)

    def _create_file_name(self, lang: LangType = LangType.EN) -> None:
        """ Create translation file name.
        Parameters:
            lang: Translation file language type.
        """
        self._load(self._file_name + "_" + lang + ".json")

    def _load(self, file_name: str) -> None:
        """ Load translation file.
        Parameters:
            file_name: Translation file name.
        """
        file_path = self._tr_dir / file_name
        if not self._tr_dir.exists():
            raise ValueError(f"translation file is not found. file path:{file_path}")
        self._tr_dict = json.loads(file_path.read_text())
        
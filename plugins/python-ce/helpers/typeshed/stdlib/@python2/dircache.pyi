from typing import MutableSequence, Text

def reset() -> None: ...
def listdir(path: Text) -> list[str]: ...

opendir = listdir

def annotate(head: Text, list: MutableSequence[str] | MutableSequence[Text] | MutableSequence[str | Text]) -> None: ...

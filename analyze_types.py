from typing import NewType
Punctuation = NewType('Punctuation', tuple[int, int, int, int, int])
Word = NewType('Word', str)
Handle = Iterable[str]
Frequency = dict[Word, int]

from markdown2 import markdown, Markdown
from pathlib import Path

class Note:
    name: str
    description: str
    contents: Markdown
    filename: str

    def __init__(self, filename: Path) -> None:
        with open(filename, 'r') as f:
            self.contents=markdown(f.read(), extras=['metadata', 'fenced-code-blocks'])
        
        self.name = self.contents.metadata['name']
        self.description = self.contents.metadata['description']
        self.filename = filename

    def to_dict(self):
        return {'name':self.name, 'description':self.description, 'contents':self.contents, 'filename':self.filename.name}
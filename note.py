from markdown2 import markdown, Markdown
from pathlib import Path
from datetime import datetime

class Note:
    name: str
    description: str
    created: datetime
    updated: datetime
    contents: Markdown
    filename: str

    def __init__(self, filename: Path) -> None:
        with open(filename, 'r') as f:
            self.contents=markdown(f.read(), extras=['metadata', 'fenced-code-blocks'])
        
        self.name = self.contents.metadata['name']
        self.description = self.contents.metadata['description']
        # self.created = datetime.fromisoformat(self.contents.metadata['created'])
        # self.updated = datetime.fromisoformat(self.contents.metadata['updated'])
        self.filename = filename

    def to_dict(self) -> dict:
        return {'name':self.name, 'description':self.description, 'contents':self.contents, 'filename':self.filename.name}

    def metadata(self) -> dict:
        return {'name': self.name, 'description': self.description, 'filename': self.filename.name}
from markdown2 import markdown
from pathlib import Path

class Note:
    name: str
    description: str
    contents: str
    filename: str

    def __init__(self, filename: Path) -> None:
        with open(filename, 'r') as f:
            self.name = f.readline() # The name and description are in the first two lines.
            self.description = f.readline()
            temp_contents = []
            self.contents=markdown(f.read())
            self.filename = filename

    def to_dict(self):
        return {'name':self.name, 'description':self.description, 'contents':self.contents, 'filename':self.filename.name}
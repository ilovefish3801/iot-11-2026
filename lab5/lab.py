class File:
    """A class that represents a file with a name, an extension and a size in KB"""

    def __init__(self,
                 name: str = "",
                 extension: str = "",
                 size: int = 0):
        self.name = name
        self.extension = extension
        self.size = size

    @property
    def full_name(self) -> str:
        return f"{self.name}.{self.extension}"

    def __str__(self):
        return f"{self.full_name} ({self.size} KB)"


class Folder:
    """A class that represents a folder that can contain files and other folders"""

    def __init__(self,
                 name: str = "folder"):
        self.name = name
        self.children: list[File | Folder] = []

    def add(self, item: "File | Folder"):
        """Add a file or a folder to this folder."""
        self.children.append(item)

    def print_tree(self, level=0):
        """Print this folder and everything inside it as an indented tree"""
        print("\t" * level, f"{self.name}/")
        level += 1
        for item in self.children:
            if isinstance(item, Folder):
                item.print_tree(level=level)
            elif isinstance(item, File):
                print("\t" * level, f"{item}")

    def get_longest_path(self) -> str | None:
        """Return the longest path from this folder to a file

        Only paths that end in a file count, so empty folders are skipped
        Returns None if there are no files inside this folder
        """
        paths = []
        for item in self.children:
            if isinstance(item, Folder):
                child_path = item.get_longest_path()
                if child_path is not None:
                    paths.append(child_path)
            elif isinstance(item, File):
                paths.append(item.full_name)

        if not paths:
            return None

        longest_child = max(paths, key=len)
        return f"{self.name}/{longest_child}"


def main():
    """Build a sample folder tree, print it and show its longest path"""
    root = Folder("root")
    docs = Folder("documents")
    media = Folder("media")
    work_projects = Folder("work_projects")
    archive_2026 = Folder("archive_2026")
    empty_dir = Folder("empty_folder")

    readme = File("readme", "md", 12)
    resume = File("file", "pdf", 450)
    song = File("video", "mp3", 8400)
    secret_report = File("excel_table", "xlsx", 2048)

    archive_2026.add(secret_report)
    work_projects.add(archive_2026)

    docs.add(resume)
    docs.add(work_projects)
    media.add(song)

    root.add(readme)
    root.add(docs)
    root.add(media)
    root.add(empty_dir)

    root.print_tree()

    longest_path = root.get_longest_path()
    print(f"\nНайдовший шлях: \n{longest_path}")


if __name__ == "__main__":
    main()

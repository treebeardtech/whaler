from pathlib import Path

from whaler.report import Report
from whaler.scan import Scan

pytest_plugins = "pytester"


class TestNotebookRun:
    def test_scan(self, testdir):
        Path("a/b").mkdir(parents=True)
        Path("a/a.txt").write_text("asdfasdfasdfadsf")
        Path("a/b/b.txt").write_text("blah")

        nodes = Scan(Path("/Users/a/git/treebeardtech/whaler/.venv")).scan()

        Report(nodes).create(Path("rep.html"))
        pass

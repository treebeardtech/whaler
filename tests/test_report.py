from pathlib import Path

from whaler.report import Node, Report

pytest_plugins = "pytester"


class TestNotebookRun:
    def test_run(self, testdir):
        nodes = [
            Node(Path("venv"), 8),
            Node(Path("venv/bin"), 3),
            Node(Path("venv/bin/python.exe"), 3),
            Node(Path("venv/lib"), 5),
            Node(Path("venv/lib/f.txt"), 2),
            Node(Path("venv/lib/e.dist-info"), 3),
        ]
        r = Report(nodes, Path("rep.html"))
        r.create()

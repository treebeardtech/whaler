from dataclasses import dataclass
from pathlib import Path
from typing import List

import pandas as pd
import plotly.express as px
import plotly.offline
from humanfriendly import format_size

from .node import Node


@dataclass
class Report:
    nodes: List[Node]

    @classmethod
    def create_treemap_node(cls, node: Node):
        return {
            "id": str(node.path.as_posix()),
            "name": node.path.name,
            "parent": str(node.path.parent),
            "size": node.size,
            "desc": f"{str(node.path.as_posix())} ({format_size(node.size * 1000)})",
            "type": node.path.suffix,
        }

    def create(self, out: Path):
        df = pd.DataFrame([Report.create_treemap_node(nn) for nn in self.nodes])

        fig = px.treemap(
            df,
            names="name",
            hover_name="desc",
            ids="id",
            parents="parent",
            values="size",
            color="type",
            # maxdepth=6
        )
        filename = str(out.absolute())
        plotly.offline.plot(fig, filename=filename, auto_open=False)
        print(f"Saved file://{filename}")

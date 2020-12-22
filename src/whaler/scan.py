from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from subprocess import check_output
from typing import List

import pandas as pd

from .node import Node


@dataclass
class Scan:
    path: Path

    def scan(self) -> List[Node]:
        out = check_output(["du", "-a", "-k", str(self.path)])
        df = pd.read_csv(BytesIO(out), sep="\t", names=["size", "path"])
        return [Node(Path(nn["path"]), nn["size"]) for nn in df.T.to_dict().values()]

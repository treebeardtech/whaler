from dataclasses import dataclass
from pathlib import Path


@dataclass
class Node:
    path: Path
    size: int

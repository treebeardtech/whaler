from pathlib import Path
from subprocess import check_output
from typing import Optional

import click
from rich import print

DEFAULT_OUT = "_whaler"
DU_FILENAME = "du.tsv"


@click.command()
@click.option("--image", help="docker image", default=None)
@click.option("--out", help="output path", default=DEFAULT_OUT)
@click.argument("directory", default=".")
def run(directory: str, out: str, image: Optional[str]):
    """"""
    cmd = ["du", "-a", "-k", directory]
    print(f"Running {' '.join(cmd)}")
    du_out = check_output(cmd).decode()
    out_path = Path(out)
    out_path.mkdir(exist_ok=True, parents=True)
    (out_path / DU_FILENAME).write_text(du_out)


if __name__ == "__main__":
    run()

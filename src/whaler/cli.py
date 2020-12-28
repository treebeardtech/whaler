import shutil
from pathlib import Path
from subprocess import check_output
from typing import Optional

import click
from rich import print

DEFAULT_OUT = "_whaler"
HTML_DIR = "html"
DU_FILENAME = "du.tsv"
UI_FILENAME = "html.zip"


@click.command()
@click.option("--image", help="docker image", default=None)
@click.option("--out", help="output path", default=DEFAULT_OUT)
@click.argument("directory", default=".")
@click.option(
    "--server/--no-server",
    default=True,
    help="Run web server on output to immediately view",
)
def run(directory: str, out: str, image: Optional[str], server: bool):
    """"""
    cmd = ["du", "-a", "-k", directory]
    print(f"Running {' '.join(cmd)}")
    du_out = check_output(cmd).decode()
    out_path = Path(out)
    html_path = out_path / HTML_DIR
    html_path.mkdir(exist_ok=True, parents=True)
    (html_path / DU_FILENAME).write_text(du_out)

    ui = Path(__file__).parent / "static" / UI_FILENAME

    shutil.unpack_archive(ui, extract_dir=out_path)

    if server:
        server_cmd = ["python3", "-m", "http.server", "8000"]
        print(f"Running {' '.join(server_cmd)}")
        check_output(server_cmd, cwd=str(html_path))


if __name__ == "__main__":
    run()

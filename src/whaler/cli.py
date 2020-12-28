import shutil
from pathlib import Path
from subprocess import check_output
from typing import Optional, Tuple, Union

import click
from rich import print

DEFAULT_OUT = "_whaler"
HTML_DIR = "html"
DU_FILENAME = "du.tsv"
DU_ARGS = ("-a", "-k")
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

    du_out = shell(get_du_cmd(Path(directory), image))
    out_path = Path(out)
    html_path = out_path / HTML_DIR
    html_path.mkdir(exist_ok=True, parents=True)
    (html_path / DU_FILENAME).write_text(du_out)

    ui = Path(__file__).parent / "static" / UI_FILENAME

    shutil.unpack_archive(ui, extract_dir=out_path)

    if server:
        server_cmd = "python3", "-mhttp.server", "8000", f"--directory={html_path}"
        shell(server_cmd)
        check_output(server_cmd)


def get_du_cmd(directory: Path, image: Optional[str]) -> Tuple[str, ...]:
    if image:
        return "docker", "run", "--rm", "--entrypoint", "du", image
    else:
        return ("du",) + DU_ARGS + (str(directory),)


def shell(cmd: Union[str, Tuple[str, ...]]):
    if isinstance(cmd, str):
        print(f"Running {cmd}")
        return check_output(cmd, shell=True).decode()
    else:
        print(f"Running {' '.join(cmd)}")
        return check_output(cmd).decode()


if __name__ == "__main__":
    run()

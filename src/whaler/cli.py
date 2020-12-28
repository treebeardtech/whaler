import shutil
import subprocess
from pathlib import Path
from subprocess import STDOUT, CalledProcessError
from typing import Optional, Tuple, Union

from rich.console import Console

console = Console()

import click
from rich import print

DEFAULT_OUT = "_whaler"
HTML_DIR = "html"
DU_FILENAME = "du.txt"
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
    try:
        du_out = shell(get_du_cmd(Path(directory), image))

        out_path = Path(out)
        html_path = out_path / HTML_DIR
        html_path.mkdir(exist_ok=True, parents=True)
        (html_path / DU_FILENAME).write_text(du_out)

        ui = Path(__file__).parent / "static" / UI_FILENAME

        shutil.unpack_archive(ui, extract_dir=out_path)

        if server:
            server_cmd = (
                "python3",
                "-m",
                "http.server",
                "8000",
                f"--directory={html_path}",
            )
            print(
                "[bold green]Done. Serving output at http://localhost:8000 (ctrl+c to exit)"
            )
            shell(server_cmd)
    except ShellError as se:
        print(se.args[0])
        exit(2)


def get_du_cmd(directory: Path, image: Optional[str]) -> Tuple[str, ...]:
    if image:
        return "docker", "run", "--rm", "--entrypoint=du", "--pull=never", image
    else:
        return ("du",) + DU_ARGS + (str(directory),)


def shell(cmd: Union[str, Tuple[str, ...]]):
    try:
        with console.status(""):

            if isinstance(cmd, str):
                print(f"Running {cmd}")
                return subprocess.check_output(cmd, shell=True, stderr=STDOUT).decode()
            else:
                print(f"Running {' '.join(cmd)}")
                return subprocess.check_output(cmd, stderr=STDOUT).decode()
    except CalledProcessError as err:
        raise ShellError(
            f"""
[bold red]subprocess failed with status {err.returncode}.
stdout: {(err.stdout or b'-').decode()}
stderr: {(err.stderr or b'-').decode()}
"""
        )


class ShellError(BaseException):
    pass


if __name__ == "__main__":
    run()

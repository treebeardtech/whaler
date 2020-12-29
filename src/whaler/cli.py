import shutil
import subprocess
from pathlib import Path
from subprocess import CalledProcessError
from typing import Optional, Tuple, Union

from rich.console import Console

console = Console()

import click
from rich import print

DEFAULT_OUT = "_whaler"
HTML_DIR = "html"
DU_FILENAME = "du.txt"
DU_ARGS = ("-a", "-k")
UI_FILENAME = "html.tgz"


@click.command()
@click.option("--image", help="docker image", default=None)
@click.option("--port", help="port to serve the outputs on", default=8000)
@click.option("--out", help="output path", default=DEFAULT_OUT)
@click.argument("directory", default=".")
@click.option(
    "--server/--no-server",
    default=True,
    help="Run web server on output to immediately view",
)
def run(directory: str, out: str, image: Optional[str], server: bool, port: int):
    """"""
    try:
        du_out = du(Path(directory), image)

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
                str(port),
                f"--directory={html_path}",
            )
            print(
                f"[bold green]Done. Serving output at http://localhost:{port} (ctrl+c to exit)"
            )
            shell(server_cmd)
    except CalledProcessError as err:
        msg = f"""
[bold red]subprocess failed with status {err.returncode}.
stderr:\n\n{(err.stderr or b'-').decode()}
stdout (truncated):\n\n{(err.stdout or b'-').decode()[:100]}
"""
        print(msg)

        exit(2)


def du(directory: Path, image: Optional[str]) -> str:

    if image:
        cmd = ("docker", "run", "--rm", "--entrypoint=du")
        if str(directory) != ".":
            cmd += (f"--workdir={directory}",)
        cmd += (image, *DU_ARGS)
    else:
        cmd = ("bash", "-c", f"cd {directory} && du {' '.join(DU_ARGS)}")

    try:
        return shell(cmd)
    except CalledProcessError as err:
        if len(err.output) == 0:
            raise err

        print(
            f"Ignoring what seems to be non-fatal error(s):\n{(err.stderr or b'-').decode()}"
        )
        return err.output.decode()


def shell(cmd: Union[str, Tuple[str, ...]]):
    with console.status(""):

        if isinstance(cmd, str):
            print(f"Running {cmd}")
            return subprocess.check_output(
                cmd, shell=True, stderr=subprocess.PIPE
            ).decode()
        else:
            print(f"Running {' '.join(cmd)}")
            return subprocess.check_output(cmd, stderr=subprocess.PIPE).decode()


class ShellError(BaseException):
    pass


if __name__ == "__main__":
    run()

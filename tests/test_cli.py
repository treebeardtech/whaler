from subprocess import CalledProcessError, check_output
from unittest.mock import patch

from click.testing import CliRunner
from pytest import fixture

from whaler import cli

pytest_plugins = "pytester"
from pathlib import Path


@fixture
def testimage():
    print("Pulling image...")

    image = "alpine:20201218"
    check_output(["docker", "pull", image])
    print("Done.")
    return image


def test_when_local_dir_then_success(testdir):
    runner = CliRunner()

    result = runner.invoke(cli.run, "--no-server", catch_exceptions=False)

    html_dir = Path(testdir.tmpdir) / cli.DEFAULT_OUT / cli.HTML_DIR

    assert result.exit_code == 0
    assert (html_dir / cli.DU_FILENAME).exists()
    assert (html_dir / "index.html").exists()


# todo: invalid inputs, port already taken
def test_when_docker_dir_then_success(testdir, testimage):
    runner = CliRunner()
    directory = "usr"
    result = runner.invoke(
        cli.run, f"--image={testimage} --no-server {directory}", catch_exceptions=False
    )

    html_dir = Path(testdir.tmpdir) / cli.DEFAULT_OUT / cli.HTML_DIR

    assert result.exit_code == 0
    assert (html_dir / cli.DU_FILENAME).exists()
    assert (html_dir / "index.html").exists()


def test_when_subprocess_error_then_appropriate_msg(testdir):
    runner = CliRunner()
    exc_msg = "blah".encode()

    with patch("subprocess.check_output") as mock:
        mock.side_effect = CalledProcessError(1, "", exc_msg)
        result = runner.invoke(cli.run, "--no-server", catch_exceptions=True)

    assert result.exit_code == 1
    assert result.exception.output == exc_msg

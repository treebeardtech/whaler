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


def test_when_custom_out_dir_then_success(testdir):
    runner = CliRunner()
    out_path = "blah"
    result = runner.invoke(
        cli.run, f"--out={out_path} --no-server", catch_exceptions=False
    )

    html_dir = Path(testdir.tmpdir) / out_path / cli.HTML_DIR

    assert result.exit_code == 0
    assert (html_dir / cli.DU_FILENAME).exists()
    assert (html_dir / "index.html").exists()


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
    stdout = "hfgh546"
    stderr = "fhgf3"
    cmd = "hjgh 8787"

    with patch("subprocess.check_output") as mock:
        mock.side_effect = CalledProcessError(1, cmd, stdout.encode(), stderr.encode())
        result = runner.invoke(cli.run, "--no-server", catch_exceptions=True)

    assert result.exit_code == 2
    assert stdout in result.output
    assert stderr in result.output


def test_when_invalid_image_then_fails(testdir):
    runner = CliRunner()

    result = runner.invoke(cli.run, "--image jk --no-server")

    assert result.exit_code == 2
    assert not (Path(testdir.tmpdir) / cli.DEFAULT_OUT).exists()


def test_when_image_not_pulled_then_fails(testdir):
    runner = CliRunner()

    result = runner.invoke(cli.run, "--image cheers --no-server")

    assert result.exit_code == 2
    assert not (Path(testdir.tmpdir) / cli.DEFAULT_OUT).exists()


def test_when_invalid_dir_then_fails(testdir):
    runner = CliRunner()
    invalid_dir = "lkj"

    result = runner.invoke(cli.run, f"--no-server {invalid_dir}")

    assert result.exit_code == 2
    assert not (Path(testdir.tmpdir) / cli.DEFAULT_OUT).exists()

from subprocess import check_output

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
    return image


def test_when_local_dir_then_success(testdir):
    runner = CliRunner()
    result = runner.invoke(cli.run, "--no-server", catch_exceptions=False)

    html_dir = Path(testdir.tmpdir) / cli.DEFAULT_OUT / cli.HTML_DIR

    assert result.exit_code == 0
    assert (html_dir / cli.DU_FILENAME).exists()
    assert (html_dir / "index.html").exists()


# todo: docker dir, invalid inputs
def test_when_docker_dir_then_success(testdir, testimage):
    runner = CliRunner()
    result = runner.invoke(
        cli.run, f"--image={testimage} --no-server", catch_exceptions=False
    )

    html_dir = Path(testdir.tmpdir) / cli.DEFAULT_OUT / cli.HTML_DIR

    assert result.exit_code == 0
    assert (html_dir / cli.DU_FILENAME).exists()
    assert (html_dir / "index.html").exists()

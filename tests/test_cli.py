from click.testing import CliRunner

from whaler import cli

pytest_plugins = "pytester"
from pathlib import Path


def test_when_local_dir_then_success(testdir):
    runner = CliRunner()
    result = runner.invoke(cli.run, "--no-server", catch_exceptions=False)

    html_dir = Path(testdir.tmpdir) / cli.DEFAULT_OUT / cli.HTML_DIR

    assert result.exit_code == 0
    assert (html_dir / cli.DU_FILENAME).exists()
    assert (html_dir / "index.html").exists()

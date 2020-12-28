from click.testing import CliRunner

from whaler import cli

pytest_plugins = "pytester"
from pathlib import Path


def test_when_local_dir_then_success(testdir):
    runner = CliRunner()
    result = runner.invoke(cli.run)
    out_dir = Path(testdir.tmpdir) / cli.DEFAULT_OUT

    assert result.exit_code == 0
    assert out_dir.exists()
    assert (out_dir / cli.DU_FILENAME).exists()

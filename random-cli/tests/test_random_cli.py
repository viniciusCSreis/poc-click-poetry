from click.testing import CliRunner

from random_cli import __version__
from random_cli.cmd import cli


def test_version():
    assert __version__ == '0.1.0'


def test_hello():
    runner = CliRunner()
    result = runner.invoke(cli, ['hello'])
    assert result.exit_code == 0
    assert result.output == 'sum: 11\n'

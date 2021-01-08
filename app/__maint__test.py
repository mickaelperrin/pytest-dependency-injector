from click.testing import CliRunner
from app.__main__ import cli


runner = CliRunner()


def test_conf():
    response = runner.invoke(cli, ['key'])
    assert(response == 'value')
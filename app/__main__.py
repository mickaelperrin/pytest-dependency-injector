#!/usr/bin/env python3
import click
import sys
from dependency_injector.wiring import inject, Provide
from app.Container import Container
from app.Config import Config


@click.command()
@click.option('-c', '--configuration-file', help='Configuration file path', default='config.yml')
@click.argument('test_key')
@inject
def cli(test_key, configuration_file, config: Config = Provide[Container.config]) -> None:
    config.from_yaml(configuration_file)
    config.override_config_from_cli(**locals())
    print(config.get(test_key))
    pass


def start():
    container = Container()
    container.init_resources()
    container.wire(modules=[sys.modules[__name__]])
    cli()


if __name__ == '__main__':
    start()

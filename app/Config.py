from dependency_injector.providers import Configuration


class Config(Configuration):

    def override_config_from_cli(self, **kwargs):
        for key, value in kwargs.items():
            if not value:
                continue
            self.set(key, value)
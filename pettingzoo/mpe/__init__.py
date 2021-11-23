from pettingzoo.utils.deprecated_module import DeprecatedModule


def __getattr__(env_name):
    return DeprecatedModule(env_name, __path__, __name__)

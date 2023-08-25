import hashlib


class PostInitCaller(type):
    def __call__(cls, *args, **kwargs):
        obj = type.__call__(cls, *args, **kwargs)
        obj.__post_init__()
        return obj


class Modelo(metaclass=PostInitCaller):
    PARAMETROS_DE_IDENTIDADE = []

    def __init__(self, id=None):
        self.id = id

    def __post_init__(self):
        if getattr(self, "id", None) is None:
            _identidade = []
            for parametro in self.PARAMETROS_DE_IDENTIDADE:
                valor = getattr(self, parametro)
                if isinstance(valor, Modelo):
                    valor = valor.id

                _identidade.append(str(valor))

            self.id = hashlib.md5("|".join(_identidade).encode()).hexdigest()

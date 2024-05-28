# TODO: Implementa el código del ejercicio aquí


class ReglaValidacion:
    def __init__(self,longitud_esperada: int):
        self.longitud = longitud_esperada
    
    def _validar_longitud(self, clave:str):
        if len(clave) >= self.longitud:
            return True
        else:
            return False
    def _contiene_mayuscula(self, clave: str):
        if clave.isupper():
            return True
        else:
            return False
    def _contiene_minuscula(self, clave: str):
        if clave.islower():
            return True
        else:
            return False
    def _contiene_numero(self, clave: str):
        if clave.isdigit():
            return True
        else:
            return False
    def es_valida(self, clave:str):
        if self._validar_longitud(clave) and self._contiene_mayuscula(clave) and self._contiene_minuscula(clave) and self._contiene_numero(clave):
            return True
        else:
            return False


class ReglaValidacionGanimedes:
    def contiene_caracter_especial(self, clave: str):
        special_characters = "!@#$%^&*()-+?_=,<>/"""
        if any(c in special_characters for c in clave):
            return True
        else:
            return False
    
class ReglaValidacionCalisto:
    def contiene_calisto(self, clave: str):
        if clave.find("calisto") > 0:
            return True
        else:
            return False
        
class Validador:
    def __init__(self, regla: ReglaValidacion) -> None:
        self.regla = regla
    def es_valida(self, clave:str):
        validar = self.regla.es_valida(clave)
        return validar
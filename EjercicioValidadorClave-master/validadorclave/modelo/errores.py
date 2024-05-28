class ValidadorError(Exception):
    print("La clave no valida")


class NoCumpleLongitudMinimaError(ValidadorError):
    print("La clave no cumple con la minima longitud")


class NoTieneLetraMayusculaError(ValidadorError):
    print("La clave no contiene letra mayuscula")


class NoTieneLetraMinusculaError(ValidadorError):
    print("La clave no contiene letra minuscula")


class NoTieneNumeroError(ValidadorError):
    print("La clave no contiene algun numero")


class NoTieneCaracterEspecialError(ValidadorError):
    print("La clave no contiene un caracter especial")


class NoTienePalabraSecretaError(ValidadorError):
    print("La clave no contiene la palabra de seguridad")
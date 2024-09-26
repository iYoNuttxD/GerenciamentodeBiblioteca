def cor(texto='', estilo=0, letra=31, fundo=0, fim=False):
    if fim:
        return f'\033[{estilo};{letra};{fundo}m{texto}\033[m'
    else:
        return f'\033[{estilo};{letra};{fundo}m{texto}'

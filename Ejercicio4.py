def ordenar_eventos(eventos , expresion=False):
    eventos.sort(reverse=bool(expresion))
    return eventos
if __name__ == "__main__":
    lista = ["Kermes" , "Concurso de comida" , "Reunion del consejo municipal"]
import pokemon.models

def criar():
    import json
    
    print('tetando criar os registros...')
    with open('pokemons.json', 'r') as f:
        pokemons = json.loads(f.read())
        for numero, valores in pokemons.items():
            novo_pokemon = pokemon.models.Pokemon(
                    numero=numero, nome=valores['nome'],
                    tipos=valores['tipos'],
                    imagem_origem=valores['imagem_origem'])
            print(f'registro {numero} criado com sucesso.')
            novo_pokemon.save()


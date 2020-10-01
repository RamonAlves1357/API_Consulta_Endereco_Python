import requests

def main():
    print("\n==============================")
    print("| Bem vindo ao Consulta CEP! |")
    print("==============================\n")

    CEP = input("=> Informe o CEP para a consulta: ")

    if len(CEP) != 8:
        print("Ops! CEP invalido, por favor tente novamente")
        exit()

    r = requests.get(f'https://viacep.com.br/ws/{CEP}/json')

    address_data = r.json()

    if 'erro' not in address_data:
        print(" ===> CEP encontrado <===")
        print(f" | CEP: {address_data['cep']}")
        print(f" | Logradouro: {address_data['logradouro']}")
        print(f" | Complemento: {address_data['complemento']}")
        print(f" | Bairro: {address_data['bairro']}")
        print(f" | Localidade: {address_data['localidade']}")
        print(f" | UF: {address_data['uf']}")
        print(f" | IBGE: {address_data['ibge']}")
        print(f" | DDD: {address_data['ddd']}")
        print(" =========================")
    else:
        print(f"Ops! Algo errado com o CEP: {CEP}, por favor tente novamente.")

    print("\n**************************************")
    op = input('Deseja realizar uma nova consulta (S/n)?')
    if op.upper() == "S":
        main()
    else:
        print("Obg por usar o script!")
        exit()

if __name__ == '__main__':
    main()
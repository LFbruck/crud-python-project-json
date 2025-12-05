from typing import List,Dict
from storage import  load_data, save_data, get_next_id, find_by_id

def list_itens(data: List[Dict]) -> None:
    if not data:
        print("Nenhum registro foi encontrado no sistema")
        return
    print("\nRegistros Encontrados:")
    for item in data:
        print(f"ID: {item['id']} | Nome: {item.get('name')} | Email: {item.get('email')}")
        print()

def criar_item(data: List[Dict]) -> None:
    name= input("Nome:").strip()
    email = input("Email:").strip()

    new={
        "id": get_next_id(data),
        "name": name,
        "email": email
    }

    data.append(new)
    save_data(data)
    print("Novo registro criado com sucesso! ID:", new["id"])


def ler_item(data: List[Dict]) -> None:
    try:
        id_ = int(input("ID do registro:"). strip())
    except ValueError:
        print("Valor invalido")
        return

    item = find_by_id(data, id_)

    if not item:
        print("registro não encontrado.")
        return

    print(f"\nID: {item['id']} | Nome: {item.get('name')} | Email: {item.get('email')}")

def atualizar_item(data: List[Dict]) -> None:
    try:
        id_ = int(input("ID para poder atualizar:"). strip())
    except ValueError:
        print("ID invalido")
        return

    item = find_by_id(data, id_)
    if not item:
        print("Registro não foi encontrado.")
        return

    print("Deixe em branco para manter o valor atual.")

    name = input(f"Nome [{item.get('name')}]: ").strip()
    email = input(f"Email [{item.get('email')}]: ").strip()

    if name:
        item['name'] = name
    if email:
        item ["email"] = email
    save_data(data)
    print("Registro foi atualizado com sucesso!")

def deletar_item(data: List[Dict]) -> None:
    try:
        id_=int(input("ID que quer excluir:"). strip())
    except ValueError:
        print("ID invalido")
        return

    item = find_by_id(data, id_)

    if not item:
        print("registor nao encotrado")
        return

    confirm = input("Deseja remover o registro? [S/N]").strip().lower()
    if confirm == "s":
        data.remove(item)
        save_data(data)
        print("Registro foi excluido!")

    else:
        print("Cancelado")

def menu():
    data = load_data()

    while True:
        print("== Projeto CRUD Simples (.JSON) ==")
        print("(1) - Listar Registros")
        print("(2) - Criar Registros")
        print("(3) - Ler Registros usando ID")
        print("(4) - Atualizar Registros")
        print("(5) - Exlcuir Registro")
        print("(0) - Sair ")

        choice = input("Sua escolha:").strip()

        if choice == "1":
           list_itens(data)
        elif choice == "2":
            criar_item(data)
        elif choice == "3":
            ler_item(data)
        elif choice == "4":
            atualizar_item(data)
        elif choice == "5":
            deletar_item(data)
        elif choice == "0":
            print("Saindo... Obrigado por utilizar meu sistema.")
            break
        else:
            print("Essa opção é inválida.\n")

if __name__ == "__main__":
    menu



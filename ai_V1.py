def lib(ai):
    if ai == "SPG-AI":
        user_input = input("digite as quantias usando , pra dividir cada uma: ")
        user_limit = input("digite os limites das quantias usando , pra dividir cada uma: ")
        user_input = [user_input]
        user_limit = [user_limit]
        if user_input < user_limit:
            print("Valor Ruim (Menor do que o limite)")
        elif user_input == user_limit:
            print("Valor OK (Igual)")
        elif user_input > user_limit:
            print("Valor Bom (Maior que o limite)")

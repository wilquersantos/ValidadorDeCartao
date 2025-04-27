def validar_cartao(numero_cartao):
    """
    Valida o número do cartão de crédito com base nos prefixos e intervalos fornecidos.
    """
    numero_cartao = str(numero_cartao)

    # Validação para Visa (12 ou 16 dígitos)
    if numero_cartao.startswith("4") and len(numero_cartao) in [12, 16]:
        return "Visa"

    # Validação para MasterCard
    if (51 <= int(numero_cartao[:2]) <= 55) or (2221 <= int(numero_cartao[:4]) <= 2720):
        return "MasterCard"

    # Validação para Elo
    prefixos_elo = ["4011", "4312", "4389"]
    if any(numero_cartao.startswith(prefixo) for prefixo in prefixos_elo):
        return "Elo"

    # Validação para American Express
    if numero_cartao.startswith("34") or numero_cartao.startswith("37"):
        return "American Express"

    # Validação para Discover
    if numero_cartao.startswith("6011") or numero_cartao.startswith("65") or (644 <= int(numero_cartao[:3]) <= 649):
        return "Discover"

    # Validação para Hipercard
    if numero_cartao.startswith("6062"):
        return "Hipercard"

    # Validação para Aura
    if numero_cartao.startswith("50"):
        return "Aura"

    # Validação para Voyager
    if numero_cartao.startswith("8699"):
        return "Voyager"

    return "Bandeira desconhecida"


# Testes
if __name__ == "__main__":
    cartoes_teste = [
        "411111111111",       # Visa (12 dígitos)
        "4111111111111111",   # Visa (16 dígitos)
        "5500000000000004",   # MasterCard
        "4011222233334444",   # Elo
        "371449635398431",    # American Express
        "6011111111111117",   # Discover
        "6062828888888888",   # Hipercard
        "5012345678901234",   # Aura
        "869912345678901",    # Voyager
        "1234567890123456"    # Desconhecido
    ]

    for cartao in cartoes_teste:
        print(f"Número: {cartao} - Bandeira: {validar_cartao(cartao)}")
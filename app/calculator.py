from app.games import get_game


def convert_sensitivity(
    from_game_id: str,
    to_game_id: str,
    sensitivity: float,
    from_dpi: int = None,
    to_dpi: int = None,
    from_weight: float = None,
    to_weight: float = None,
) -> dict:
    """
    Converte a sensibilidade entre jogos, DPIs e pesos de mouse.

    Retorna um dicionário com o resultado e os detalhes do cálculo.
    """

    from_game = get_game(from_game_id)
    to_game = get_game(to_game_id)

    # Passo 1: converte entre jogos usando o yaw
    # Fórmula: sens_nova = sens_atual * (yaw_origem / yaw_destino)
    converted = sensitivity * (from_game["yaw"] / to_game["yaw"])

    # Passo 2: ajusta para mudança de DPI (se informado)
    # Fórmula: sens_nova = sens_atual * (dpi_antigo / dpi_novo)
    if from_dpi and to_dpi and from_dpi != to_dpi:
        converted = converted * (from_dpi / to_dpi)

    # Passo 3: ajusta para mudança de peso do mouse (se informado)
    # Mouse mais pesado = mais resistência = precisa de mais sens
    # Mouse mais leve = menos resistência = precisa de menos sens
    if from_weight and to_weight and from_weight != to_weight:
        converted = converted * (from_weight / to_weight)

    return {
        "from_game": from_game["name"],
        "to_game": to_game["name"],
        "original_sensitivity": sensitivity,
        "converted_sensitivity": round(converted, 4),
        "from_dpi": from_dpi,
        "to_dpi": to_dpi,
        "from_weight": from_weight,
        "to_weight": to_weight,
    }
# Cada jogo tem um "yaw" — quantos graus a tela gira por unidade de sensibilidade.
# Essa constante é o que permite converter entre jogos diferentes.

GAMES = {
    "cs2": {
        "name": "Counter-Strike 2",
        "yaw": 0.022,
    },
    "valorant": {
        "name": "Valorant",
        "yaw": 0.07,
    },
    "apex": {
        "name": "Apex Legends",
        "yaw": 0.022,
    },
    "overwatch2": {
        "name": "Overwatch 2",
        "yaw": 0.0066,
    },
    "r6siege": {
        "name": "Rainbow Six Siege",
        "yaw": 0.00573,
    },
    "fortnite": {
        "name": "Fortnite",
        "yaw": 0.5590,
    },
}


def get_game(game_id: str) -> dict:
    """Retorna os dados de um jogo pelo ID. Levanta erro se não encontrar."""
    game = GAMES.get(game_id)
    if not game:
        raise ValueError(f"Jogo '{game_id}' não encontrado.")
    return game


def list_games() -> list:
    """Retorna lista de jogos disponíveis com id e nome."""
    return [{"id": key, "name": value["name"]} for key, value in GAMES.items()]
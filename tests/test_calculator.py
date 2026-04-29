import pytest
from app.calculator import convert_sensitivity
from app.games import get_game, list_games


# ─── Testes de conversão entre jogos ────────────────────────────────────────

def test_cs2_para_valorant():
    """Conversão básica: CS2 1.8 deve virar ~0.5657 no Valorant."""
    result = convert_sensitivity("cs2", "valorant", 1.8)
    assert result["converted_sensitivity"] == 0.5657


def test_mesmo_jogo_mesma_sens():
    """Convertendo do mesmo jogo para ele mesmo, a sens não muda."""
    result = convert_sensitivity("cs2", "cs2", 2.0)
    assert result["converted_sensitivity"] == 2.0


def test_cs2_para_apex():
    """CS2 e Apex têm o mesmo yaw, então a sens deve ser igual."""
    result = convert_sensitivity("cs2", "apex", 1.5)
    assert result["converted_sensitivity"] == 1.5


# ─── Testes de conversão de DPI ─────────────────────────────────────────────

def test_dpi_dobrado_reduz_sens_pela_metade():
    """Dobrar o DPI deve resultar em metade da sensibilidade."""
    result = convert_sensitivity("cs2", "cs2", 2.0, from_dpi=800, to_dpi=1600)
    assert result["converted_sensitivity"] == 1.0


def test_dpi_igual_nao_altera_sens():
    """DPI igual não deve alterar a sensibilidade."""
    result = convert_sensitivity("cs2", "valorant", 1.8, from_dpi=800, to_dpi=800)
    assert result["converted_sensitivity"] == 0.5657


# ─── Testes de peso do mouse ─────────────────────────────────────────────────

def test_mouse_mais_leve_reduz_sens():
    """Trocar para mouse mais leve deve reduzir a sensibilidade."""
    result = convert_sensitivity("cs2", "cs2", 2.0, from_weight=100.0, to_weight=50.0)
    assert result["converted_sensitivity"] == 1.0


def test_peso_igual_nao_altera_sens():
    """Peso igual não deve alterar a sensibilidade."""
    result = convert_sensitivity("cs2", "cs2", 2.0, from_weight=80.0, to_weight=80.0)
    assert result["converted_sensitivity"] == 2.0


# ─── Testes de erro ──────────────────────────────────────────────────────────

def test_jogo_invalido_levanta_erro():
    """Jogo inexistente deve levantar ValueError."""
    with pytest.raises(ValueError):
        convert_sensitivity("jogo_falso", "valorant", 1.8)


# ─── Testes de games.py ──────────────────────────────────────────────────────

def test_get_game_retorna_dados_corretos():
    """get_game deve retornar o nome e yaw corretos do CS2."""
    game = get_game("cs2")
    assert game["name"] == "Counter-Strike 2"
    assert game["yaw"] == 0.022


def test_list_games_retorna_todos():
    """list_games deve retornar pelo menos 6 jogos."""
    games = list_games()
    assert len(games) >= 6


def test_list_games_tem_id_e_nome():
    """Cada item de list_games deve ter 'id' e 'name'."""
    games = list_games()
    for game in games:
        assert "id" in game
        assert "name" in game
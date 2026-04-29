from app.calculator import convert_sensitivity

# Teste 1: CS2 sens 1.8 -> Valorant, mesmo DPI
resultado = convert_sensitivity(
    from_game_id="cs2",
    to_game_id="valorant",
    sensitivity=1.8,
)
print("CS2 -> Valorant:", resultado["converted_sensitivity"])
# Esperado: ~0.5657

# Teste 2: mesma conversão mas mudando DPI de 800 para 1600
resultado2 = convert_sensitivity(
    from_game_id="cs2",
    to_game_id="valorant",
    sensitivity=1.8,
    from_dpi=800,
    to_dpi=1600,
)
print("CS2 -> Valorant + DPI 800->1600:", resultado2["converted_sensitivity"])
# Esperado: ~0.2829 (metade, porque dobrou o DPI)

# Teste 3: com mudança de peso de mouse
resultado3 = convert_sensitivity(
    from_game_id="cs2",
    to_game_id="valorant",
    sensitivity=1.8,
    from_weight=95.0,
    to_weight=68.0,
)
print("CS2 -> Valorant + peso 95g->68g:", resultado3["converted_sensitivity"])
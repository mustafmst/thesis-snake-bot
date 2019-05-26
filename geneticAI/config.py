from snake import DEFAULT_CONFIG, AI_MODE

ai_config = dict(DEFAULT_CONFIG)
ai_config["game_mode"] = AI_MODE
ai_config['move_sleep'] = 24

RUN_CONFIG = dict(
    base_game_config=ai_config,
    network_schema=[
        ('dense', 256),
        ('dense', 256)
    ],
    population_size=12,
    generations=12,
    generation_mutation_rate=10
)

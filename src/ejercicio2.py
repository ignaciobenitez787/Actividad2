titles = [
"Speedrun de Super Mario en tiempo récord",
"Charla sobre desarrollo de videojuegos",
"Jugando al nuevo FPS del momento con amigos",
"Música en vivo: improvisaciones al piano"
]
print("El titulo mas largo es:", ' '.join(max((title.split() for title in titles), key=len)))
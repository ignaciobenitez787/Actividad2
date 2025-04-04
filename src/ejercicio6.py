descriptions = [
"Streaming de música en vivo con covers y composiciones",
"Charla interactiva con la audiencia sobre series y películas",
"Jugamos a juegos retro y charlamos sobre su historia",
"Exploramos la mejor música de los 80s y 90s",
"Programa de entretenimiento con noticias y curiosidades del mundo gamer",
"Sesión de charla con invitados especiales del mundo del streaming",
"Música en directo con improvisaciones y peticiones del chat",
"Un espacio para charlar relajada sobre tecnología y cultura digital",
"Exploramos el impacto de la música en los videojuegos clásicos"
]
charla = 0
musica = 0
entretenimiento = 0
for description in descriptions:
    words = description.lower().split()
    charla = charla + words.count("charla")
    musica = musica + words.count("música")
    entretenimiento = entretenimiento + words.count("entretenimiento")
print("Menciones de 'música':", musica)
print("Menciones de 'charla':", charla)
print("Menciones de 'entretenimiento':", entretenimiento)
def calcular_puntos(player_stats, kill_value, assist_value, death_value):
    '''Recibe un diccionario con las estadisticas de un jugador en una determinada ronda y los valores de kill, asistencia y muerte y devuelve su puntaje. '''
    return player_stats['kills'] * kill_value + player_stats['assists'] * assist_value + player_stats['deaths'] * death_value
def calcular_mvp(points):
    '''Recibe un diccionario con clave = nombre de jugador y valor = puntos del jugador y devuelve el nombre del jugador con mayor puntaje'''
    return max(points, key=points.get)
def check_username(username):
    """Recibe un nombre de usuario y verifica si es valido"""
    return (len(username) >= 5) and (any(char.isdigit() for char in username)) and (any(char.isupper() for char in username)) and (all(char.isalnum() for char in username))
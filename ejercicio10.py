from funciones import calcular_puntos
from funciones import calcular_mvp
rounds = [
{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
}
]
if rounds:
    kill_value = 3
    assist_value = 1
    death_value = -1
    round_number = 1
    column_size = 15
    stats = { player: {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'points': 0} for player in rounds[0]}
    temp_points = {player: 0 for player in stats}
    for round in rounds:
        for player, player_stats in round.items():
            temp_points[player]= calcular_puntos(player_stats,kill_value,assist_value,death_value)
            stats[player]['points'] += temp_points[player]
            for stat, stat_value in player_stats.items():
                if type(stat_value)==int:
                    stats[player][stat]=stats[player][stat]+stat_value
                elif stat_value:
                    stats[player][stat]=stats[player][stat]+1
        mvp = calcular_mvp(temp_points)
        stats[mvp]['mvps'] += 1
        print(f"Ranking ronda {round_number}:")
        round_number += 1
        print("Jugador".center(column_size),"Kills".center(column_size),"Asistencias".center(column_size),"Muertes".center(column_size),"MVPs".center(column_size-6),"Puntos".center(column_size))
        print("-"*column_size*6)
        sorted_stats = dict(sorted(stats.items(), key = lambda x: x[1].get('points'), reverse=True))
        for player, player_stats in sorted_stats.items():
            print(f'{player.center(column_size)}{str(player_stats["kills"]).center(column_size)}{str(player_stats["assists"]).center(column_size)}{str(player_stats["deaths"]).center(column_size)}{str(player_stats["mvps"]).center(column_size)}{str(player_stats["points"]).center(column_size)}')
            

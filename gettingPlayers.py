import csv
from nba_api.stats.static import players

all_players = players.get_active_players()

output_file = "nba_players.csv"

with open(output_file, "w", newline='', encoding='utf-8') as csvfile:
    names = ['id', 'full_name']
    writer = csv.DictWriter(csvfile, fieldnames=names)
    writer.writeheader()
    for player in all_players:
        player_data = {
            'id': player['id'],
            'full_name': player['full_name']
        }
        writer.writerow(player_data)

print(f"Wrote {len(all_players)} players to {output_file}")

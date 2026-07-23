import requests
import json

print("Скачиваем список героев с OpenDota...")
heroes_res = requests.get("https://api.opendota.com/api/heroes").json()

heroes = {}
for h in heroes_res:
    heroes[h['id']] = {
        "name": h['localized_name'],
        "icon": f"https://cdn.cloudflare.steamstatic.com{h['icon']}" if 'icon' in h else ""
    }

print(f"Загружено героев: {len(heroes)}")
print("Скачиваем данные по матчапам (занимает ~10 секунд)...")

matchups = {}
for hero_id in heroes:
    url = f"https://api.opendota.com/api/heroes/{hero_id}/matchups"
    res = requests.get(url)
    if res.status_code == 200:
        matchups[hero_id] = res.json()

# Сохраняем локально
with open("heroes.json", "w", encoding="utf-8") as f:
    json.dump(heroes, f, ensure_ascii=False, indent=4)

with open("matchups.json", "w", encoding="utf-8") as f:
    json.dump(matchups, f, ensure_ascii=False, indent=4)

print("Готово! База героев и контрпиков сохранена.")
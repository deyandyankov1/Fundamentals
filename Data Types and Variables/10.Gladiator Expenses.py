lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

sum_for_repair = 0
broken_shield_count = 0

for lost_fight in range(1, lost_fights_count +1):
    if lost_fight % 2 == 0:
        sum_for_repair += helmet_price
    if lost_fight % 3 == 0:
        sum_for_repair += sword_price
    if lost_fight % 2 == 0 and lost_fight % 3 == 0:
        sum_for_repair += shield_price
        broken_shield_count += 1
        if broken_shield_count % 2 == 0 and not broken_shield_count == 0:
            sum_for_repair += armor_price

print(f"Gladiator expenses: {sum_for_repair:.2f} aureus")
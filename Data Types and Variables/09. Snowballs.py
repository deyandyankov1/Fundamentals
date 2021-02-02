n_snowballs = int(input())

max_snowball_value = -9999999999999

max_snowball_snow= -9999999999999
max_snowball_time= -9999999999999
max_snowball_quality= -9999999999999

for _ in range(n_snowballs):
    snowballs_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowballs_snow / snowball_time) ** snowball_quality
    if max_snowball_value<snowball_value:
        max_snowball_value = snowball_value
        max_snowball_time = snowball_time
        max_snowball_snow = snowballs_snow
        max_snowball_quality = snowball_quality

print (f"{max_snowball_snow} : {max_snowball_time} = {max_snowball_value:.0f} ({max_snowball_quality})")
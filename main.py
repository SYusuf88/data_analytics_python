# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line


gullit = 'Ruud Gullit'
van_basten = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = str(gullit) + ' ' + str(goal_0) + ', ' + \
    str(van_basten) + ' ' + str(goal_1)
report = f'{gullit} scored in the {goal_0}nd minute\n{van_basten} scored in the {goal_1}th minute'

player = 'Ruud Gullit'
first_name = player[0:player.find(' ')]
last_name_len = len(player[player.find('G'):])
name_short = f'{player[0]}. {player[player.find("G"):]}'
chant = f'{first_name}! ' * len(first_name)
chant = chant[:-1]
good_chant = chant[-1] != " "

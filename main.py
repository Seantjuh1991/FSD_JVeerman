# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#Part 1

#1
player1 = 'Ruud Gullit'
player2 = 'Marco van Basten'

#2
goal_0 = 32
goal_1 = 54

#3
scorers = f"{player1} {goal_0}, {player2} {goal_1}"

#4
report = f"{player1} scored in the {goal_0}nd minute\n{player2} scored in the {goal_1}th minute"


#Part2

#1
player = "Ronald Koeman"

#2
first_name = player[:(player.find(" "))]

#3
last_name_len = len(player[(player.find(" ")):])-1

#4
name_short = player[0] + ". " + player[(player.find("K")):]

#5
chant = (first_name + "! ") * (len(first_name)-1) + first_name + "!"

#6
good_chant = (chant[len(chant)-1] != " ")

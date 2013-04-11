"""
Name: title.py
Purpose: Text for the project title.
Author: Nathaniel Metrock & Sean Jackson
License: GNU GPL <http://www.gnu.org/licenses/gpl.html>
"""

#####################################################################tiles_and_units#############################################################################


# unit variables

# attack = A
# defence = D 
# group = G
# cost = C
# endurance = E 
# morale = M
# health = H 
# journey = J
# level = L


# tile variables

# terrain = T
# fortify = F
# siege = S 
# rations = R
# offence = O
# weather = W


# tile to unit rules

# (terrain) x (journey) = (alt_journey) 
# (fortify) x (defence) = (alt_defence)
# (siege) x (cost) = (alt_cost)
# (rations) - (endurance) = (alt_endurance)
# (alt_defence) + (alt_endurance) = (ail_alt_defence)
# (offence) x (attack) = (alt_attack)
# (weather) x (morale) = (alt_morale)


# unit to unit rules

# (alt_morale) = (alt_morale) when unit is placed with no unit above, below, to the left, and to the right 
# (alt_morale) x (group) = (ail_alt_morale) when unit is placed with a unit above or below or to the left or to the right
# level changes all unit variables except level


##########################################################################battle#################################################################################


# army variables

#player_1 = p1
#player_2 = p2
#player_1_1rst_forward_facing_row_or_column = b1p1
#player_1_2nd_forward_facing_row_or_column = b2p1
#player_1_3rd_forward_facing_row_or_column = b3p1
#player_1_4th_forward_facing_row_or_column = b4p1
#player_1_5th_forward_facing_row_or_column = b5p1
#player_2_1rst_forward_facing_row_or_column = b1p2
#player_2_2nd_forward_facing_row_or_column = b2p2
#player_2_3rd_forward_facing_row_or_column = b3p2
#player_2_4th_forward_facing_row_or_column = b4p2
#player_2_5th_forward_facing_row_or_column = b5p2


# army battle rules

# while
# (((b1p1 health) + (b1p1 ail_alt_defence)) - ((b1p2 alt_attack) + (b1p2 (alt_morale and/or ail_alt_morale))) + (b2p1 health) = (b2p1 alt_health)
# (((b2p1 alt_health) + (b2p1 ail_alt_defence)) - ((b2p2 alt_attack) + (b2p2 (alt_morale and/or ail_alt_morale))) + (b3p1 health) = (b3p1 alt_health)
# (((b3p1 alt_health) + (b3p1 ail_alt_defence)) - ((b3p2 alt_attack) + (b3p2 (alt_morale and/or ail_alt_morale))) + (b4p1 health) = (b4p1 alt_health)
# (((b4p1 alt_health) + (b4p1 ail_alt_defence)) - ((b4p2 alt_attack) + (b4p2 (alt_morale and/or ail_alt_morale))) + (b5p1 health) = (b5p1 alt_health)
# (((b5p1 alt_health) + (b5p1 ail_alt_defence)) - ((b5p2 alt_attack) + (b5p2 (alt_morale and/or ail_alt_morale))) = (p1 alt_health)
# (((b1p2 health) + (b1p2 ail_alt_defence)) - ((b1p1 alt_attack) + (b1p1 (alt_morale and/or ail_alt_morale))) + (b2p2 health) = (b2p2 alt_health)
# (((b2p2 alt_health) + (b2p2 ail_alt_defence)) - ((b2p1 alt_attack) + (b2p1 (alt_morale and/or ail_alt_morale))) + (b3p2 health) = (b3p2 alt_health)
# (((b3p2 alt_health) + (b3p2 ail_alt_defence)) - ((b3p1 alt_attack) + (b3p1 (alt_morale and/or ail_alt_morale))) + (b4p2 health) = (b4p2 alt_health)
# (((b4p2 alt_health) + (b4p2 ail_alt_defence)) - ((b4p1 alt_attack) + (b4p1 (alt_morale and/or ail_alt_morale))) + (b5p2 health) = (b5p2 alt_health)
# (((b5p2 alt_health) + (b5p2 ail_alt_defence)) - ((b5p1 alt_attack) + (b5p1 (alt_morale and/or ail_alt_morale))) = (p2 alt_health)
# if (p1 alt_health) > (p2 alt_health): then p1 wins
# else: p2 wins


#########################################################################movement#################################################################################


# journey rules for single unit type parties
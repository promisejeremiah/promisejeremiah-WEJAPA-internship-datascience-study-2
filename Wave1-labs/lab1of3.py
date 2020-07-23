reservoir_volume = 4.445e8
rainfall = 5e6


# decrease the rainfall variable by 10% to account for runoff
rainfall = rainfall*(90/100)


# add the rainfall variable to the reservoir_volume variable
reservoir_volume = reservoir_volume+rainfall


# increase reservoir_volume by 5% to account for stormwater that flows into the reservoir in the days following the storm
reservoir_volume = reservoir_volume + reservoir_volume*(5/100)


# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume = reservoir_volume - reservoir_volume*(5/100)


# subtract 2.5e5 cubic metres from reservoir_volume to account for water that's piped to arid regions.
reservoir_volume = reservoir_volume-2.5e5


# print the new value of the reservoir_volume variable
print(reservoir_volume)


#new value of the reservoir_volume variable: 447627500.0
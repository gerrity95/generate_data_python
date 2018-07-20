import pygal

from Include.die import Die

die_1 = Die()
die_2 = Die(10)

results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()

    results.append(result)


frequencies = []
max_result = die_1.num_sides + die_2.num_sides


for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)


hist = pygal.Bar()

hist.title = 'Results of rolling the dice'

hist.x_labels = [i for i in range(1, max_result+1)]

hist.y_labels = 'Frequency of results'

hist.add('D6', frequencies)

hist.render_to_file('die_visual.svg')
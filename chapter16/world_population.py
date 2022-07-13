import json
from pygal_maps_world.maps import World
from pygal.style import RotateStyle

from country_codes import get_country_code

# Load the data into a list
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

#Build a dictionary of population data for 2010
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        #Check if the code is a valid 2-letter code or None
        #Ignore invalid codes
        if code:
            cc_populations[code] = population

#Group the countries into 3 population levels
cc_pops1, cc_pops2, cc_pops3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000: # < 10M
        cc_pops1[cc] = pop
    elif pop < 1000000000: # < 1B
        cc_pops2[cc] = pop
    else:
        cc_pops3[cc] = pop

# List the number of countries in each population level
print(len(cc_pops1), len(cc_pops2), len(cc_pops3))

#Build the world map and populate the countries with the 2010 pop data

wm_style = RotateStyle('#336699')
wm = World(style=wm_style)

wm.title = 'World Population in 2010, by Country'
wm.add('0-10M', cc_pops1)
wm.add('10M-1B', cc_pops2)
wm.add('>1B', cc_pops3)

wm.render_to_file('world_population.svg')
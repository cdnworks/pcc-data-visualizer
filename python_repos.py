import pygal
import requests
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#Make an API call to github and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print("Status Code:", r.status_code)

#Store API response in a variable
response_dict = r.json()
print("Total repos:", response_dict['total_count'])

#Explore info about the repos
repo_dicts = response_dict['items']

#Collect repo info
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    
    #Get project description if possible
    description = repo_dict['description']
    if not description:
        description = "No description provided"

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

#Create Pygal chart visualizer
chart_style = LS('#333366', base_style=LCS)
chart_style.title_font_size = 24
chart_style.label_font_size = 14
chart_style.major_label_font_size = 18

chart_config = pygal.Config()
chart_config.x_label_rotation = 45
chart_config.show_legend = False
chart_config.truncate_label = 15
chart_config.show_y_guides = False
chart_config.width = 1000

chart = pygal.Bar(chart_config, style=chart_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
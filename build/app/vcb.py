#!/usr/bin/env python

import os
import json
from jinja2 import Environment, PackageLoader, StrictUndefined, select_autoescape

class Roaster:
    def __init__(self, id_, name, map_x, map_y, state, address, url, roasts):
        self.id         = id_
        self.name       = name
        self.map_x      = map_x
        self.map_y      = map_y
        self.state      = state
        self.address    = address
        self.url        = url

        self.roasts     = roasts

class Roast:
    def __init__(self, name, level, ordered_at, roasted_at, tasting_notes, recipe):
        self.name           = name
        self.level          = level
        self.ordered_at     = ordered_at
        self.roasted_at     = roasted_at
        self.tasting_notes  = tasting_notes
        self.recipe         = recipe

class Recipe:
    def __init__(self, grams_in, grams_out, seconds, temperature):
        self.grams_in       = grams_in
        self.grams_out      = grams_out
        self.seconds        = seconds
        self.temperature    = temperature

def recipe_from_dict(d):
    if d:
        return Recipe(
                        d['grams_in'],
                        d['grams_out'],
                        d['seconds'],
                        d['temperature']
        )


def roast_from_dict(d):
    return Roast(
                    d['name'],
                    d['level'],
                    d['ordered_at'],
                    d['roasted_at'],
                    d.get('tasting_notes'),
                    recipe_from_dict(d.get('recipe'))
    )

def load_roasters(path):
    roasters = []

    for entry in os.listdir(path):
        with open(os.path.join(path, entry), 'rb') as f:
            d = json.load(f)

        roasters.append(Roaster(
                                d['id'],
                                d['name'],
                                d['map_x'],
                                d['map_y'],
                                d['state'],
                                d['address'],
                                d['url'],
                                map(roast_from_dict, d['roasts'])
        ))


    return sorted(roasters, key=lambda r: r.state)

if __name__ == "__main__":
    roasters = load_roasters('data')

    env = Environment(        
        loader=PackageLoader('vcb', 'templates'),
        autoescape=select_autoescape(['html',]),
        undefined=StrictUndefined,
    )

    template = env.get_template('index.html.j2')

    with open('html/index.html', 'w') as f:
        f.write(template.render(roasters=roasters, 
                                title="2020 Biden Victory Coffee Project", 
                                subtitle="Until Morale Improves, The Caffeination Will Continue"))

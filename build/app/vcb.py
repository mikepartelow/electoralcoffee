#!/usr/bin/env python

import os
import json
from jinja2 import Environment, PackageLoader, StrictUndefined, select_autoescape

class Roaster:
    def __init__(self, id_, name, map_x, map_y, state, address, url):
        self.id         = id_
        self.name       = name
        self.map_x      = map_x
        self.map_y      = map_y
        self.state      = state
        self.address    = address
        self.url        = url

        self.roasts     = []

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
            d['url']
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
        f.write(template.render(roasters=roasters))

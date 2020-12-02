#!/usr/bin/env python

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
    return [ 
        Roaster('spam', 'Spam Coffee',          map_x=693, map_y=242, state='CA', address="123 Sesame St.\nFremont, CA 12345", url="https://foo.com"),
        Roaster('hork', 'Hork Coffee Roasters', map_x=215, map_y=362, state='MN', address="1600 Pennsylvania Ave\n MN 98765",   url="https://bar.com"),
            ]

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

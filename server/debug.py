#!/usr/bin/env python3

from app import app
from models import *



if __name__ == '__main__':
    
    with app.app_context():
        import ipdb
        game = Game.query.first()
        print(game.to_dict())
        ipdb.set_trace()

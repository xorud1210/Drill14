from pico2d import *
import game_world
import game_framework
import random

class Ball:
    image = None

    def __init__(self, x = None, y = None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1700)
        self.y = y if y else random.randint(100, 1000)

    def draw(self):
        sx, sy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        self.image.draw(sx, sy)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def set_background(self, bg):
        # fill here
        self.bg = bg
        pass

    def get_bb(self):
        sx, sy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        return sx - 10, sy - 10, sx + 10, sy + 10

    def handle_collision(self, group, other):
        match group:
            case 'boy:ball':
                other.ball_count += 1
                game_world.remove_object(self)
                pass
            case 'zombie:ball':
                other.ball = self
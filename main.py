import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

colors = [arcade.color.YELLOW, arcade.color.ROYAL_PURPLE, arcade.color.BLUEBERRY]


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercise #1")
        pass

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

        pass


class Ball:
    def __init__(self):
        self.x = None
        self.y = None
        self.change_x = None
        self.change_y = None
        self.rayon = random.randint(10, 30)
        self.color = random.choice([arcade.color.YELLOW, arcade.color.ROYAL_PURPLE, arcade.color.BLUEBERRY])
    def update(self):
        pass
    def draw(self):
        pass

def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()



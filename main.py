import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Cree une classe ball pour que toutes les boules aient les memes attributes
class Ball:
    # Definir les attributes d'une boule
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.change_x = random.randint(-2, 3)
        self.change_y = random.randint(-2, 3)
        self.rayon = random.randint(10, 30)
        self.color = random.choice([arcade.color.YELLOW, arcade.color.ROYAL_PURPLE, arcade.color.BLUEBERRY,
                                    arcade.color.ORANGE_PEEL])

    # Definir le mouvement qu'une balle fart a chaque frame
    def update(self):
        self.x += self.change_x
        self.y += self.change_y
        if self.x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1
        if self.y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1
        if self.x < self.rayon:
            self.change_x *= -1
        if self.y < self.rayon:
            self.change_y *= -1

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)


# Cree la classe rectangle pour que tout les rectagles ai les meme attributes
class Rectangle:
    # Definir les attributes d'un rectangle
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.change_x = random.randint(-2, 3)
        self.change_y = random.randint(-2, 3)
        self.width = random.randint(10, 30)
        self.height = random.randint(10, 30)
        self.color = random.choice([arcade.color.YELLOW, arcade.color.ROYAL_PURPLE, arcade.color.BLUEBERRY,
                                    arcade.color.ORANGE_PEEL])

    # Definir l'update du rectangle
    def update(self):
        self.x += self.change_x
        self.y += self.change_y
        if self.x > SCREEN_WIDTH - self.width / 2:
            self.change_x *= -1
        if self.y > SCREEN_HEIGHT - self.height / 2:
            self.change_y *= -1
        if self.x < self.width / 2:
            self.change_x *= -1
        if self.y < self.height / 2:
            self.change_y *= -1

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercise #1")
        # Definir le nom des classes et leur donner une liste
        self.ball = Ball(0, 0)
        self.ball_list = []
        self.rect = Rectangle(0, 0)
        self.rect_list = []

    def on_update(self, delta_time):
        # Pour chaque item dans une liste invoque la methode update de cet item
        for self.ball in self.ball_list:
            self.ball.update()
        for self.rect in self.rect_list:
            self.rect.update()

    def on_draw(self):
        arcade.start_render()
        # Pour chaque item dans une liste invoque la methode draw de cet item
        for self.ball in self.ball_list:
            self.ball.draw()
        for self.rect in self.rect_list:
            self.rect.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            # Changer les x,y initial de la balle pour ceux du curseur + ajouter une balle a la liste de balles
            ball = Ball(x, y)
            self.ball_list.append(ball)

        if button == arcade.MOUSE_BUTTON_RIGHT:
            # Meme chose que les balles
            rect = Rectangle(x, y)
            self.rect_list.append(rect)


MyGame()
arcade.run()

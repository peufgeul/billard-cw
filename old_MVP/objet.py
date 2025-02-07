import numpy as np


class Ball:
    def __init__(self, number, initial_position, radius=0.00286, mass=0.162):
        assert type(initial_position) is np.ndarray, "la position doit être un vecteur numpy"
        assert initial_position.shape == (2,), "la position doit être un vecteur de dimension (2,)"
        assert mass > 0, "la masse doit être un nombre positive"
        assert radius > 0, "le rayon doit être un nombre positive"
        self.number = number
        self.radius = radius  # en m
        self.mass = mass  # en kg
        self.position = initial_position
        self.speed = np.array([0, 0])

    def set_size(self, new_radius, new_mass):
        assert new_mass > 0, "la masse doit être un nombre positive"
        assert new_radius > 0, "le rayon doit être un nombre positive"
        self.radius = new_radius
        self.mass = new_mass

    def update_position(self, vecteur_position):
        assert type(vecteur_position) is np.ndarray, "la position doit être un vecteur numpy"
        self.position = vecteur_position

    def update_speed(self, vector_vitesse):
        assert type(vector_vitesse) is np.ndarray, "la vitesse doit être un vecteur numpy"
        self.speed = vector_vitesse

    def __str__(self):
        return "La boule numéro " + str(self.number) + " se trouve à la position " + str(
            self.position) + " et a un vecteur vitesse de " + str(self.speed) + "."


class Board:
    def __init__(self, length=2.54, width=1.27):
        assert length > 0, "la longueur doit être un nombre positive"
        assert width > 0, "la largeur doit être un nombre positive"
        self.length = length
        self.width = width
        self.corners = self.get_corners()  # liste de 4 couples qui correspondent aux coordonnées des coins
        self.middle = self.get_middle()

    def get_corners(self):
        corner1 = np.array([0, 0])
        corner2 = np.array([0, self.length])
        corner3 = np.array([self.width, self.length])
        corner4 = np.array([self.width, 0])
        return [corner1, corner2, corner3, corner4]

    def get_middle(self):
        return np.array([self.width / 2, self.length / 2])

    def set_size(self, new_length, new_width):
        assert new_length > 0, "la longueur doit être un nombre positive"
        assert new_width > 0, "la largeur doit être un nombre positive"
        self.length = new_length
        self.width = new_width
        self.middle = self.get_middle()
        self.corners = self.get_corners()

    def __str__(self):
        return "La table a une largeur " + str(self.width) + " et de longueur " + str(
            self.length) + " a ses coins aux position " + str(
            self.corners) + " et son milieu se trouve aux coordonnées" + str(self.middle) + "."


class Pool:
    def __init__(self, number_of_balls, length=2.54, width=1.27):
        self.board = Board(length=length, width=width)
        self.balls = {}
        for i in range(number_of_balls):
            self.balls[i] = Ball(i, self.board.middle)
        self.number_of_balls = number_of_balls

    def __str__(self):
        chaine = ""
        for i in range(self.number_of_balls):
            chaine += str(self.balls[i]) + " - "
        return chaine


class Cue:
    def __init__(self, mass):
        self.mass = mass

    def frappe(self, energie, angle, ball):
        """Energie en J, angle en rad par rapport à l'axe x"""
        v_cue = np.sqrt(2 * energie / self.mass)
        v_ball = self.mass / ball.mass * v_cue
        ball.update_speed(np.array([np.cos(angle) * v_ball, np.sin(angle) * v_ball]))


# billard = Pool(5)
# print(billard)
# C = Cue(0.5)
# print(billard.balls["0"])
# C.frappe(1, 0, billard.balls["0"])
# print(billard.balls["0"])

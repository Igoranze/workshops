class Person:
    def __init__(self, name, sex, eye_color, hair_color, nose_size, mouth_size, rosy_cheeks=False, bald=False, hat=False, glasses=False, moustache=False, beard=False):
        self.name = name
        self.sex = sex
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.nose_size = nose_size
        self.mouth_size = mouth_size
        self.rosy_cheeks = rosy_cheeks
        self.bald = bald
        self.hat = hat
        self.glasses = glasses
        self.moustache = moustache
        self.beard = beard

    def is_a(self, sex):
        return self.sex == sex
    
    def has_hair_color(self, color):
        return self.hair_color == color

    def has_eye_color(self, color):
        return self.hair_color == color
    
    def has_nose(self, size):
        return self.nose_size == size

    def has_mouth(self, size):
        return self.nose_size == size

    def has_rosy_cheeks(self):
        return self.rosy_cheeks

    def is_bald(self):
        return self.bald

    def has_glasses(self):
        return self.glasses

    def has_hat(self):
        return self.hat

    def has_moustache(self):
        return self.moustache

    def has_beard(self):
        return self.beard


class Box:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = None

    def update_state(self, new_state):
        print(f'box {self.x} {self.y} state change from {self.state} to {new_state}')
        self.state = new_state

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'{self.x} {self.y}  state = {self.state}'



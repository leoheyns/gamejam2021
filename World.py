from Room import Room

class World:

    room = Room()

    def draw(self, WIN):
        self.room.draw(WIN)
    
    def update(self):
        pass
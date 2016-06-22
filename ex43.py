## ex43.py -- basic object-oriented analysis and design

class Scene(object):
    
    def enter(self):
        pass
        
class Engine(object):
    
    def __init__(self, scene_map):
        pass
        
    def play(self):
        pass
        
class Death(Scene):
    
    def enter(self):
        pass
        
class CentralCoridor(Scene):
    
    def enter(self):
        pass

class LaserWeaponryArmory(Scene):
    
    def enter(self):
        pass
        
class TheBridge(Scene):
    
    def enter(self):
        pass
        
class EscapePod(Scene):
    
    def enter(self):
        pass
        
class Map(object):
    
    def __init__(self, start_scene):
        pass
        
    def next_scene(self, scene_name):
        pass
        
    def opening_scene(self):
        pass
        
        
a_map = Map('CentralCoridor')
a_game = Engine(a_map)
a_game.play()
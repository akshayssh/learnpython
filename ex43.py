## ex43.py -- basic object-oriented analysis and design

from sys import exit
from random import randint

class Scene(object):
    
    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter().")
        exit(1)
        
class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
        
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            
        # be sure to print out the last scene
        current_scene.enter()
        
class Death(Scene):
    
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
        ]
        
    def enter(self):
        print Death.quips[randint(0,len(self.quips)-1)]
        exit(1)
        
class CentralCoridor(Scene):
    
    def enter(self):
        print "The Gothos of Planet Percal #25 have invaded your ship and destroyed"
        print "your entire crew. You are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put it in the bridge, and blow the spaceship after getting into an "
        print "escape pod."
        print "\n"
        
        action = raw_input("> ")
        
        if action =="Shoot!":
            print "Quick on the draw you yank out your blaster and fire it at Gothon."
            

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
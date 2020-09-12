'''
Author : Dynamic flash
import Carla egg
connects to the server
exports world object to be used to spawn new npc to existing world

'''


import glob
import os
import sys

def add_carla_egg(path = 'D:/Carla/CARLA_0.9.9.4/WindowsNoEditor/PythonAPI'):
    '''
    path::str : path of carla egg
    '''
    try:
        sys.path.append(glob.glob(path+'/carla/dist/carla-*%d.%d-%s.egg' % (
            sys.version_info.major,
            sys.version_info.minor,
            'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
    except IndexError:
        pass

def get_carla_world(carla):

    try : 
        client = carla.Client('localhost', 2000)
        client.set_timeout(2.0)

        # Once we have a client we can retrieve the world that is currently
        # running.
        world = client.get_world()
        return world
        
    except Exception as e:
        print(e)


add_carla_egg()
import carla

world = get_carla_world(carla)

__exports__ = world



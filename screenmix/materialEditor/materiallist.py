'''
Created on 18.04.2016
@author: mkennert
'''

from materialEditor.singleton import Singleton
from materials.carbonFiber import CarbonFiber
from materials.concrete import Concrete
from materials.glassFiber import GlassFiber
from materials.steel import Steel


@Singleton
class MaterialList:
    
    '''
    the class MaterialList was developed to make it possible
    to use only one materiallist and update the observerclasses
    when something has changed. the class implements the observer- and the singleton-pattern
    Attention: 
    if you add a new observer, make sure that the observer
    implements the interface iobserver
    '''
    
    # constuctor
    def __init__(self):
        self.allMaterials = [Steel(), CarbonFiber(), GlassFiber(), Concrete()]
        self.listeners = []
    
    '''
    update all listeners when a new material was added
    '''

    def update(self):
        for listener in self.listeners:
            print listener
            listener.update()

    '''
    add observer to the listeners-list.
    '''

    def add_listener(self, listener):
        self.listeners.append(listener)

    '''
    add a new material in the materiallist and 
    update all listeners
    '''

    def add_material(self, material):
        self.allMaterials.append(material)
        self.update()


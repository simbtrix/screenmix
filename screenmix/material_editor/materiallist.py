'''
Created on 18.04.2016

@author: mkennert
'''
from materials.steel import Steel
from materials.carbon_fiber import Carbon_Fiber
from materials.concrete import Concrete
from materials.glass_fiber import Glass_Fiber

'''
the class MaterialList was developed to make it possible
to use only one materiallist and update the observerclasses
when something has changed. the class implements the observer-pattern.
Attention: if you add a new observer, make sure that the observer
           implements a update-method.
'''

class MaterialList:
    #constuctor
    def __init__(self):
        self.all_materials=[Steel(),Carbon_Fiber(),Concrete(),Glass_Fiber()]
        self.listeners=[]
     
    '''
    update all listeners when a new material was added
    '''
    def update(self):
        for listener in self.listeners:
            listener.update()
    
    '''
    add observer to the listeners-list.
    '''
    def add_listener(self,listener):
        self.listeners.append(listener)
    
    '''
    add a new material in the materiallist and 
    update all listeners
    '''
    def add_Material(self, material):
        self.all_materials.append(material)
        self.update()
    
    '''
    return the length of the materiallist
    '''
    def get_length(self):
        return len(self.all_materials)
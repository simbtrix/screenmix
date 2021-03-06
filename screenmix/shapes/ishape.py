'''
Created on 26.07.2016

@author: mkennert
'''
from abc import abstractmethod


class IShape:
    
    '''
    IShape is the interface which the shapes must implement. it makes sure,
    that the shapes has the necessary methods, which the other components
    are uses
    '''
    
    #############################################################################
    # the following methods must implemented individual in the class,           #
    # which implements the interface                                            #
    #############################################################################
    
    @abstractmethod
    def calculate_weight_price(self):
        # calculate the weight and the price of 
        # the cross-section-shape
        raise NotImplemented('not implemented')

    @abstractmethod
    def calculate_strength(self):
        # calculate the cracking stress of 
        # the cross-section-shape
        raise NotImplemented('not implemented')

    @abstractmethod
    def set_reinforcement_editor(self, editor):
        raise NotImplemented('not implemented')
    
    #############################################################################
    # the following methods must not implemented in the class,                  #
    # which implements the interface                                            #
    #############################################################################
    
    '''
    the method add_layer add new layer in the view
    '''

    def add_layer(self, percent, material):
        # make sure that the method add_layer is implemented 
        # in the view
        self.view.add_layer(percent, material)

    '''
    the method delete_layer delete the selected materials
    '''

    def delete_layer(self):
        # make sure that the method delete_layer is implemented 
        # in the view
        self.view.delete_layer()

    '''
    the method update_layinfo update the layer
    after a layer get the focus
    '''

    def update_layinfo(self, name, price, density, stiffness, strength, percent):
        self.refEdit.update_layinfo(name, price, density, stiffness,strength, percent)
    
    '''
    reset the layer_information
    '''
    def reset_layer_information(self):
        self.refEdit.reset_layer_information()
    
    '''
    the method update_layinfo update the cross section information
    '''

    def update_cs_information(self):
        self.refEdit.update_cs_information(self.price, self.weight, self.strength)

    '''
    the method update_percent change the percentage share of the selected materials
    '''

    def update_percent(self, value):
        self.view.update_percent(value)

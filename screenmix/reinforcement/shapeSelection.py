'''
Created on 13.05.2016

@author: mkennert
'''
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from ownComponents.design import Design
from ownComponents.ownButton import OwnButton
from ownComponents.ownGraph import OwnGraph
from plot.line import LinePlot
from kivy.properties import ObjectProperty

Window.clearcolor = (1, 1, 1, 0.5)
class ShapeSelection(GridLayout):
    information = ObjectProperty()
    #constructor

    def __init__(self, **kwargs):
        super(ShapeSelection, self).__init__(**kwargs)
        self.padding = [10, 10, 10, 10]
        self.cols = 2
        self.spacing = 5
        self.btnHeight = Design.btnHeight
    '''
    create the gui
    '''

    def create_gui(self):
        self.create_graphs()
        self.create_selection()
    '''
    create all graphs
    '''

    def create_graphs(self):
        self.create_graph_rectangle()
        # default-shape Rectangle
        self.add_widget(self.graphRectangle)
        self.focusGraph = self.graphRectangle
        ###################################################################
        # here you can add more shapes.                                    #
        # implement a graph which represent the shape                      #
        ###################################################################

    '''
    create the plot graph
    '''

    def create_graph_rectangle(self):
        self.graphRectangle = OwnGraph(
            border_color=[0.5, 0.5, 0.5, 0],
            x_ticks_major=0.1, y_ticks_major=0.05,
            y_grid_label=True, x_grid_label=True,
            xmin=0, xmax=0.5, ymin=0, ymax=0.25)
        self.p = LinePlot(color=[1, 1, 1, 1], points=self.draw_rectangle())
        self.graphRectangle.add_plot(self.p)

    '''
    draw the plot
    '''

    def draw_rectangle(self):
        c = 1e-2
        h = 0.23
        w = 0.45
        return [(c, c), (c, h), (w, h), (w, c), (c, c)]

    '''
    create the right area where you can select 
    the shape
    '''

    def create_selection(self):
        self.create_btns()
        self.contentRight = GridLayout(cols=1)
        # self.contentRight.add_widget(self.focusShape)
        self.btns = GridLayout(cols=1, spacing=10, size_hint_y=None)
        # self.contentRight.add_widget(self.btns)
        # Make sure the height is such that there is something to scroll.
        self.btns.bind(minimum_height=self.btns.setter('height'))
        self.btns.add_widget(self.plot)
        ###################################################################
        # here you can add more shapes.                                    #
        # implement the button in the create_btns method                   #
        ###################################################################
        layout = GridLayout(cols=2, spacing=15)
        layout.add_widget(self.btnOK)
        layout.add_widget(self.btnCancel)
        self.btns.add_widget(layout)
        self.shapes = ScrollView()
        self.shapes.add_widget(self.btns)
        self.contentRight.add_widget(self.shapes)
        self.add_widget(self.contentRight)

    '''
    create and bind all btns from the gui
    '''

    def create_btns(self):
        self.btnOK = OwnButton(text='ok', size_hint_y=None, height=self.btnHeight)
        self.btnOK.bind(on_press=self.finished)
        self.btnCancel = OwnButton(
            text='cancel', size_hint_y=None, height=self.btnHeight)
        self.btnCancel.bind(on_press=self.cancel)
        # default-shape=plot
        self.focusShape = OwnButton(
            text='plot', size_hint_y=None, height=self.btnHeight)
        self.focusShape.bind(on_press=self.show_shapes_btn)
        # btns
        self.plot = OwnButton(
            text='rectangle', size_hint_y=None, height=self.btnHeight)
        self.plot.bind(on_press=self.show_rectangle)
        #######################################################################
        # here you can add more shapes                                         #
        # Attention: make sure that the buttons habe the properties            #
        # size_hint_y=None, height=self.btnSize and a bind-method             #
        # like the show_rectangle-method                                       #
        #######################################################################

    '''
    show Rectangle-Graph
    '''

    def show_rectangle(self, btn):
        self.remove_widget(self.focusGraph)
        self.add_widget(self.graphRectangle, 1)
        self.focusGraph = self.graphRectangle
        self.focusShape.text = btn.text
        
    #######################################################
    # if you want add new shapes make sure, that the shape# 
    # has a show-method like the show_rectangle           # 
    #######################################################
    
    '''
    show the btns where you can select the shape
    '''

    def show_shapes_btn(self, btn):
        self.contentRight.remove_widget(self.focusShape)
        self.contentRight.add_widget(self.shapes)

    '''
    finished the totally selection and call the 
    finished_shape_selection of the information
    '''

    def finished(self, btn):
        self.information.finished_shape_selection(self.focusShape)

    '''
    cancel the shape selection 
    '''

    def cancel(self, btn):
        self.information.cancel_shape_selection()

    '''
    set the information
    '''

    def set_information(self, information):
        self.information = information
        self.create_gui()
    
'''
Created on 07.04.2016

@author: mkennert
'''
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

'''
The class Keyboard was developed to give the user the possibility
to write words with a keyboard. 
the keyboard-object is a popup
'''
class Keyboard(Popup):
    #Constructor
    def __init__(self, **kwargs):
        super(Keyboard, self).__init__(**kwargs)
        self.alphabet_small='qwertzuiopasdfghjkl_.yxcvbnm'
        self.create_small_keyboard()
        self.content=self.layout
        self.title='Keyboard'
    
    '''
    the method create_small_keyboard create the
    gui of the keyboard
    '''
    def create_small_keyboard(self):
        self.textinput = Label(text='')
        self.layout=GridLayout(cols=1)
        self.layout.add_widget(self.textinput)
        self.small_keyboard=GridLayout(cols=10)
        for i in range(0,len(self.alphabet_small)):
            cur=Button(text=self.alphabet_small[i])
            cur.bind(on_press=self.appending)
            self.small_keyboard.add_widget(cur)
        btn_delete=Button(text='<<')
        btn_delete.bind(on_press=self.delete)
        btn_finished=Button(text='ok')
        btn_finished.bind(on_press=self.close_popup)
        self.small_keyboard.add_widget(btn_delete)
        self.small_keyboard.add_widget(btn_finished)
        self.layout.add_widget(self.small_keyboard)
    '''
    the method appending appends character at the end.
    the method is called when the user use the keyboard
    '''
    def appending(self,button): 
        self.textinput.text+=button.text
    
    '''
    the method delete delete character at the end.
    the method is called when the press the button '<<'
    '''
    def delete(self,button):
        self.textinput.text=self.textinput.text[:-1]
    '''
    the method close_popup close the popup when the user
    is finished and press the button 'ok'
    '''
    def close_popup(self,button):
        self.dismiss()
    
    '''
    the method reset_text reset the text of the label
    the method must be called from the developer when
    the text must be deleted
    '''
    def reset_text(self):
        self.textinput.text=''
    
class NumPadApp(App):
    def build(self):
        return Keyboard()

if __name__ == '__main__':
    NumPadApp().run()
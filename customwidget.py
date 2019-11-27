#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 18:49:30 2018

@author: Haneen
"""

import kivy
from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.widget import Widget

class CustomWidget(Widget):
    pass

class CustomWidgetApp(App):
    
    def build(self):
        return CustomWidget()
num = CustomWidgetApp()
num.run()
#!/usr/bin/python3
# -*- coding: utf-8 -*-


import gi
import subprocess
import gtk
import os
from subprocess import Popen, PIPE, STDOUT

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class SwitcherWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Warp GUI")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        switch = Gtk.Switch()
        switch.connect("notify::active", self.on_switch_activated)
        hbox.pack_start(switch, True, True, 0)

        button = Gtk.Button.new_with_label("Check Status")
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)

        output = subprocess.check_output(["warp-cli", "status"], encoding='cp437')
        connect = "Connected"
        disconnect = "Disconnected"
        if disconnect in output:
        	output = disconnect
        else: 
        	output = connect
        self.label = Gtk.Label(output)
        hbox.pack_start(self.label, True, True, 0)

    def on_switch_activated(self, switch, gparam):
        if switch.get_active():
            state = "on"
            connect = "Connected"
            disconnect = "Disconnected"
            subprocess.call(["warp-cli", "connect"])
            output = subprocess.check_output(["warp-cli", "status"], encoding='cp437')
            if disconnect in output:
            	output = disconnect
            else:
            	output = connect
            self.label.set_text(output)
        else:
            state = "off"
            connect = "Connected"
            disconnect = "Disconnected"
            subprocess.call(["warp-cli", "disconnect"])
            subprocess.call(["warp-cli", "status"])
            output = subprocess.check_output(["warp-cli", "status"], encoding='cp437')
            if disconnect in output:
            	output = disconnect
            else:
            	output = connect
            self.label.set_text(output)
        print("Switch was turned", state)

    def on_click_me_clicked(self, button):
        output = subprocess.check_output(["warp-cli", "status"], encoding='cp437')
        connect = "Connected"
        disconnect = "Disconnected"
        print (output)
        if disconnect in output:
        	output = disconnect
        else:
        	output = connect
        self.label.set_text(output)


win = SwitcherWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

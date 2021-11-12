#!/usr/bin/python3
# -*- coding: utf-8 -*-


import gi
import subprocess
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class SwitcherWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Warp GUI")
        self.set_border_width(30)

        hbox = Gtk.Box(spacing=10)
        self.add(hbox)

        switch = Gtk.Switch()
        switch.connect("notify::active", self.on_switch_activated)
        hbox.pack_start(switch, True, True, 0)

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


win = SwitcherWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

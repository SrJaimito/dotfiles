from libqtile import widget
from libqtile.widget import base

from qtile_extras import widget as widget_extra

import psutil
import iwlib

from colors import catppuccin


#############
# Group Box #
#############

GROUP_COLORS = [
    catppuccin['mocha']['flamingo'],
    catppuccin['mocha']['pink'],
    catppuccin['mocha']['mauve'],
    catppuccin['mocha']['red'],
    catppuccin['mocha']['peach'],
    catppuccin['mocha']['yellow'],
    catppuccin['mocha']['green'],
    catppuccin['mocha']['sky'],
    catppuccin['mocha']['blue']
]


class DotGroupBox(widget_extra.GroupBox):

    def draw(self):
        self.drawer.clear(self.background or self.bar.background)

        offset = self.margin_x
        for i, group in enumerate(self.groups):
            bw = self.box_width([group])

            # label = '\u25cf'
            label = '\uf111'
            color = catppuccin['mocha']['text']
            
            if group.screen:
                if self.qtile.current_screen == group.screen:
                    # label = '\uf4c3'
                    label = '\uf192'
                else:
                    label = '\ueabc'

            if group.windows or group.screen:
                color = GROUP_COLORS[i]

            self.drawbox(
                offset,
                label,
                None,
                color,
                highlight_color = self.highlight_color,
                width = bw,
                rounded = self.rounded,
                block = False,
                line = False,
                highlighted = False,
            )

            offset += bw + self.spacing

        self.drawer.draw(
            offsetx = self.offset,
            offsety = self.offsety,
            width = self.width
        )


########
# WLAN #
########

valid_interface = False
is_wifi = False


class WlanInfo(base.InLoopPollText):

    def poll(self):
        global valid_interface
        global is_wifi

        interfaces = []
        for name, stats in psutil.net_if_stats().items():
            if stats.isup:
                if name[0] == 'w' or name[0] == 'e':
                    interfaces.append(name)

        current_interface = interfaces[0]

        if current_interface[0] == 'w':
            valid_interface = True
            is_wifi = True

            return bytes(iwlib.get_iwconfig(current_interface)['ESSID']).decode()

        elif current_interface[0] == 'e':
            valid_interface = True
            is_wifi = False

            return 'Eth'

        else:
            valid_interface = False
            is_wifi = False

            return 'N/A'


class WlanIcon(base.InLoopPollText):

    def poll(self):
        global valid_interface
        global is_wifi

        if valid_interface:
            if is_wifi:
                return '\uf1eb'
            else:
                return '\U000f0200'

        return ''


#########
# Clock #
#########

class MacosClock(widget.Clock):

    def __init__(self, **config):
        widget.Clock.__init__(self, **config)
        self.format = '%a %-d %b %H:%M'


    def poll(self):
        original_string = super().poll()

        capitalized_words = [word.capitalize() for word in original_string.split(' ')]
        capitalized_string = ' '.join(capitalized_words)

        return capitalized_string


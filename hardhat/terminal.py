import sys
from .util import Object


class Terminal(Object):
    normal = '0'
    bold = '1'
    light = '2'

    # Foreground
    black = '30'
    red = '31'
    green = '32'
    yellow = '33'
    blue = '34'
    purple = '35'
    cyan = '36'
    white = '37'

    @staticmethod
    def normal_green(text):
        return Terminal.color(text, Terminal.normal, Terminal.green)

    @staticmethod
    def normal_red(text):
        return Terminal.color(text, Terminal.normal, Terminal.red)

    @staticmethod
    def normal_white(text):
        return Terminal.color(text, Terminal.normal, Terminal.white)

    @staticmethod
    def light_green(text):
        return Terminal.color(text, Terminal.light, Terminal.green)

    @staticmethod
    def light_red(text):
        return Terminal.color(text, Terminal.light, Terminal.red)

    @staticmethod
    def light_white(text):
        return Terminal.color(text, Terminal.light, Terminal.white)

    @staticmethod
    def bold_red(text):
        return Terminal.color(text, Terminal.bold, Terminal.red)

    @staticmethod
    def bold_white(text):
        return Terminal.color(text, Terminal.bold, Terminal.white)

    @staticmethod
    def normal_yellow(text):
        return Terminal.color(text, Terminal.normal, Terminal.yellow)

    @staticmethod
    def color(text, boldness, color):
        start = '\x1b[%s;%sm'
        end = '\x1b[0m'

        if sys.stdout.isatty():
            return start % (boldness, color) + text + end
        return text

    @staticmethod
    def strip(text):
        i = 0
        while i < len(text) - 4:
            if text[i] == '\x1b' and text[i+1] == '[':
                start = i
                i += 2
                while text[i] != 'm':
                    i += 1
                text = text[:start] + text[i + 1:]
                i = start
            i += 1
        return text

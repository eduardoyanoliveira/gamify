from colour import Color

def is_color(color):
    try:
        color = color.replace(" ", "")
        Color(color)
        return True
    except ValueError:
        return False
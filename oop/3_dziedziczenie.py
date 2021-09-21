# Dziedziczenie

# Button
# TextButton
# Checkbox

# enable()
# disable()
# setPosition()


class UIWidget:
    def enable(self):
        print("Enable")


class TexButton(UIWidget):
    pass

t = TexButton()
t.enable()

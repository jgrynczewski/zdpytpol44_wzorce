import abc


# Interfejs
class UIWidget(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        pass

    @abc.abstractmethod
    def enable(self):
        pass


class CheckBox(UIWidget):
    def draw(self):
        print("Draw Checkbox")

    def enable(self):
        print("Enable Checkbox")



class MojaNowaKlasa(UIWidget):
    def draw(self):
        print("Print MojaNowaKlasa")
    def enable(self):
        print("Enable MojaNowaKlasa")


def draw_widget(item: UIWidget) -> None:
    item.enable()


draw_widget(MojaNowaKlasa())
draw_widget(CheckBox())

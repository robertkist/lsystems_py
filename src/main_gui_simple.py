from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from lsys.lsystem import LSystem

"""
A simple L-System viewer without the rest of the GUI
"""


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        """Constructor"""
        super().__init__()
        self.label = QLabel(self)
        self.setCentralWidget(self.label)
        self.img = QImage(800, 600, QImage.Format_ARGB32)
        self.p = QPainter()
        self.p.begin(self.img)
        self.p.fillRect(self.img.rect(), QColor(20, 20, 20))
        self.p.end()
        self.lsystem = LSystem()
        self.__timer_id: int = 0
        self.stop: bool = False

    def progress_slot(self, count: int, total: int) -> None:
        """Dummy slot"""

    def finish_slot(self) -> None:
        """Dummy slot"""

    def start_slot(self) -> None:
        """Dummy slot"""

    def draw_slot(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """Draws the l-system"""
        self.p.begin(self.img)
        self.p.setPen(QPen(Qt.white, 1))
        self.p.drawLine(x1, y1, x2, y2)
        self.p.end()
        QApplication.processEvents()
        self.label.setPixmap(QPixmap(self.img))

    def showEvent(self, event: QShowEvent) -> None:
        """Qt Window show event: we use a timer to start the l-system drawing"""
        self.__timer_id = self.startTimer(1)

    def closeEvent(self, event: QCloseEvent) -> None:
        """stop drawing"""
        self.stop = True

    def timerEvent(self, event: QTimerEvent) -> None:
        """draw the l-system"""
        self.killTimer(self.__timer_id)
        f = {
            "angle": 90,
            "axiom": "X",
            "desc": "Hilbert Curve",
            "distance": 4,
            "itermax": 7,
            "iterations": 6,
            "orientation": [1, 0],
            "pos": [
                10,
                10
            ],
            "rules": {
                "X": "-YF+XFX+FY-",
                "Y": "+XF-YFY-FX+"
            }
        }
        cmd = self.lsystem.generate_lsystem(rules=f['rules'], axiom=f['axiom'],
                                            iterations=f['iterations'])
        self.lsystem.draw(cmd=cmd, px=f['pos'][0], py=f['pos'][1],
                          rx=f['orientation'][0], ry=f['orientation'][1],
                          angle=f['angle'], distance=f['distance'],
                          draw_callback=self.draw_slot,
                          finish_callback=self.finish_slot,
                          progress_callback=self.progress_slot,
                          abort_callback=self.start_slot)


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication()
    mw = MainWindow()
    mw.show()
    app.exec_()

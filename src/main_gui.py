import os
import json
from typing import Any, Dict
from PySide2.QtCore import QRect
from PySide2.QtWidgets import QTreeWidgetItem, QMainWindow, QApplication
from PySide2.QtGui import QCloseEvent, Qt, QImage, QPainter, QColor, QPixmap, QPen
from gui.mainwindow_ui import Ui_MainWindow
from lsys.lsystem import LSystem

"""
A simple GUI for trying out various L-Systems:
Fractals, space filling curves, trees, etc.
"""

CATEGORY: int = 0
LSYSTEM: int = 1
SAVE_PNG: bool = False
IMG_WIDTH: int = 800
IMG_HEIGHT: int = 600
WINDOW_TITLE: str = "L-Systems"
DATA_FILE: str = os.path.join(os.path.dirname(__file__), "data", "lsystems.json")


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        """Constructor"""
        super().__init__()
        # init UI
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        self.combobox_updating = False
        self.setWindowTitle(WINDOW_TITLE)
        # create display image
        self.img: QImage = QImage(IMG_WIDTH, IMG_HEIGHT, QImage.Format_ARGB32)
        self.p: QPainter = QPainter()
        self.clear_image()
        self.__ui.label.setPixmap(QPixmap(self.img))
        self.maxx: int = 0
        self.minx: int = self.img.width()
        self.maxy: int = 0
        self.miny: int = self.img.height()
        # load l-system JSON
        with open(DATA_FILE, "rt", encoding='utf8') as fp:
            systems = json.loads(fp.read())
        for category in systems:
            cat_item: QTreeWidgetItem = QTreeWidgetItem()
            cat_item.setText(0, category)
            cat_item.type = CATEGORY
            self.__ui.treeWidget.addTopLevelItem(cat_item)
            # populate tree widget
            for s in systems[category]:
                item: QTreeWidgetItem = QTreeWidgetItem()
                item.setText(0, s['desc'])
                item.dict = s
                item.type = LSYSTEM
                cat_item.addChild(item)
            cat_item.setExpanded(True)
        self.__ui.treeWidget.itemClicked.connect(self.item_clicked_slot)
        self.__ui.comboBox.currentIndexChanged.connect(self.combobox_changed_slot)
        # init lsystem
        self.lsystem: LSystem = LSystem()
        self.iter: int = 1

    def closeEvent(self, _: QCloseEvent) -> None:
        """Qt Window Close event: stop l-system drawing"""
        self.lsystem.stop()

    def combobox_changed_slot(self, idx: int) -> None:
        """User picked a different iteration depth"""
        if self.combobox_updating:
            return
        self.iter = int(self.__ui.comboBox.itemText(idx))
        if self.lsystem.running:
            self.lsystem.stop()
        else:
            self.start_slot()

    def clear_image(self) -> None:
        """Clears the viewport"""
        self.p.begin(self.img)
        self.p.fillRect(self.img.rect(), QColor(20, 20, 20))
        self.p.end()

    def item_clicked_slot(self, item: QTreeWidgetItem, _: Any) -> None:
        """User clicked on an entry in the l-systems list GUI"""
        if item.type == LSYSTEM:
            self.combobox_updating = True
            self.__ui.comboBox.clear()
            self.__ui.comboBox.addItems(str(i) for i in range(1, item.dict['itermax'] + 1))
            self.__ui.comboBox.setCurrentIndex(item.dict['iterations'] - 1)
            self.iter = item.dict['iterations']
            self.combobox_updating = False
            if self.lsystem.running:
                self.lsystem.stop()
            else:
                self.start_slot()

    def start_slot(self) -> None:
        """Start drawing"""
        self.clear_image()
        self.paint_lsystem(self.__ui.treeWidget.currentItem().dict)

    def progress_slot(self, i: int, total: int) -> None:
        """Drawing progress update"""
        self.statusBar().showMessage("%s of %s" % (i, total), 0)

    def draw_slot(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """Does the actual drawing"""
        self.p.begin(self.img)
        self.p.setPen(QPen(Qt.white, 1))
        self.p.drawLine(x1, y1, x2, y2)
        # get the extents of the drawing
        if SAVE_PNG:
            self.minx = x1 if x1 < self.minx else self.minx
            self.minx = x2 if x2 < self.minx else self.minx
            self.maxx = x1 if x1 > self.maxx else self.maxx
            self.maxx = x2 if x2 > self.maxx else self.maxx
            self.miny = y1 if y1 < self.miny else self.miny
            self.miny = y2 if y2 < self.miny else self.miny
            self.maxy = y1 if y1 > self.maxy else self.maxy
            self.maxy = y2 if y2 > self.maxy else self.maxy
        self.p.end()
        QApplication.processEvents()
        self.__ui.label.setPixmap(QPixmap(self.img))

    def finish_slot(self) -> None:
        """Called when drawing has finished"""
        if not SAVE_PNG:
            return
        border = 5
        width = self.maxx - self.minx + border * 2 + 1
        height = self.maxy - self.miny + border * 2 + 1
        r = QRect(self.minx - border,
                  self.miny - border,
                  width, height)

        img = QImage(width, height, QImage.Format_RGB32)
        self.p.begin(img)
        self.p.drawImage(QRect(0, 0, width, height), self.img, r, Qt.AutoColor)
        self.p.end()

        fn = self.__ui.treeWidget.currentItem().text(0).replace(' ', "_") + ".png"
        os.makedirs(os.path.join(os.path.dirname(__file__), "img"), exist_ok=True)
        path = os.path.join(os.path.dirname(__file__), "img", fn)
        print("saving as", path)
        img.save(path, "png")

        self.p.begin(self.img)
        self.p.setPen(QPen(Qt.green, 1))
        self.p.drawRect(r)
        self.p.end()
        self.__ui.label.setPixmap(QPixmap(self.img))

    def paint_lsystem(self, f: Dict[Any, Any]) -> None:
        """Generates the l-system and then draws it"""
        self.maxx = 0
        self.minx = self.img.width()
        self.maxy = 0
        self.miny = self.img.height()
        cmd = self.lsystem.generate_lsystem(rules=f['rules'], axiom=f['axiom'],
                                            iterations=self.iter)
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

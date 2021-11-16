import math
from typing import Union, Any


class LTurtle:
    """A class to implement a simple Logo-style turtle for drawing l-systems"""

    def __init__(self,
                 px: Union[int, float],
                 py: Union[int, float],
                 rx: Union[int, float],
                 ry: Union[int, float],
                 angle: Union[int, float],
                 distance: int,
                 draw_func: Any) -> None:
        """
        Constructor.
        :param px: start x position on the screen in pixels.
        :param py: start y position on the screen in pixels.
        :param rx: initial orientation vector x component (use 0, 1, -1)
        :param ry: initial orientation vector x component (use 0, 1, -1)
        :param angle: turn angle for + and - commands .
        :param distance: distance in pixels for F command.
        :param draw_func: called when a line should be drawn. Callback param1: line start x, param2: line start y, param3: line end x, param4: line end y
        """
        self.__px: Union[int, float] = px  # position
        self.__py: Union[int, float] = py
        self.__rx: Union[int, float] = rx  # direction vector
        self.__ry: Union[int, float] = ry
        self.__angle: Union[int, float] = angle
        self.__set_angle(self.__angle)
        self.__distance: Union[int, float] = distance
        self.__draw_func: Any = draw_func

    @property
    def px(self) -> Union[int, float]:
        """Returns turtle's x position"""
        return self.__px

    @property
    def py(self) -> Union[int, float]:
        """Returns turtle's x position"""
        return self.__py

    @property
    def rx(self) -> Union[int, float]:
        """Returns tutle's orientation vector's x component"""
        return self.__rx

    @property
    def ry(self) -> Union[int, float]:
        """Returns tutle's orientation vector's y component"""
        return self.__ry

    def forward(self) -> None:
        """Moves the turtle forward and draws a line"""
        ox: Union[int, float] = self.__px
        oy: Union[int, float] = self.__py
        self.__px += self.__rx * self.__distance
        self.__py += self.__ry * self.__distance
        self.__draw_func(ox, oy, self.__px, self.__py)

    def left(self) -> None:
        """Rotates the turtle counter-clockwise"""
        self.__rotate_func(self.__angle)

    def right(self) -> None:
        """Rotates the turtle clockwise"""
        self.__rotate_func(-self.__angle)

    def __set_angle(self, a: float) -> None:
        """Sets the turtle's rotational angle"""
        self.__angle = a
        if self.__angle == 90:
            self.__rotate_func = self.__rotate_90
        else:
            self.__rotate_func = self.__rotate_any

    def __rotate_any(self, a: float) -> None:
        """Rotates the turtle in any direction by any degrees"""
        a = math.radians(a)
        sin_a = math.sin(a)
        cos_a = math.cos(a)
        xn = self.__rx * cos_a - self.__ry * sin_a
        yn = self.__rx * sin_a + self.__ry * cos_a
        self.__rx = xn
        self.__ry = yn

    def __rotate_90(self, a: float) -> None:
        """
        Rotates the turtle in any direction by 90 degrees.
        This method is much faster as we're just swapping vector components around.
        """
        if a < 0:
            dx = self.__ry
            self.__ry = -self.__rx
            self.__rx = dx
        else:
            dx = -self.__ry
            self.__ry = self.__rx
            self.__rx = dx

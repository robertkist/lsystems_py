from typing import Union, Any, Dict, Optional
from .lturtle import LTurtle


class LSystem:
    """
    A class for generating and drawing l-systems.
    Drawing is implemented via callbacks: simply supply a function that draws a line, using
    your particular graphics library or framework (e.g. Pillow, Qt, etc.)
    """

    def __init__(self) -> None:
        """Constructor"""
        self.__running: bool = False  # l-system generation is currently running
        self.__stop: bool = False  # used to stop l-system generation

    @classmethod
    def generate_lsystem(cls, rules: Dict[str, str], axiom: str, iterations: int) -> str:
        """
        Generates the l-system.
        :param rules: rules as dict { 'key': 'rule' }
        :param axiom: axion as string
        :param iterations: how many iterations to generate
        """
        for _ in range(0, iterations):
            out = ''
            for c in axiom:
                out += rules.get(c, c)
            axiom = out
        return axiom

    @property
    def running(self) -> bool:
        """Returns true if l-ssytem generation is currently running"""
        return self.__running

    def stop(self) -> None:
        """Stops a currently running l-system generation"""
        self.__stop = True

    def draw(self,
             cmd: str,
             px: Union[int, float],
             py: Union[int, float],
             rx: Union[int, float],
             ry: Union[int, float],
             angle: Union[int, float],
             distance: int,
             draw_callback: Any,
             finish_callback: Any,
             progress_callback: Any,
             abort_callback: Any,
             i: int = 0) -> Optional[int]:
        """
        Iteratively draws the l-system. Use rx and ry to specify the start direction for drawing
        the l-system.
        :param cmd: the l-system string as generated by self.generate_lsystem()
        :param px: start x position on the screen in pixels.
        :param py: start y position on the screen in pixels.
        :param rx: initial orientation vector x component (use 0, 1, -1)
        :param ry: initial orientation vector x component (use 0, 1, -1)
        :param angle: turn angle for + and - commands .
        :param distance: distance in pixels for F command.
        :param draw_callback: called when a line should be drawn. Callback param1: line start x, param2: line start y, param3: line end x, param4: line end y
        :param finish_callback: called when drawing has finished successfully. Callback takes no parameters.
        :param progress_callback: called after each command. Callback param1: current command number, param2: total number of commands.
        :param abort_callback: called when user calls stop(). Callback takes no parameters.
        :param i: iteration depth (defaults to 0; for internal use only)
        :return: None (number of commands executed if iteration depth > 0 - for internal use only)
        """
        self.__running = True
        self.__stop = False
        t = LTurtle(px=px,
                    py=py,
                    rx=rx,
                    ry=ry,
                    angle=angle,
                    distance=distance,
                    draw_func=draw_callback)
        len_cmd: int = len(cmd)
        while i < len(cmd):
            c = cmd[i]
            if c == 'F':
                t.forward()
            elif c == '+':
                t.right()
            elif c == '-':
                t.left()
            elif c == '[':
                j: Optional[int] = self.draw(cmd=cmd, px=t.px, py=t.py, rx=t.rx, ry=t.ry,
                                             angle=angle, distance=distance,
                                             draw_callback=draw_callback,
                                             finish_callback=finish_callback,
                                             progress_callback=progress_callback,
                                             abort_callback=abort_callback, i=i + 1)
                if j is None:
                    return None
                i = j
            elif c == ']':
                return i
            i += 1
            progress_callback(i, len_cmd)
            if self.__stop:
                break
        self.__running = False
        if self.__stop:
            abort_callback()
        else:
            finish_callback()
        self.__stop = True
        return None

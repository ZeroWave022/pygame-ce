from typing import Optional, Tuple, Union, final

from pygame._common import Coordinate
from pygame.locals import WINDOWPOS_UNDEFINED
from pygame.surface import Surface

def get_grabbed_window() -> Optional[Window]: ...
@final
class Window:
    def __init__(
        self,
        title: str = "pygame window",
        size: Coordinate = (640, 480),
        position: Union[int, Coordinate] = WINDOWPOS_UNDEFINED,
        **flags: bool
    ) -> None: ...
    def destroy(self) -> None: ...
    def set_windowed(self) -> None: ...
    def set_fullscreen(self, desktop: bool = False) -> None: ...
    def focus(self, input_only: bool = False) -> None: ...
    def hide(self) -> None: ...
    def show(self) -> None: ...
    def restore(self) -> None: ...
    def maximize(self) -> None: ...
    def minimize(self) -> None: ...
    def set_modal_for(self, parent: Window) -> None: ...
    def set_icon(self, icon: Surface) -> None: ...

    grab: bool
    title: str
    resizable: bool
    borderless: bool
    always_on_top: bool
    relative_mouse: bool
    opacity: float

    @property
    def id(self) -> int: ...
    @property
    def display_index(self) -> int: ...
    @property
    def size(self) -> Tuple[int, int]: ...
    @size.setter
    def size(self, value: Coordinate) -> None: ...
    @property
    def position(self) -> Tuple[int, int]: ...
    @position.setter
    def position(self, value: Union[int, Coordinate]) -> None: ...
    @classmethod
    def from_display_module(cls) -> Window: ...

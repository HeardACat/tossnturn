# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pyfltk",
#     "pynput",
# ]
# ///

from pynput.mouse import Controller
import time
import threading
import fltk


class MainWindow(fltk.Fl_Window):
    def __init__(self):
        super().__init__(300, 150, "Toss and Turn")
        self.mouse = Controller()
        self.is_running = False
        self.thread = None
        
        # Create status label
        self.status_label = fltk.Fl_Box(20, 20, 260, 30, "Toss and Turn Status: Enabled")
        self.status_label.box(fltk.FL_FLAT_BOX)
        self.status_label.labelsize(14)
        
        # Create toggle button
        self.toggle_button = fltk.Fl_Button(100, 60, 100, 30, "Toggle")
        self.toggle_button.callback(self.on_toggle)
        
        self.end()
        self.show()

    def on_toggle(self, widget):
        if not self.is_running:
            self.is_running = True
            self.thread = threading.Thread(target=self.move_mouse)
            self.thread.daemon = True
            self.thread.start()
        else:
            self.is_running = False
        self._update_label()

    def _update_label(self):
        status = "Disabled" if self.is_running else "Enabled"
        self.status_label.label(f"Toss and Turn Status: {status}")
        self.redraw()

    def move_mouse(self):
        eps = 1
        timeout = 280
        while self.is_running:
            self.mouse.move(eps, 0)
            self.mouse.move(-eps, 0)
            time.sleep(timeout)


def main() -> None:
    window = MainWindow()
    fltk.Fl.run()


if __name__ == "__main__":
    main()

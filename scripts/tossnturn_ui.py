# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pynput",
#     "wxpython",
# ]
# ///

from pynput.mouse import Controller
import time
import wx
import threading


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Toss and Turn', size=(300, 150))
        self.mouse = Controller()
        self.is_running = False
        self.thread = None
        
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.status_label = wx.StaticText(panel, label='Toss and Turn Status:')
        self.toggle_button = wx.Button(panel, label='Enabled')
        self.toggle_button.Bind(wx.EVT_BUTTON, self.on_toggle)
        
        vbox.Add(self.status_label, 0, wx.ALL | wx.CENTER, 20)
        vbox.Add(self.toggle_button, 0, wx.ALL | wx.CENTER, 20)
        panel.SetSizer(vbox)
        
        self.Centre()
        self.Show()

    def _update_label(self):
        self.status_label.SetLabel(f'Toss and Turn Status: {"Disabled" if self.is_running else "Enabled"}')

    def on_toggle(self, event):
        if not self.is_running:
            self.is_running = True
            self.toggle_button.SetLabel('Toggle')
            self.thread = threading.Thread(target=self.move_mouse)
            self.thread.daemon = True
            self.thread.start()
        else:
            self.is_running = False
            self.toggle_button.SetLabel('Toggle')
        self._update_label()

    def move_mouse(self):
        eps = 1
        timeout = 280
        while self.is_running:
            self.mouse.move(eps, 0)
            self.mouse.move(-eps, 0)
            time.sleep(timeout)
        


def main() -> None:
    app = wx.App()
    _ = MainFrame()
    app.MainLoop()


if __name__ == "__main__":
    main()

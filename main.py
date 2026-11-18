"""
Word Counter - offline, client-side only Android app (Kivy).

- Shows "Word Counter" at the top.
- Shows a large numerical counter that increases automatically over time.
- Starts from a big number (the idea behind range(1000000, 102930233)).
- Remembers the counter value locally so it survives app restarts.
- Uses LMAO.png as a full-screen wallpaper behind the interface.
"""

import json
import os

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label

# Big-number bounds inspired by range(1000000, 102930233).
# Well within 64-bit integer limits, so nothing will overflow/crash.
COUNT_START = 1_000_000
COUNT_LIMIT = 102_930_233

TICK_RATE = 1.0 / 60.0  # increment ~60 times per second
SAVE_INTERVAL = 1.0     # persist the value to disk once per second

WHITE = (1, 1, 1, 1)
SHADOW = (0, 0, 0, 0.55)


class WordCounterApp(App):
    def build(self):
        # Restore the previously saved value, or start big on first launch.
        self.counter = self._load_counter()

        root = FloatLayout()

        # Full-screen wallpaper, sitting behind every other widget.
        wallpaper = Image(
            source="LMAO.png",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={"x": 0, "y": 0},
        )
        root.add_widget(wallpaper)

        # Title: near the top, horizontally centred.
        self.title_label = Label(
            text="Word Counter",
            font_size="30sp",
            bold=True,
            color=WHITE,
            outline_color=SHADOW,
            outline_width=2,
            size_hint=(1, None),
            height="60sp",
            pos_hint={"center_x": 0.5, "top": 0.92},
        )
        root.add_widget(self.title_label)

        # Counter: the main focus, centred both ways.
        self.counter_label = Label(
            text=self._format(self.counter),
            font_size="86sp",
            bold=True,
            color=WHITE,
            outline_color=SHADOW,
            outline_width=3,
            size_hint=(1, None),
            height="140sp",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        root.add_widget(self.counter_label)

        # Drive the counter and its local memory.
        Clock.schedule_interval(self._tick, TICK_RATE)
        Clock.schedule_interval(self._save_counter, SAVE_INTERVAL)

        return root

    @staticmethod
    def _format(value):
        """Thousand-separated digits, e.g. 1,000,000."""
        return f"{value:,}"

    def _tick(self, dt):
        """Automatically increase the counter over time."""
        self.counter += 1
        if self.counter >= COUNT_LIMIT:
            self.counter = COUNT_START
        self.counter_label.text = self._format(self.counter)

    @property
    def _storage_path(self):
        # App-private, persistent location on both desktop and Android.
        return os.path.join(self.user_data_dir, "word_counter.json")

    def _load_counter(self):
        try:
            with open(self._storage_path, "r", encoding="utf-8") as f:
                return int(json.load(f)["counter"])
        except (OSError, ValueError, KeyError, TypeError):
            return COUNT_START

    def _save_counter(self, dt=None):
        try:
            os.makedirs(self.user_data_dir, exist_ok=True)
            with open(self._storage_path, "w", encoding="utf-8") as f:
                json.dump({"counter": self.counter}, f)
        except OSError:
            pass

    def on_pause(self):
        self._save_counter()
        return True  # let Android pause instead of destroying the app

    def on_stop(self):
        self._save_counter()


if __name__ == "__main__":
    WordCounterApp().run()

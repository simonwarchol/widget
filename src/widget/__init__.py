import importlib.metadata
import pathlib

import anywidget
import traitlets

try:
    __version__ = importlib.metadata.version("widget")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"


main_data = {
    "table": [
        {"a": "A", "b": 28},
        {"a": "B", "b": 55},
        {"a": "C", "b": 43},
        {"a": "D", "b": 91},
        {"a": "E", "b": 81},
        {"a": "F", "b": 53},
        {"a": "G", "b": 19},
        {"a": "H", "b": 87},
        {"a": "I", "b": 52},
    ]
}


class Widget(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "Widget.js"
    _css = pathlib.Path(__file__).parent / "static" / "Widget.css"

    data = traitlets.Dict(main_data).tag(sync=True)
    value = traitlets.Int(0).tag(sync=True)
    max_value = traitlets.Int(100).tag(sync=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.observe(self._on_value_changed, names="max_value")

    def _on_value_changed(self, change):
        print(f"Max Value changed tooo {change['new']}")
        try:
            parsed_max_int = int(change["new"])
        except ValueError:
            print("Error: Non-numeric value provided")
            return
        # Filter data by all values greater than title_int
        filtered_data = [x for x in main_data["table"] if x["b"] < parsed_max_int]

        filtered_data_table = {"table": filtered_data}
        self.set_state({"data": filtered_data_table})

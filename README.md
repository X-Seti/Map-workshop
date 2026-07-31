# Map Workshop

A PyQt6-based editor for GTA map data (IPL/IDE/DAT/IMG), built as a
standalone spin-off from [IMG Factory 1.6](https://github.com/X-Seti/Img-Factory-1.6).

Map Workshop started life as a fork of IMG Factory's Model Workshop
(itself originally derived from a DP5-style bitmap editor), progressively
stripped of paint-tool functionality and built out into a dedicated
GTA map/instance editor.

## Status

Active development / work in progress. Core editing panels (Object
Browser, Instance List, Editing Panel with IPL/IDE/DAT/IMG tabs,
Control Panel, World Viewport) are wired up and functional. Undo/redo
for mapping changes (instance placement, rotation, IPL edits) is not
yet implemented - it needs its own instance/IPL-state design rather
than reusing the old bitmap-canvas undo system.

## Structure

```
apps/
  components/
    Map_Editor/
      map_workshop.py           - main application
      map_workshop_old_version.py - reference copy, pre-refactor
      model_mesh_editor.py
      dockable_toolbar.py
      depends/                   - Map Editor-specific dependencies
    Model_Editor/depends/        - vendored COL classes (shared with Model Workshop)
    Col_Editor/depends/          - vendored COL core classes
  methods/                       - vendored shared utilities (icon factory,
                                    DFF/TXD parsing, viewport base class, etc.)
  debug/                         - vendored debug logging helpers
  gui/                           - vendored shared GUI mixins
  utils/                         - vendored app settings system
  themes/                        - UI theme JSON files
```

The `apps/methods`, `apps/debug`, `apps/gui`, `apps/utils`, and
`apps/components/Model_Editor` / `apps/components/Col_Editor`
directories are vendored copies of shared code from IMG Factory 1.6,
kept in sync manually rather than via a package dependency or
submodule. If you're pulling in updates from IMG Factory 1.6, check
whether any of these vendored files have changed upstream too.

## Running

Requires PyQt6. From the repo root:

```bash
pip install PyQt6 --break-system-packages
python3 -c "
import sys
from PyQt6.QtWidgets import QApplication
sys.path.insert(0, '.')
from apps.components.Map_Editor.map_workshop import MapWorkshop
app = QApplication(sys.argv)
w = MapWorkshop()
w.show()
app.exec()
"
```

## License

MIT - see [LICENSE](LICENSE).

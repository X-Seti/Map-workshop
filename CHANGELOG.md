# Changelog

All notable changes to `map_workshop.py` are tracked here. Version
numbers refer to the `#vers` marker in the file's own header comment,
which is bumped on every substantive change.

## v208-209 - Viewport consolidation and dock/ribbon architecture

- Consolidated the standalone "World View" dock into the single
  remaining Viewport dock - the Top/Side/3D map panes are now the
  Viewport dock's actual content, with an eye-icon "Show All Panes"
  toggle in the World ribbon to switch between single (3D only,
  "Full View") and all three panes.
- Parked the old `_create_world_viewport_dock` aside
  (`_create_world_viewport_dock_tmp`) rather than deleting it.
- Split ribbons back into their own nested `QMainWindow` (`_inner_mw`),
  separate from the dock-owning `_outer_mw`. An earlier attempt to
  unify ribbons and docks into one shared window broke Qt's dock/
  ribbon edge-snap drag preview entirely (confirmed not a Wayland
  compositor issue via `QT_QPA_PLATFORM=xcb` testing, and confirmed
  not caused by custom dock title bars since plain `QToolBar`s lost
  snapping too) - reverted back to the working separate-window
  architecture that the original `map_workshop_old_version.py` used.

## v205-207 - Viewport as a dock, not the central widget

- Made the viewport a proper `QDockWidget` instead of `outer_mw`'s
  fixed central widget, so it gets a movable header and can snap like
  every other pane. `outer_mw`'s real central widget became a
  trivial collapsed empty `QWidget`.
- Found the hidden Viewport dock could still leak through when
  dragging a nearby splitter (`setVisible(False)` alone wasn't
  enough - it still occupied a slot in the dock area's internal
  splitter chain). Fixed by fully detaching it via
  `removeDockWidget()` instead of just hiding it.

## v200-204 - Porting real features from the old version

- Ported ~101 methods from `map_workshop_old_version.py` in
  confirmed groups: 7 standalone classes (`MapSettings`,
  `MapSettingsDialog`, `_CornerOverlay`, `_InstanceEditPanel`,
  `_FilteredLoaderStub`, `_ObjectBrowserModel`, `_InstanceTableModel`),
  Object Browser, Instance List/Edit Panel, Control Panel, Editing
  Panel (IPL/IDE/DAT/IMG tabs), world viewport/LOD/ribbon framework,
  and shared icon-rendering utilities.
- Deliberately skipped ~95 DP5 paint-tool dead-code methods
  (dithering, brush/palette tools, canvas undo/redo, etc.) - not
  applicable to a map editor.
- Found and fixed a duplicate Ribbon Manager: a ported
  `_open_ribbon_manager` (with underscore) was unreachable, since the
  actually-working system is `open_ribbon_manager` (no underscore) +
  `RibbonManagerDialog`, already present in the Model Workshop base.
  Removed the duplicate and added a real "World" ribbon (LOD display
  mode, Cull Boxes toggle).
- Unified `_inner_mw` and `_outer_mw` into one `QMainWindow` for
  drag-anywhere ribbons/panes (later reverted - see above).
- Hid the Model Workshop-specific left docks (Files/Models/Frame
  Hierarchy/Textures) rather than removing them, since they're not
  applicable to map editing.
- Fixed two dock-visibility bugs: a safety-net in
  `_restore_outer_layout` was forcing hidden docks back visible on
  every startup; none of the dock widgets had
  `DockWidgetClosable` set, so Qt disabled their `toggleViewAction`
  entirely, making the right-click show/hide menu inert.

## Earlier

`map_workshop.py` started as a direct copy of Model Workshop
(`Model_Editor/model_workshop.py` v193), renamed throughout for Map
Workshop, with `map_workshop_old_version.py` kept as a reference for
which of the original DP5-fork's features were real map-editing
functionality worth porting forward versus DP5 paint-tool dead code.

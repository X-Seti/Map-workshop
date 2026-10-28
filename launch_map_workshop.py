#!/usr/bin/env python3
"""
X-Seti - December14 2025 - Map_Workshop 1.6 - Root Launcher
#this belongs in root /launch_map_workshop.py - Version: 5
"""
import sys
from pathlib import Path

# Get the root directory (where this launcher is located)
root_dir = Path(__file__).parent.resolve()

# Add root to path so we can import from apps/
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

# Now import and run txd_workshop from apps/components/Txd_Editor/
if __name__ == "__main__":
    try:
        print("Map_Workshop 1.6 Starting...")
        
        # Import the main module
        from apps.components.Map_Editor import map_workshop
        
        # If txd_workshop has a main() function, call it
        if hasattr(map_workshop, 'main'):
            sys.exit(map_workshop.main())
        else:
            # No main() function - run workshop directly
            from PyQt6.QtWidgets import QApplication
            
            app = QApplication(sys.argv)
            workshop = map_workshop.ModelWorkshop()   # Map Workshop class keeps its Model Workshop name
            workshop.setWindowTitle("Map Workshop - Standalone")
            workshop.resize(1200, 800)
            workshop.show()
            
            sys.exit(app.exec())
            
    except ImportError as e:
        print(f"ERROR: Failed to import map_workshop: {e}")
        print(f"Root directory: {root_dir}")
        print(f"Expected path: {root_dir}/apps/components/Map_Editor/map_workshop.py")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Failed to start map_workshop: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

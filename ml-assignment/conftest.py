import sys
from pathlib import Path

# Add ml-assignment directory to Python path
ml_assignment_dir = Path(__file__).parent
if str(ml_assignment_dir) not in sys.path:
    sys.path.insert(0, str(ml_assignment_dir))


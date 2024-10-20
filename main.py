import sys
import os

# Ensure the root directory is in the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.scheduler import run_scheduler

if __name__ == "__main__":
    run_scheduler()

"""
Package for the application.
"""

import signal
from app.views import ExitHandler
signal.signal(signal.SIGINT, ExitHandler)
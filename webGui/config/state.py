# state.py

# Holds references to user callback functions dynamically mapped to component IDs
EVENT_REGISTRY = {}

# Holds the live pywebview window instance once running
ACTIVE_WINDOW = None

_PENDING_JS = []
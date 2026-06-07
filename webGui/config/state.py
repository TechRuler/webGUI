# state.py

# Holds references to user callback functions dynamically mapped to component IDs
EVENT_REGISTRY = {}

# Holds the live pywebview window instance once running
ACTIVE_WINDOW = None

_PENDING_JS = []

_FUTURES = {}
_LAST_EVENT_TIME = {}
EVENT_HANDLERS = {}
EVENT_DATA = {}
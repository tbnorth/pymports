from thepkg import *

print(list(i for i in locals() if not i.startswith("_")))

# With __all__ in __init__.py you only get:
['parta', 'partb']

# Without __all__ in __init__.py you get:
['parta', 'thepkg', 'partb', 'fromB']


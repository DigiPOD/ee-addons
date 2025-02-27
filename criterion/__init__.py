import inspect

from .dexmed_patients import *
from .intraop_patients import *
from .noop import *
from .patients import *
from .postop_patients import *
from .preop_patients import *

__all__ = [
    name
    for name, obj in globals().items()
    if inspect.isclass(obj)
    and obj.__module__.startswith(__name__)
    and issubclass(obj, Criterion)
]

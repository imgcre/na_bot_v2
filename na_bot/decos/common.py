import inspect
from na_bot.utils.attr import ensure_attr
from na_bot.core.desc import *

def route(name):
    def wrapper(target):
        if inspect.isclass(target):
            config = ensure_attr(target, PluginDesc)
            config.name = name
        else:
            desc = ensure_attr(target, InstrDesc)
            desc.name = name
        return target
    return wrapper

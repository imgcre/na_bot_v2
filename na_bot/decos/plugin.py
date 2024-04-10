from na_bot.utils.attr import ensure_attr
from na_bot.core.desc import PluginDesc
from .common import *

def use_state():
    def wrapper(target):
        config = ensure_attr(target, PluginDesc)
        config.use_state = True
        return target
    return wrapper


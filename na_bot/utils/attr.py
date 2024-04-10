from typing import TypeVar, Type
import inflection

def ensure_attr[T](target, cls: Type[T]) -> T:
    attr_name = get_cls_attr_name(cls)
    return create_or_get_attr(target, attr_name, cls)

def guard_attr[T](target, cls: Type[T]) -> bool:
    attr_name = get_cls_attr_name(cls)
    return hasattr(target, attr_name)

def get_cls_attr_name(cls):
    return f'__{inflection.underscore(cls.__name__).upper()}__'

def create_or_get_attr(target, attr_name, factory):
    if not hasattr(target, attr_name):
        setattr(target, attr_name, factory())
    return getattr(target, attr_name)
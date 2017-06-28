# coding: utf-8

import imp
import sys
import time
import types
import inspect


def get_mod(module_name):
    """
    Get module
    :param module_name: the module name
    :return: the module
    """
    try:
        mod = sys.modules[module_name]
        if not isinstance(mod, types.ModuleType):
            raise KeyError
    except KeyError:
        # The last [''] is very important!
        mod = __import__(module_name, globals(), locals(), [''])
        sys.modules[module_name] = mod

    # reload taf_logging.py
    if sys.modules.has_key("framework.logging"):
        imp.reload(__import__("framework.taf_logging", globals(), locals(), ['']))

    return mod


def get_class(module_name, class_name, parent_class=None):
    """
    Get class from the module
    :param module_name: the module name
    :param class_name: the class name
    :param parent_class: the parent class
    :return: the reference to the class itself
    """
    _mod = get_mod(module_name)
    _cla = getattr(_mod, class_name)

    # assert that the class is a *callable* attribute.
    assert callable(_cla), u"%s is not callable." % class_name

    # assert that the class is a subclass of parentClass.
    if parent_class is not None:
        if not issubclass(_cla, class_name):
            raise TypeError(u"%s is not a subclass of %s" % (class_name, parent_class))

    # return a reference to the class itself, not an instantiated object.
    return _cla()


def apply_func(obj, function_name, args):
    """
    Apply specified function
    :param obj: the module or class
    :param function_name: the function name
    :param args: the function args
    :return: the function return result
    """
    _function = None
    _timeout = 100
    while _timeout > 0:
        try:
            _function = getattr(obj, function_name)
            break
        except:
            time.sleep(0.1)
            _timeout -= 1
    if _function is None:
        raise Exception("The function '%s' cannot be found." % function_name)

    _argsSpec = inspect.getargspec(_function)
    _argList = _argsSpec[0]
    _defaultValueList = _argsSpec[3]
    _targetArgs = []
    for i in range(len(_argList)):
        _arg = _argList[i]
        if _arg == "self":
            continue

        if args is None:
            continue

        j = len(args)
        for _key, _value in args.items():
            if _arg.lower() == _key.lower():
                _targetArgs.append(_value)
                break
            else:
                j -= 1
        if j == 0:
            if _defaultValueList is not None and i >= len(_argList) - len(_defaultValueList):
                n = len(_argList) - len(_defaultValueList)
                _targetArgs.append(_defaultValueList[i - n])
            else:
                raise Exception("The param '%s' cannot be found for function '%s'." % (_arg, function_name))
    return apply(_function, _targetArgs)


def execute_function(module_name, class_name, function_name, args):
    """
    Execute specified function
    :param module_name: the module (contains the function) name
    :param class_name: the class (contains the function) name
    :param function_name: the function name
    :param args: the function parameters
    :return: the return value
    """
    print "Executing underlying function execute_function with module_name=%s, class_name=%s, function_name=%s, " \
          "args=%s" % (module_name, class_name, function_name, args)

    if class_name is not None:
        _obj = get_class(module_name, class_name)
    else:
        _obj = get_mod(module_name)

    _return_value = apply_func(_obj, function_name, args)
    return _return_value

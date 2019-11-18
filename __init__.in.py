__docformat__ = "restructuredtext en"
__all__ = [
    "load_ipython_extension", "unload_ipython_extension",
    "error", "crystal", "physics", "misc", "tools", "ewald", "decorations",
    "periodic_table", "vasp", "process", "jobfolder", "logger", "espresso", "physics"]

from collections import namedtuple
version_info = namedtuple('version_info', ['major', 'minor'])\
    (int("@Pylada_VERSION_MAJOR@"), int("@Pylada_VERSION_MINOR@"))
""" Tuple containing version info. """
version = "{0[0]}.{0[1]}".format(version_info)
""" String containing version info. """


def __find_config_files(pattern="*.py", rcfile=False):
    """ Finds configuration files

        Looks for files with a given pattern in the following directory:

        - config subdirectory of the pylada package
        - directory pointed to by the "PYLADA_CONFIG_DIR" environment variable, if it exists
        - in "~/.pylada" if it exist and is a directory
    """
    from os.path import expandvars, expanduser
    from py.path import local
    from os import environ
    filenames = local(__file__).dirpath("config").listdir(fil=pattern, sort=True)
    if 'LADA_CONFIG_DIR' in environ:
        configdir = expandvars(expanduser(environ["LADA_CONFIG_DIR"]))
        filenames += local(configdir).listdir(fil=pattern, sort=True)
    pylada = local(expanduser("~/.pylada"))
    if pylada.isdir():
        filenames += pylada.listdir(fil=pattern, sort=True)
    elif rcfile and pylada.check(file=True):
        filenames += [pylada]
    return filenames


def __exec_config_files(pattern="*.py", rcfile=False, logger=None):
    """ Executes all config files with given pattern """
    global_dict = {"pyladamodules": __all__}
    local_dict = {}
    for filename in __find_config_files(pattern, rcfile):
        if logger != None:
            logger.debug("Reading configuration file %s" % filename)
        exec(compile(filename.read(), str(filename), 'exec'), global_dict, local_dict)

    return {k: v for k, v in local_dict.items() if k[0] != '_'}


def __setup_logger():
    """ Logger is set up before anything else is done """
    from os import environ
    import logging
    import sys
    local_dict = __exec_config_files("logging.py")
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                        stream=sys.stdout)
    logging_level = environ.get('LADA_LOGGING_LEVEL', local_dict['logging_level'])
    try:
        level = int(logging_level)
    except:
        pass
    else:
        logging_level = level
    root_logger = local_dict['root_logger']
    logger = logging.getLogger(root_logger)
    if hasattr(logging, 'upper'):
        logging.setLevel(logging_level.upper())
    else:
        logger.setLevel(logging_level)
    for filename in __find_config_files("logging.py"):
        logger.debug("Read configuration file %s" % filename)
    return logger

# import logger first, so we can print config files
logger = __setup_logger()

# does actual config call.
locals().update(__exec_config_files(rcfile=True, logger=logger))

# import submodules
from . import error, crystal, physics, misc, tools, ewald, decorations, periodic_table, vasp, \
    process, jobfolder, logger, espresso

# Add a function to easily run the tests
try:
    from pytest import mark
except ImportError:
    pass
else:
    # recursion
    @mark.skipif(True, "Helper function to aggregate tests")
    def test(**kwargs):
        
        from os.path import dirname
        from pytest import main
        return main(dirname(__file__), **kwargs)


# Make this an IPython module
from .ipython import load_ipython_extension, unload_ipython_extension

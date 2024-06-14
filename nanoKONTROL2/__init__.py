import Live
from .nanoKONTROL2 import nanoKONTROL2


def create_instance(c_instance):
    """ Creates and returns the APC20 script """
    return nanoKONTROL2(c_instance)

# local variables:
# tab-width: 4

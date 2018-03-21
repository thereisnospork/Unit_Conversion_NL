import re
import numpy as np
from .models import unitOfMeasure


def input_units(input):
    """returns 2 unit list/tuple where [0] = number as np.float64 and [1] =
    unit abreviation -OR- name as string

    some sample inputs: '100 meters'  or '100 m' or 100m """
    striped = input.strip()
    numbers = re.search('[0-9,\.,\,]*',striped).group(0) ##works! inc comma and decimal support
    numbers = np.float64(numbers)

    letters = re.search('[a-zA-Z,\/]{1,99}',striped).group(0)
    # if len(letters)>3:
    #     letters = letters.rstrip('s') #dealing with plurals.  double check for other plural or names that end in 's'
    return [numbers, letters]

def find_unit(unit_string):
    """Looks up string in unit of Measure,
    returns Queryset of unit matching abbrev. or name"""
    try:
        unit_string = unitOfMeasure.objects.get(name__iexact = unit_string)  # iexact for name exact for abbrevs
    except Exception:
        try:
            unit_string = unitOfMeasure.objects.get(name__iexact = unit_string.rstrip('s'))
        except Exception:
            try:
                unit_string = unitOfMeasure.objects.get(abbrev__iexact=unit_string)  # iexact for name exact for abbrevs
            except Exception:
                try:
                    unit_string = unitOfMeasure.objects.get(abbrev__iexact=unit_string.rstrip('s'))
                except Exception:
                    return None

    return unit_string


def input_conversion_target(input):
    # input=input.strip().rstrip('s')
    return input

#
# a = input_units('1000KJoule/s')
#
# print(a)
#
# b = input_conversion_target('  meters ')
# print(b)
b = find_unit('meter')
print(b)
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UnitForm
from .convert_method import input_units, find_unit, input_conversion_target
from .models import unitOfMeasure, prefix
from django.views import generic


class ListUnits(generic.ListView):
    model = unitOfMeasure
    template_name = 'units.html'


def index(request, convert_f='', convert_t=''):
    """Takes two input fields, splits the first into numerals and text via input_units()
    Second should consist of text only.  the two text fields are searched in the units db
    for exact matching unit (with and w/out plural 's' !!Feet/foot remains an edge case!!
    conversion factors are x-referenced to db entry and unit conversion is calculated
    and output via index.html

    to do: add abbreviation support chk
    add support for multiple abbreviations/duplicate entries for edge cases (feet/foot)
    add page for list of all units
            done, mess with ordering/grouping later
                add link to home page
    add more units!
    debug etc...
    add is_valid to POST form requests

    """

    form = UnitForm(request.POST or None) ###None needed to remove this field required message or use if/else paradigm
    convert_t = form['convert_from'].value()
    try:
        in_num, in_unit = input_units(convert_t)
    except Exception:
        return render(request, 'index.html',{'form': form})  # return empty render request

    # try:
    #     in_db_entry = unitOfMeasure.objects.get(name__iexact = in_unit)  # iexact for name exact for abbrevs
    # except Exception:
    #     try:
    #         in_db_entry = unitOfMeasure.objects.get(name__iexact = in_unit.rstrip('s'))
    #     except Exception:
    #         try:
    #             in_db_entry = unitOfMeasure.objects.get(name__iexact = in_unit.rstrip('e'))
    #         except Exception:
    #             return render(request, 'index.html',{'form': form, 'error': 'input unit not found in db'})  # return empty render request

    in_db_entry = find_unit(in_unit)

    if not in_db_entry:  #bail if find unit not found
           return render(request, 'index.html',{'form': form, 'error': 'input unit not found in db'})  # return empty render request

    in_factor = in_db_entry.val  ####these are the 'exchange rate, cat, name.
    in_name = in_db_entry.name   ##logic later for compatible cat, math the factors
    in_cat = in_db_entry.cat
    # in_ab

    out_unit = form['convert_to'].value()
    out_db_entry = find_unit(out_unit)

    if not out_db_entry:#bail if find unit not found
        return render(request, 'index.html', {'form': form,'error':'output unit not found in db'})  # return empty render request

    out_factor = out_db_entry.val
    out_name = out_db_entry.name
    out_cat = out_db_entry.cat

    try:
        if in_cat == out_cat:
            out_num = in_num*in_factor/out_factor

        return render(request, 'index.html',{'form':form,'in_val':in_num, 'out_val':out_num,
                                         'in_name':in_name,'out_name':out_name
                                         })# 'in_unit': in_unit, 'in_val':in_number})
    except Exception:
        return render(request, 'index.html', {'form': form, 'error': 'you are trying to convert incompatible units'})  # return empty render request

    # print(type(out_factor))
    # if in_cat == out_cat:
    #     out_value =






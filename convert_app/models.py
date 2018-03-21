from django.db import models
import networkx as nx
# Create your models here.

# G = nx.Graph()


class unitOfMeasure(models.Model):
    """A class which defines the meaningful properties of a unit of measure,
    eg. meter, or degree celsius value is relative to metric standard """
    name = models.CharField('name of unit', max_length = 100)
    abbrev = models.CharField('abbreviation of unit',max_length = 10, blank = True)
    cat = models.CharField('unit category', max_length = 100)
    val = models.FloatField('value of unit relative to metric standard')
    # def __init__(self,name, abbrev, cat, val):
    #     self.name = name
    #     self.abbrev = abbrev
    #     self.cat = cat
    #     self.val = val


class prefix(models.Model):
    """A class which defines the relative multiplicative
    values of prefixes eg. centi or cm"""
    name = models.CharField('name of prefix',max_length = 100)
    abbrev = models.CharField('abbreviation of prefix',max_length = 10)
    val = models.FloatField('value of prefix')


    # def __init__(self, name, abbrev, val):
    #     self.name = name
    #     self.abbrev = abbrev
    #     self.val = val


#
#
# meter = unitOfMeasure('meter','m','length', 1.)
# foot = unitOfMeasure('foot','ft','length',.3048)
# centimeter = unitOfMeasure('centimeter','cm','length', .01)
# decimeter = unitOfMeasure('centimeter','cm','length', .1)
#
# G.add_node(meter)
# G.add_node(foot)
# G.add_node(centimeter)



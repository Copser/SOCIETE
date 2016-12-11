# utils/choices.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

# Personal Informations
FIVE_BOROUGH = (
    ('manhattan', _('Manhattan')),
    ('brooklyn', _('Brooklyn')),
    ('queens', _('Queens')),
    ('bronx', _('Bronx')),
    ('Staten Island', _('Staten Island')),
)

# Experience Information
SKILL_CHOICE_TYPE = (
    ('carpenter', _('Carpenter')),
    ('housekeep', _('Housekeep')),
    ('plumbing', _('Plumbing')),
    ('electrical', _('Electrical')),
    ('construction', _('Construction')),
    ('hvac', _('HVAC')),
)

TRAINING_CHOICE_FIELD = (
    ('self taught', _('Self Taught')),
    ('vocational school', _('Vacational School')),
    ('apprenticeship', _('Apprenticeship')),
    ('other', _('Other')),
)

EXPERIENCE_CHOICE_TYPE = (
    ('less then one year', _('Less then one year')),
    ('one year', _('One Year')),
    ('one year +', _('One Year +')),
    ('two years', _('Two Years')),
    ('three years', _('Three Years')),
    ('four years', _('Four Yers')),
    ('five yers +', _('Five Years +'))
)

TRAINING_CHOICE_FIELD = (
    ('self taught', _('Self Taught')),
    ('vocational school', _('Vacational School')),
    ('apprenticeship', _('Apprenticeship')),
    ('other', _('Other')),
)

# Other Iformation
WORK_HOURS_CHOICE_FIELD = (
    ('10+', _('10+')),
    ('20+', _('20+')),
    ('30+', _('30+')),
    ('40+', _('40+')),
)

WORK_PERMIT_CHOICE_FIELD = (
    ('yes', _('Yes')),
    ('no', _('No')),
)

DRIVERS_LICENSE_CHOICE_FIELD = (
    ('a', _('A')),
    ('b', _('B')),
    ('c', _('C')),
    ('d', _('D')),
    ('e', _('E')),
    ('m', _('M')),
)

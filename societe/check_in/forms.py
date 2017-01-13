# check_in/forms.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _,\
        ugettext
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap
from crispy_forms.bootstrap import InlineField

from check_in.models import InitialCharacteristicModel


class InitialCharacteristicForm(forms.ModelForm):
    """TODO: Custom form for InitialCharacteristicModel,
    I'm using django crispy_forms to utilaze and customize it
    return: TODO
    """
    def __init__(self, *args, **kwargs):
        super(InitialCharacteristicForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.method = "POST"
        self.helper.form_action = ""

        self.helper.layout = layout.Layout(
            layout.Fieldset(
                _("Personal Information"),
                layout.Field(
                    "first_name",
                    css_class="input-block-level",
                    placeholder="First Name"
                ),
                layout.Field(
                    "last_name",
                    css_class="input-block-level",
                    placeholder="Last Name",
                ),
                layout.Field(
                    bootstrap.PrependedText("email", "@",
                                          css_class="input-block-level",
                                          placeholder="youremail@example.com"),
                ),
                layout.Field(
                    "country",
                ),
                layout.Field(
                    "move_in_date",
                    css_class="input-block-level",
                    placeholder="Move in date",
                ),
                layout.Field(
                    "move_out_date",
                    css_class="input-block-level",
                    placeholder="Move out date",
                ),
                layout.Field(
                    "message",
                    placeholder="Message",
                ),
                bootstrap.FormActions(
                    layout.Submit("submit", _("Submit")),
                )
            )
        )

    class Meta:
        model = InitialCharacteristicModel
        fields=[ "first_name", "last_name", "email", "country",
                "move_in_date", "move_out_date", "message"]


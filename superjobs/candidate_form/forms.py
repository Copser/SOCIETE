# candidate_form/forms.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _,\
        ugettext

from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap

from candidate_form.models import CandindateFormModel


class CandidateForm(forms.ModelForm):
    """TODO: Deffine model form for CandindateFormModel,
    I'm attaching a form helper to the form in the
    initialization method itself
    return: TODO
    """
    class Meta:
        model = CandindateFormModel
        fields = ["first_name", "last_name", "email", "mobile_phone_number",
                  "city", "street_address", "candidate_skill", "candidate_experience",
                  "candidate_hospitality_experience", "candidate_training", "reference_letter",
                  "work_hours", "payed_per_hour", "valid_work_permit", "drivers_license", "upload_cv"]

        def __init__(self, *args, **kwargs):
            super(CandindateForm, self).__init__(*args, **kwargs)

            self.helper = FormHelper()
            self.helper.form_action = ""
            self.helper.form_method = "POST"

            self.fields["city"].widget = \
                forms.RadioSelect()
            # delete empty choice for the type
            del self.fields["city"].choices[0]

            self.helper.layout = layout.Layout(
                layout.Fieldset(
                    _("Personal Information"),
                    layout.Field(
                        "first_name",
                        css_class="input-block-level"
                    ),
                    layout.Field(
                        "last_name",
                        css_class="input-block-level"
                    ),
                    layout.Field(
                        bootstrap.PrependedText("email", "@",
                                                css_class="input-block-level",
                                                placeholder="youremail@example.com"),
                    ),
                    layout.Div(
                        bootstrap.PrependedText("mobile_phone_number",
                                                """<span class="glyphicon glyphicon-earphone">
                                                </span>""",
                                                css_class="input-block-level"),
                        bootstrap.PrependedText("confirm_mobile_phone_number",
                                                """<span class="glyphicon glyphicon-earphone">
                                                </span>""",
                                                css_class="input-block-level"),
                    ),
                    layout.Field(
                        "city"
                    ),
                    layout.Field(
                        "street_address",
                        css_class="input-block-level"
                    ),
                ),
                layout.Fieldset(
                    _("Experience Informaition"),
                    layout.Field(
                        "candidate_skill"
                    ),
                    layout.Field(
                        "candidate_experience"
                    ),
                    layout.Field(
                        "candidate_hospitality_experience"
                    ),
                    layout.Field(
                        "candidate_training"
                    ),
                    layout.Field(
                        "reference_letter"
                    ),
                    layout.HTML(
                        u"""{% load i18n %}
                        <p class="help-block">{% trans
                        "Avaliable formats are PDF, docx.
                        Minimal size is 25mb." %}</p>
                    """),
                    title=_(
                        "Upload Reference Letter"
                    ),
                    css_id="reference_letter_fieldset",
                ),
                layout.Fieldset(
                    _("Other Informations"),
                    layout.Field(
                        "work_hours"
                    ),
                    layout.Field(
                        "payed_per_hour",
                        css_class="input-block-level"
                    ),
                    layout.Field(
                        "valid_work_permit"
                    ),
                    layout.Field(
                        "drivers_license"
                    ),
                    layout.Field(
                        "upload_cv"
                    ),
                    layout.HTML(
                        u"""{% load i18n %}
                        <p class="help-block">
                        {% trans "Avaliable formats are PDF and docx.Minimal size is 25 mb." %}</p>
                        """,
                    ),
                    title=_(
                        "Upload CV"
                    ),
                    css_id="upload_cv_fieldset",
                ),
                bootstrap.FormActions(
                    layou.Submit("submit", _("Submit")),
                )
            )

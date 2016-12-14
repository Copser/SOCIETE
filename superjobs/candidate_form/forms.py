# candidate_form/forms.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _,\
        ugettext

from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap
from crispy_forms.bootstrap import InlineField

from candidate_form.models import CandindateFormModel


class CandidateForm(forms.ModelForm):
    """TODO: Deffine model form for CandindateFormModel,
    I'm attaching a form helper to the form in the
    initialization method itself
    return: TODO
    """
    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "POST"
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
                    placeholder="Last Name"
                ),
                layout.Field(
                    bootstrap.PrependedText("email", "@",
                                            css_class="input-block-level",
                                            placeholder="youremail@example.com"),
                ),
                layout.Div(
                    bootstrap.PrependedText("mobile_phone",
                                            """<span class="glyphicon glyphicon-earphone">
                                            </span>""",
                                            css_class="input-block-level",
                                            placeholder="Mobile Phone Number"),
                    bootstrap.PrependedText("confirm_mobile_phone",
                                            """<span class="glyphicon glyphicon-earphone">
                                            </span>""",
                                            css_class="input-block-level",
                                            placeholder="Confirm Mobile Phone Number"),
                ),
                layout.Field(
                    "city",
                ),
                layout.HTML(
                    u"""{% load i18n %}
                    <p class="help-block">
                    {% trans "Where do you live in New York? Thank you." %}</p>
                    """,
                ),
                layout.Field(
                    "street_address",
                    css_class="input-block-level",
                    placeholder="You're Street Address"
                ),
            ),
            layout.Fieldset(
                _("Experience Informaition"),
                layout.Field(
                    "candidate_skill"
                ),
                layout.HTML(
                    u"""{% load i18n %}
                    <p class="help-block">
                    {% trans "Please apply for just one profile we have listed for you. Thank you." %}</p>
                    """,
                ),
                layout.Field(
                    "candidate_experience"
                ),
                layout.HTML(
                    u"""{% load i18n %}
                    <p class="help-block">
                    {% trans "How much real experience do you have?." %}</p>
                    """,
                ),
                layout.Field(
                    "candidate_hospitality_experience"
                ),
                layout.HTML(
                    u"""{% load i18n %}
                    <p class="help-block">
                    {% trans "How much real Hospitality Experience do you have?" %}</p>
                    """,
                ),
                layout.Field(
                    "candidate_training"
                ),
                layout.HTML(
                    u"""{% load i18n %}
                    <p class="help-block">
                    {% trans "Where did you get you're training from, plese select only one field" %}</p>
                    """,
                ),
            ),
            layout.Fieldset(
                _("Other Informations"),
                layout.Field(
                    "work_hours"
                ),
                layout.HTML(
                    u"""{% load i18n %}
                    <p class="help-block">
                    {% trans "How much time are you planing to spend on the job?" %}</p>
                    """,
                ),
                layout.Field(
                    "payed_per_hour",
                    css_class="input-block-level"
                ),
                layout.HTML(
                    u"""{% load i18n %}
                    <p class="help-block">
                    {% trans "What would be you're wanted wage?"  %}</p>
                    """,
                ),
                layout.Field(
                    "valid_work_permit"
                ),
                layout.HTML(
                    u"""{% load i18n %}
                    <p class="help-block">
                    {% trans "Do you have a Valid Work Permit?" %}</p>
                    """,
                ),
                layout.Field(
                    "drivers_license"
                ),
                layout.HTML(
                    u"""{% load i18n %}
                    <p class="help-block">
                    {% trans "What kind a drivers licence do you possess?" %}</p>
                    """,
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
                layout.Submit("submit", _("Submit")),
            )
        )

    class Meta:
        model = CandindateFormModel
        fields = ["first_name", "last_name", "email", "mobile_phone", "confirm_mobile_phone",
                  "city", "street_address", "candidate_skill", "candidate_experience",
                  "candidate_hospitality_experience", "candidate_training", "work_hours",
                  "payed_per_hour", "valid_work_permit", "drivers_license", "upload_cv"]

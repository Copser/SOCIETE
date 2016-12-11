# utils/fields/py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils.translation import get_language
from django.utils.translation import string_concat


class MultilingualCharField(models.CharField):
    """TODO: Implementing simple multilingual content into
    are model.
    return: TODO
    """
    def __init__(self, verbose_name=None, **kwargs):
        self._blank = kwargs.get("blank", False)
        self._editable = kwargs.get("editable", True)

        super(MultilingualCharField, self).\
                __init__(verbose_name, **kwargs)

    def contribute_to_class(self, cls, name, virtual_only=False):
        # generate language specific fields dynamically
        if not cls._meta.abstract:
            if not cls._meta.abstract:
                for lang_code, lang_name in settings.LANGUAGES:
                    if lang_code == settings.LANGUAGE_CODE:
                        _blank = self._blank
                    else:
                        _blank = True

                    localized_field = models.CharField(
                        string_concat(self.verbose_name,
                                      " (%s)" % lang_code),
                        name=self.name,
                        primary_key=self.primary_key,
                        max_length=self.max_length,
                        unique=self.unique,
                        blank=_blank,
                        null=False,
                        # we ignore the null argument!
                        db_index=self.db_index,
                        rel=self.rel,
                        default=self.default or "",
                        editable=self._editable,
                        serialize=self.serialize,
                        choices=self.choices,
                        help_text=self.help_text,
                        db_column=None,
                        db_tablespace=self.db_tablespace
                    )
                    localized_field.contribute_to_class(
                        cls,
                        "%s_%s" % (name, lang_code),
                    )

    def tranlated_value(self):
        language = get_language()
        val = self.__dict__["%s_%s" % (name, language)]
        if not val:
            val = self.__dict__["%s_%s" %\
                                (name, settings.LANGUAGE_CODE)]
            return val
        setattr(cls, name, property(tranlated_value))



class MultilingualTextField(models.TextField):
    """TODO: Implementing simple multilingual content into
    are model, add an analogous multilingual text field.
    return: TODO
    """
    def __init__(self, verbose_name=None, **kwargs):
        self._blank = kwargs.get("blank", False)
        self._editable = kwargs.get("_editable", True)

        super(MultilingualTextField, self).\
                __init__(verbose_name, **kwargs)

    def contribute_to_class(self, cls, name,
                            virtual_only=False):
        # generate language specific fields dynamically
        if not cls._meta.abstract:
            if not cls._meta.abstract:
                for lang_code, lang_name in settings.LANGUAGES:
                    if lang_code == settings.LANGUAGE_CODE:
                        _blank = self._blank
                    else:
                        _blank = True

                    localized_field = models.TextField(
                        string_concat(self.verbose_name,
                                      " (%s)" % lang_code),
                        name=self.name,
                        primary_key=self.primary_key,
                        max_length=self.max_length,
                        unique=self.unique,
                        blank=_blank,
                        null=False,
                        # we ignore the null argument!
                        db_index=self.db_index,
                        rel=self.rel,
                        default=self.default or "",
                        editable=self._editable,
                        serialize=self.serialize,
                        choices=self.choices,
                        help_text=self.help_text,
                        db_column=None,
                        db_tablespace=self.db_tablespace
                    )
                    localized_field.contribute_to_class(
                        cls,
                        "%s_%s" % (name, lang_code),
                    )

    def tranlated_value(self):
        language = get_language()
        val = self.__dict__["%s_%s" % (name, language)]
        if not val:
            val = self.__dict__["%s_%s" %\
                                (name, settings.LANGUAGE_CODE)]
            return val
        setattr(cls, name, property(tranlated_value))

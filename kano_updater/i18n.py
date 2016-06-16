# i18n.py
#
# Copyright (C) 2016 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# I18n helpers for the updater

def to_unicode(string):
    if type(string).__name__ == "str":
        return string.decode('utf-8')
    return string


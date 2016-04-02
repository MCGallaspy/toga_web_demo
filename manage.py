#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_demo.settings")
    os.environ.setdefault("TOGA_PLATFORM", "django.toga_config")  # FIXME: "toga" is prepended to the module name, which makes this a little odd.

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

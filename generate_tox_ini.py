# Copyright 2010-2012 Canonical Ltd.  This software is licensed under
# the GNU Lesser General Public License version 3 (see the file LICENSE).

# This file generates tox.ini file based on the list of things in the settings
# section bellow

### settings

python_versions = ["2.6", "2.7"]
django_versions = ["1.1.4", "1.2.7", "1.3.1", "1.4-alpha-1"]

additional_deps = ["mock"]

custom_django_versions = {
    "1.4-alpha-1": "http://www.djangoproject.com/download/1.4-alpha-1/tarball/"
}

### End of settings

tox_ini = [
    "[testenv]",
    "commands = python setup.py test",
    ]

envlist = []

for python_version in python_versions:
    for django_version in django_versions:
        envname = "py{0}-django{1}".format(python_version, django_version)
        envlist.append(envname)
        tox_ini.append("[testenv:{0}]".format(envname))
        tox_ini.append("basepython = python{0}".format(python_version))

        if django_version in custom_django_versions:
            django_dep = custom_django_versions[django_version]
        else:
            django_dep = "Django=={0}".format(django_version)

        depslist = "\n    ".join([django_dep] + additional_deps)
        tox_ini.append("deps = {0}".format(depslist))

tox_ini.insert(0, "[tox]")
tox_ini.insert(1, "envlist = {0}".format(", ".join(envlist)))

open("tox.ini", "w").write("\n".join(tox_ini))

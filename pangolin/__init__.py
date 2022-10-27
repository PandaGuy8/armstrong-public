#!/usr/bin/env python3
import os
import re
import sys
import subprocess

from blessings import Terminal
from collections import namedtuple


Outputs = namedtuple('Outputs', ['exit_status', 'stdout', 'stderr'])


class Executable:
    def __init__(self, filename):
        self.filename = filename

        if not self._is_executable(filename):
            raise ValueError("Program %s is not executable!" % filename)

    def run(self, *args, stdin=None):
        p = subprocess.Popen([self.filename, *[str(a) for a in args]],
                             stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             stderr=subprocess.STDOUT)

        stdout, stderr = p.communicate(input=stdin)

        return Outputs(p.returncode, GreppableString(stdout), GreppableString(stderr))

    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)

    @staticmethod
    def _is_executable(filename):
        return os.path.isfile(filename) and os.access(filename, os.X_OK)


class GreppableString(str):
    def grep(self, pattern):
        return re.findall(pattern, self)


class Test:
    def __init__(self):
        self.t = Terminal()
        self.tests = 0
        self.errors = 0
        for i, test in enumerate(self.collect()):
            if test.__doc__:
                print(self.t.bold(test.__doc__))
            test()
            print("")

        if self.errors == 0:
            print(f"Éxecuté {self.tests} tests avec succès\n\nOK")
            sys.exit(0)
        else:
            s = "s" if self.errors > 1 else ""
            print(
                f"Éxecuté {self.tests - self.errors} sur {self.tests} tests avec succès, {self.errors} erreur{s}\n\nFAIL")
            sys.exit(1)

    def collect(self):
        return [getattr(self, method) for method in dir(self) if method.startswith('test_')]

    def test(self, message, assertion, error_message=None):
        print(f"{self.tests}. {message}...", end='', flush=True)
        if assertion:
            print(self.t.green(" ok"), flush=True)
        else:
            self.errors += 1
            print(self.t.red(" erreur"), flush=True)
            if error_message:
                print(self.t.red("   " + error_message))
        self.tests += 1

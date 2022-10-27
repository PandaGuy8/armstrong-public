#!/usr/bin/env python3
import random

from pangolin import Executable, Test
from itertools import permutations
from ctypes import cdll, c_bool

Armstrong = Executable('./armstrong')


def is_armstrong(n):
    return sum([int(i)**len(str(n)) for i in str(n)]) == n


def get_armstrong_number():
    n = random.choice([
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        153, 370, 371, 407, 1634, 8208, 9474,
        54748, 92727, 93084, 548834, 1741725, 4210818,
        9800817, 9926315, 24678050, 24678051, 88593477,
        146511208, 472335975, 534494836, 912985153])
    assert(is_armstrong(n))
    return n


def get_not_armstrong_number():
    n = random.randint(10, 2**31 - 1)
    if is_armstrong(n):
        return get_not_armstrong_number()
    return n


class TestArmstrong(Test):

    def test_basic(self):
        "Test des valeurs de base"

        for args, exit_status in {33: True, 153: False, 154: True, -10: True}.items():
            out = Armstrong(args).exit_status
            self.test(f"Valeur {args}",  out == exit_status)

        for i in range(10):
            self.test(f"Valeur {i}", Armstrong(i).exit_status == 0)

    def test_random_not_armstrong(self):
        "Test aléatoire pour des nombres non narcissiques"

        for n in [get_not_armstrong_number() for i in range(10)]:
            out = Armstrong(n).exit_status
            self.test(f"Valeur {n} n'est pas un nombre d'Armstrong", out == int(not is_armstrong(n)))

    def test_random_armstrong(self):
        "Test aléatoire pour des nombres narcissiques"

        for n in [get_armstrong_number() for i in range(10)]:
            out = Armstrong(n).exit_status
            self.test(f"Valeur {n} est un nombre d'Armstrong", out == int(not is_armstrong(n)))

    def test_version(self):
        "Test de l'option --version"

        num = random.randint(10, 100000)

        for args in list(permutations(['--version', '--verbose', str(num)], 3)):
            self.test(f"armstrong {' '.join(args)}", Armstrong(
                *args).stdout.grep('(?i)version'))

        self.test("Présence d'email", Armstrong(
            '--version').stdout.grep('<.*?@.*?>'))

    def test_verbose(self):
        "Test de l'option --verbose"

        n = 564
        self.test(f"Valeur {n} sur stdout avec --verbose",  len(
            Armstrong('--verbose', n).stdout.grep(r'\b%d\b' % n)))

        self.test(f"Valeur {n} sur stdout avec -v",  len(
            Armstrong('-v', n).stdout.grep(r'\b%d\b' % n)))

        for n in [get_armstrong_number() for i in range(3)]:
            self.test(f"Valeur {n}", Armstrong('--verbose', n).stdout.grep("est un|is an?"))

        for n in [get_not_armstrong_number() for i in range(3)]:
            self.test(f"Valeur {n}", Armstrong('--verbose', n).stdout.grep("n'est pas un|is not an?"))

    def test_stdin(self):
        "Test avec stdin"

        self.test("cat 153 | armstrong", Armstrong(stdin=b'153').exit_status == 0)
        self.test("cat 154 | armstrong", Armstrong(stdin=b'154').exit_status == 1)
        self.test("cat 9 | armstrong", Armstrong('--verbose', stdin=b'9').exit_status == 0)

    def test_incoherent(self):
        "Test d'incohérences"

        self.test("./armstrong foo", Armstrong('foo').exit_status == 2)
        self.test("cat foo | ./armstrong", Armstrong(stdin=b'foo').exit_status == 2)
        self.test("./armstrong foo bar", Armstrong('foo').exit_status == 2)

    def test_unit(self):
        "Unit tests"

        armstrong = cdll.LoadLibrary('./libarmstrong.so')

        valid = True
        try:
            armstrong.is_armstrong.restype = c_bool
        except AttributeError:
            valid = False

        self.test("Fonction is_armstrong présente", valid)

        for n in [get_armstrong_number() for i in range(5)]:
            self.test(f"assert(is_armstrong({n}))", valid and armstrong.is_armstrong(n))
        for n in [get_not_armstrong_number() for i in range(5)]:
            self.test(f"assert(!is_armstrong({n}))", valid and not armstrong.is_armstrong(n))

TestArmstrong()

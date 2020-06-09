#!/usr/bin/env python

import unittest
import bash_python_caller as ph
import re


class TestPythonHelper(unittest.TestCase):
    def test_helper_should_reject_calls_if_wrong_number_of_arguments_used(self):
        # not expecting any arguments
        def f():
            pass

        # pass in an argument that isnt expected
        self.assertRaises(Exception, ph.main, ["programName", "arg1"], f)


    def test_helper_should_reject_calls_if_not_enough_arguments_used(self):
        # not expecting any arguments
        def f(x, y, z):
            pass

        # pass in too many arguments for the function
        self.assertRaises(Exception, ph.main, ["programName", "arg1"], f)


    def test_helper_should_work_if_no_args_are_required(self):
        # not expecting any arguments
        def f():
            return ["no args required"]

        expected = ["no args required"]

        # pass in an argument that isnt expected
        actual = ph.main(["programName"], f)

        self.assertEqual(expected, actual)


    def test_helper_fail_if_more_than_max_arguments_provided(self):
        def f(a, b, c, d, e, f, g, h, i, j, k, l):
            pass

        self.assertRaises(Exception, ph.main, list(range(0, 13)), f)


    def test_main_helper_only_accepts_lists_from_functions(self):
        def f():
            return []

        actual = ph.main(["programName"], f)
        self.assertIsInstance(actual, list, msg="all functions should return a list, but got {}".format(type(actual)))


    def test_main_helper_should_throw_exception_if_func_doesnt_return_a_list(self):
        def f():
            return 10

        self.assertRaises(Exception, ph.main, ["programName"], f)  


    def test_if_the_only_argument_is_a_question_mark_should_print_pydoc(self):
        def f():
            """this is the documentation
            it spans multiple lines"""
            pass

        expected = ["this is the documentation it spans multiple lines"]
        actual = ph.main(["programName", "?"], f)

        actual_trimmed = [" ".join(actual[0].split())]

        self.assertEqual(expected, actual_trimmed)


    def test_if_no_py_doc_is_provided_print_helpful_message(self):
        def f():
            pass

        expected = ["warning: function contains no documentation"]
        actual = ph.main(["programName", "?"], f)

        self.assertEqual(expected, actual)

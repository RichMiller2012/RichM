from tests.plugins.ReqTracer import requirements
from unittest import TestCase
from question_answer_wrapper import question_answer_wrapper
from useful_question import *
import time

class QALogTests(TestCase):

    @requirements(['#0050','#0051','#0052'])
    def test_output_question(self):
        ask = "What type of triangle is 9 9 9 ?"
        ms = question_answer_wrapper(ask)
        self.assertLess(ms, 50)
        
        """ check log """
        QA_log = open("QA_log", "r")
        logged = QA_log.readline()
        self.assertTrue(ask in logged)
        self.assertTrue('equilateral' in logged)

    @requirements(['#0053'])
    def test_load_test_system_pi(self):
        total_ms = 0;
        ask = "What is the nth prime number"
        for i in range(1,5000):
            ms = question_answer_wrapper(ask + " " + str(10) + " ?")
            total_ms += ms

        self.assertLess(total_ms, 10000)

    @requirements(['#0054'])
    def test_spike_test_system_pi(self):
        total_ms = 0;
        ask = "What is the nth prime number"
        start = time.clock()
        ms = question_answer_wrapper(ask + " " + str(10) + " ?")
        if start * 1000 > 1:
            for i in range(1,500):
                ms = question_answer_wrapper(ask + " " + str(10) + " ?")
                total_ms += ms

       
        
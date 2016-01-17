from source.main import Interface
from tests.plugins.ReqTracer import requirements
from unittest import TestCase

NOT_A_QUESTION_RETURN = "Was that a question?"
UNKNOWN_QUESTION = "I don't know, please provide the answer"
NO_QUESTION = 'Please ask a question first'
NO_TEACH = 'I don\'t know about that. I was taught differently'
NOT_A_STRING = 'Not A String!'

class QATest(TestCase):


    @requirements(['#0006', '#0008'])
    def test_ask_takes_string_and_answers_valid_string(self):
        interface = Interface()
        result = interface.ask("How are you?")
        self.assertIsNotNone(result)
        self.assertEqual(result, UNKNOWN_QUESTION)

    @requirements(['#0007'])
    def test_ask_accepts_valid_keyword_What(self):
        interface = Interface()
        result = interface.ask("What is up?")
        self.assertEqual(result, UNKNOWN_QUESTION)


    @requirements(['#0009'])
    def test_ask_accepts_no_question_mark(self):
        interface = Interface()
        result = interface.ask('Go away')
        self.assertEqual(result, NOT_A_QUESTION_RETURN)

    @requirements(['#0010'])
    def test_ask_breaks_down_words(self):
        interface = Interface()
        result = interface.ask('one two three')

    @requirements(['#0011'])
    def test_ask_checks_90_percent_match(self):
        interface = Interface()
        result = interface.ask('What type of triangle is?')
        self.assertEqual(result, "NP")
        
    



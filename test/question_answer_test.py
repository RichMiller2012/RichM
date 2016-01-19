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
    def test_ask_breaks_down_words_by_space(self):
        interface = Interface()
        result = interface.ask('Who What     Why?')
        self.assertEqual(interface.last_question, "Who What Why")

    @requirements(['#0011','#0013'])
    def test_ask_checks_90_percent_match(self):
        interface = Interface()
        result = interface.ask('What type of angle is 9.2 9.2 9.2 ?')
        self.assertEquals(result, "equilateral")
    
    @requirements(['#0011', '#0012'])
    def test_ask_check_less_90_percent_match(self):
        interface = Interface()
        result = interface.ask('What type of is 9 9 9 ?')
        self.assertEqual(result, UNKNOWN_QUESTION)
     
    @requirements(['#0014']) 
    def test_check_unknown_question(self):
        interface = Interface()
        result = interface.ask("What type of circle is 9 ?")
        self.assertEqual(result, UNKNOWN_QUESTION)


    @requirements(['#0015', '#0016', '#0020']) 
    def test_previously_asked_question(self):
       interface = Interface()
       result = interface.ask("What type of circle is 9 ?")
       self.assertEqual(result, UNKNOWN_QUESTION)
       interface.teach("A big one")
       self.assertEqual(interface.question_answers[interface.last_question].question, "What type of circle is")
       self.assertEqual(interface.question_answers[interface.last_question].value, "A big one")

    @requirements(['#0017', '#0021'])
    def test_no_previous_questions_asked(self):
        interface = Interface();
        result = interface.teach("A big one")
        self.assertEqual(result, NO_QUESTION)

    @requirements(['#0018'])
    def test_previous_question_teach_different_answer(self):
       interface = Interface()
       result = interface.ask("What type of circle is 9 ?")
       self.assertEqual(result, UNKNOWN_QUESTION)
       interface.teach("A big one")
       result = interface.teach("A small one")
       self.assertEqual(result, NO_TEACH)

    @requirements(['#0019'])
    def test_update_answer_to_previous_question(self):
       interface = Interface()
       result = interface.ask("What type of circle is 9 ?")
       self.assertEqual(result, UNKNOWN_QUESTION)
       interface.teach("A big one")
       
       self.assertEqual(interface.question_answers[interface.last_question].question, "What type of circle is")
       self.assertEqual(interface.question_answers[interface.last_question].value, "A big one")

       interface.correct("A small one")
       self.assertEqual(interface.question_answers[interface.last_question].question, "What type of circle is")
       self.assertEqual(interface.question_answers[interface.last_question].value, "A small one")

   
          
    



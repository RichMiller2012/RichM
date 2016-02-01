from question_answer import QA
from time import gmtime, strftime
from shape_checker import get_triangle_type, get_rectangle_type, get_four_sided_shape_type 
from math import pi
from copy import deepcopy
from useful_question import get_prime_number, valid_phone_number, solve_quadratic, highest_common_factor, set_ops

import difflib
NOT_A_QUESTION_RETURN = "Was that a question?"
UNKNOWN_QUESTION = "I don't know, please provide the answer"
NO_QUESTION = 'Please ask a question first'
NO_TEACH = 'I don\'t know about that. I was taught differently'


class Interface(object):
    def __init__(self):
        self.how_dict = {}
        self.what_dict = {}
        self.where_dict = {}
        self.who_dict = {}

        self.keywords = ['How', 'What', 'Where', 'Who', "Why", "Is"]
        self.question_mark = chr(0x3F)

        self.question_answers = {
            'What type of triangle is ': QA('What type of triangle is ', get_triangle_type),
            'What type of quadrilateral is ': QA('What type of rectangular object is ', get_rectangle_type),
            'What is the nth prime number ' : QA('What is the nth prime number ', get_prime_number),
            'Is this a valid phone number ' : QA('Is this a valid phone number ', valid_phone_number),
            'What are the quadratic results ' : QA('What are the quadratic results ', solve_quadratic),
            'What is the highest common factor of these two numbers ' : QA('What is the highest common factor of these two numbers ', highest_common_factor),
            'What is the result set of these two list and operation ' : QA('What is the result set of these two list and operation ', set_ops)
            }
        self.original_questions = deepcopy(self.question_answers)
        self.last_question = None

    def ask(self, question=""):
        if not isinstance(question, str):
            self.last_question = None
            raise Exception('Not A String!')
        if question[-1] != self.question_mark or question.split(' ')[0] not in self.keywords:
            self.last_question = None
            return NOT_A_QUESTION_RETURN
        else:
            parsed_question = ""
            args = []
            for keyword in question[:-1].split(' '):
                try:
                    args.append(float(keyword))
                except:
                    if(keyword != ''):                   
                        parsed_question += "{0} ".format(keyword)
            print parsed_question
            parsed_question = parsed_question[0:-1]
            self.last_question = parsed_question
            
            for answer in self.question_answers.values():
                if difflib.SequenceMatcher(a=answer.question, b=parsed_question).ratio() >= .90:
                    if answer.function is None:
                        return answer.value
                    else:
                        try:
                            print args
                            return answer.function(args)
                        except:
                            raise Exception("Too many extra parameters")
            return UNKNOWN_QUESTION

    def teach(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        elif self.last_question in self.question_answers.keys():
            return NO_TEACH
        else:
            self.__add_answer(answer)

    def correct(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        else:
            self.__add_answer(answer)

    def __add_answer(self, answer):
        self.question_answers[self.last_question] = QA(self.last_question, answer)

    """ lab3 additional test method """
        
    def getTime(self):
        return strftime("%Y-%m-%d %H:%M:%S", gmtime())

    def fib(self, n):
        if n == 0:
            return 0
        elif n == 1:
             return 1
        else:
            return self.fib(n-1) + self.fib(n-2)

    def clearMemory(self):
        self.question_answers = self.original_questions  
           
    def askOpen(self, open, user):
        if open == "Open the door hal":
            return "I'm afraid I can't do that " + user

    def pi(self, n):
        return None


    def convert(self, num, fromUnit, toUnit):

        conversions = {
              "km":{"m":1000},
              "m":{"cm":100},
              "dm":{"cm":10},
              "cm":{"mm":100},
              "mm":{"nm":1000},
              "mi":{"ft":5280},
              "ft":{"in":12},
              "yd":{"ft":3},
              "g":{"mg":1000},
              "kg":{"g":1000},
              "mt":{"kg":1000}  
        }

        return conversions[fromUnit][toUnit] * num

    def avg(self, list):
        ans = 0
        for num in list:
            ans += num
        return ans/(len(list))

    def high(self, list):
        ans = 0
        for num in list:
            if num > ans:
                ans = num
        return ans

    def low(self, list):
        ans = list[0]
        for num in list:
            if num < ans:
                ans = num
        return ans

    def sum(self, list):
        ans = 0;
        for num in list:
            ans += num
        return ans

    def mult(self, list):
        ans = 1
        for num in list:
            ans *= num
        return ans


                
                
            
from tests.plugins.ReqTracer import story
from unittest import TestCase
from time import gmtime, strftime
from source.main import Interface

class TddTest(TestCase):

    @story("* What time is it?")
    def test_what_time_is_it(self):
        interface = Interface()
        timeNow = interface.getTime()
        self.assertEqual(timeNow, strftime("%Y-%m-%d %H:%M:%S", gmtime()))

    @story("* what is the fib number?")
    def test_what_is_the_fib_number(self):
        interface = Interface()
        fib = interface.fib(8)
        self.assertEqual(fib, 21)

        """ TO DO
    @story("* What is n digit of pi?")
    def test_what_is_n_digit_of_pi(self):
        interface = Interface()
        pi = interface.pi(10)
        self.assertEqual(pi, 3.141592653)
        """

    @story("* Please clear memory")
    def test_please_clear_memory(self):
        interface = Interface()
        interface.ask("What type of circle is 9 ?")
        interface.teach("A big one")
        self.assertEqual(len(interface.question_answers), 3)
        interface.clearMemory()
        self.assertEqual(len(interface.question_answers), 2)

    @story("* Hal can't open door")
    def test_hal_cant_open_door(self):
        interface = Interface()
        ans = interface.askOpen("Open the door hal", "RichMiller2012")
        self.assertEqual(ans, "I'm afraid I can't do that RichMiller2012")

    @story("* Convert some units")
    def test_convert_some_units(self):
        interface = Interface()
        converted = interface.convert(10, "km", "m")
        self.assertEqual(converted, 10000)

    @story("* Convert up to ten different units")
    def test_convert_up_to_ten_units(self):
        interface = Interface()      
        self.assertEqual(interface.convert(1, "km", "m"), 1000)
        self.assertEqual(interface.convert(1, "m", "cm"), 100)
        self.assertEqual(interface.convert(1, "dm", "cm"), 10)
        self.assertEqual(interface.convert(1, "cm", "mm"), 100)
        self.assertEqual(interface.convert(1, "mm", "nm"), 1000)
        self.assertEqual(interface.convert(1, "mi", "ft"), 5280)
        self.assertEqual(interface.convert(1, "ft", "in"), 12)   
        self.assertEqual(interface.convert(1, "g", "mg"), 1000)
        self.assertEqual(interface.convert(1, "kg", "g"), 1000)
        self.assertEqual(interface.convert(1, "mt", "kg"), 1000)

    @story("* return the average of a set of numbers")
    def test_return_average_numbers(self):
        interface = Interface()
        avg = interface.avg([5, 10, 15])
        self.assertEqual(avg, 10)

    @story(" * return highest number in a set of numbers")
    def test_return_highest_number(self):
        interface = Interface()
        high = interface.high([5, 10, 15])
        self.assertEqual(high, 15)

    @story("* return lowest number in a set of numbers")
    def test_return_lowest_number(self):
        interface = Interface()
        low = interface.low([5, 10, 15])
        self.assertEqual(low, 5)

    @story("* return sum of numbers in a set")
    def test_return_sum_of_numbers(self):
        interface = Interface()
        sum = interface.sum([5, 10, 15])
        self.assertEqual(sum, 30)

    @story("* return the multiple of all numbers in a set")
    def test_return_multiple_of_numbers(self):
        interface = Interface()
        mult = interface.mult([5, 10, 15])
        self.assertEqual(mult, 750)





from main import Interface
import time


def question_answer_wrapper(question):
    interface = Interface()
    interface.ask(question)
    
    start = time.clock()
    QA_log = open("QA_log", 'w')
    QA_log.write(question + ': ')
    QA_log.write(str(interface.ask(question)) + ' time: ')
    proc_time = time.clock() - start

    ms = int(proc_time * 1000)
    QA_log.write(str(ms) + 'ms')
   
    return ms

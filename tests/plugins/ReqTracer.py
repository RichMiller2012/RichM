from nose2.events import Plugin

class ReqTracerPlugin(Plugin):
    configSection = 'req-tracer'
    def afterTestRun(self, event):
        print 'TESTS COMPLETED'
        outputFile = open('results', 'w')

        outputFile.write("STORIES \n\n")

        for key in Stories:
            outputFile.write(key + '\n')
            outputFile.write('\t' + Stories[key] + '\n')

        outputFile.write("\n\n\n")
        outputFile.write("REQUIREMENTS \n\n")

        for key in Requirements:
            print key
            outputFile.write(Requirements[key].req_text + '\n')
            for func in Requirements[key].func_name:
               outputFile.write('   ' + func + '\n')

class RequirementTrace(object):
    req_text = ""
    def __init__(self, text):
        self.req_text = text
        self.func_name = []

Requirements = {}
Stories = {}

def requirements(req_list):
    def wrapper(func):
        def add_req_and_call(*args, **kwargs):
            for req in req_list:
                if req not in Requirements.keys():
                    raise Exception('Requirement {0} not defined'.format(req))
                Requirements[req].func_name.append(func.__name__)
            return func(*args, **kwargs)       
        return add_req_and_call
    return wrapper

with open('requirements.txt') as f:
    for line in f.readlines():
        if '#0' in line:
            req_id, desc = line.split(' ', 1)
            Requirements[req_id] = RequirementTrace(desc)


def story(story):
    def wrapper(func):
        def add_req_and_call(*args, **kwargs):   
            Stories[story] = func.__name__
            return func(*args, **kwargs)   
        return add_req_and_call
    return wrapper
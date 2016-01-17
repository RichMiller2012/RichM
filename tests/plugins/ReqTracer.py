from nose2.events import Plugin

class ReqTracerPlugin(Plugin):
    configSection = 'req-tracer'
    def afterTestRun(self, event):
        print 'TESTS COMPLETED'
        outputFile = open('results', 'w')
        for key in Requirements:
            outputFile.write(Requirements[key].req_text + '\n')
            for func in Requirements[key].func_name:
               outputFile.write('   ' + func + '\n')

class RequirementTrace(object):
    req_text = ""
    def __init__(self, text):
        self.req_text = text
        self.func_name = []

Requirements = {}

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

with open('Requirements.txt') as f:
    for line in f.readlines():
        if '#00' in line:
            req_id, desc = line.split(' ', 1)
            Requirements[req_id] = RequirementTrace(desc)

"""
timer.py
"""

import time, sys

class Timer:
    """
    resume_data is a dict with:
    resume_data = {
    'label' = 'string'
    'time' : x.x,
    'splits' : [x.x, x.x, x.x, ... ]
    }
    """

    def __init__(self, label = None, resume_data = None):
        if resume_data:
            self.label = resume_data['label']
            self.current_time = resume_data['time']
            self.splits = resume_data['splits']
        else:
            if label: self.label = label
            else: self.label = "Unlabeled Timer"
            self.current_time = 0.0
            self.splits = [0.0]
        self.started = False
        self.active = False
        self.init_time = None

    def start(self):
        if self.init_time != None:
            print("Error: attempted to re-initialize timer.")
            sys.exit(1)

        self.init_time = time.time() - self.current_time
        self.started = True
        self.active = True
        return self.current_time

    def get_time(self):
        if self.active: self.current_time = time.time() - self.init_time
        return self.current_time

    def pause(self):
        p = self.get_time()
        self.active = False
        return p

    def resume(self):
        self.init_time = time.time() - self.current_time
        self.active = True
        return self.current_time

    def split(self):
        """ Returns new split as most recent split """
        s = self.get_time()
        self.splits.append(s)
        return s

    def unsplit(self):
        """ Returns the split before deleted split as most recent split """
        self.splits.pop()
        return self.splits[-1]

    def since_split(self):
        return self.current_time - self.splits[-1]

    def last_split(self):
        return self.splits[-1]

    def data(self):
        d = {}
        d['label'] = self.label
        d['time'] = self.get_time()
        d['splits'] = self.splits
        return d
    
    


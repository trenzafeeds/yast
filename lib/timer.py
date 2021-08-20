"""
timer.py
"""

import time, sys, json, os

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
        if label: self.label = label
        else: self.label = "Unlabeled_Timer"
        if not self.load(self.label):
            self.current_time = 0.0
            self.splits = [0.0]
        self.started = False
        self.active = False
        self.init_time = 0.0

    def start(self):
        if self.init_time != 0.0:
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
        return self.last_split()

    def unsplit(self):
        """ Returns the split before deleted split as most recent split """
        self.splits.pop()
        return self.splits[-1]

    def since_split(self):
        return self.current_time - self.splits[-1]

    def last_split(self):
        if len(self.splits) > 1:
            return self.splits[-1] - self.splits[-2]
        else: return self.splits[-1]

    def data(self):
        d = {}
        d['label'] = self.label
        d['time'] = self.get_time()
        d['splits'] = self.splits
        return d

    def get_json(self):
        return json.dumps(self.data())

    def save(self):
        with open('save/'+self.label+'.yast', 'w') as f:
            return f.write(self.get_json())

    def load(self, fname):
        if not os.path.exists('save/'+fname+'.yast'):
            return False
        else:
            with open('save/'+fname+'.yast') as f:
                load_data = json.loads(f.read())
            if load_data:
                self.current_time = load_data['time']
                self.splits = load_data['splits']
                return True
            else: return False
            
            


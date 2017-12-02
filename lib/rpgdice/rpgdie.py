import re
import math
import functools
import random
#The class representing an die.
#commonly represented in string as NdD
class RpgDie:
    
    __regex = r'(\+?[0-9]+(?:d[0-9]+)?)'
    def combiner(x,y):
        return list(map(lambda a,b:a+b, x,y))
    
    def __init__(self, in_str:str, components=[], parent=True):
        self.text = in_str
        self.components = components
        self.nodes = []
        self.parent=parent
        
        
    def __add__(self, other):
        if type(other)==RpgDie:
            val = RpgDie.combiner(self.rollDie(),other.rollDie())
            return RpgDie(str(val[0]))
        elif type(other)==int:
            return RpgDie(str(self.rollDie()+other))
    def __radd__(self, other):
        if type(other)==RpgDie:
            val = RpgDie.combiner(self.rollDie(),other.rollDie())
            return RpgDie(str(val[0]))
        elif type(other)==int:
            return RpgDie(str(self.rollDie()+other))
    
    def rollDie(self):
        #parse our text
        self.components = re.findall(RpgDie.__regex,self.text)
        if len(self.components) > 1:
            #complex die expression, break into child nodes
            self.nodes = list(map(lambda x:RpgDie(x, parent=False), self.components))
        elif len(self.components) == 0:
            return 0
        elif len(self.components) == 1:
            return self.__calc_roll()
        #lambda x,y: list(map(lambda a,b:a+b, x,y))
        tres = (functools.reduce(lambda x,y: RpgDie(str(RpgDie.combiner(x.rollDie(),y.rollDie())[0])), self.nodes))
        return tres.rollDie()
    
    def average(self):
        #parse our text
        self.components = re.findall(RpgDie.__regex,self.text)
        if len(self.components) > 1:
            #complex die expression, break into child nodes
            self.nodes = list(map(lambda x:RpgDie(x, parent=False), self.components))
        elif len(self.components) == 0:
            return 0
        elif len(self.components) == 1 and not self.parent:
            return self.__calc_avg()
        else:
            avgs = list(map(lambda x: x.average(), self.nodes))
            return int(math.ceil(functools.reduce(lambda x, y: x + y, avgs)/len(avgs)))
        
    def get_int_value(self):
        try:
            return int(self.text)
        except:
            return self.average()
            
    def __calc_roll(self):
        def __roll_die(numb:int,times:int, high_edge=None, low_edge=None):
            high_count = 0
            low_count = 0
            total = 0
            if times==0:
                return [numb, high_count, low_count]
            elif not high_edge and not low_edge:
                return [functools.reduce(lambda x,y:x+y, list(random.randint(1, numb) for r in range(times))), high_count, low_count]
            else:
                #account for critical succces and critical failure
                for r in range(times):
                    result = random.randint(1,numb)
                    total+=result
                    if len(list(filter(lambda x: x == high_edge))):
                        high_count+=1
                    elif len(list(filter(lambda x: x == low_edge))):
                        low_count+=1
                return [result, high_count, low_count]
        def __get_times_numb(in_str:str):
            out = list(map(lambda x: int(x), in_str.split('d')))
            if out is None or len(out)!=2:
                out = [0,int(in_str)]
            return out
        if self.text.startswith('-'):
            #negative case
            working_text = self.text[1:]
            t, n = __get_times_numb(working_text)
            rresult= __roll_die(n,t)
            rresult[0]*=-1
            return rresult
        elif self.text.startswith('+'):
            working_text = self.text[1:]
            t, n = __get_times_numb(working_text)
            rresult=__roll_die(n,t)
            return rresult
        else:
            t ,n = __get_times_numb(self.text)
            rresult = __roll_die(n,t)
            return rresult
            
    def __calc_avg(self):
        return 0 #todo: implement
        
        
    def __str__(self):
        return '<rpgdie.RpgDie object {}>'.format(self.text)
    
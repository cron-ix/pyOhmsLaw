#
# Python Class for using Ohm's law
#

import math

#
# Static methods for calculating voltage, current, resistance and power
# using Ohms Law
#
class Ohm:

    # return voltage or empty 
    @staticmethod
    def getVoltage(i:float=0, r:float=0, p:float=0, threePhase:bool=False):
        if threePhase:
            t=math.sqrt(3)
        else:
            t=math.sqrt(1)
        # v = Squareroot(p*r)
        if p>0 and r>0:
            return math.sqrt(p*r)
        # v = p / i
        elif p>0 and i>0:
            return p/i
        # v = i * r
        elif i>0 and r>0:
            return i*r
        else:
            return ""

    # return current or empty
    @staticmethod
    def getCurrent(v:float=0, r:float=0, p:float=0, threePhase:bool=False):
        if threePhase:
            t=math.sqrt(3)
        else:
            t=math.sqrt(1)
        # i = v / r
        if v>0 and r>0:
            return v/r
        # i = p / v
        elif p>0 and v>0:
            return p/v/t
        # i = Squareroot (p / r)
        elif p>0 and r>0:
            return math.sqrt(p/(r*t))
        else:
            return ""

    # return power or empty
    @staticmethod
    def getPower(v:float=0, i:float=0, r:float=0, threePhase:bool=False):
        if threePhase:
            t=math.sqrt(3)
        else:
            t=math.sqrt(1)
        # p = v * i
        if v>0 and i>0:
            return v*i*t
        # p = i² * r
        elif i>0 and r>0:
            return math.pow(i, 2)*r
        # p = v²/r
        elif v>0 and r>0:
            return math.pow(v, 2)/r
        else:
            return ""

    # return resitance or empty
    @staticmethod
    def getResistance(v:float=0, i:float=0, p:float=0, threePhase:bool=False):
        if threePhase:
            t=math.sqrt(3)
        else:
            t=math.sqrt(1)
        # r = v / i
        if v>0 and i>0:
            return v/i
        # r = v² / p
        elif v>0 and p>0:
            return math.pow(v, 2)/p
        # r = p / i²
        elif p>0 and i>0:
            return p/math.pow(i, 2)
        else:
            return ""
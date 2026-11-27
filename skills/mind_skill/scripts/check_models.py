"""Small deterministic checks. Does not establish causality or natural-language truth."""
from itertools import product
from fractions import Fraction

def stock(initial, inflow, outflow, dt=1):
    values = [Fraction(str(x)) for x in (initial, inflow, outflow, dt)]
    s, i, o, t = values
    if s < 0 or i < 0 or o < 0 or t <= 0:
        raise ValueError('nonnegative stock/rates and positive dt required')
    result = s + (i-o)*t
    if result < 0:
        raise ValueError('outflow exceeds available stock; refine the interval/model')
    return result

def loop(signs):
    if not signs or any(s not in ('+', '-') for s in signs):
        raise ValueError('supply known signs for a closed loop')
    return 'balancing' if signs.count('-') % 2 else 'reinforcing'

def argument(names, premises, conclusion):
    if not names or len(names) != len(set(names)):
        raise ValueError('unique explicit variable names required')
    witnesses=[]
    for bits in product((False,True),repeat=len(names)):
        assignment=dict(zip(names,bits))
        if all(p(assignment) for p in premises) and not conclusion(assignment):
            witnesses.append(assignment)
    return {'valid': not witnesses, 'counterexamples': witnesses}

if __name__ == '__main__':
    print('Import stock, loop, argument; see repository tests for executable examples.')

import sys
from copy import deepcopy

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

def is_flip_flop(module: str):
    return module.startswith('%')

def is_conjunction(module: str):
    return module.startswith('&')

broadcast_list = []
flip_flops = {}
conjunctions = {}

def get_conjunction_module(symbol, lines, initial_outputs):
    ret = {}
    for line in lines:
        parts = line.split('->')
        name = parts[0].strip()[1:]

        outputs = [item.strip() for item in parts[1].strip().split(',')]
        if symbol in outputs:
            ret[name] = False
    
    return (ret, initial_outputs)


for line in lines:
    parts = line.split('->')
    outputs = [item.strip() for item in parts[1].strip().split(',')]
    module = parts[0].strip()
    name = module[1:]

    if module == 'broadcaster':
        broadcast_list = outputs
    elif is_flip_flop(module):
        flip_flops[name] = (False, outputs)
    elif is_conjunction(module):
        conjunctions[name] = get_conjunction_module(name, lines, outputs)

initial_flip_flops = deepcopy(flip_flops)
initial_conjunctions = deepcopy(conjunctions)


def simulate_press(flip_flops, conjunctions):
    signal_queue = []
    for module in broadcast_list:
        signal_queue.append(('broadcaster', module, False))
    
    total_lows = 1
    total_highs = 0

    while len(signal_queue) != 0:
        source, dest, signal = signal_queue.pop(0)
        if signal:
            total_highs += 1
        else:
            total_lows += 1

        if dest in flip_flops:
            if signal:
                continue
            
            state, outputs = flip_flops[dest]
            state = not state
            flip_flops[dest] = (state, outputs)
            for output in outputs:
                signal_queue.append((dest, output, state))
        elif dest in conjunctions:
            state, outputs = conjunctions[dest]
            state[source] = signal
            new_signal = not all(state.values())
            conjunctions[dest] = (state, outputs)
            for output in outputs:
                signal_queue.append((dest, output, new_signal))
    
    return total_lows, total_highs

total_lows = 0
total_highs = 0
for i in range(1000):
    lows, highs = simulate_press(flip_flops, conjunctions)
    total_lows += lows
    total_highs += highs

print(total_lows)
print(total_highs)
print(total_lows * total_highs)

def monkey_banana(state):
    def next_states(s):
        actions = {
            'move_to_box': ('at_box', s[1], s[2]),
            'climb_box': (s[0], 'on_box', s[2]),
            'grab_banana': (s[0], s[1], 'has_banana') if s[0] == 'at_box' and s[1] == 'on_box' else s
        }
        return [(a, actions[a]) for a in actions if s != actions[a]]

    if state == ('at_box', 'on_box', 'has_banana'):
        return ["Banana grabbed!"]
    
    for action, new_state in next_states(state):
        result = monkey_banana(new_state)
        if result:
            return [action] + result

# Initial state: ('at_door', 'on_floor', 'no_banana')
steps = monkey_banana(('at_door', 'on_floor', 'no_banana'))
print("Steps to get the banana:" if steps else "No solution found.")
for step in steps:
    print(step)

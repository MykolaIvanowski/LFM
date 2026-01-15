# sort(data, by=greedy_key)
#
# answer = []
# state = initial_state
#
# for item in data:
#     if greedy_condition(item, state):
#         answer.append(item)
#         update(state, item)
#
# return answer



def greedy(data, key):
    data.sort(key=key)
    answer = []
    state = initial_state()

    for x in data:
        if condition(x, state):
            answer.append(x)
            update_state(state, x)

    return answer
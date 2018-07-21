def commit_next_val(partial_answer,datastruct, val):
    partial_answer.append(val)
    datastruct[val] -= 1

def uncommit_val(partial_answer,datastruct, val):
    partial_answer.pop()
    datastruct[val] += 1

def gen_nex_vals(datastruct):
    return [i for i in datastruct if datastruct[i] > 0]

def generate_permuts(partial_answer, dest_size, datastruct):
    if len(partial_answer) == dest_size:
        print ("".join(partial_answer))
        return
    next_vals = gen_nex_vals(datastruct)
    for i in next_vals:
        commit_next_val(partial_answer,datastruct, i)
        generate_permuts(partial_answer, dest_size, datastruct)
        uncommit_val(partial_answer,datastruct, i)
    return

def data_by_str(input_str):
    res = {}

    for i in set(input_str):
        res[i] = 0

    for i in input_str:
        res[i] += 1
    return res

if __name__ == '__main__':
    test = list("Tanya")
    generate_permuts([], len(test), data_by_str(test))

    

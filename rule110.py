def rule_110(gen, next_gen, i):
    """
    Applies the rule 110 cellular automaton to the given generation.

    The rule_110 function takes two lists and a number `i`,
    corresponding to the position in the two lists, and returns a
    list.  The list `gen` is kept unmutated whereas the list
    `next_gen` could be mutated if one of the conditions for a cell's
    state-change dictated by rule 110 occurs.
    """
    right = i + 1
    if right < len(gen):
        if gen[i] is 1:
            if gen[i + 1] is 1 and gen[i - 1] is 1:
                next_gen[i] = 0
        else:
            if gen[i + 1] is 1:
                next_gen[i] = 1
        rule_110(gen, next_gen, right)
    return next_gen


def generator(gens):
    """
    Applies the rule_110 function to the last list of the list and 
    appends the return value.  

    The generator function takes a list of lists and returns a list of 
    lists.
    """
    if len(gens) < 20:
        gens.append(rule_110(gens[-1], gens[-1].copy(), 1))
        generator(gens)
    return gens


n = input("Insert a number between 0 and 65536: ")  # The input number `n` is
# converted into the first generation, that is a list of 0s and 1s
# corresponding to `n` binary notation in 16 bits.
binary_n = format(int(n), '016b')
generation_zero = [int(d) for d in binary_n]
set(map(print, generator([generation_zero])))

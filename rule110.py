def rule_110(gen, i):
    """
    Apply the rule 110 cellular automaton to the given generation.
    """
    right = i + 1
    if right < len(gen):
        if gen[i] is 1:
            if gen[i + 1] is 1 and gen[i - 1] is 1:
                gen[i] = 0
        else:
            if gen[i + 1] is 1:
                gen[i] = 1
        rule_110(gen, right)
    return gen


n = input("Insert a number between 0 and 65536: ")    # The input number `n` is
# converted into the first generation, that is a list of 0s and 1s
# corresponding to `n` binary notation in 16 bits.
binary_n = format(int(n), '016b')
generation_zero = [int(d) for d in binary_n]
print(generation_zero)
generation_to_process = generation_zero
generation = 0
while generation < 20:    # Number of generations before the halt.
    new_generation = rule_110(generation_to_process, 1)
    print(new_generation)
    generation_to_process = new_generation
    generation += 1

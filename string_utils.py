def split_before_each_uppercases(formula):
    if not isinstance(formula, str):
        formula = str(formula)
    if formula == "":
        return []

    start = 0
    split_formula = []

    for i in range(1, len(formula)):
        if formula[i].isupper():
            split_formula.append(formula[start:i])
            start = i

    split_formula.append(formula[start:])
    return split_formula



def split_at_first_digit(formula):
    digit_location = 1
    for ch in formula[1:]:
        if ch.isdigit():
            break
        digit_location += 1

    if digit_location == len(formula):
        return formula, 1

    prefix = formula[:digit_location]
    number_part = formula[digit_location:]

    return prefix, int(number_part)


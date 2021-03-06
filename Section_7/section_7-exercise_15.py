class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


def base_convert(number):
    a = ""
    hex = "0123456789ABCDEF"
    while number > 0:
        a = hex[number % 3] + a
        number = number // 3
    return int(a)


def count_digits(number):
    one_count = 0
    two_count = 0
    while number != 0:
        c = number % 10
        number //= 10
        if c == 1:
            one_count += 1
        if c == 2:
            two_count += 1
    return one_count, two_count


def remove_key_elements(first):
    p = None
    q = first
    if first is None:
        return None
    converted_p = base_convert(q.value)
    while q is not None:
        digits = count_digits(converted_p)
        if digits[0] > digits[1]:
            p = q.next
            if p is None:
                break
            q = p.next
        else:
            p = q
            q = p.next
        converted_p = base_convert(p.value)
    if p is not None:
        digits = count_digits(converted_p)
        if digits[0] > digits[1]:
            p.next = None

def can_split_consecutive(ch: str) -> bool:
    n = len(ch)
    for length in range(1, n // 2 + 1):
        first_str = ch[:length]

    
        if first_str[0] == '0' and len(first_str) > 1:
            continue

        first = int(first_str)
        pointer = length
        next_num = first + 1

        while pointer < n:
            next_str = str(next_num)
            next_len = len(next_str)
            sub = ch[pointer:pointer + next_len]

            if sub != next_str:
                break

            pointer += next_len
            next_num += 1

        if pointer == n:
            return True

    return False



print(can_split_consecutive("99100"))        # True
print(can_split_consecutive("979899100101")) # True

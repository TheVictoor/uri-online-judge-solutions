def is_substr(main_str: str, current_str: str):
    # work with pointers should be faster than mutate the original array
    end_main_str = len(main_str)
    end_current_str = len(current_str)

    pointer_main_str = 0
    pointer_current_str = 0

    while pointer_main_str < end_main_str:
        current_main_char = main_str[pointer_main_str]
        pointer_main_str += 1
        if current_main_char == current_str[pointer_current_str]:
            pointer_current_str += 1
            if pointer_current_str >= end_current_str:
                return "Yes"

    return "No"


n_cases = int(input())

for case in range(n_cases):
    main_str = input()
    n_tests = int(input())

    for test in range(n_tests):
        current_str = input()
        print(is_substr(main_str, current_str))

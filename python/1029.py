cases = int(input())


def execute(cases):
    for _ in range(cases):

        def fib(n):
            if n <= 1:
                calculated[n] = [n, 1]
                return calculated[n]

            if calculated.get(n):
                return calculated.get(n)

            f1 = fib(n - 1)
            f2 = fib(n - 2)

            fib_result = f1[0] + f2[0]
            calls_result = f1[1] + f2[1] + 1
            calculated[n] = (fib_result, calls_result)

            return calculated[n]

        case = int(input())
        calculated = {}
        result = fib(case)

        print(f"fib({case}) = {result[1] - 1} calls = {result[0]}")


execute(cases)

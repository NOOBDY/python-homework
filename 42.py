from sys import stdin

if __name__ == "__main__":
    for line in stdin:
        tokens = line.strip().split()

        first_pass = [tokens[0]]

        for i in range(1, len(tokens)):
            if tokens[i - 1] == "*":
                first_pass[-2] = str(int(first_pass[-2]) * int(tokens[i]))
                first_pass = first_pass[:-1]

            elif tokens[i - 1] == "/":
                first_pass[-2] = str(int(int(first_pass[-2]) / int(tokens[i])))
                first_pass = first_pass[:-1]

            elif tokens[i - 1] == "%":
                first_pass[-2] = str(int(first_pass[-2]) % int(tokens[i]))
                first_pass = first_pass[:-1]

            else:
                first_pass.append(tokens[i])

        second_pass = [first_pass[0]]

        for i in range(1, len(first_pass)):
            if first_pass[i - 1] == "+":
                second_pass[-2] = str(int(second_pass[-2]
                                          ) + int(first_pass[i]))
                second_pass = second_pass[:-1]

            elif first_pass[i - 1] == "-":
                second_pass[-2] = str(int(second_pass[-2]
                                          ) - int(first_pass[i]))
                second_pass = second_pass[:-1]

            else:
                second_pass.append(first_pass[i])

        print(second_pass[0])

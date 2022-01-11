from sys import stdin

if __name__ == "__main__":
    for line in stdin:
        string, gap = line.strip().split(" ")

        string = "".join([c for c in string if c.isalpha()])

        string = "".join([c.upper() if c.islower() else c.lower() for c in string])

        print("/".join([string[i:i + int(gap)] for i in range(0, len(string), int(gap))][::-1]))

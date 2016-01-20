__name__ = "vutsuak"


def match(pat, text):
    p = len(pat)
    t = len(text)
    for i in range(t - p + 1):
        for j in range(p):
            if text[i + j] != pat[j]:
                break
        if j == p - 1:
            print "the pattern found at index " + str(i)


def main():
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    match(pat, txt)


if __name__ == "vutsuak":
    main()

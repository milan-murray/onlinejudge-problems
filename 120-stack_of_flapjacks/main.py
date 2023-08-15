from sys import stdin, stdout

if __name__ == '__main__':
    pile = stdin.readline().strip()
    while pile != '':
        pile_list = [int(i) for i in pile.split()]
        test_list = pile_list[:]
        test_list.sort()
        stdout.write(" ".join([str(i) for i in pile_list]))
        stdout.write("\n")
        i = len(pile_list)
        while test_list != pile_list:
            m = pile_list.index(max(pile_list[:i]))
            if m != i-1:
                if m != 0:
                    pile_list[:m+1] = reversed(pile_list[:m+1])
                    stdout.write(str(len(pile_list)-m) + " ")
                pile_list[:i] = reversed(pile_list[:i])
                stdout.write(str(len(pile_list)+1-i)+" ")
            i -= 1
        stdout.write("0\n")
        pile = stdin.readline().strip()


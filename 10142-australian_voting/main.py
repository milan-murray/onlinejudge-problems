from sys import stdin, stdout

cases = int(stdin.readline())
stdin.readline()
for c in range(cases):
    num_candidate = int(stdin.readline().strip())
    candidates = list()
    for i in range(num_candidate):
        candidates.append(stdin.readline().strip())
    candidates_vote = []
    current_vote = stdin.readline().strip()
    while current_vote != '':
        vote = [int(i)-1 for i in current_vote.split()]
        candidates_vote.append(vote)
        current_vote = stdin.readline().strip()
    has_winner = 0
    eliminated = set()
    if c > 0:
        stdout.write("\n")
    while not has_winner:
        vote_cnt = [0] * num_candidate
        for voter in candidates_vote:
            for v in voter:
                if v in eliminated:
                    continue
                else:
                    vote_cnt[v] += 1
                    break
        max_vote = max(vote_cnt)
        if max_vote > len(candidates_vote)/2:
            has_winner = 1
            for v in range(len(vote_cnt)):
                if vote_cnt[v] == max_vote:
                    # print(candidates[v])
                    stdout.write(candidates[v] + "\n")
        else:
            min_vote = -1
            for ind, val in enumerate(vote_cnt):
                if ind not in eliminated:
                    if min_vote == -1:
                        min_vote = val
                    else:
                        min_vote = min(val, min_vote)
            if min_vote == max_vote:
                has_winner = 1
                for ind, val in enumerate(candidates):
                    if ind not in eliminated:
                        # print(val)
                        stdout.write(val + "\n")
            else:
                for j in range(num_candidate):
                     if vote_cnt[j] == min_vote:
                        eliminated.add(j)

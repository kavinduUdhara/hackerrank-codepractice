def climbingLeaderboard(ranked, player):
    #take distinct values O(n) complexity
    rank_dict = {}
    rank_arr = []
    count = 0
    for rank in ranked:
        if rank not in rank_dict:
            count += 1
            rank_dict[rank] = count
            rank_arr.append(rank)
    
    result = []
    
    print(rank_arr)
    print(rank_dict)
    for play in player:
        if play in rank_dict:
            result.append(rank_dict[play])
            continue
        s = 0
        e = len(rank_arr) - 1
        arr_len = len(rank_arr) - 1
        while (s != e):
            m = (s + e) // 2
            print(f"s {s} | e {e} | m {m}| m+1 {m+1} | play {play}")
            if play > rank_arr[m + 1] and play < rank_arr[m]:
                result.append(rank_dict[rank_arr[m]] + 1)
                break
            elif play < rank_arr[m + 1] and play < rank_arr[m]:
                s = m + 1
            elif play > rank_arr[m + 1] and play > rank_arr[m]:
                e = m
            if s == e:
                if e == arr_len:
                    result.append(arr_len + 2)
                elif s == 0:
                    result.append(1)
                print(f"s: {s} | e: {e}")
    print(result)

climbingLeaderboard([100,100,50,40,40,20,10],[5,25,50,120])
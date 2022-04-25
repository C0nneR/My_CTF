import json
from collections import defaultdict, Counter

with open('hyperlink.json', 'r') as f:
    data = json.load(f)

legal_chars = 'abcdefghijklmnopqrstuvwxyz{}_'
links = [data['links'][c] for c in legal_chars]
cnt_dict = defaultdict(Counter)
combi = []
for i in range(164):
    for j in range(len(legal_chars)):
        char = legal_chars[j]
        link = links[j]
        cnt_dict[i][link[i]] += 1
    
    curr_cnt = cnt_dict[i]
    # if len(curr_cnt) != 1:
    #     least_frequent = curr_cnt.most_common()[::-1][:-1]
    #     for num, _ in least_frequent:
    #         for j in range(len(legal_chars)):
    #             char = legal_chars[j]
    #             link = links[j]
    #             if num == link[i]:
    #                 print(char, end = ' ')
    #     print('')

    if len(curr_cnt) == 2:
        temp = ''
        least_frequent = curr_cnt.most_common()[::-1][:-1]
        for num, _ in least_frequent:
            for j in range(len(legal_chars)):
                char = legal_chars[j]
                link = links[j]
                if num == link[i]:
                    temp += char
        combi.append(temp)

combi_3 = []
for i in range(len(combi) // 3):
    temp = combi[i * 3] + combi[i * 3 + 1] + combi[i * 3 + 2]
    combi_3.append(temp)
print(combi_3)

# combi = 'geb ear ver lge {ev r_a _li thi hin ing s_l ce{ alg lin is_ _al g_i e{e ar_ ery _is ice eve ine nea dic bra ryt ra} yth ebr ng_'
# combi = combi.split()

# start = 'dic'
# flag = [start]
# while True:
#     prefix = start[-2:]
#     for one_combi in combi:
#         if one_combi in flag:
#             continue
#         if one_combi[:2] == prefix:
#             flag.append(one_combi)
#             start = one_combi
#             break
#     if start[-1] == '}':
#         break

# final_flag = ''
# for i in range(len(flag) - 1):
#     final_flag += flag[i][0]
# final_flag += flag[-1]
# print(final_flag)
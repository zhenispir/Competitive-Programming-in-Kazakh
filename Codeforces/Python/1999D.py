def can_form_subsequence(s, t):
    s_list = list(s)
    t_len = len(t)
    s_len = len(s)

    t_index = 0
    
    for i in range(s_len):
        if t_index < t_len and (s_list[i] == t[t_index] or s_list[i] == '?'):
            s_list[i] = t[t_index]  
            t_index += 1

    if t_index == t_len:
        for i in range(s_len):
            if s_list[i] == '?':
                s_list[i] = 'a'
        return "YES", ''.join(s_list)
    else:
        return "NO", ""

T = int(input())
results = []

for _ in range(T):
    s = input().strip()
    t = input().strip()
    result, modified_string = can_form_subsequence(s, t)
    if result == "YES":
        results.append(f"YES\n{modified_string}")
    else:
        results.append("NO")

for result in results:
    print(result)

def format_stats(stats):
    stats_dict = {
        "General": {},
        "Attack": {},
        "Defence": {},
        "Possession": {},
        "Physical": {},
        "Discipline": {}
    }
    cur_obj = "General" ## changed once we encounter the next heading
    skip_cur = False
    for i in range(len(stats)):
        if skip_cur: ## skip the numbers
            skip_cur = False
            continue
        elif stats[i] in set(stats_dict.keys()):
            cur_obj = stats[i]
            continue
        stats_dict[cur_obj][stats[i]] = stats[i+1]
        skip_cur = True
    return stats_dict
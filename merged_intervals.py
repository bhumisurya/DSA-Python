def merged_intervals(interval):
    if not interval:
        return []

    interval.sort(key= lambda int : int[0])
    merged = [interval[0][:]]

    for start, end in interval[1:]:
        last_end = merged[-1][1]

        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start,end])

    return merged

data = [[1,3],[2,6],[8,12]]
print(merged_intervals(data))
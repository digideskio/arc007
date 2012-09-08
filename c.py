import sys

PAT = [c == 'o' for c in sys.stdin.readline().strip()]
N = len(PAT)

def merge(to_, from_, offset):
    from_ = from_[offset:] + from_[:offset]
    return [any(x) for x in zip(to_, from_)]

def minimum_pattern(current_pattern, now=1):
    if all(current_pattern):
        return now
    pos = current_pattern.index(0)
    minimum = 100

    for i, c in enumerate(PAT):
        if c:
            offset = i - pos
            if offset < 0:
                offset += N
            depth = minimum_pattern(merge(current_pattern, PAT, offset), now+1)
            if depth < minimum:
                minimum = depth
    return minimum


print minimum_pattern(PAT)

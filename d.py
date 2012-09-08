import sys

def check_diff(diff, head, remain, pos):
    N = len(remain)
    while pos < N:
        head += diff
        s = str(head)
        t = remain[pos:pos+len(s)]
        if not s.startswith(t):
            return False
        pos += len(s)
    return True

def main(C):
    if C[0] == '0':
        first = 1
        for i, c in enumerate(C):
            if c != '0':
                break
            first *= 10
        else:
            i += 1
        remain = C[i:]
    else:
        end = 1
        while end < len(C) and C[end] == '0':
            end += 1
        first = int(C[:end])
        remain = C[end:]

    if not remain:
        print first, 1
        return True

    for second_num in xrange(1, len(remain)+1):
        second = int(remain[:second_num])
        if second <= first:
            continue
        diff = second - first
        #print >>sys.stderr, '>', second_num, second, diff
        if check_diff(diff, second, remain, second_num):
            print first, diff
            return True

    second = int(remain) * 10
    while second <= first:
        second *= 10
    print first, second-first
    return True

def test():
    import random
    import string
    while True:
        c = ''.join([random.choice(string.digits) for _ in xrange(random.randint(1, 1000))])
        try:
            if not main(c):
                print c
                break
        except:
            print c
            break

if __name__ == '__main__':
    #main(sys.stdin.readline().strip())
    pass

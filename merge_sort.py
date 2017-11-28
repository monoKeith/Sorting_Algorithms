def ran_list(length, min, max):
    import random
    result = []
    for times in range(length):
        result.append(random.randint(min, max))
    return result

def sort(source):
    if len(source) == 1:
        return source
    else:
        left = sort(source[:len(source)//2])
        right = sort(source[len(source)//2:])
        return merge(left, right)

def merge(left, right):
    l, r, result = 0, 0, []
    for times in range(len(left)+len(right)):
        if l != len(left) and r != len(right):
            if left[l] > right[r]:
                result.append(right[r])
                r += 1
            else:
                result.append(left[l])
                l += 1
        elif l == len(left):
            result.append(right[r])
            r += 1
        elif r == len(right):
            result.append(left[l])
            l += 1
    return result

def main():
    import time
    samplesize = int(input("Input sample size: "))
    num_range = int(input("Input the range numbers: "))
    s_time = time.time()
    lis = ran_list(samplesize, 0, num_range)
    g_time = time.time()
    sort(lis)
    f_time = time.time()
    print("Generating time was: ", g_time - s_time)
    print("Sorting time was: ", f_time - g_time)
while True:
    main()

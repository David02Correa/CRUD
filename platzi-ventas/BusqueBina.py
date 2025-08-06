import random

def binary_search(data, target, low, high):
    if low > high:
        return False

    mid = (low + high) // 2

    if data[mid] == target:
        return True
    elif data[mid] < target:
        return binary_search(data, target, mid + 1, high)
    else:
        return binary_search(data, target, low, mid - 1)

if __name__ == '__main__':
    data = [random.randint(0, 100) for _ in range(10)]

    data.sort()
    print(data)

    target = int(input('Enter the number to search: '))
    found = binary_search(data, target, 0, len(data) - 1)

    print(found)
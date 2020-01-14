__author__ = 'Joystick'
def candies(n, arr):
    rew = [1 for i in range(len(arr))]
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            rew[i] = rew[i-1] + 1

    
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > arr[i+1]:
            rew[i] = max(rew[i], rew[i+1] + 1)

    return str(sum(rew))
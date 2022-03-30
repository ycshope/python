if __name__ == "__main__":
    while True:
        try:
            arr = [ch for ch in input().split(',')]
            arr.sort()
            print(','.join(arr))
        except:
            break

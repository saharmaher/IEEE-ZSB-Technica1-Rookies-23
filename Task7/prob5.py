def libraryFine(d1, m1, y1, d2, m2, y2):
    if (d2>=d1 and m2>=m1 and y2>=y1) or (m2>m1 and y2>=y1) or (y2>y1):
      fine=0
    elif d2<d1 and m2==m1 and y2>=y1:
      fine=15*abs(d2-d1)
    elif m2<m1 and y2==y1:
      fine=500*abs(m2-m1)
    else:
     fine=10000
    return fine


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
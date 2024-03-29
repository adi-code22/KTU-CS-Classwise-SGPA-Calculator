import csv

filename = 'marks.csv'


def calculate(x):
    mark = 0
    if x[1] == ')':
        x = x[0]
        if x == 'S':
            mark += 10;
        elif x == 'A':
            mark += 8.5
        elif x == 'B':
            mark += 7.5
        elif x == 'C':
            mark += 6.5
        elif x == 'D':
            mark += 6
        elif x == 'P':
            mark += 5.5
        elif x == 'F':
            mark += 0
        else:
            print("1Returned error due to mismatch of defined grades from input grades")
    else:

        if x[1] == 'b':
            mark += 0
        elif x[0] == 'A':
            mark += 9
        elif x[0] == 'B':
            mark += 8
        elif x[0] == 'C':
            mark += 7
        else:
            print("2Returned error due to mismatch of defined grades from input grades")
    return mark


with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    dict = {}
    for row in datareader:
        sgpa = 0
        w = 0
        # print("\n")
        for i in row:
            temp = 0
            if w == 0:
                # print(i)
                new = i
                w += 1
            else:
                if i[0: 7] == " MCN301":
                    pass
                elif i[0: 7] == " CST301":
                    temp += calculate(i[8: 10])
                    temp *= 4
                    sgpa += temp
                elif i[0: 7] == " CST303":
                    temp += calculate(i[8: 10])
                    temp *= 4
                    sgpa += temp
                elif i[0: 7] == " CST305":
                    temp += calculate(i[8: 10])
                    temp *= 4
                    sgpa += temp
                elif i[0: 7] == " CST307":
                    temp += calculate(i[8: 10])
                    temp *= 4
                    sgpa += temp
                elif i[0: 7] == " CST309":
                    temp += calculate(i[8: 10])
                    temp *= 3
                    sgpa += temp
                elif i[0: 7] == " CSL331":
                    temp += calculate(i[8: 10])
                    temp *= 2
                    sgpa += temp
                elif i[0: 7] == " CSL333":
                    temp += calculate(i[8: 10])
                    temp *= 2
                    sgpa += temp
                else:
                    print("Returned error due to bad subject code read from input")

        # print((sgpa / 220) * 10);
        dict[new] = (sgpa / 230) * 10
    j = 0
    store = 0
    for i in sorted(dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True):
        k = 0
        for l in i:
            if k == 1:
                if l != store:
                    j += 1
                store = l
            k += 1
        print("Rank",j, "-->", i, "\n")
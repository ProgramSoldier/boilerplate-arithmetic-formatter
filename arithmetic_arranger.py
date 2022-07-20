def arithmetic_arranger(problems, *decision):
    countProblems = len(problems)
    if (countProblems > 5):
        return "Error: Too many problems."
    arranged_problems = [""] * countProblems *4
    for i in range(countProblems):
        problems[i] = problems[i].split(" ")
        if (problems[i][1] != "+" and problems[i][1] != "-"):
            return "Error: Operator must be '+' or '-'."
        elif not (problems[i][0].isdigit() and problems[i][2].isdigit()):
            return "Error: Numbers must only contain digits."
        elif (len(problems[i][0]) > 4 or len(problems[i][2]) > 4):
            return "Error: Numbers cannot be more than four digits."
        problems[i].append(max(len(problems[i][0]), len(problems[i][2])))

    for i in range(countProblems):
        if i != countProblems -1:
            arranged_problems[countProblems * 0 + i] = "{0:>{1}}".format(problems[i][0], problems[i][3]+2)+"    "
            arranged_problems[countProblems * 1 + i] = problems[i][1] + "{0:>{1}}".format(problems[i][2], problems[i][3] + 1) + "    "
            arranged_problems[countProblems * 2 + i] = "-"*(problems[i][3]+2)+"    "
            if (problems[i][1] == "+"):
                arranged_problems[countProblems * 3 + i] = "{0:>{1}}".format(str(int(problems[i][0]) + int(problems[i][2])),
                                                                             problems[i][3]+2)+"    "
            else:
                arranged_problems[countProblems * 3 + i] = "{0:>{1}}".format(str(int(problems[i][0]) - int(problems[i][2])),
                                                                             problems[i][3] + 2) + "    "
        else:
            arranged_problems[countProblems * 0 + i] = "{0:>{1}}".format(problems[i][0], problems[i][3] + 2) +"\n"
            arranged_problems[countProblems * 1 + i] = problems[i][1] + "{0:>{1}}".format(problems[i][2],
                                                                                          problems[i][3] + 1) + "\n"
            arranged_problems[countProblems * 2 + i] = "-" * (problems[i][3] + 2)  +"\n"
            if (problems[i][1] == "+"):
                arranged_problems[countProblems * 3 + i] = "{0:>{1}}".format(int(problems[i][0]) + int(problems[i][2]),
                                                                         problems[i][3] + 2) + "\n"
            else:
                arranged_problems[countProblems * 3 + i] = "{0:>{1}}".format(int(problems[i][0]) - int(problems[i][2]),
                                                                             problems[i][3] + 2) + "\n"

    return "".join(arranged_problems)
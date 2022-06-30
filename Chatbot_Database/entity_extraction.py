import pandas as pd


# %%

def split_course_name(fpath='./tt_course.csv'):
    filename = './tt_course.csv'
    df = pd.read_csv(filename)
    course_list = df['COURSE_NO'].unique().tolist()
    print(course_list)

    fname = []
    sname = []

    for course in course_list:
        first, second = course.split(' ')
        fname.append(first)
        sname.append(second)

    fname = list(set(fname))
    sname = list(set(sname))
    sorted(fname)
    sorted(sname)

    with open('./tt_coursenameF.txt', 'w') as f:
        for name in fname:
            print(name, file=f)
    with open('./tt_coursenameS.txt', 'w') as f:
        for name in sname:
            print(name, file=f)


# %%

with open('./tt_coursenameF.txt', 'r') as f:
    while True:
        s = f.readline()
        if not s:
            break
        print(s, end="")



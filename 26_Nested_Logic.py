import datetime
def day_count(ret_date, due_date):
    if ret_date == due_date:
        return 0
    ret = datetime.date(ret_date[-1], ret_date[-2], ret_date[-3])
    due = datetime.date(due_date[-1], due_date[-2], due_date[-3])
    dif = str(ret-due)
    dif = int(dif.split()[0])
    return dif

ret_date = [int(x) for x in input().split()]
due_date = [int(x) for x in input().split()]
days = day_count(ret_date, due_date)
if days <= 0:
    fine = 0
else:
    if ret_date[1] == due_date[1]:
        fine = 15*days
    elif ret_date[2] == due_date[2]:
        fine = 500 * (ret_date[1]-due_date[1])
    else:
        fine = 10000
print(fine)

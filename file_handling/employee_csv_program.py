#emp_id,name,salary
#101,Alice,50000
#102,Bob,45000
#103,Charlie,60000

import csv

with open('employee.csv', 'w', newline = '') as fobj:
    writer = csv.writer(fobj)

    writer.writerows([['emp_id', 'name', 'salary'],
                      [101, 'Alice', 50000],
                      [102, 'Bob', 45000],
                      [103, 'Charlie', 60000]])
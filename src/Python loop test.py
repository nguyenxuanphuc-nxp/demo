"""
LAB EXERCISE: The BI Multi-Report
-------------------------------------------
USER STORY:
As an Analyst, I have a batch of department data strings. 
I need to process the entire list and print a summary for each.

GOAL:
Use a 'for' loop to iterate through a list of strings, 
unpack them, and pass them to your 'evaluate_department' function.

DATA TO PROCESS:
batch_data = [
    "Sales:95:90:92",
    "Marketing:70:75:80",
    "IT:60:50:65",
    "HR:not_a_number:80:90"
]

EXPECTED OUTPUT:
- A printed dictionary for the first three.
- An error message for the HR department.
-------------------------------------------
"""
def evaluate_department(dept_name, mkt, sales, it):
    try:
        str(dept_name)
    except ValueError:
        return('Department name invaild')
    try:
        mkt = int(mkt)
        sales = int(sales)
        it = int(it)        
    except ValueError:
        return('Scores must be integers')
    score_set = [mkt, sales, it]
    if not 0 <= mkt <= 100 or not 0 <= sales <= 100 or not 0 <= it <= 100:
        return('Scores out of bounds')
    average_score = round(sum(score_set)/len(score_set),1)
    if average_score >= 90:
        status = 'Elite'
    elif 70 <= average_score < 90:
        status = 'Stable'
    else:
        status = 'Underperforming'
    performace = {'dept': dept_name, 'avg': average_score, 'status': status}
    return performace

def evaluate_department(dept_name, mkt, sales, it):
    try:
        str(dept_name)
    except ValueError:
        return('Department name invaild')
    try:
        mkt = int(mkt)
        sales = int(sales)
        it = int(it)        
    except ValueError:
        return('Scores must be integers')
    score_set = [mkt, sales, it]
    if not 0 <= mkt <= 100 or not 0 <= sales <= 100 or not 0 <= it <= 100:
        return('Scores out of bounds')
    average_score = round(sum(score_set)/len(score_set),1)
    if average_score >= 90:
        status = 'Elite'
    elif 70 <= average_score < 90:
        status = 'Stable'
    else:
        status = 'Underperforming'
    performace = {'dept': dept_name, 'avg': average_score, 'status': status}
    return performace 


user_input = input('Please enter data using the format "Name:score1:score2:score3":')
batch_data = user_input.split(', ')
def data_process(batch_data):
    final_report = []
    for data_index, data in enumerate(batch_data):
        name, s1, s2, s3 = (batch_data[data_index].split(':'))
        result = evaluate_department(name, s1, s2, s3)
        final_report.append(result)
    return final_report
print(data_process(batch_data))

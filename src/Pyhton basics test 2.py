"""
LAB EXERCISE: The Analyst's Grading Tool
-------------------------------------------
USER STORY:
As a Junior BI Analyst, I need a tool that evaluates department scores 
(Marketing, Sales, IT). The tool calculates the average and assigns a 
Performance Profile for reporting in our BI dashboards.

INPUT: 
    - dept_name (str): The name of the department.
    - mkt (int): Marketing score.
    - sales (int): Sales score.
    - it (int): IT score.

OUTPUT:
    - dict: {'dept': str, 'avg': float, 'status': str} if successful.
    - str: An error message if validation fails.

VALIDATION RULES:
    1. Data Types: All scores (mkt, sales, it) must be integers.
    2. Range: All scores must be between 0 and 100 inclusive.

CATEGORIZATION LOGIC:
    - Average >= 90: 'Elite'
    - 70 <= Average <= 89: 'Stable'
    - Average < 70: 'Underperforming'

ERROR MESSAGES:
    - 'Scores must be integers'
    - 'Scores out of bounds'

NOTE: Round the average to 1 decimal place.
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

# Test 1: High Performance
print(evaluate_department("Global-Sales", 95, 90, 92))
# Expected: {'dept': 'Global-Sales', 'avg': 92.3, 'status': 'Elite'}

# Test 2: Mid Range
print(evaluate_department("Marketing", 70, 75, 80))
# Expected: {'dept': 'Marketing', 'avg': 75.0, 'status': 'Stable'}

# Test 3: Invalid Input
print(evaluate_department("IT", "Perfect", 100, 100))
# Expected: 'Scores must be integers'


    
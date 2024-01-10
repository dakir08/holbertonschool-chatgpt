#!/usr/bin/python3
def calculate_grade(mark):
    """
    Calculate and return the corresponding grade based on the provided mark.

    Parameters:
    mark (int or float): The numerical mark to be graded. It should be within the range 0-100.

    Returns:
    str: The grade associated with the input mark.

    Raises:
    ValueError: If the input mark is outside the valid range (not between 0 and 100).

    Grade Scale:
    - If mark < 50: 'Not yet successful'
    - If 50 <= mark <= 60: 'Pass'
    - If 61 <= mark <= 75: 'Credit'
    - If 76 <= mark <= 85: 'Distinction'
    - If mark > 85: 'High Distinction'

    Example:
    >>> calculate_grade(75)
    'Credit'

    Note:
    - This function calculates grades based on a predefined scale.
    - Grades are determined using the provided mark according to the specified ranges.
    - Make sure to handle possible exceptions (ValueError) when calling this function.

    """
    if mark < 0 or mark > 100:
        raise ValueError("Mark must be in the range 0-100")
    
    if mark < 50:
        return 'Not yet successful'
    elif mark <= 60:
        return 'Pass'
    elif mark <= 75:
        return 'Credit'
    elif mark <= 85:
        return 'Distinction'
    else:
        return 'High Distinction'


result = calculate_grade(50)
print(result)
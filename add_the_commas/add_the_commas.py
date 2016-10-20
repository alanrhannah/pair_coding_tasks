def add_the_commas(i):
    """
    Complete the funtion such that the assertations below are
    True due to the commas being correctly added. 
    You cannot use python string formatting for this task, i.e.
    '{:,}'.format(i)
    """
    
    return str(i)

if __name__ == '__main__':

    assert add_the_commas(1234) == '1,234'
    assert add_the_commas(123456) == '123,456'
    assert add_the_commas(123456789) == '123,456,789'
    assert add_the_commas(10) == '10'


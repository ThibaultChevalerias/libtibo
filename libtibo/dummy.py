"""
Dummy module for testing pytest
"""

def flip_list(l: list) -> list:
    """Flip a list

    If this function were slightly more complex, I would add an extended description here.

    Args:
        l: a list
    
    Returns:
        The flipped list
    
    Examples:
        >>> flip_list([1, 2, 3])
        [3, 2, 1]
    """
    return l[::-1]

def get_hello_str(name: str) -> str:
    """Make a greetings string

    Args:
        name: a name
    
    Returns:
        The greetings message formed with 'Hello', followed by the input name
    
    Examples:
        It's going to be simple.

        >>> get_hello_str('Alice')
        'Hello Alice!'
    """
    return 'Hello {}!'.format(name)

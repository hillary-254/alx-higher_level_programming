def text_indentation(text):
    """
    Prints the given text with two new lines after each occurrence of '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If the 'text' parameter is not a string.

    Returns:
        None
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    text_length = len(text)
    idx = 0
    new_string = ''
    starting = True

    while idx < text_length:
        if text[idx] == ' ' and starting is True:
            idx += 1
            continue

        starting = False

        if text[idx] in '.?:':
            new_string += text[idx]
            new_string += '\n'
            new_string += '\n'
            idx += 1

            while idx < text_length and text[idx] == ' ':
                idx += 1

            continue

        if idx < text_length:
            new_string += text[idx]
            idx += 1

    print(new_string, end='')

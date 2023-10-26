def timeInWords(h, m):
    numbers = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    if m == 0:
        return f"{numbers[h]} o' clock"
    
    if m == 15:
        return f"quarter past {numbers[h]}"
    
    if m == 30:
        return f"half past {numbers[h]}"
    
    if m == 45:
        return f"quarter to {numbers[h + 1]}"
    
    if m < 30:
        if m < 20:
            return f"{numbers[m]} {'minute' if m == 1 else 'minutes'} past {numbers[h]}"
        else:
            return f"twenty {numbers[m % 10]} {'minute' if m % 10 == 1 else 'minutes'} past {numbers[h]}"
    else:
        m = 60 - m
        if m < 20:
            return f"{numbers[m]} {'minute' if m == 1 else 'minutes'} to {numbers[h + 1]}"
        else:
            return f"twenty {numbers[m % 10]} {'minute' if m % 10 == 1 else 'minutes'} to {numbers[h + 1]}"

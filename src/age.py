"""A simple module to test GitHub Actions."""

def categorize_by_age(age: int) -> str:
    """Categorizes a person to a group based on their age.

    Args:
        age (int): The age of the person.

    Returns:
        str: The group they belong to.
    """
    if 0 <= age <= 9:
        return "Child"
    elif 9 < age <= 18:
        return "Adolescent"
    elif 18 < age <= 65:
        return "Adult"
    elif 65 < age <= 150:
        return "Golden age"
    else:
        return f"Invalid age: {age}"

class TypeCasting(Exception):
    pass


def safe_int_cast(value):
    try:
        return int(value)
    except (ValueError, TypeError) as e:
        raise TypeCasting(f"Cannot convert '{value}' to int. Invalid type or format: {e}")


def safe_float_cast(value):
    """Convert value to float with exception handling"""
    try:
        return float(value)
    except (ValueError, TypeError) as e:
        raise TypeCasting(f"Cannot convert '{value}' to float. Invalid type or format: {e}")


def safe_str_cast(value):
    """Convert value to string with exception handling"""
    try:
        return str(value)
    except Exception as e:
        raise TypeCasting(f"Cannot convert '{value}' to string: {e}")


def safe_bool_cast(value):
    """Convert value to bool with exception handling"""
    try:
        if isinstance(value, str):
            if value.lower() in ('true', '1', 'yes'):
                return True
            elif value.lower() in ('false', '0', 'no'):
                return False
            else:
                raise ValueError(f"Cannot convert string '{value}' to bool")
        return bool(value)
    except Exception as e:
        raise TypeCasting(f"Cannot convert '{value}' to bool: {e}")


# Example usage with exception handling
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("123", "int"),
        ("hello", "int"),  # This will raise exception
    ]
    
    for value, target_type in test_cases:
        try:
            if target_type == "int":
                result = safe_int_cast(value)
                print(f"✓ '{value}' -> int: {result}")
            elif target_type == "float":
                result = safe_float_cast(value)
                print(f"✓ '{value}' -> float: {result}")
            elif target_type == "str":
                result = safe_str_cast(value)
                print(f"✓ {value} -> str: '{result}'")
            elif target_type == "bool":
                result = safe_bool_cast(value)
                print(f"✓ '{value}' -> bool: {result}")
        except TypeCasting as e:
            print(f"✗ Error: {e}")


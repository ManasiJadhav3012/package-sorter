def sort(width, height, length, mass):
    
    volume = width * height * length

    is_bulky = volume >= 1000000 or max(width, height, length) >= 150

    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    return "SPECIAL" if is_bulky or is_heavy else "STANDARD"


if __name__ == "__main__":
    # Test cases
    print(sort(100, 100, 50, 10)) 
    print(sort(200, 200, 200, 10)) 
    print(sort(50, 50, 50, 30))    
    print(sort(200, 200, 200, 30))  

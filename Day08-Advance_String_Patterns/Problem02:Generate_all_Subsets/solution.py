def get_input():
    try:
        user_input = input("Enter elements separated by space: ")
        elements = user_input.strip().split()
        return elements
    except Exception as e:
        print("Invalid input:", e)
        return []

def recursive(elements):
    result = []

    def backtrack(start, path):
        result.append(path[:])  # Add a copy of current subset
        for i in range(start, len(elements)):
            path.append(elements[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result

elements = get_input()
recursive(elements)

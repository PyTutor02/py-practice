import keyword

print(len(keyword.kwlist))  #No of Keywords
print(keyword.kwlist)       #list of kw
print(keyword.softkwlist)
print(keyword.iskeyword('if')) #checking if str is standard kw
print(keyword.issoftkeyword('if'))  #checking if str is soft kw

#Soft Keywords Demonstration
def check_data(data):
    # 'match' starts the block
    match data:
        # 'case' defines a specific pattern
        case [x, y]:
            print(f"Found a pair: {x} and {y}")
        
        # 'case' with a literal
        case "admin":
            print("Admin access granted.")
        
        # '_' is the wildcard (soft keyword context)
        case _:
            print("Unknown format or user.")

# Demonstration
check_data([10, 20])  # Output: Found a pair: 10 and 20
check_data("guest")
check_data("admin")   # Output: Unknown format or user.

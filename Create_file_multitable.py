for i in range(2,3):
    with open(f"table_multiplication_file_{i}.txt","w") as f:
        for j in range(1,11):
            f.write(f"{i}*{j}={i*j}")
            if j!=10:
                f.write("\n")
def save_results(data): 
    with open(f"subdomains_virustotal.csv", "w") as output:
        data_output = ""
        for row in data:
            data_output += ",".join(row) + "\n"
        output.write(data_output)
        print(data_output)
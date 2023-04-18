cars_status = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars_status:
    if status == "faulty":
        print("Faulty car encountered")
        break
    print(f"The car status is {status}")
else: 
    print("All cars built successfully")
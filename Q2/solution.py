rec = input()
tmp = rec.split('\n')
total_rec = int(tmp[0])
rec_lines = []
for x in range(1, total_rec+1):
    rec_lines.append(tmp[x])

allValid = "true"
errorCodes = []
for record in rec_lines:
    record_arr = record.split(" ")
    isValid = record_arr[1]
    if allValid == "true":
        allValid = isValid
    if isValid != "true":
        errorCodes.append(record_arr[2])

if allValid == "true":
    print("Yes")
else:
    print("No")
    errors = errorCodes[0]
    for x in range(1, len(errorCodes)):
        errors += " "
        errors += errorCodes[x]
    print(errors)
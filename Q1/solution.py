req = input()
tmp = req.split('\n')
total_tshirts = tmp[0]
sizes_avail = tmp[1]
no_req = tmp[2]
sizes_req = tmp[3]

sizes_avail_arr = sizes_avail.split(' ')
sizes_avail_dict = dict()
sizes_req_arr = sizes_req.split(" ")
sizes_req_dict = dict()
# S = 0, M = 1, L = 2
for size in sizes_avail_arr:
    if size == "M":
        sizes_avail_dict[size] = 1
    elif size[-1] == "S":
        sizes_avail_dict[size] = 0 - (len(size) - 1)
    elif size[-1] == "L":
        sizes_avail_dict[size] = 2 - (len(size) - 1)

for size in sizes_req_arr:
    if size == "M":
        sizes_req_dict[size] = 1
    elif size[-1] == "S":
        sizes_req_dict[size] = 0 - (len(size) - 1)
    elif size[-1] == "L":
        sizes_req_dict[size] = 2 - (len(size) - 1)

sizes_avail_dict = dict(sorted(sizes_avail_dict.items()))
sizes_req_dict = dict(sorted(sizes_req_dict.items()))

sizes_avail_arr_ref = [sizes_avail_dict[x] for x in sizes_avail_arr]
sizes_avail_arr_ref.sort(reverse=True)

sizes_req_arr_ref = [sizes_req_dict[x] for x in sizes_req_arr]
sizes_req_arr_ref.sort(reverse=True)
j = 0
flag = True
for s in sizes_req_arr_ref:
    if sizes_req_arr_ref[j] >= s:
        j+=1
    else:
        print("No")
        flag = False
        break
if flag == True:
    print("Yes")
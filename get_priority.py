import json
input_file = open('data/support_tickets.json')
data = json.load(input_file)  # get the data list
all_priority = []
for element in data:  # iterate on each element of the list
    # element is a dict
    priority = element['priority']
    all_priority.append(priority)
print(all_priority)

deduped_all_priority = list(dict.fromkeys(all_priority))
print(deduped_all_priority)

with open('priorities.txt', 'w') as f:
    for tag in deduped_all_priority:
        f.write(f"{tag}\n")
import json
input_file = open('data/support_tickets.json')
data = json.load(input_file)  # get the data list
all_tags = []
for element in data:  # iterate on each element of the list
    # element is a dict
    tags = element['tags']
    for tag in tags:
        all_tags.append(tag)
print(all_tags)

deduped_all_tags = list(dict.fromkeys(all_tags))
print(deduped_all_tags)

with open('tags.txt', 'w') as f:
    for tag in deduped_all_tags:
        f.write(f"{tag}\n")
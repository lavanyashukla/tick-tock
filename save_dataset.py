import json
import weave
from weave.weaveflow import Dataset


# Initialize Weave
weave.init('ticktock')


# load json file
with open('wandb_zd_2_yr.json') as f:
    data = json.load(f)

    # Create a dataset
    dataset = Dataset(data)

    # Publish the dataset
    weave.publish(dataset, 'data')

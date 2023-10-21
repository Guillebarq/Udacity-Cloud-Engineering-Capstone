#!/usr/bin/env bash

## Complete the following steps to get Docker running locally

# Step 1:
# Build image and add a descriptive tag
docker build --tag=joknes-in-a-container .

# Step 2: 
# List docker images
docker images

# Step 3: 
# Run flask app
docker run -it --rm --name joknes-in-a-container -p 5000:5000 joknes-in-a-container

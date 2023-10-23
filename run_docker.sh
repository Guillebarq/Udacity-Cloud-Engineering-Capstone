#!/usr/bin/env bash

## Complete the following steps to get Docker running locally

# Step 1:
# Build image and add a descriptive tag
docker build --tag=jokes-in-a-container .

# Step 2: 
# List docker images
docker images

# Step 3: 
# Run flask app
docker run -it --rm --name jokes-in-a-container -p 80:80 jokes-in-a-container

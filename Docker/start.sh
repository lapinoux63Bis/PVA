#!/bin/bash

# Stop and remove container
docker stop ReceiverTest
docker remove ReceiverTest

# Build container
docker build -t python_receiver Container/

# Run container
docker run -d -p 12345:12345 -p 12346:12346 --name ReceiverTest python_receiver

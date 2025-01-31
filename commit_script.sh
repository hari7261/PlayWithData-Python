#!/bin/bash

# Create a temporary file
temp_file=$(mktemp)

# Loop to run the commit process every minute for 5 minutes
for minute in {1..5}
do
  # Loop to make 25 commits
  for i in {1..25}
  do
    # Write to the temporary file
    echo "Commit number $i in minute $minute" >> $temp_file

    # Add the changes to the staging area
    git add $temp_file

    # Commit the changes
    git commit -m "Automated commit number $i in minute $minute"
  done

  # Wait for 60 seconds before the next iteration
  sleep 60
done

# Remove the temporary file
rm $temp_file

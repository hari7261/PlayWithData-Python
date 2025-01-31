#!/bin/bash

# Create a temporary file
temp_file=$(mktemp)

# Loop to make 25 commits
for i in {1..25}
do
  # Write to the temporary file
  echo "Commit number $i" >> $temp_file

  # Add the changes to the staging area
  git add $temp_file

  # Commit the changes
  git commit -m "Automated commit number $i"
done

# Remove the temporary file
rm $temp_file

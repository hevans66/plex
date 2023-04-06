#!/bin/sh

if [ $# -ne 1 ]; then
  echo "Usage: $0 DOI"
  exit 1
fi

DOI="$1"
RESPONSE=$(curl -s "https://api.semanticscholar.org/v1/paper/${DOI}")

TITLE=$(echo "${RESPONSE}" | jq -r '.title')
YEAR=$(echo "${RESPONSE}" | jq -r '.year')
JOURNAL=$(echo "${RESPONSE}" | jq -r '.venue')

# Extract author names
AUTHORS=$(echo "${RESPONSE}" | jq -r '.authors[].name' | awk -vORS=',' '{print $0}' | sed 's/,$//')

# Generate the BibTeX entry
echo "@article{${DOI//\//-},
  title={${TITLE}},
  author={${AUTHORS}},
  journal={${JOURNAL}},
  year={${YEAR}},
  doi={${DOI}}
}"

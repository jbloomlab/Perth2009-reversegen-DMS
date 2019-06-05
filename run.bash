#!/bin/bash

set -e

RESULTSDIR="results/notebooks"

mkdir -p $RESULTSDIR

NB="analyze_revgen.ipynb"

echo "Running $NB"

jupyter nbconvert \
   --to notebook \
   --execute \
   --inplace \
   --ExecutePreprocessor.timeout=-1 \
   $NB

echo "Converting $NB to markdown"
jupyter nbconvert \
   --output-dir $RESULTSDIR \
   --to markdown \
   $NB
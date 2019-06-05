#!/bin/bash

set -e

RESULTSDIR="results/notebooks"

mkdir -p $RESULTSDIR

NB="analysis_notebook.ipynb"

echo "Running $NB"

jupyter nbconvert \
   --to notebook \
   --execute \
   --inplace \
   --ExecutePreprocessor.timeout=-1 \
   $NB

echo "Converting $NB to pdf"
jupyter nbconvert \
   --output-dir $RESULTSDIR \
   --to pdf \
   $NB
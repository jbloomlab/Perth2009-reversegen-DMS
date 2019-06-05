# Perth2009-reversegen-DMS
Analysis of Perth/2009 H3 HA mutant libraries generated by reverse genetics.

Experiments and analysis performed by Juhye Lee, Rachel Eguia, and Jesse Bloom.

## Brief Summary & Rationale
This repository contains analysis of Perth/2009 H3 HA mutant libraries generated by reverse genetics, which can be found here: [results/notebooks/analysis_notebook.md](./results/notebooks/analysis_notebook.md).
These libraries were generated and used for mutational antigenic profiling of monoclonal antibodies and polyclonal sera. 

As described in [Lee et al (2018)](https://www.pnas.org/content/115/35/E8276), we previously generated mutant virus libraries of the Perth/2009 H3 HA using a helper-virus approach [Doud and Bloom (2016)](https://www.mdpi.com/1999-4915/8/6/155).
However, the titers of these viral libraries were relatively low, and to ensure that we would have sufficient virus library for immune selection experiments, we generated the libraries using reverse genetics. 
This involved re-mutagenizing the wildtype Perth/2009 HA gene, rescuing mutant virus library, and passaging the viral libraries in cell culture to select for functional HA variants.

In this repository, we will analyze and create summary plots of the deep sequencing data of the reverse-genetics libraries. 

## Organization
The repository is organized into the following files & directories:

  - [data/](./data): contains all input data necessary to run the analysis. This includes the [Perth09_HA_reference.fa](./data/Perth09_HA_reference.fa) FASTA file giving the sequence of the wildtype Perth/2009 HA used in the experiments to align deep sequencing reads. There is also a subdirectory ([data/SangerAnalysis](./data/SangerAnalysis/)) which contains the `pdf` plots generated by analyzing Sanger sequencing data of 30 randomly selected clones from the mutant plasmid libraries.
  - [results/](./results): all results are placed in this directory. The `markdown` ouput of the `analysis_notebook` can be found in the [results/notebooks](./results/notebooks) subdirectory.
  - [analysis_notebook.ipynb](analysis_notebook.ipynb): this is the Jupyter notebook that contains the code to analyze the deep sequencing data.
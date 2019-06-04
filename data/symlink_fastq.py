"""Symbolically link to FASTQ files."""
import os
import glob
import pandas as pd

origpathdict = {'A': '/shared/ngs/illumina/jmlee34/180912_SN367_1261_AHLKHJBCX2/Unaligned/Project_jmlee34/', 
                'B': '/shared/ngs/illumina/jmlee34/190116_D00300_0668_AHVHCFBCX2/Unaligned/Project_jmlee34/', 
                'C': '/shared/ngs/illumina/jmlee34/190326_D00300_0706_AHWYTCBCX2/Unaligned/Project_jmlee34/'}

fastqdir = './results/FASTQ_files/'
if not os.path.isdir(fastqdir):
    os.mkdir(fastqdir)

exp_list = pd.read_csv('./data/experiment_list.csv')
    
for index, row in exp_list.iterrows():
    sample = row['name']
    print('\nAnalyzing sample {0}'.format(sample))
    origpath = origpathdict[row['FASTQkey']]
    dirs = [d for d in os.listdir(origpath) if row['experiment'] in d]
    print('Found {0} directories.'.format(len(dirs)))
    ifile = 1
    for d in dirs:
        fulld = '{0}/{1}'.format(origpath, d)
        print(fulld)
        for f in glob.glob('{0}/*R1*.fastq.gz'.format(fulld)):
            newf = "{0}/{1}_R1_file{2}.fastq.gz".format(fastqdir, sample, ifile)
            print("File {0} is {1} -- linking to {2}".format(ifile, f, newf))
            ifile += 1
            if not os.path.isfile(newf):
                os.symlink(f, newf)
            f2 = f.replace('_R1', '_R2')
            assert os.path.isfile(f2)
            newf2 = newf.replace('_R1', '_R2')
            if not os.path.isfile(newf2):
                os.symlink(f2, newf2)


print('Program complete.')
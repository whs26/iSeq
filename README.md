iSeq

This package can:
(1) automatically run the alignment using Bowtie2 (which can be visualised using IGV viewer),
(2) show you a report of the alignment in a txt file,
(3) call out all mutations in a csv file (if the csv file is absence, it may indicate the absence of mutation)
(4) generate a consensus sequence file in .txt format
The package and this explanation are intended to be clear and easy for complete beginner.

Key advantages:
(1) Takes only a few seconds to drag and drop your alignment files and reference file into the terminal. Minimal input required
(2) Run multiple alignments in multiple terminal tabs at once, all using drag and drop command. Super fast to setup and particularly suitable when you have many small alignments to do regularly
(3) The source code is open and users are able to customise the setting and parameters for alignment and even add a few extra commands etc.
(4) All packages required are contained in a single folder (IGVtools, Samtools, Bowtie2) and save users a lot of time to download and install individually (which can be hard for a complete beginner).

Motivation:
I couldn’t find any easy-to-use, either commercially available or open source, alignment tool that can align many files quickly and easily. Ugene is a free software that uses graphic user interface for alignment but users need to manually enter each alignment files and set parameters and it offers limited ability for customization. It also does not generate a mutation list, a consensus file and an alignment summary. The motivation is to combine all these into a single easy-to-use drag-and-drag alignment package.

Limitations:
(1) Currently, it takes only paired-end inputs
(2) While I have satisfactory alignment results using the default setting and parameters, users who prefer to customise the setting would need to modify the run.sh file. Some understanding of Bowtie2 command and programming skills are required (Please refer to Bowtie2 manual for command)


Requirement:
- Python 3 (Google it and install)
- Java 7 or above (Google it and install)
- Java Development Kit (JDK) (Google it and install)
- Python package: Pandas (To install, open the terminal and type 'pip3 install pandas')
- Python package: Biopython (To install, open the terminal and type 'pip3 install biopython')

To-Use:
1. Download the ‘iSeq’ file and place it at the Desktop (not anywhere else). Unzip samtools, IGVtools and bowtie2 within the folder.
2. Open the terminal (you can use search to locate it, just search ‘terminal’)
3. Inside the terminal, type ‘nano ~/.bash_profile’ (this opens up a word editor called nano and edit a hidden file called .bash_profile)
4. At the bottom of the script (if there is already something there), type: PATH="./Desktop/iSeq-master" and on the next line, type: export PATH  (the purpose is to add ‘./Desktop/iSeq-master’ into your default PATH for easy access)
5. Press ‘Ctrl + x’ to exit. When asked whether to save it or not, press ‘y’ and then ‘Enter’.

6. Now you are ready to use the program. In the terminal, type ‘run.sh’ follow by a space, then drag and drop the three items in order (1) first_paired_end_file.fastq
 (2) second_paired_end_file.fastq (3) reference_file_in_fasta_format.fasta

Example: 
run.sh paired1.fastq paired2.fastq ref.fasta

7. The program will run automatically. When it is done, a message ‘Done’ will be shown at the terminal. In the folder where you have the reference.fasta file, you will see a number of new files. The key files are:

(1) a filename ended with …fa_sorted.bam       - this file can be opened and visualised in IGV Viewer (…fa_sorted.bam.bai must also present in the same folder, do not delete it)
(2) a filename ended with …fa_call.csv         - this file contains a list of all mutations
(3) a filename ended with …fa.stat.txt.        - this file contains the stat for the alignment. Refer to Bowtie2 manual for details
(4) a filename ended with …_consensus_seq_txt  - this file contains the consensus sequence of the alignment

8. To multiplex, in the terminal, press ‘Ctrl + T’ to open a new tab and repeat step 6. You can open as many terminal as you like and leaves them run overnight. 



Disclaimer:
Some packages from other sources are included sorely for convenience to the users. The credits for these packages solely belong to the original content creators. The packages are:
(1) Bowtie2-2.3.2-legacy URL: http://bowtie-bio.sourceforge.net/bowtie2/index.shtml
(2) IGVtools URL: https://software.broadinstitute.org/software/igv/igvtools
(3) Samtools-1.3.1 URL: http://samtools.sourceforge.net
iSeq is intended to help beginners to easily align deep sequencing data. The users are solely responsible for output and the use of iSeq. 

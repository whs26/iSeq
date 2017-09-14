iSeq

This package can:
(1) automatically run the alignment using Bowtie2 (which can be visualised using IGV viewer),
(2) show you a report of the alignment in a txt file,
(3) call out all mutations in a csv file
(4) generate a consensus sequence file in .txt format
The package is intended to be clear and easy to use.

Key advantages:
(1) Takes only a few seconds to drag-and-drop your alignment files and the reference file into the terminal. Minimal input required
(2) Run multiple alignments in multiple terminal tabs at once, all using just drag-and-drop commands. Super fast to setup and particularly suitable when you have many small alignments to do regularly
(3) The source code is open and users can customise the setting and parameters and even add thier own commands.
(4) All packages required are contained in a single folder (IGVtools, Samtools, Bowtie2) and save users a lot of time to download and install them individually.

Motivation:
I couldn’t find any easy-to-use, either commercially available or open source, alignment tool that can align many files quickly and easily. Ugene is a free software that uses graphic user interface for alignment but users need to manually enter each alignment files and set parameters. It also offers limited customization and does not generate a mutation list, a consensus file and an alignment summary. The motivation of this package is to combine all of these into a single easy-to-use drag-and-drag alignment package.

Limitations:
(1) Currently, it takes only paired-end inputs
(2) While I have satisfactory alignment results using the default setting and parameters, users who prefer to customise the setting would need to modify the run.sh file. Some understanding of Bowtie2 command and programming skills are required (Please refer to Bowtie2 manual for command)
(3) So far only tested on Mac

Requirement:
- Python 3 (Google it and install)
- Java 7 or above (Google it and install)
- Java Development Kit (JDK) (Google it and install)
- Python package: Pandas (To install, open the terminal and type 'pip3 install pandas' after you install Python 3)
- Python package: Biopython (To install, open the terminal and type 'pip3 install biopython' after you install Python 3)

To-Use:
1. Download the ‘iSeq-master’ file and place it at the Desktop (not anywhere else). Unzip samtools, IGVtools and bowtie2 within the folder.
2. Open the terminal (you can use the Search function in Mac to locate it, just search for ‘terminal’)
3. Inside the terminal, type ‘nano ~/.bash_profile’ (this opens up a word editor called nano and edit a hidden file called .bash_profile)
4. At the bottom of the script, type: export PATH=$PATH:./Desktop/iSeq-master (the purpose is to add ‘./Desktop/iSeq-master’ into your default PATH for easy access)
5. Press ‘Ctrl + x’ to exit. When asked whether to save it or not, press ‘y’ and then ‘Enter’.

6. Now you are ready to use the program. In the terminal, type ‘run.sh’ follow by a space, then drag and drop the following three items in order: 
(1) first_paired_end_file.fastq
(2) second_paired_end_file.fastq 
(3) reference_file_in_fasta_format.fasta

Example: 
run.sh paired1.fastq paired2.fastq ref.fasta

& press Enter.

7. The program will run automatically. When it is done, a message ‘Done’ will appear at the terminal. In the folder where you have the reference.fasta file, you will see a number of new files. The key files are:

(1) a filename ends with …fa_sorted.bam       - this file can be opened and visualised in IGV Viewer (…fa_sorted.bam.bai must also be present in the same folder, do not delete it)
(2) a filename ends with …fa_call.csv         - this file contains a list of all mutations
(3) a filename ends with …fa.stat.txt.        - this file contains the stat for the alignment. Refer to Bowtie2 manual for details
(4) a filename ends with …_consensus_seq_txt  - this file contains the consensus sequence of the alignment

8. To run multiple alignment in parallel, press ‘Ctrl + T’ in the terminal to open a new tab and repeat step 6. You can open as many terminals as you like and leaves them running overnight. 

Disclaimer:
Some packages from other sources are included sorely for convenience to the users. The credits for these packages belong to the original content creators. The packages are:
(1) Bowtie2-2.3.2-legacy URL: http://bowtie-bio.sourceforge.net/bowtie2/index.shtml
(2) IGVtools URL: https://software.broadinstitute.org/software/igv/igvtools
(3) Samtools-1.3.1 URL: http://samtools.sourceforge.net

iSeq is intended to make it easily to align deep sequencing data. The users are solely responsible for output and the use of iSeq. 

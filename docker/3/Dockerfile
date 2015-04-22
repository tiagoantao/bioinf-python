FROM ubuntu:utopic
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y git wget build-essential unzip
RUN apt-get install -y samtools mafft muscle raxml tabix

#R
RUN apt-get install -y r-bioc-biobase

RUN apt-get install -y graphviz libgraphviz-dev pkg-config  # phylo/biopython
RUN apt-get install -y swig  # simupop
RUN apt-get install -y libx11-dev
RUN apt-get install -y libgsl0ldbl

RUN apt-get clean

#genepop
RUN mkdir genepop
WORKDIR /genepop
RUN wget http://kimura.univ-montp2.fr/~rousset/sources.tar.gz
RUN tar zxf sources.tar.gz
RUN g++ -DNO_MODULES -o Genepop GenepopS.cpp -O3
RUN cp Genepop /usr/bin
WORKDIR /
RUN rm -rf genepop

#fastsimcoal
RUN wget http://cmpg.unibe.ch/software/fastsimcoal2/downloads/fsc_linux64.zip
RUN unzip fsc_linux64.zip
RUN chmod a+x fsc_linux64/fsc252
RUN cp fsc_linux64/fsc252 /usr/bin
RUN rm -rf fsc_*

#plink
RUN wget https://www.cog-genomics.org/static/bin/plink150418/plink_linux_x86_64.zip
RUN unzip plink_linux_x86_64.zip
RUN mv plink /usr/bin

#trimal
RUN wget http://trimal.cgenomics.org/_media/trimal.v1.2rev59.tar.gz
RUN tar zxf trimal.v1.2rev59.tar.gz
WORKDIR /trimAl/source
RUN make
RUN cp trimal /usr/bin
WORKDIR /

RUN wget http://repo.continuum.io/miniconda/Miniconda-3.7.3-Linux-x86_64.sh
#Presumes aceptance of the license
RUN bash Miniconda-3.7.3-Linux-x86_64.sh -b
RUN root/miniconda/bin/conda install --yes biopython=1.65 python=3.4
RUN root/miniconda/bin/conda install --yes scipy 
RUN root/miniconda/bin/conda install --yes cython numba
RUN root/miniconda/bin/conda install --yes matplotlib
RUN root/miniconda/bin/conda install --yes ipython-notebook
RUN root/miniconda/bin/conda install --yes binstar
RUN root/miniconda/bin/conda install --yes scikit-learn
RUN root/miniconda/bin/conda install --yes statsmodels
#RUN root/miniconda/bin/conda install --yes pysam
#RUN root/miniconda/bin/conda install -c https://conda.binstar.org/bcbio --yes gffutils
RUN root/miniconda/bin/conda install --yes conda-build
RUN root/miniconda/bin/conda install --yes pip
RUN root/miniconda/bin/conda install --yes requests
RUN root/miniconda/bin/conda install --yes -c https://conda.binstar.org/simupop simuPOP

RUN root/miniconda/bin/pip install rpy2
#RUN root/miniconda/bin/pip install pygraphviz
RUN root/miniconda/bin/pip install seaborn
RUN root/miniconda/bin/pip install pyvcf
#RUN root/miniconda/bin/pip install dendropy
RUN root/miniconda/bin/pip install pexpect
RUN root/miniconda/bin/pip install reportlab
RUN root/miniconda/bin/pip install networkx
RUN root/miniconda/bin/pip install pygenomics

#RUN echo "install.packages('RMySQL', repos='http://cran.us.r-project.org')" > R.inst
RUN echo "install.packages('ggplot2', repos='http://cran.us.r-project.org')" >> R.inst
RUN echo "install.packages('gridExtra', repos='http://cran.us.r-project.org')" >> R.inst
RUN R --no-save <  R.inst

#smartpca
RUN wget https://github.com/DReichLab/EIG/archive/master.zip
RUN unzip master.zip
RUN rm master.zip
RUN cp EIG-master/bin/smartpca /usr/bin



EXPOSE 9875

RUN git clone https://github.com/tiagoantao/bioinf-python.git
WORKDIR /bioinf-python/notebooks

CMD /root/miniconda/bin/ipython notebook --ip=0.0.0.0 --no-browser --port=9875

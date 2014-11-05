FROM ubuntu:utopic
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

##We need this for phylip
#RUN echo 'deb http://archive.ubuntu.com/ubuntu utopic multiverse' >> /etc/apt/sources.list

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y git wget gcc g++ unzip make
#RUN apt-get install -y r-base
#RUN apt-get install -y clustalw fasttree t-coffee
#RUN apt-get install -y bwa ncbi-blast+ emboss clustalo phylip mafft muscle
#RUN apt-get install -y samtools phyml wise raxml language-pack-en
#RUN apt-get install -y embassy-phylip paml probcons

##For BioSQL
#RUN apt-get install -y postgresql

#for Phylo_CDAO
#RUN pip3 install rdflib

RUN apt-get clean

##Database servers
#RUN echo "host    all             all             ::1/128                 trust" > /etc/postgresql/9.3/main/pg_hba.conf
#RUN echo "service postgresql start" > .bashrc
#RUN echo "export LANG=en_US.UTF-8" >> .bashrc
#RUN echo "service postgresql start" > entrypoint.sh
#RUN echo "export LANG=en_US.UTF-8" >> entrypoint.sh

#Manual software


##reportlab fonts
#RUN wget http://www.reportlab.com/ftp/fonts/pfbfer.zip
#WORKDIR cd /usr/lib/python3.4/dist-packages/reportlab
#RUN  mkdir fonts
#WORKDIR cd /usr/lib/python3.4/dist-packages/reportlab/fonts
#RUN unzip /pfbfer.zip
#WORKDIR /
#RUN rm pfbfer.zip

##genepop
#RUN mkdir genepop
#WORKDIR /genepop
#RUN wget http://kimura.univ-montp2.fr/~rousset/sources.tar.gz
#RUN tar zxf sources.tar.gz
#RUN g++ -DNO_MODULES -o Genepop GenepopS.cpp -O3
#RUN cp Genepop /usr/bin
#WORKDIR /
#RUN rm -rf genepop

##fastsimcoal
#RUN wget http://cmpg.unibe.ch/software/fastsimcoal2/downloads/fsc_linux64.zip
#RUN unzip fsc_linux64.zip
#RUN chmod a+x fsc_linux64/fsc251
#RUN cp fsc_linux64/fsc251 /usr/bin
#RUN rm -rf fsc_*

RUN wget http://repo.continuum.io/miniconda/Miniconda3-3.7.0-Linux-x86_64.sh
#Presumes aceptance of the license
RUN bash Miniconda3-3.7.0-Linux-x86_64.sh -b
RUN root/miniconda3/bin/conda install --yes biopython=1.64
RUN root/miniconda3/bin/conda install --yes scipy matplotlib ipython-notebook binstar
RUN root/miniconda3/bin/conda install --yes scikit-learn
RUN root/miniconda3/bin/conda install --yes conda-build

EXPOSE 9875

#WORKDIR /usr/src/notebook

CMD /root/miniconda3/bin/ipython notebook --ip=0.0.0.0 --no-browser --port=9875
#RUN echo "echo hello" > entrypoint.sh
#RUN echo "echo hello" >> entrypoint.sh
#ENTRYPOINT bash entrypoint.sh


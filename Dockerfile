FROM osgeo/gdal
# # FROM python:3

RUN apt-get update
RUN apt install -y python3-pip
#ENV TINI_VERSION v0.6.0
#ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
#RUN chmod +x /usr/bin/tini


# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

#ADD src /app
#ADD requirements.txt /requirements.txt
#RUN pip install -r /requirements.txt
#RUN pip install debugpy -t /tmp
RUN pip install jupyterlab
RUN pip install runipy 
RUN pip install pandas 
RUN pip install matplotlib 
RUN pip install plotly 
RUN pip install gdal 
RUN pip install georaster
RUN pip install scipy
RUN pip install pyproj
RUN pip install basemap

RUN useradd jupyter

RUN mkdir /home/jupyter
#ADD documenttoadd /home/jupyter/

RUN chown -R jupyter:jupyter /home/jupyter

USER jupyter
WORKDIR /home/jupyter

COPY plot_geotiff.py /home/jupyter/

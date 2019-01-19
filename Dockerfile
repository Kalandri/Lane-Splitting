FROM tensorflow/tensorflow:latest-py3
ADD . /developer
RUN apt-get update && apt-get install -y \
    libsm6 \
    libxrender1 \
    libxext6 \
    nano

RUN pip install \
    tensorflow \
    numpy \
    scipy \
    opencv-python \
    pillow \
    matplotlib \
    h5py \
    keras

RUN pip3 install \
    https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.2/imageai-2.0.2-py3-none-any.whl
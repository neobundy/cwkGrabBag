1. Generate `requirements.txt` from yaml file. Ask your GPT to do it for you. Specifically ask it to include only pip packages. Otherwise you'd have to repeat the process of removing the conda packages from the `requirements.txt` file.

```bash
  pip install --use-pep517 -r requirements.txt
```

`--use-pep517` is used to force the use of PEP 517 for building the wheel, without it the installation may fail.

2. Some errors may occur during the installation due to conda-specific packages. Ask your GPT to remove them from the `requirements.txt` file, and then install them manually. Better yet, ask your GPT to seprate the conda packages from the pip packages in the first place.

Note that MKL(Math Kernel Library by Intel) should be installed separately due to licensing shit. Go ahead and go through the hassle if you do need them.

```bash
conda install \
    bzip2 \
    ca-certificates \
    jpeg \
    libpng \
    libtiff \
    freetype \
    zlib \
    lz4-c \
    eigen \
    glib \
    gstreamer \
    gst-plugins-base \
    hdf5 \
    libwebp \
    libvorbis \
    libprotobuf \
    openssl \
    sqlite \
    tk \
    xz \
    zstd
```

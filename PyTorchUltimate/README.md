# What's in this folder?

Just a bunch of files modified or added for the following course to work on Apple Silicon:

# PyTorch Ultimate 2024 - From Basics to Cutting-Edge

👉 PyTorch Ultimate 2024 - From Basics to Cutting-Edge
https://www.oreilly.com/videos/pytorch-ultimate-2024/9781801070089/

👉 GitHub Repository:
https://github.com/DataScienceHamburg/PyTorchUltimateMaterial

## Installation

1. Generate `requirements.txt` from the YAML file provided in the author's repo. Ask your GPT to do it for you, specifically to include only pip packages. Otherwise, you'd go back and forth with your GPT repeatedly removing the conda packages from the `requirements.txt` file.

```bash
  pip install --use-pep517 -r requirements.txt
```

`--use-pep517` is used to force the use of PEP 517 for building the wheel; without it, the installation may fail.

2. Some errors may occur during the installation due to conda-specific packages. Ask your GPT to remove them from the `requirements.txt` file and install them manually. Better yet, ask your GPT to separate the conda packages from the pip packages in the first place.

Note that MKL (Math Kernel Library by Intel) should be installed separately due to licensing issues. Go ahead and deal with the hassle if you need them.
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

## Files

- `requirements.txt` (generated from the YAML file removing conda packages)

- `install-conda-packages.sh`(script to install conda packages separately)
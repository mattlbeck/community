tag: terminal
and tag: user.conda
-
conda create:
    insert("conda env create -f environment.yml")

conda update:
    insert("conda env update -f environment.yml")
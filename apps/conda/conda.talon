tag: terminal
tag: user.conda
-
conda create:
    insert("conda env create -f environment.yml")

conda update:
    insert("conda update -f environment.yml")

conda activate <user.environment_name>:
    insert("conda activate " + environment_name)  
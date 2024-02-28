os: mac
mode: command
-
# Homerow (with search + labels enabled)
^ax: user.homerow()

# Work around a rare word being inserted instead of "ax…" in mixed mode
# "Axtell" instead of "ax tell"
^Axtell: user.homerow_search("tell")

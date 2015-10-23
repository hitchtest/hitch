Package Isolation
-----------------

Hitch provides package isolation by shunning system packages
and, where it can, downloading and compiling its own.

It stores these packages in the ~/.hitchpkg directory. This
directory can contain multiple versions of the same software
side by side (e.g. postgresql) and they will not conflict.

Why does my test require me to sudo and install packages?
=========================================================

Some of your tests may require you to install packages using sudo - e.g. when running
any test that requires postgres, you will need the "libpq-dev" package. Hitch should
be smart enough to figure out the equivalent on your computer (e.g. postgresql-libs on
Arch).

If you enter your sudo password, it should install the package for you before
continuing.

What if I don't trust the test to use sudo?
-------------------------------------------

When your tests attempt to use sudo to install packages, it will print the command
you need to run to install the packages. If you like, you can copy and paste the
command in a separate window and run it there instead.

When it has finished, simply hit enter three times in your paused test so that you
see this::

  [sudo] password for yourusername:
  Sorry, try again.
  [sudo] password for yourusername:
  Sorry, try again.
  [sudo] password for yourusername:
  Sorry, try again.
  sudo: 3 incorrect password attempts

After that, your test will verify once again if the package is installed. If it
is, it will continue happily.

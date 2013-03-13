PyCon 2013 Scikit-learn Tutorial
================================

*Instructor: Jake VanderPlas*

This repository will contain files and other info associated with my PyCon
2013 scikit-learn tutorial.  I anticipate working on this during the weeks
leading up to PyCon, so check back here often for updates!

Installation Notes
------------------
This tutorial will require recent installations of *numpy*, *scipy*,
*matplotlib*, *scikit-learn*, and *ipython* with ipython notebook.
The last one is important: you should be able to type

    ipython notebook

in your terminal window and see the notebook panel load in your web browser.
Because Python 3 compatibility is still being ironed-out for these packages
(we're getting close, I promise!) participants should plan to use Python 2.6
or 2.7 for this tutorial.

For users who do not yet have these  packages installed, a relatively
painless way to install all the requirements is to use a package such as
[Anaconda CE](http://store.continuum.io/ "Anaconda CE"), which can be
downloaded and installed for free.

Downloading the Tutorial Materials
----------------------------------
I would highly recommend using git, not only for this tutorial, but for the
general betterment of your life.  Once git is installed, you can clone the
material in this tutorial by using the git address shown above:

    git clone git://github.com/jakevdp/sklearn_pycon2013.git

If you can't or don't want to install git, there is a link above to download
the contents of this repository as a zip file.

Data Downloads
--------------
The data for this tutorial is not included in the repository.  We will be
using several data sets during the tutorial: most are built-in to scikit-learn,
and one is culled from the
[Sloan Digital Sky Survey](http://skyserver.sdss.org/public/en/)
The tutorial includes code which automatically downloads and caches these
data.  Because the wireless network
at conferences can often be spotty, it would be a good idea to download these
data sets before arriving at the conference.

To cache the required data on your computer, please download the tutorial
materials as described above, and execute the script called
``download_data.py`` in this directory.  It will cache several datasets to
the appropriate places.
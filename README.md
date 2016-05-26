PyCon 2013 Scikit-learn Tutorial
================================

**Note: for updated tutorial content, please see** http://github.com/jakevdp/sklearn_tutorial/

*Instructor: Jake VanderPlas*

- email: <jakevdp@cs.washington.edu>
- twitter: [@jakevdp](https://twitter.com/jakevdp)
- github: [jakevdp](http://github.com/jakevdp)

This repository will contain files and other info associated with my PyCon
2013 scikit-learn tutorial.

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
the contents of this repository as a zip file.  I may make minor changes to
the repository in the days before the tutorial, however, so cloning the
repository is a much better option.

Data Downloads
--------------
The data for this tutorial is not included in the repository.  We will be
using several data sets during the tutorial: most are built-in to
scikit-learn, and one is culled from the
[Sloan Digital Sky Survey](http://skyserver.sdss.org/public/en/).
The tutorial includes code which automatically downloads and caches these
data.  Because the wireless network
at conferences can often be spotty, it would be a good idea to download these
data sets before arriving at the conference.

To cache the required data on your computer, please download the tutorial
materials as described above, and execute the script called
``download_data.py`` from the top directory.  It will cache several datasets
to the appropriate places, and you'll be ready to go when it comes time for
the tutorial!


Notebook Listing
----------------
These notebooks in this repository can be statically viewed using the
excellent [nbviewer](http://nbviewer.ipython.org) site.  They will not
be able to be modified within nbviewer.  To modify them, first download
the tutorial repository, change to the notebooks directory, and type
``ipython notebook``.  You should see the list in the ipython notebook
launch page in your web browser.

- [01_introduction.ipynb](http://nbviewer.ipython.org/urls/raw.github.com/jakevdp/sklearn_pycon2013/master/notebooks/01_introduction.ipynb)
- [02_sklearn_data.ipynb](http://nbviewer.ipython.org/urls/raw.github.com/jakevdp/sklearn_pycon2013/master/notebooks/02_sklearn_data.ipynb)
- [03_machine_learning_101.ipynb](http://nbviewer.ipython.org/urls/raw.github.com/jakevdp/sklearn_pycon2013/master/notebooks/03_machine_learning_101.ipynb)
- [04_houses_regression.ipynb](http://nbviewer.ipython.org/urls/raw.github.com/jakevdp/sklearn_pycon2013/master/notebooks/04_houses_regression.ipynb)
- [05_iris_classification.ipynb](http://nbviewer.ipython.org/urls/raw.github.com/jakevdp/sklearn_pycon2013/master/notebooks/05_iris_classification.ipynb)
- [06_iris_dimensionality.ipynb](http://nbviewer.ipython.org/urls/raw.github.com/jakevdp/sklearn_pycon2013/master/notebooks/06_iris_dimensionality.ipynb)
- [07_iris_clustering.ipynb](http://nbviewer.ipython.org/urls/raw.github.com/jakevdp/sklearn_pycon2013/master/notebooks/07_iris_clustering.ipynb)
- [08_linearly_separable.ipynb](http://nbviewer.ipython.org/urls/raw.github.com/jakevdp/sklearn_pycon2013/master/notebooks/08_linearly_separable.ipynb)
- [09_validation_and_testing.ipynb](http://nbviewer.ipython.org/urls/raw.github.com/jakevdp/sklearn_pycon2013/master/notebooks/09_validation_and_testing.ipynb)
- [10_digits_classification.ipynb](http://nbviewer.ipython.org/urls/raw.github.com/jakevdp/sklearn_pycon2013/master/notebooks/10_digits_classification.ipynb)
- [11_photoz_regression.ipynb](http://nbviewer.ipython.org/urls/raw.github.com/jakevdp/sklearn_pycon2013/master/notebooks/11_photoz_regression.ipynb)

Note that some of the code in these notebooks will not work outside the
directory structure of this tutorial.

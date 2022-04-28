Make Label
==========

Utility to create address labels from a csv file.

Based on an idea found here:
https://g-thomson.blog/posts/spreadsheet-to-print-labels-in-python/

The original was to print labels to classify jars with collected seeds. I
adjusted this to print address labels instead.

Note that the default address template here uses dutch variable names:
naam = name
straat = address (street + housenumber)
postcode = zip
plaats = city

The names used in the template must be present as column-headers in the csv file.

Also note that I assume here that the semicolon, ";" will be used as a field-
separator.

Installation:

- clone this repository

- create a venv:

  `$ python3 -m venv venv`

  `$ . venv/bin/activate`

  `$ pip --install --upgrade pip`

  `$ pip install -r requirements.txt`

- Run the make_label.py script which will create one label per page:

  `$ python make_labels.py -i ~/Documents/my-subdirectory/input.csv`

- Run the pdfnup command to create labels. In this case 3 in a row, 8 rows on a
  page (Like Avery 3474):

  `$ pdfjam --suffix nup --no-landscape --nup 3x8 output.pdf`

Note: the pdfjam command on Debian/Mxlinux is part of the texlive-extra-utils package.
      Apart from that the texlive-latex-recommended package is needed.

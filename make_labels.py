#! /usr/bin/env python

import click
import pandas as pd
from blabel import LabelWriter


@click.command()
@click.option(
    "-i",
    "--input",
    required=True,
    type=str,
    help="CSV file with columns that match the variables in the HTML template",
)
@click.option(
    "-o", "--output", default="output.pdf", type=str, help="Name of the output PDF"
)
@click.option(
    "-t",
    "--template",
    default="address_label_template.html",
    type=str,
    help="Name of the HTML template file",
    show_default="address_label_template.html",
)
@click.option(
    "-s",
    "--style",
    default="style.css",
    type=str,
    help="Name of the CSS file",
    show_default="style.css",
)
def write_labels(input, output, template, style):
    df = pd.read_csv(input, sep=";")
    records = df.to_dict("records")
    label_writer = LabelWriter(template, default_stylesheets=(style,))
    label_writer.write_labels(records, target=output)


if __name__ == "__main__":
    write_labels()

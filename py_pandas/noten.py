"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""
import argparse
import os
import sys
import pandas as pd
import re


def read_csv(file_path: str, delimiter: str = ';') -> pd.DataFrame:
    """
    Read a CSV file and return a pandas DataFrame.
    """
    if not os.path.exists(file_path):
        sys.stderr.write(f"Error: File '{file_path}' does not exist.\n")
        sys.exit(1)
    try:
        return pd.read_csv(file_path, delimiter=delimiter, dtype=str)
    except pd.errors.EmptyDataError:
        sys.stderr.write(f"Error: File '{file_path}' is empty.\n")
        sys.exit(1)


def read_xml(file_path: str) -> pd.DataFrame:
    """
    Read an XML file and return a pandas DataFrame.
    """
    if not os.path.exists(file_path):
        sys.stderr.write(f"Error: File '{file_path}' does not exist.\n")
        sys.exit(1)

    with open(file_path) as f:
        content = f.read()

    pattern = re.compile(
        r'<Schueler>\s*<Nummer>(.*?)</Nummer>\s*<Anrede>(.*?)</Anrede>\s*<Vorname>(.*?)</Vorname>\s*<Nachname>('
        r'.*?)</Nachname>\s*<Geburtsdatum>(.*?)</Geburtsdatum>\s*<Geschlecht>(.*?)</Geschlecht>\s*<Postleitzahl>('
        r'.*?)</Postleitzahl>\s*<Ort>(.*?)</Ort>\s*<Straße>(.*?)</Straße>\s*<Hausnummer>('
        r'.*?)</Hausnummer>\s*<Lieblingsfarbe>(.*?)</Lieblingsfarbe>\s*<Lieblingsspeise>('
        r'.*?)</Lieblingsspeise>\s*<Groesse>(.*?)</Groesse>\s*<Gewicht>(.*?)</Gewicht>',
        flags=re.DOTALL)

    results = re.findall(pattern, content)
    columns = ["Nummer", "Anrede", "Vorname", "Nachname", "Geburtsdatum", "Geschlecht", "Postleitzahl", "Ort", "Straße",
               "Hausnummer", "Lieblingsfarbe", "Lieblingsspeise", "Groesse", "Gewicht"]
    return pd.DataFrame(results, columns=columns, dtype=str)


def merge_dataframes(df1: pd.DataFrame, df2: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Merges two DataFrames on a specified column.


    >>> df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    >>> df2 = pd.DataFrame({'A': [1, 2], 'C': [5, 6], 'D': [7, 8]})
    >>> merge_dataframes(df1, df2, 'A')
       A  B  C  D
    0  1  3  5  7
    1  2  4  6  8
    """
    try:
        return pd.merge(df1, df2, on=column_name)
    except KeyError:
        sys.stderr.write(f"Error: Column '{column_name}' not found in DataFrames.\n")
        sys.exit(1)


def filter_dataframe(df: pd.DataFrame, selected_subject: str) -> pd.DataFrame:
    """Filters a DataFrame based on a column value."""
    if selected_subject not in df.columns:
        raise ValueError(f"Das ausgewählte Fach '{selected_subject}' ist nicht in den Spalten vorhanden.")

    return df[['Nummer', selected_subject]]


def calculate_average(df: pd.DataFrame, selected_column: list) -> pd.DataFrame:
    """Calculates the average of selected columns."""
    df['Durchschnitt'] = df[selected_column].astype(float).mean(axis=1)
    return df


def write_csv(df: pd.DataFrame, output_file: str) -> None:
    """Writes a DataFrame to a CSV file."""
    df.to_csv(output_file, index=False)


def main():
    parser = argparse.ArgumentParser(description="noten.py by Filip Ilic / HTL Rennweg")
    parser.add_argument("outfile", help="Output file (e.g., result.csv)")
    parser.add_argument("-n", help="csv-Datei mit den Noten der Schüler")
    parser.add_argument("-s", help="xml-Datei mit den Schülerdaten")
    parser.add_argument("-m", default="Nummer", help="Name der Spalte, die zu verknüpfen ist (default = Nummer)")
    parser.add_argument("-f", help="Name des zu filternden Gegenstandes (z.B. SEW)")
    parser.add_argument("-d", help="Debug Modus")
    verbosity_group = parser.add_mutually_exclusive_group()
    verbosity_group.add_argument("-v", "--verbose", action="store_true", help="Gibt die Daten Kommandozeile aus")
    verbosity_group.add_argument("-q", "--quiet", action="store_true", help="keine Textausgabe")
    args = parser.parse_args()

    try:
        grades_df = read_csv(args.n)
        student_df = read_xml(args.s)

        if args.d:
            sys.stdout.write(f"Grades: Dataframe with {grades_df.shape[0]} rows and {grades_df.shape[1]} columns\n")
            sys.stdout.write(str(grades_df.head(5)))
            sys.stdout.write(f"Students: Dataframe with {student_df.shape[0]} rows and {student_df.shape[1]} columns\n")
            sys.stdout.write(str(student_df.head(5)))

    except pd.errors.ParserError as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)

    try:
        # Merge DataFrames
        merged_df = merge_dataframes(grades_df, student_df, args.m)
    except KeyError:
        sys.stderr.write(f"Error: Column '{args.m}' not found in DataFrames.\n")
        sys.exit(1)

    # Filter DataFrame

    if args.f:
        subjects_to_keep = ['E', 'RK', 'D', 'GGP', 'WIR', 'BSP', 'AM', 'NW', 'SEW', 'ITP', 'INSI', 'NWT']
        write_csv(filter_dataframe(merged_df, subjects_to_keep), args.outfile)
    else:
        write_csv(merged_df, args.outfile)

    # Output verbosity
    if not args.quiet:
        if args.verbose:
            print(f"csv-Datei mit den Noten: {args.n}")
            print(f"xml-Datei mit den Schülerdaten: {args.s}")
            print(f"Name der Spalte, die zu verknüpfen ist: {args.m}")
        print(f"Output-Datei: {args.outfile}")


if __name__ == "__main__":
    main()

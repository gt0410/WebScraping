


# -*- coding: utf-8 -*-
# Example main.py
import argparse

import project0

def main(url):
    # Download data
    data = project0.fetchincidents(url)

    # Extract Data
    incidents = project0.extractincidents()

    # Create Dataase
    project0.createdb()

    # Insert Data
    project0.populatedb(incidents)

    # Print Status
    s = project0.status()
    print(s)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--arrests", type=str, required=True,
                         help="The arrest summary url.")

    args = parser.parse_args()
    if args.arrests:
        main(args.arrests)


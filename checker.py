#!/usr/bin/env python

import argparse
import sys
import re
import csv
from pip.utils import get_installed_distributions

# Specify the information you would like to
# gather on each package for your project.
data_to_collect = [
    'License: ',
    'Home-page: ',
    'Version: ',
    'Requires-Dist: '
]

# By default hide the following python packages.
filter_out_sys_packages = ['wheel', 'setuptools', 'pip']

parser = argparse.ArgumentParser(description="Lists all installed packages from sys.path.")
parser.add_argument("-t", "--terminal", help="writes out data to terminal", action="store_true")
parser.add_argument("-f", "--file", help="writes out data to a CSV file", action="store_true")
args = parser.parse_args()


def collect_meta():
    """Gathers data_to_collect from all packages metadata"""
    meta_files_to_check = ['PKG-INFO', 'METADATA']
    packages = []

    for installed_distribution in get_installed_distributions():
        for metafile in meta_files_to_check:
            if not installed_distribution.has_metadata(metafile):
                continue
            package = {}
            l = []
            for line in installed_distribution.get_metadata_lines(metafile):
                if re.compile('|'.join(data_to_collect), re.IGNORECASE).search(line):
                    (k, v) = line.split(': ', 1)
                    if k not in package:
                        package[k] = v
                    else:
                        l.append(v)
            package['Requires-Dist'] = ' | '.join(l)
            package['Package'] = installed_distribution.project_name
            packages.append(package)

    return packages


def write_csv(packages):
    """Generates CSV file."""
    try:
        with open('project_packages.csv', 'w') as csvfile:
            dict_writer = csv.DictWriter(csvfile, fieldnames=packages[0].keys())
            dict_writer.writeheader()
            dict_writer.writerows(packages)
            # for package in packages:
            #     if package['Requires-Dist']:
            #         dict_writer.writerow(', '.join(package['Requires-Dist']))
            #     else:
            #         dict_writer.writerow(package)
    except IOError as (errno, strerror):
        print("I/O Error({0}): {1}").format(errno, strerror)
    return


def print_data(packages):
    """Writes packages to terminal"""
    sys.stdout.write('Your Projects package information:\n********\n')
    for i in packages:
        sys.stdout.write(
            "{project_name}: {version}\n"
            "License: {license} Home-page: {license}\n"
            "Requires: {requires_dist}\n-----\n".format(
                project_name=i['Package'],
                version=i['License'],
                license=i['Home-page'],
                requires_dist=i['Requires-Dist']
            )
        )


def filtered_packages(packages):
    """Writes packages to terminal"""
    filtered_packages = []
    for i in packages:
        if i['Package'] not in filter_out_sys_packages:
            filtered_packages.append(i)
    return filtered_packages


def main():
    all_packages = collect_meta()
    non_sys_packages = filtered_packages(all_packages)

    if args.terminal:
        print_data(non_sys_packages)
    elif args.file:
        write_csv(non_sys_packages)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()

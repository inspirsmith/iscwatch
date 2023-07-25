# iscwatch - A Command Line Application For Monitoring Intel Security Center Product Advisories

![Version](https://img.shields.io/badge/version-0.3.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Description

`iscwatch` is a command line application that searches for summaries of [Intel's Security Center Product Advisories](https://www.intel.com/content/www/us/en/security-center/default.html) and outputs those summaries in CSV format. Included in the output per advisory is its title, full text url, advisory ID, updated date, and released date.

## Features

- Fetches summaries of Intel's Security Center Product Advisories.
- Outputs advisory data in CSV format to stdout.
- Optionally filters advisories based on date using the --since option.
- Enables or disables CSV column headers with --headers and --no-headers options, respectively.

## Installation

You can install `iscwatch` using pip:

```
pip install iscwatch
```

## Usage

```
Usage: iscwatch [OPTIONS]

Retrieve Security Advisory summaries from Intel website and output as CSV.

Options
--since                     Output only those summaries released or updated since specified date. [default: None]
--version    --no-version   Output product version and exit. [default: no-version]
--headers    --no-headers   Include column headers in CSV output. [default: headers]
--help                      Show this message and exit.
```

The application will fetch the latest advisories from Intel's Security Center and display the summaries in CSV format to the standard output (stdout). You can redirect the output to a file if needed:

```bash
iscwatch > advisories.csv
```

## CSV Format

The CSV output will contain the following columns:

- Advisory Title
- Advisory Page Link
- Advisory ID
- Updated Date
- Released Date

```bash
> iscwatch --since 2023-07-01 --no-headers
2023.2 IPU – BIOS Advisory,https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00807.html,INTEL-SA-00807,2023-07-07,2023-05-09
Intel® NUC Laptop Kit Advisory,https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00712.html,INTEL-SA-00712,2023-07-07,2022-08-09
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to create an issue or submit a pull request.

## Acknowledgments

- This application relies on Intel's Security Center for fetching advisories data.

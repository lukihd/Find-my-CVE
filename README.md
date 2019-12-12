# CVE_Download

Download cvedetails.com's CVEs by product in JSON format.

## Install

```
git clone https://github.com/lukihd/Find-my-CVE/tree/cve_download
```

## Usage

```
./cve_dl.sh --id </xxx/yyy> --prod <product-name> --pages <total-of-pages>
```

## help

```
./cve-dl.sh --help
Usage : ./test.sh --id </xxx/yyy> --prod <product-name> --pages <total-of-pages>

xxx -> vendor_id
yyy -> product_id
pages -> go on 'All Versions' page of the product to look at

Example : ./test.sh --id /45/66/ --prod /Apache-Http-Server --pages 6

https://cvedetails.com/

More info at : https://github.com/lukihd/Find-my-CVE
```

### This script is not finished

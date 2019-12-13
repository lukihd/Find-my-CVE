# CVE_Download

Download [CVEdetails](https://cvedetails.com)'s CVEs by product in JSON format.

## Requirement

* [Pup](https://github.com/EricChiang/pup)

```
go get github.com/ericchiang/pup
```

## Install

```
git clone https://github.com/lukihd/Find-my-CVE/tree/cve_download
```

## Usage

```
./cve_dl.sh --id </xxx/yyy> --prod </product-name> --pages <total-of-pages>
```

## Example

```
./test.sh --id /45/66/ --prod /Apache-Http-Server --pages 6
```

## Help


All these variables can be find at [CVEdetails](https://cvedetails.com)
```
xxx -> vendor_id
yyy -> product_id
pages -> total of pages at 'All Versions' page of the product
```

### This script is not finished


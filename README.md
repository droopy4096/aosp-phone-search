# Intro

Set of tools to parse phone data from GSM Arena's filtered search, and LineageOS device list page.

# Usage

## Quick environment setup

create directories for storing data:

```shell
mkdir -p data/{inputs,outputs}
```

## Get list of phones from GSM Arena

1. Using [search](https://www.gsmarena.com/search.php3) function get page with the list of phones you're interested in.
2. Save page into `data/inputs/myphones.html` 

## Generate a simplified list of desired phones

```shell
./gsm_arena_devices.sh inputs/myphones.html > outputs/myphones.list
```

## Get List of LineageOS supported phones

1. Open [Lineage OS Devices](https://wiki.lineageos.org/devices/) page
2. Save page into `data/inputs/los-devices.list`

## Generate simplified list of LOS phones

```shell
./los_device_list.sh data/inputs/los-devices.html
```

## Compare the lists

provided `word_diff.py` tool is opinionative and biased towards provided phone lists trying to find the closest matches between two lists specified:

```shell
python word_diff.py data/outputs/los_device.list data/outputs/myphones.list
```

Due to differences in notation etc. it's hard to find exact matches, thus tool produces colorized output similar to following:

```
Motorola: edge
Samsung: Galaxy Note10+ 5G
Sony: Xperia 1 II
Xiaomi: Mi 11 Lite 5G

Asus: ZenFone 8 
Asus: Zenfone 8 Flip 

Motorola: edge 20 
Motorola: Edge 20 Lite 

Motorola: edge 20 pro 
Motorola: Edge 20 Lite 

Samsung: Galaxy A52 4G 
Samsung: Galaxy A52 5G 

Samsung: Galaxy S10 5G 
Samsung: Galaxy A33 5G 

Samsung: Galaxy S10 5G 
Samsung: Galaxy A42 5G 

Xiaomi: Xiaomi 11 Lite 5G NE / 11 Lite NE 5G / Mi 11 LE 
Xiaomi: 11 Lite 5G NE 
```

first 4 lines are exact matches - i.e. phones that were found in both lists. Following line pairs is tool's attempt to find lines where at least 75% of the words from one string have a match in a second string (as could be seen by the last match).

unfortunately that produces a rather "noisy" output, however it does help to narrow down the search significantly.
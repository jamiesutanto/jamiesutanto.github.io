# hugo-theme-comic: Hugo Comic Theme

Don't worry, this theme does not change your Hugo site's default font to <span style="font-family: &quot;Comic Sans MS&quot;, &quot;Comic Sans&quot;, cursive;">Comic Sans</span>. 😌

Instead, it renders comic strips that are organized by date:

![alt text](https://gitlab.com/mrubli/hugo-theme-comic/-/raw/master/images/screenshot.png){width=532px}

## Features

* Home view with a jump list to each year and the most recent strips
* Yearly view with a jump list to each month
* Monthly view
* Menu for fast year selection

## Demo

[Hugo Comic Theme Demo](https://mrubli.gitlab.io/hugo-xkcd/)

[Source code for the demo site](https://gitlab.com/mrubli/hugo-xkcd/)

The comic strips for the demo site are from: https://xkcd.com/

## Installation

Download the theme:
```sh
mkdir themes
cd themes
git clone https://gitlab.com/mrubli/hugo-theme-comic
```

Update your Hugo site configuration file (e.g. `hugo.yaml`) to include this line:
```yaml
theme: hugo-theme-comic
```

## Directory structure

The comic strip files are expected to live in the `content/` directory, in a `yyyy/mm/yyyy-mm-dd.ext` structure.
Furthermore, all directories must contain an empty `_index.md` file, so that Hugo processes the directory.

For example:
```
content/
└── 2024
    ├── 01
    │   ├── 2024-01-01.jpg
    │   ├── 2024-01-02.jpg
    │   ├── 2024-01-03.jpg
    │   ├── …
    │   ├── 2024-01-31.jpg
    │   └── _index.md
    ├── 02
    │   ├── 2024-02-01.jpg
    │   ├── …
    │   └── _index.md
```

The following command can be used to create `_index.md` files in all relevant directories.

```
find content/???? -type d -exec touch {}/_index.md \;
```

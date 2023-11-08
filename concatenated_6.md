# quarto-web/docs/authoring/code-annotation-example/revealjs.qmd

---
format: revealjs
code-annotations: hover
---

## Reveal Presentation

``` r
library(tidyverse)
library(palmerpenguins)
penguins |>                                      # <1>
  mutate(                                        # <2>
    bill_ratio = bill_depth_mm / bill_length_mm, # <2>
    bill_area  = bill_depth_mm * bill_length_mm  # <2>
  )                                              # <2>
```

1.  Take `penguins`, and then,
2.  add new columns for the bill ratio and bill area.


# quarto-web/docs/authoring/_embed-examples/sample-notebook-view.qmd

---
title: Exploration of penguin characteristics
author: Norah Jones
toc: true
notebook-view:
  - notebook: penguins.ipynb
    title: "Plots and Computations"
    url: https://colab.research.google.com/drive/12GsIPQ644SI4vkEEHiZn-Qqfbr-bD1
---

## How distinct are the species on the bill dimensions?

One interesting aspect of penguins is their bill shapes. Different species of penguins have bills that are adapted to their specific diet and habitat. 

{{< embed ../penguins.ipynb#fig-bill-marginal >}}

## What if we look at both dimensions together?


# quarto-web/docs/authoring/_embed-examples/sample.qmd

---
title: Exploration of penguin characteristics
author: Norah Jones
toc: true
---

## How distinct are the species on the bill dimensions?

One interesting aspect of penguins is their bill shapes. Different species of penguins have bills that are adapted to their specific diet and habitat. 

{{< embed ../penguins.ipynb#fig-bill-marginal >}}

## What if we look at both dimensions together?

# quarto-web/docs/download/prerelease.qmd

---
title: "{{< meta prerelease-title >}} Builds"
subtitle: "Install a {{< meta prerelease-lower >}} build of Quarto."
format:
  html:
    include-in-header: 
      - '_download.html'
    include-after-body: 
      text: |
        <script type="text/javascript">
        window['quarto-download-prerelease'] = true;
        window['quarto-download-archives'] = true;
        window["quarto-prerelease-mode"] = '{{< meta prerelease-mode >}}';
        </script>
page-layout: full
toc: false
anchor-sections: false
editor: source
image: /images/hero_right.png
---

::: {.content-visible when-profile="prerelease"}

:::{.callout-note}
Pre-release builds are intended for testing purposes, and are not recommended for general use. For stable builds, please visit [Release Builds](release.qmd).
:::

:::

{{< include _download-pre.md >}}


# quarto-web/docs/download/tarball.qmd

---
title: Tarball Installation On Linux
format:
  html:
    include-in-header: 
      - '_download.html'
    include-after-body: tarball-after-body.html
search: false
---

::: {#download-button .download-button}
<div>

[\_](_ "Download Quarto"){#download-url .btn .btn-action .btn-action-primary}
[Find your operating system in the table below]{#download-text .hidden .download-text}

</div>
:::


You can install Quarto for a single user on Linux by using the Quarto tarball and following the below set of steps. 

**1. Download the tarball**

```{.bash filename="Terminal"}
wget https://github.com/quarto-dev/quarto-cli/releases/download/v^version^/quarto-^version^-linux-amd64.tar.gz
```

**2. Extract Files**

Extract the contents of the tarball to the location where you typically install software (e.g. `~/opt`). For example:

```{.bash filename="Terminal"}
mkdir ~/opt
tar -C ~/opt -xvzf quarto-^version^-linux-amd64.tar.gz
```

**3. Create a Symlink**

Create a symlink to `bin/quarto` in a folder that is in your path. If there is no such folder, you can create a folder such as `~/bin` and place the symlink there. For example:

For example:

```{.bash filename="Terminal"}
mkdir ~/bin
ln -s ~/opt/quarto-^version^/bin/quarto ~/bin/quarto
```

**4. Add Folder to Path**

Ensure that the folder where you created a symlink is in the path. For example:

```{.bash filename="Terminal"}
( echo ""; echo 'export PATH=$PATH:~/bin\n' ; echo "" ) >> ~/.profile
source ~/.profile
```

**5. Check The Installation**

Use `quarto check` to confirm that the installation is successful:

```{.bash filename="Terminal"}
quarto check
```




# quarto-web/docs/download/index.qmd

---
title: "Download Quarto"
subtitle: "Install a release or pre-release build of Quarto."
format:
  html:
    include-in-header: 
      - '_download.html'
    include-after-body: 
      text: |
        <script type="text/javascript">
        window['quarto-download-prerelease'] = true;
        window['quarto-download-release'] = true;
        window['quarto-download-archives'] = true;
        window["quarto-prerelease-mode"] = '{{< meta prerelease-mode >}}';
        </script>
page-layout: full
toc: false
anchor-sections: false
editor: source
image: /images/hero_right.png
listing:
  id: download-older
  contents: 
    - id: version12
      title: v1.2.475
      date: 2023/03/22
      path: https://github.com/quarto-dev/quarto-cli/releases/tag/v1.2.475
    - id: version11
      title: v1.1.189
      date: 2022/09/04
      path: https://github.com/quarto-dev/quarto-cli/releases/tag/v1.1.189
    - id: version10
      title: v1.0.38
      date: 2022/08/04
      path: https://github.com/quarto-dev/quarto-cli/releases/tag/v1.0.38
  fields: 
    - title
    - date
    - path
  field-display-names: 
    path: "Url"
  field-links: 
    - path
    - title
  type: table
  filter-ui: false
  sort-ui: false
---


::: {.content-visible when-profile="rc"}

::: {.panel-tabset}

## **{{< meta prerelease-title >}}** --- v[]{.download-pre-version}

{{< include _download-pre.md >}}


## **Current Release** --- v[]{.download-version}

{{< include _download.md >}}

## **Older Releases**

Pages containing all installers for the most recent releases of older versions of Quarto are linked below.

:::{#download-older}

:::

:::

:::

::: {.content-hidden when-profile="rc"}

::: {.panel-tabset}

## **Current Release** --- v[]{.download-version}

{{< include _download.md >}}

## **{{< meta prerelease-title >}}** --- v[]{.download-pre-version}

{{< include _download-pre.md >}}

## **Older Releases**

Pages containing all installers for the most recent releases of older versions of Quarto are linked below.

:::{#download-older}

:::

:::

:::





# quarto-web/docs/download/release.qmd

---
title: "Release Builds"
subtitle: "Install a release build of Quarto."
format:
  html:
    include-in-header: 
      - '_download.html'
    include-after-body: 
      text: |
        <script type="text/javascript">
        window['quarto-download-release'] = true;
        window['quarto-download-archives'] = true;
        </script>
page-layout: full
toc: false
anchor-sections: false
editor: source
image: /images/hero_right.png
---

{{< include _download.md >}}


# quarto-web/docs/dashboards/index.qmd

---
title: "Quarto Dashboards"
code-annotations: select
lightbox: auto
format:
  html:
    include-in-header: 
      - '../download/_download.html'
    include-after-body: 
      text: |
        <script type="text/javascript">
        window['quarto-download-release'] = true;
        window['quarto-download-prerelease'] = true;
        window['quarto-download-nonews'] = true;
        window["quarto-prerelease-mode"] = '{{< meta prerelease-mode >}}';
        </script>   
---

{{< include /docs/prerelease/1.4/_pre-release-feature.qmd >}}

## Overview

Quarto Dashboards make it easy to create interactive dashboards using Python, R, Julia, and Observable:

-   Publish a group of related data visualizations as a dashboard. Use a wide variety of components including [Plotly](https://plotly.com/python/), [Leaflet](https://ipyleaflet.readthedocs.io/en/latest/), [Jupyter Widgets](/docs/interactive/widgets/jupyter.qmd), [htmlwidgets](https://www.htmlwidgets.org/); static graphics (Matplotlib, Seaborn, ggplot2, etc.); tabular data; value boxes; and text annotations.

-   Flexible and easy to specify row and column-based [Layouts](layouts.qmd). Components are intelligently re-sized to fill the browser and adapted for display on mobile devices.

-   Author using any notebook editor ([JupyterLab](/docs/tools/jupyter-lab.qmd), etc.) or in plain text markdown with any text editor ([VS Code](/docs/tools/vscode.qmd), [RStudio](/docs/tools/rstudio.qmd), [Neovim](/docs/tools/neovim.qmd), etc.)

-   Dashboards can be deployed as static web pages (no special server required) or you can optionally integrate a backend [Shiny Server](/docs/dashboards/interactivity/shiny-python/index.qmd) for enhanced interactivity.

## Examples

You can create highly customized layouts and use a wide variety of dashboard themes as illustrated in these examples (click to see them in more detail):

::: {layout-ncol="3"}
![](/docs/dashboards/examples/thumbnails/stock-explorer-dashboard.png){.border fig-alt="Screenshot of a Stock Trader dashboard: a row of three values boxes, then a row with a stock ticker graph and a table of closing values. Navy blue and green theme."}

![](/docs/dashboards/examples/thumbnails/customer-churn-dashboard.png){.border fig-alt="Screenshot of a Customer Churn dashboard: a row of three values boxes, then a row with two plots, then a row with a table. Light blue and yellow theme."}

![](/docs/dashboards/examples/thumbnails/penguins-dashboard.png){.border fig-alt="Screenshot of a Palmer Penguins dashboard: a sidebar with checkboxes and a dropdown, and two plots in main panel. Blue theme."}
:::

For live versions of these dashboards, source code, and additional examples see the [examples gallery](examples/index.qmd).

## Walkthrough

Here we'll walk through a simple example to illustrate the basics. Then, we'll provide detailed instructions on how to get started with building your own dashboards.

This simple single-page Python dashboard uses interactive Plotly visualizations to explore development indicators in the [Gapminder](http://www.gapminder.org/data/) dataset. The dashboard includes two rows, the second of which includes two columns:

![](images/gapminder.png){.border fig-alt="Screenshot of a Development Indicators dashboard: a row titled GDP and Life Expectancy with a single plot, then a row with two plots arranged side by side titled Population and Life Expectancy."}

Dashboards consist of several components:

1)  **Navigation Bar** --- Icon, title, and author along with links to sub-pages (if more than one page is defined).

2)  **Pages, Rows, Columns, and Tabsets** --- Pages, rows and columns are defined using markdown headings (with optional attributes to control height, width, etc.). Tabsets can be used to further divide content within a row or column.

3)  **Cards and Sidebars** --- Cards are containers for plots, data display, and free form content. The content of cards typically maps to *cells* in your notebook or source document. Sidebars are used to present inputs within interactive dashboards.

Dashboards can be created either using Jupyter notebooks (`.ipynb`) or using plain text markdown (`.qmd`). Here is the code for the notebook version of the above example (click the image for a zoomed view):

![](images/gapminder-jupyter.png){.border fig-alt="Screenshot of a gapminder-notebook.ipynb open in Jupyter Lab. After cells for Quarto settings and python setup, there is a markdown cell containing the heading Row, followed by a python code cell generating a plot. Then another markdown cell containing the heading Row, followed by two python code cells each generating a plot."}

Here is the plain text `.qmd` version of the dashboard (click on the numbers on the far right for additional explanation of syntax and mechanics):

```` python
--- 
title: "Development Indicators by Continent" # <1>
author: "Gapminder Analytics Group" # <1>
format: dashboard # <1>
--- 

```{{python}}
import plotly.express as px
df = px.data.gapminder()
```

## Row {height=60%} # <2>

```{{python}}  # <3>
#| title: GDP and Life Expectancy 
px.scatter(  
  df, x="gdpPercap", y="lifeExp", 
  animation_frame="year", animation_group="country", 
  size="pop", color="continent", hover_name="country",
  facet_col="continent", log_x=True, size_max=45, 
  range_x=[100,100000], range_y=[25,90] 
)  
``` # <3>

## Row {height=40%}

```{{python}} # <4>
#| title: Population
px.area(
  df, x="year", y="pop", 
  color="continent", line_group="country"
)
```

```{{python}}
#| title: Life Expectancy
px.line(
  df, x="year", y="lifeExp", 
  color="continent", line_group="country"
)
``` # <4>
````

1.  The document options define the `title` and `author` for the navigation bar as well as specifying the use of the `dashboard` format.
2.  Rows and columns are defined using headings. In this example we define two rows and specify their relative sizes using the `height` option.
3.  Computational cells become cards that live within rows or columns. Cards can have an optional title (which here we specify using the `title` option).
4.  The second row includes two computational cells, which are automatically split into two side by side cards.

## Getting Started

### Step 1: Install Quarto Pre-Release

Dashboards are a feature in the upcoming 1.4 release of Quarto and are still under active development. Before you get started, make sure you install the **latest pre-release** version of Quarto.

If you are using Quarto within a Python environment you can install the pre-release with `pip` as follows:

```{.bash filename="Terminal"}
pip install git+https://github.com/quarto-dev/quarto-cli
```

Alternatively, run the global installer for your platform:

{{< include ../download/_download-pre.md >}}

```{=html}
<style type="text/css">
#download-pre-table {
  display: none;
}
</style>
```

You can find release notes and installers for all platforms at <https://quarto.org/docs/download/prerelease.html>

### Step 2: Learn the Basics

Start by learning how to lay out your dashboard and populate it with content:

[Dashboard Components](components.qmd) shows you how to control the navigation bar, and how to arrange your content across pages, rows, columns, tabsets, sidebars, and cards.

[Data Presentation](data-presentation.qmd) shows you how to display data in your dashboard as plots, tables, value boxes, and text.

### Step 3: Explore Further

Once you've mastered the basics, check out these additional articles to learn more.

[Layouts](layouts.qmd) includes a variety of sample layouts which you can use as a starting point for your own dashboards.

[Examples](examples/index.qmd) provides a gallery of example dashboards you can use as inspiration for your own.

[Theming](theming.qmd) describes the various way to customize the fonts, colors, layout and other aspects of dashboard appearance.

[Parameters](parameters.qmd) explains how to create dashboard variants by defining parameters and providing distinct values for them on the command line.

[Deployment](deployment.qmd) covers how to deploy both static dashboards (which require only a web host, but not a server) and Shiny dashboards (which require a Shiny Server).

Interactive dashboards are covered in the articles on using [Shiny for Python](interactivity/shiny-python/index.qmd), [Shiny for R](interactivity/shiny-r.qmd), and [Observable JS](interactivity/observable.qmd).



# quarto-web/docs/dashboards/parameters.qmd

---
title: Dashboard Parameters
document: "dashboard"
---

{{< include /docs/computations/_parameters.md >}}

# quarto-web/docs/dashboards/deployment.qmd

---
title: "Dashboard Deployment"
lightbox: auto
---

## Overview

There are a wide variety of ways to deploy dashboards created using Quarto. The mechanics of deployment are different depending on whether you are publishing a [Static Dashboard](#static-dashboards) (with no server dependencies) or a [Shiny Dashboard](#shiny-dashboards). Both scenarios are covered in detail below.

## Static Dashboards {#static-dashboards}

If you are deploying a static dashboard (i.e. not using Shiny for interactivity) then you can publish dashboards to any web server. Quarto includes a `quarto publish` command to make it easy to publish to a few popular services as well as automate publishing via Continuous Integration (CI).

To get started, review the documentation for using one of the following publishing services:

{{< include /docs/publishing/_providers.md >}}

```{=html}
<style type="text/css">
/* remove confluence */
#static-dashboards table tr:nth-child(5) {
  display: none;
}
</style>
```
## Shiny Dashboards {#shiny-dashboards}

Dashboards that use [Shiny for Python](/docs/dashboards/interactivity/shiny-python/index.qmd) or [Shiny for R](/docs/dashboards/interactivity/shiny-r.qmd) are web applications that require a server for deployment (so they can't just be deployed to a generic web host). Deployment options for Shiny applications include:

-   Public hosting services like [shinyapps.io](https://www.shinyapps.io) and [Hugging Face](https://huggingface.co/docs/hub/spaces-sdks-docker-shiny).

-   [Shiny Server](https://posit.co/products/open-source/shinyserver/) (an open-source server developed by the Shiny team).

-   [Posit Connect](https://posit.co/products/enterprise/connect/) (an on-premises commercial server product).

Below we'll cover some deployment basics for Python and R and provide links to additioanal documentation on using the various available methods.

### Shiny for Python

{{< include interactivity/shiny-python/_shiny-deployment.md >}}

### Shiny for R

Quarto Dashboards that use Shiny for R can be deployed using all of the tooling and services available for normal Shiny applications. Shiny for R dashboards are run using the `quarto serve` command:

``` {.bash filename="Terminal"}
quarto serve dashboard.qmd
```

The `quarto serve` command is supported natively by [shinyapps.io](https://www.shinyapps.io), [Shiny Server](https://posit.co/products/open-source/shinyserver/) , and [Posit Connect](https://posit.co/products/enterprise/connect/). See the in-depth documentation on [Shiny for R Deployment](/docs/interactive/shiny/running.qmd#deployment) for details.

# quarto-web/docs/dashboards/components.qmd

---
title: "Dashboard Components"
lightbox: auto
---

{{< include /docs/prerelease/1.4/_pre-release-feature.qmd >}}

Dashboards are compositions of components used to provide navigation and present data. Below we'll describe the components that are used to structure the navigation and layout of dashboards.

## Navigation

All dashboards include a top-level navigation bar that provide a title and (optionally) a logo and author. Dashboards with [multiple pages](#pages) also contain a link to each page on the navigation bar:

![](images/navigation-toolbar.png){fig-alt="Screenshot of a dashboard navigation bar. The bar begins with a logo of three penguins, then the title Palmer Penguins followed by the author Cobblepot Analytics. There are also three links to pages: Bills, Flippers and Data."}

The `title` and `author` are specified as they are with normal documents. You can also include a `logo` and one or more `nav-buttons`:

``` yaml
--- 
title: "Palmer Penguins"
author: "Cobblepot Analytics"
format: 
  dashboard:
    logo: images/penguins.png
    nav-buttons: [linkedin, twitter, github]
---
```

The following special aliases are recognized for navigation buttons: `linkedin`, `facebook`, `reddit`, `twitter`, and `github`. You can also create custom buttons as described in [Nav Items](/docs/reference/projects/websites.html#nav-items). For example:

```` yaml
format:
  dashboard:
    nav-buttons:
      - reddit
      - icon: gitlab
        href: https://gitlab.com/
````

## Layout

Within a page, dashboard components are laid out using alternating sets of rows and columns. Rows and columns are in turn defined by markdown headings and computational cells. For example, here's a simple layout with two rows, where the second row is split into two columns:

::: {.chart-example .grid}
::: g-col-5
```` {.python .pymd}
---
title: "Palmer Penguins"
author: "Cobblepot Analytics"
format: dashboard
---
    
## Row {height=70%}

```{{python}}
```

## Row {height=30%}

```{{python}}
```

```{{python}}
```
````
:::

::: g-col-7
![](images/chart-focal-top.png){fig-alt="A schematic of a page layout showing Chart 1 at the top using the full page width, then Chart 2 and Chart 3 side by side in a row below it."}
:::
:::

Here, level 2 markdown headings (e.g. `## Row {height=70%}`) define the contents of rows as well as their relative height. The ```` ```{python} ```` code cells in turn automatically create cards that are laid out in columns within the row. 


::: {.callout-note}

## Heading text isn't required

Although markdown headings are used to define the layout of rows and columns in Quarto dashboards, the heading text itself is discarded. We use the headings `Row` and `Column` in these docs to aid understanding of the layouts, but you can use more descriptive headings if they help you navigate your source code.

:::

### Orientation

By default, dashboard pages are laid out first by row, then by column. However, you can change this by specifying the `orientation: columns` document option:

::: {.chart-example .grid}
::: g-col-5
```` {.python .pymd}
---
title: "Diamonds Explorer"
format: 
  dashboard:
    orientation: columns
---
    
## Column {width=60%}

```{{python}}
```

## Column {width=40%}

```{{python}}
```

```{{python}}
```
````
:::

::: g-col-7
![](images/chart-focal-left.png){fig-alt="A schematic of a page layout showing Chart 1 on the left using the full page height, and on the right Chart 2 and Chart 3 are one above the other."}
:::
:::

### Fill vs. Flow

Each row in your dashboard that is not given an explicit height will determine its size by either filling available space or by flowing to its natural height. Filling layout is generally the default, however for certain types of content (e.g. markdown text) flow layout is the default.

If the default behavior isn't what you want, you can explicitly specify filling or flowing behavior usign the `.fill` and `.flow` classes applied to a row. For example:

````{.python .pymd}
## Row {.fill}

## Row {.flow}
````



### Scrolling

By default, dashboard content fills all available space in the page. You can alternatively specify the `scrolling: true` option to layout content using its natural height and scroll to accommodate page overflow. For example:

::: {.chart-example .grid}
::: g-col-5
```` {.python .pymd}
---
title: "Scrolling"
format: 
  dashboard:
    scrolling: true 
---
    
```{{python}}
```

```{{python}}
```

```{{python}}
```
````
:::

::: g-col-7
![](images/chart-stack-scrolling.png){fig-alt="A schematic of a dashboard layout showing three charts stacked vertically."}
:::
:::

Because of its ability to scroll this layout could easily accommodate many more charts. While this is useful, you might also consider [Pages](#pages) and [Tabsets](#tabsets) (described in the next two sections) as alternate ways to present content within layouts that fill their page.

The article on [Dashboard Layouts](layouts.qmd) provides extensive additional example layouts which you can use as a basis for your own dashboards.

## Pages {#pages}

The layout examples above demonstrated only single-page dashboards. To introduce multiple pages, use level 1 headings above the level 2 headings used to define rows and columns. The text of the level 1 headings will be used to link to the pages in the navigation bar. For example, here is a dashboard that splits content across two pages:

```` {.python .pymd}
---
title: "Palmer Penguins"
format: dashboard
---
    
# Bills 

```{{python}}
```

# Flippers {orientation="columns"}

## Column

```{{python}}
```

```{{python}}
```

## Column 

```{{python}}
```
````

Note that we can set a per-page orientation by adding an `orientation` attribute to the page heading (here `orientation="columns"` for the second page).

## Tabsets {#tabsets}

Use tabsets to include multiple views of data or to include content of secondary importance without having it crowd the main display. Tabsets are created by adding the `.tabset` class to a row or column. For example, this layout displays the bottom row as a set of two tabs.

::: {.chart-example .grid}
::: g-col-5
```` {.python .pymd}
---
title: "Palmer Penguins"
format: dashboard
---
    
## Row

```{{python}}
```

## Row {.tabset}

```{{python}}
#| title: Chart 2
```

```{{python}}
#| title: Chart 3
```
````
:::

::: g-col-7
![](images/chart-tabset-row.png){fig-alt="Schematic of a dashboard layout showing Chart 1 at the top using the full page width. Below Chart 1, a panel with two tabs is shown: the Chart 2 tab is selected and occupies the full page width; the Chart 3 tab is unselected."}
:::
:::

You can include tabsets at arbitrarily deep levels. Here we include a tabset within a column of a top level row:

::: {.chart-example .grid}
::: g-col-5
```` {.python .pymd}
---
title: "Palmer Penguins"
format: dashboard
---
    
## Row {height=70%}

```{{python}}
```

## Row {height=30%}

### Column {.tabset}

```{{python}}
#| title: Chart 2
```

```{{python}}
#| title: Chart 3
```

### Column

```{{python}}
```
````
:::

::: g-col-7
![](images/chart-tabset-card.png){fig-alt="Schematic of a dashboard layout showing Chart 1 at the top using the full page width. The row below Chart 1 is split into two columns. In the left column is a panel with two tabs: Chart 2 and Chart 3. In the right column is Chart 4."}
:::
:::

Each cell within the tabset column becomes a tab, and we provide navigational titles for our tabs by adding a `title` option to the cell used to produce each tab.

You can also have tabs that contain only markdown. To do this use a `::: {.card}` div and include a `title` attribute for the tab:

````python
::: {.card title="My Title"}
Card text 
:::
````

In the examples above, each tab included a single card. If you want tabs to contain multiple cards, introduce another level of headings below the tabset row or column. For example:

````{.python .pymd}
---
title: "Palmer Penguins"
format: dashboard
---
    
## Row {.tabset}

### Plots

```{{python}}
```

```{{python}}
```

### Data

```{{python}}
```
````


## Cards {#cards}

Cards are the fundamental unit of display within dashboards. Cards are created automatically for cells and markdown content that are within rows and columns. So for example, each of the Python cells here become cards:

```` {.python .pymd}
## Column {width=40%}

```{{python}}
```

```{{python}}
```
````

You can also create cards that contain arbitrary markdown via a `.card` div. For example:

```` {.python .pymd}
## Column {width=40%}

```{{python}}
```

::: {.card}
This text will be displayed within a card
:::

```{{python}}
```
````

To provide a title for a markdown card use the `title` attribute. For example:

````python
::: {.card title="My Title"}
This text will be displayed within a card
:::
````

Note that if you are authoring within a Jupyter Notebook then markdown cells automatically become `.card` divs.

For additional details on how cells and their content are mapped to cards (e.g. excluding cells, cells with multiple outputs, etc.), see [Cell Output](data-presentation.qmd#cell-output).

### Display Options

By default, cards are displayed with no title and a small bit of padding around the edges. Here is a card that displays a [Leaflet](https://ipyleaflet.readthedocs.io) map:

![](images/leaflet-card.png){fig-alt="Screenshot of a map inset from a light grey border around the card."}

You can add a title to a card by including the `title` cell option. You can also customize the padding using the `padding` option. For example, here we add a title and remove the padding entirely:

```` {.python .pymd}
```{{python}}
#| title: "World Map"
#| padding: 0px
from ipyleaflet import Map, basemaps, basemap_to_tiles
Map(basemap=basemap_to_tiles(basemaps.OpenStreetMap.Mapnik),
    center=(48.204793, 350.121558), zoom=2)
```
````

![](images/leaflet-card-title-padding.png){fig-alt="Screenshot of a card with the title World Map displayed in the light grey bar at the top. The card contains a map with no inset from the card border."}


You can create a dynamic `title` by printing a `title=` expression as a cell's first output. For example:

{{< include _dynamic-title.md >}}

#### Expanding Cards

By default, you can zoom in on the content of cards using the expand button in the bottom right:

![](images/leaflet-card-expandable.png){fig-alt="Screenshot of a card with the cursor hovering over an icon in the bottom right showing the pop up text Expand."}

If you don't want cards to be expandable you can specify `expandable: false` (either at the document level or for individual cards).

## Sidebars

Sidebars are a great place to group inputs for Shiny interactive dashboards. To include a sidebar, add the `.sidebar` class to a level 2 heading:

::: {.chart-example .grid}
::: g-col-5
```` {.python .pymd}
---
title: "Sidebar"
format: dashboard
---
    
## {.sidebar}

```{{python}}
```

## Column 

```{{python}}
```

```{{python}}
```
````
:::

::: g-col-7
![](images/chart-input-sidebar.png){fig-alt="Schematic of a dashboard layout showing a sidebar as grey column on the left filling the page height. On the left, Chart 1 and Chart 2 are one above the other."}
:::
:::

### Global Sidebar

If you have a dashboard with [multiple pages](#pages), you may want the sidebar to be global (i.e. visible across all pages). To do this, add the `.sidebar` class to a level one heading:

```` {.python .pymd}
---
title: "Sidebar"
format: dashboard
---
    
# {.sidebar}

Sidebar content

# Page 1 

```{{python}}
```

# Page 2

```{{python}}
```
````

## Learning More

[Data Presentation](data-presentation.qmd) shows you how to display data in your dashboard as plots, tables, value boxes, and text.

[Layouts](layouts.qmd) includes a variety of sample layouts which you can use as a starting point for your own dashboards.

[Examples](examples/index.qmd) provides a gallery of example dashboards you can use as inspiration for your own.

[Theming](theming.qmd) describes the various way to customize the fonts, colors, layout and other aspects of dashboard appearance.

[Parameters](parameters.qmd) explains how to create dashboard variants by defining parameters and providing distinct values for them on the command line.

[Deployment](deployment.qmd) covers how to deploy both static dashboards (which require only a web host, but not a server) and Shiny dashboards (which require a Shiny Server).

Interactive dashboards are covered in the articles on using [Shiny for Python](interactivity/shiny-python/index.qmd), [Shiny for R](interactivity/shiny-r.qmd), and [Observable JS](interactivity/observable.qmd).



# quarto-web/docs/dashboards/data-presentation.qmd

---
title: "Data Presentation"
lightbox: auto
---

{{< include /docs/prerelease/1.4/_pre-release-feature.qmd >}}

Dashboards are compositions of components used to provide navigation and present data. Below we'll cover presenting data using plots, tables, and value boxes, as well how to include narrative content within dashboards.

## Plots

Plots are by far the most common content type displayed in dashboards. Both interactive JavaScript-based plots (e.g. [Plotly](https://plotly.com/graphing-libraries/)) and standard raster based plots (e.g. [Matplotlib](https://matplotlib.org) or [ggplot2](https://ggplot2.tidyverse.org)) are supported.

Below we provide some language specific tips and techniques for including plots within dashboards.

::: {.panel-tabset group="language"}
## Python

### plotly

[Plotly](https://plotly.com/python/) is a popular Python package for JavaScript based plots, and works very well in dashboard layouts. Plotly is also noteworthy because it includes many interactive features while still not requiring a server. For example, this plot supports an animated display of values changing over time:

```` {.python .pymd}
```{{python}}
import plotly.express as px
df = px.data.gapminder()
px.scatter(
  df, x="gdpPercap", y="lifeExp", 
  animation_frame="year", animation_group="country",
  size="pop", color="continent", hover_name="country", 
  facet_col="continent", log_x=True, size_max=45, 
  range_x=[100,100000], range_y=[25,90]
)
```
````

![](images/plotly-interactive.png){fig-alt="Screenshot of a card titled GDP and Life Expectancy. The card contains a plot with a set of scatterplots. Below the plot is a slider of years with a play and stop button."}

### matplotlib

{{< include _plots-raster.md >}}

If you are using [Matplotlib](https://matplotlib.org) (or libraries built on it like [Seaborn](https://seaborn.pydata.org)) then you can set plot sizes using the `figure.figsize` global option (or alternatively per-figure if that's more convenient):

```` python
```{{python}}
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12, 3)
```
````

In the case that your plots are laid out at a wider aspect ratio, setting this option can make a huge difference in terms of using available space. For example, the top plot in the stack below uses the default figure size of 8 x 5 and the bottom one uses the 12 x 3 ratio specified above:

![](images/matplotlib-size.png){fig-alt="Screenshot of a two cards one above the other. The top card contains a plot with large areas of white space on either side. The bottom card contains the same plot but resized to reduce the white space."}

Note that the need to explicitly size plots is confined to traditional plotting libraries---if you use Plotly or another JavaScript based plotting system plots will automatically resize to fill their container.

## R

### htmlwidgets

The [htmlwidgets](https://www.htmlwidgets.org/) framework provides high-level R bindings for JavaScript data visualization libraries. Some popular htmlwidgets include [Plotly](https://plot.ly/r/), [Leaflet](https://rstudio.github.io/leaflet/), and [dygraphs](https://rstudio.github.io/dygraphs).

You can use htmlwidgets just like you use normal R plots. For example, here is how we embed a Leaflet map:

```` python
```{{r}}
library(leaflet)
leaflet() %>%
  addTiles() %>% 
  addMarkers(lng=174.768, lat=-36.852, 
             popup="The birthplace of R")
```
````

There are dozens of packages on CRAN that provide htmlwidgets. You can find example uses of several of the more popular htmlwidgets in the htmlwidgets [showcase](https://www.htmlwidgets.org/showcase_leaflet.html) and browse all available widgets in the [gallery](https://gallery.htmlwidgets.org).

### R Graphics

You can use any chart created with standard R raster graphics (base, lattice, grid, etc.) within dashboards. When using standard R graphics with static dashboards, you'll need to pay a bit more attention to getting the size of plots right for the layout they'll be viewed in. Note that this is not a concern for plots in interactive Shiny dashboards since all plot types are resized dynamically by Shiny.

The key to good sizing behavior in static dashboards is to define knitr `fig-width` and `fig-height` options that enable the plots to fit into their layout container as closely as possible.

Here's an example of a layout that includes 3 charts from R base graphics:

```` {.python .pymd}
## Row {height="65%"}

```{{r}}
#| fig-width: 10
#| fig-height: 8
plot(cars)
```

## Row {height="35%"}
        
```{{r}}
#| fig-width: 5
#| fig-height: 4
plot(pressure)
```
    
```{{r}}
#| fig-width: 5
#| fig-height: 4
plot(airmiles)
```
````

We've specified an explicit `fig-height` and `fig-width` for each plot so that their rendered size fits their layout container as closely as possible. Note that the ideal values for these dimensions typically need to be determined by experimentation.
:::

::: callout-tip
{{< include _plots-interactive.md >}}
:::

## Tables

You can include data tables within dashboards in one of two ways:

-   As a simple tabular display.
-   As an interactive widget that includes sorting and filtering.

Below we provide some language specific tips and techniques for including tables within dashboards.

::: {.panel-tabset group="language"}
## Python

There are many Python packages available for producing tabular output. We'll cover two of the more popular libraries (tabulate and itables) below.

### tabulate

The Python [tabulate](https://github.com/astanin/python-tabulate) package supports creating markdown tables from Pandas data frames, NumPy arrays, and many other data types. You can generate a markdown table from any Pandas data frame via the `to_markdown()` method (being sure to wrap it as `Markdown` output using IPython):

```` python
```{{python}}
import pandas as pd
from IPython.display import Markdown
penguins = pd.read_csv("penguins.csv")
Markdown(penguins.to_markdown(index=False))
```
````

Note that the `index = False` parameter supresses the display of the row index. Here is a card containing output from `tabulate`:

![](images/tabulate.png){fig-alt="Screenshot of a card showing a table of penguins data. The data frame column names appear bold in a row at top. Data rows have a background that alternates between white and grey."}

You can also import `tabulate` directly and pass in the object to print directly:

```` python
```{{python}}
from tabulate import tabulate
Markdown(
  tabulate(penguins, showindex=False, 
           headers=penguins.columns)
)
```
````

### itables

The Python [itables](https://mwouts.github.io/itables/quick_start.html) package supports creating interactive data tables from Pandas and Polars DataFrames that you can sort and filter.

Use the `show()` method from `itables` to display an interactive table:

```` python
```{{python}}
from itables import show
show(penguins)
```
````

![](images/itables-scrolling.png){fig-alt="Screenshot of a card showing a table of penguins data. Above the table a Search box appears. The data frame column names appear bold in a row at top and each columns has sorting buttons."}

#### Downsampling

When a table is displayed, the table data is embedded in the dashboard output. To prevent dashboards from being too heavy to load for larger datasets, itables will display only a subset of the table---one that fits into `maxBytes` (1024kb by default).

If you wish, you can increase the value of `maxBytes` or even deactivate the limit (with `maxBytes=0)`. For example, to set a limit of 200kb:

```` python
```{{python}}
show(penguins, maxBytes = 200 * 1024)
```
````

#### Options

Note that a few `itables` options are set automatically within dashboards to ensure that they display well in cards of varying sizes. The option defaults are:

``` python
from itables import options
options.paging = False
options.dom = "ifrt"
options.maxBytes = 1024 * 1024
options.classes = "display nowrap compact"
options.language = { "info": "Showing _TOTAL_ entries" }
```

You can specify alternate options as you like to override these defaults.

## R

There are many R packages available for producing tabular output. We'll cover two of the more popular approaches (kable and DT) below.

### kable

Simple markdown tables are ideal for smaller numbers of records (i.e. 20-250 rows). Use the `knitr::kable()` function to output markdown tables:

```` {.python .pymd}
```{{r}}
knitr::kable(mtcars)
```
````

![](images/kable.png){fig-alt="Screenshot of a card showing a table of penguins data. The data frame column names appear bold in a row at top. Data rows have a background that alternates between white and grey."}

Simple markdown tables in dashboards automatically fill their container (scrolling horizontally and vertically as required).

### DT

The [DT](https://rstudio.github.io/DT/) package (an interface to the DataTables JavaScript library) can display R matrices or data frames as interactive HTML tables that support filtering, pagination, and sorting.

To include a DataTable you use the `DT::datatable` function:

```` {.python .pymd}
```{{r}}
library(DT)
datatable(mtcars)
```
````

![](images/dt.png){fig-alt="Screenshot of a card showing a table of penguins data. Above the table a Search box appears. The data frame column names appear bold in a row at top and each columns has sorting buttons."}

#### Options

Note that a few `DT` options are set automatically within dashboards to ensure that they display well in cards of varying sizes. The option defaults are:

``` r
options(DT.options = list(
  bPaginate = FALSE, 
  dom = "ifrt", 
  language = list(info = "Showing _TOTAL_ entries")
))
```

You can specify alternate options as you like to override these defaults.
:::

## Value Boxes

Value boxes are a great way to prominently display simple values within a dashboard. For example, here is a dashboard row with three value boxes:

![](images/value-boxes.png){fig-alt="A row of three value boxes. The first has a grey background, a large pencil icon, small text that says Articles per day, and a large number 45. The second has a grey background, a large comment icon, small text that says Comments per day, and a large number 126. The third has a yellow background, a large trashcan icon, small text that says Spam per day, and a large number 50. "}

Here is the code you might use to create these value boxes. Note that we use a mix of Python and R cells in this example to illustrate the syntax for each language. Note also that we assume the variables `articles`, `comments`, and `spam` are computed previously within the document.

```` {.python .pymd}
## Row 

```{{python}}
#| content: valuebox
#| title: "Articles per day"
#| icon: pencil
#| color: primary
dict(
  value = articles
)
```

```{{python}}
#| content: valuebox
#| title: "Comments per day"
dict(
  icon = "chat",
  color = "primary",
  value = comments
)
```

```{{r}}
#| content: valuebox
#| title: "Spam per day"
list(
  icon = "trash",
  color = "danger",
  value = spam
)
```
````

You can choose between specifying value box options within YAML or within a `dict()` or `list()` (for Python and R, respectively) printed by the cell. The latter syntax is handy when you want the `icon` or `color` to be dynamic based on the value.

### Icon and Color

The `icon` used in value boxes can be any of the 2,000 available [bootstrap icons](https://icons.getbootstrap.com).

The `color` can be any CSS color value, however there are some color aliases that are tuned specifically for dashboards that you might consider using by default: 

{{< include _valuebox-colors.md >}}

While the aliases apply to all [themes](theming.qmd), the colors they correspond to vary.

### Shiny

In a Shiny interactive dashboard you can have value boxes that update dynamically based on the state of the application. The details on how to do this are language-specific:

::: {.panel-tabset group="language"}

#### Python

Use the `ui.value_box()` function within a function decorated with `@render.ui`. For example:

````python
```{{python}}
from shiny import render, ui
@render.ui
def value():
    return ui.value_box("Value", input.value())
```
````

#### R

Use the `bslib::value_box()` function along with an optional icon drawn from the `bsicons` package. For example:

````python
```{{r}}
library(bslib)
library(bsicons)
value_box(
  title = "Value",
  value = textOutput("valuetext"),
  showcase = bs_icon("music-note-beamed")
)
```
````

:::


### Markdown Syntax

You can also create value boxes using plain markdown, in which case you'll typically include the value via an inline expression. For example:

``` {.python .pymd}
## Row

::: {.valuebox icon="pencil" color="blue"}
Articles per day

`{python} articles`
:::
```

## Text Content

While you often fill dashboard cards with plots and tables, you can also include arbitrary markdown content anywhere within a dashboard. 

### Content Cards

Here is a dashboard where the last card in a column is plain markdown:

![](images/text-content-column.png){.border fig-alt="Screenshot of a dashboard with three cards arranged vertically in a column. The first two cards contain plots, the last card contains text that begins 'Gapminder combines data ...'."}

To do this just include a `.card` div alongside the other cells:

```` {.python .pymd}
## Column

```{{python}}
#| title: Population
px.area(df, x="year", y="pop", color="continent", 
        line_group="country")
```

```{{python}}
#| title: Life Expectancy
px.line(df, x="year", y="lifeExp", color="continent", 
        line_group="country")
```

::: {.card}
Gapminder combines data from multiple sources into
unique coherent time-series that can’t be found
elsewhere. Learn more about the Gampminder dataset at
<https://www.gapminder.org/data/>.
:::
````

Note that if you are authoring using a Jupyter Notebook then markdown cells automatically become `.card` divs (i.e. they don't need the explicit `:::` div enclosure).

### Content within Cells

To include content alongside the ouptut of a cell, just enclose the both the cell and the content in a `.card` div. For example:

````{.python .pymd}
::: {.card title="Life Expectancy"}

```{{python}}
px.line(df, x="year", y="lifeExp", color="continent", 
        line_group="country")
```

Gapminder combines data from multiple sources into
unique coherent time-series that can’t be found
elsewhere. Learn more about the Gampminder dataset at
<https://www.gapminder.org/data/>.
:::
````

![](images/text-content-fused.png){.border fig-alt="Screenshot of a single card. The card contains a plot then text below it that begins 'Gapminder combines data...'."}

### Leading Content

Content that is included at the very top of a dashboard (and not explicitly within a `.content` div) is considered leading content, and will be included as is with no card styling (e.g. with no border). For example:

````{.python .pymd}
---
title: "My Dashboard"
format: dashboard
---

This content will appear above all of the other 
rows/columns, with no border.

## Row

```{{python}}
```
````


### Dynamic Content

You can use [inline expressions](/docs/prerelease/1.4/inline.qmd) to make text content dynamic. For example, here we have a row with text content that makes use of Python expressions:

``` {.python .pymd}
::: {.card}
The sample size was `{python} sample`. The mean reported 
rating was `{python} rating`.
:::
```

## Cell Output {#cell-output}

The output of each computational cell within your notebook or source document will be contained within a [Card](components.qmd#cards). Below we describe some special rules observed when creating cards.

### Dynamic Titles

You can create a dynamic `title` by printing a `title=` expression as a cell's first output (in contrast to including the `title` as a YAML cell option). For example:

{{< include _dynamic-title.md >}}

### Excluded Cells

Cells that produce no output do not become cards (for example, cells used to import packages, load and filter data, etc). If a cell produces unexpected output that you want to exclude add the `output: false` option to the cell:

```` {.python .pymd}
```{{python}}
#| output: false
# (code that produces unexpected output)
```
````

### Expression Printing

By default, all output from top level expressions is displayed within dashboards. This means that multiple plots can easily be generated from a cell. For example:

```` {.python .pymd}
```{{python}}
#| title: "Tipping Behavior"
px.box(df, x="sex", y="total_bill", color="smoker")
px.violin(df, x="sex", y="total_bill", color="smoker")
```
````

This behavior corresponds to the `"all"` setting for [Jupyter shell interactivity](https://ipython.readthedocs.io/en/stable/config/options/terminal.html#configtrait-InteractiveShell.ast_node_interactivity). You can customize this behavior within Quarto using the `ipynb-shell-interactivity` option.

### Card Layout

If a cell produces multiple outputs you can use cell layout options to organize their display. For example, here we modify the example to display plots side-by-side using the `layout-ncol` option:

```` {.python .pymd}
```{{python}}
#| title: "Tipping Behavior"
#| layout-ncol: 2
px.box(df, x="sex", y="total_bill", color="smoker")
px.violin(df, x="sex", y="total_bill", color="smoker")
```
````

![](images/card-layout-ncol.png){fig-alt="A screenshot of a dashboard card with the title Tipping behavior showing two plots side by side."}

See the article on [Figures](/docs/authoring/figures.qmd#complex-layouts) for additional documentation on custom layouts.

## Learning More


[Dashboard Components](components.qmd) shows you how to control the navigation bar, and how to arrange your content across pages, rows, columns, tabsets, sidebars, and cards.

[Layouts](layouts.qmd) includes a variety of sample layouts which you can use as a starting point for your own dashboards.

[Examples](examples/index.qmd) provides a gallery of example dashboards you can use as inspiration for your own.

[Theming](theming.qmd) describes the various way to customize the fonts, colors, layout and other aspects of dashboard appearance.

[Parameters](parameters.qmd) explains how to create dashboard variants by defining parameters and providing distinct values for them on the command line.

[Deployment](deployment.qmd) covers how to deploy both static dashboards (which require only a web host, but not a server) and Shiny dashboards (which require a Shiny Server).

Interactive dashboards are covered in the articles on using [Shiny for Python](interactivity/shiny-python/index.qmd), [Shiny for R](interactivity/shiny-r.qmd), and [Observable JS](interactivity/observable.qmd).



# quarto-web/docs/dashboards/layouts.qmd

---
title: "Dashboard Layouts"
---

## Overview

This page includes a variety of sample layouts which you can use as a starting point for your own dashboards.

When creating a layout, it's important to decide up front whether you want your charts to fill the web page vertically (changing in height as the browser changes) or if you want the charts to maintain their original height (with the page scrolling as necessary to display all of the charts).

Filling the page is generally a good choice when you have only one or two charts vertically stacked. Alternatively you can use `scrolling: true` to specify a scrolling layout, which is generally a better choice for three or more charts vertically stacked.

## Chart Stack

This layout is a simple stack of two charts. This dashboard fills the page and allocates height evenly across the two charts.

::: {.chart-example .grid}
::: g-col-6
```` {.python .pymd}
---
title: "Stack"
format: dashboard  
---
    
```{{python}}

```

```{{python}}

```







````
:::

::: g-col-6
![](images/chart-stack-fill.png){fig-alt="Page is split into two equal height rows: Chart 1 is in top row, Chart 2 in bottom row. Dashboard Schematic."}
:::
:::

## Chart Stack (Height)

Here we use the `height` option to allocate more space to the top chart. Note that we don't specify a height on the bottom chart as it will be automatically computed to fill the remaining space.

::: {.chart-example .grid}
::: g-col-6
```` {.python .pymd}
---
title: "Stack w/ Height"
format: dashboard
---
    
```{{python}}
#| height: 70%

```

```{{python}}

```




````
:::

::: g-col-6
![](images/chart-stack-height.png){fig-alt="Page is split into two rows, the top row has a larger height than bottom row. Chart 1 is in top row, Chart 2 in bottom row. Dashboard Schematic."}
:::
:::

## Chart Stack (Scrolling)

This layout is a simple stack of three charts. To provide enough room to display all the charts a scrolling layout is used (`scrolling: true`). Note that because of its ability to scroll this layout could easily accommodate many more charts.

::: {.chart-example .grid}
::: g-col-6
```` {.python .pymd}
---
title: "Stack (Scrolling)"
format: 
  dashboard:
    scrolling: true 
---
    
```{{python}}
```

```{{python}}
```

```{{python}}
```

````
:::

::: g-col-6
![](images/chart-stack-scrolling.png){fig-alt="Page is split into three equal height rows. Chart 1 is in top row, Chart 2 in middle row, Chart 3 in bottom row. Dashboard Schematic."}
:::
:::

## Focal Chart (Top)

This layout fills the page completely and gives prominence to a single chart at the top (with two secondary charts included below). To achieve this layout it specifies `height` attributes on each row to establish their relative sizes.

::: {.chart-example .grid}
::: g-col-6
```` {.python .pymd}
---
title: "Focal (Top)"
format: dashboard
---
    
## Row {height=70%}

```{{python}}
```

## Row {height=30%}

```{{python}}
```

```{{python}}
```
````
:::

::: g-col-6
![](images/chart-focal-top.png){fig-alt="Page is split into two rows. The top row has a larger height than the second row. Chart 1 is in the top row and spans the full page width. The bottom row is split into two equal width columns. Chart 3 is in the left column; Chart 4 is in the right column. Dashboard Schematic."}
:::
:::

## Focal Chart (Left)

This layout fills the page completely and gives prominence to a single chart on the left (with two secondary charts included to the right). To achieve this layout we use `orientation: columns` (so that top level headings map to columns rather than rows). Additionally, we specify `width` attributes on each column to establish their relative sizes.

::: {.chart-example .grid}
::: g-col-6
```` {.python .pymd}
---
title: "Focal (Left)"
format: 
  dashboard:
    orientation: columns
---
    
## Column {width=60%}

```{{python}}
```

## Column {width=40%}

```{{python}}
```

```{{python}}
```
````
:::

::: g-col-6
![](images/chart-focal-left.png){fig-alt="Page is split into two columns. The left column is wider than the right, and contains Chart 1 spanning the full page height. The second column is split into two equal height rows: Chart 2 in the top row, and Chart 3 in the bottom row. Dashboard Schematic."}
:::
:::

## Chart Grid (2x2)

This layout is a 2x2 grid of charts. This layout uses the default filling behavior however depending on the ideal display size for the charts it might be preferable to allow the page to scroll (`scrolling: true`).

::: {.chart-example .grid}
::: g-col-6
```` {.python .pymd}
---
title: "Grid (2x2)"
format: dashboard
---
    
## Row 

```{{python}}
```

```{{python}}
```

## Row

```{{python}}
```

```{{python}}
```
````
:::

::: g-col-6
![](images/chart-grid.png){fig-alt="Page is split into a grid with two equal height rows and two equal width columns. Chart 1 top left; Chart 2 top right; Chart 3 bottom left; Chart 4 bottom right. Dashboard Schematic."}
:::
:::

## Multiple Pages

This layout defines multiple pages using level 1 markdown headers. Each page has its own top-level navigation tab. Further, the second page uses a distinct orientation via the `orientation` attribute. The use of multiple columns and rows with custom `width` and `height` attributes is also demonstrated.

````{.python .pymd}
---
title: "Multiple Pages"
format: dashboard
---

# Page 1
    
## Column {width="60%"}
    
```{{python}}
```
   
## Column {width="40%"}
   
```{{python}}
```  

# Page 2 {orientation="rows"}
   
## Row {height="60%"}
 
```{{python}}
```

## Row {height="40%"}
   
```{{python}}
```
    
````

## Tabset (Column)

This layout displays the right column as a set of two tabs. Tabs are especially useful when you have a large number of components to display and prefer not to require the user to scroll to access everything. Note that we specify a `title` option in each of the cells that produce a tab.

::: {.chart-example .grid}
::: g-col-6
```` {.python .pymd}
---
title: "Tabset (Column)"
format: 
  dashboard:
    orientation: columns
---
    
## Column

```{{python}}
```

## Column {.tabset}

```{{python}}
#| title: Chart 2
```

```{{python}}
#| title: Chart 3
```
````
:::

::: g-col-6
![](images/chart-tabset-column.png){fig-alt="Page is split into two equal width columns. The left column has Chart 1 spanning the full page height. The right column has a tabset spanning the full page height: Chart 2 is selected; Chart 3 is unselected. Dashboard Schematic."}
:::
:::

## Tabset (Row)

This layout displays the bottom row as a set of two tabs.

::: {.chart-example .grid}
::: g-col-6
```` {.python .pymd}
---
title: "Tabset (Row)"
format: dashboard
---
    
## Row

```{{python}}
```

## Row {.tabset}

```{{python}}
#| title: Chart 2
```

```{{python}}
#| title: Chart 3
```
````
:::

::: g-col-6
![](images/chart-tabset-row.png){fig-alt="Page is split into two equal height rows. The top row has Chart 1 spanning the full page width. The bottom row has a tabset spanning the full page width: Chart 2 is selected; Chart 3 is unselected. Dashboard Schematic."}
:::
:::

## Tabset (Nested)

You can include tabsets as arbitrarily deep levels. Here we include a tabset within a column of a top level row.

::: {.chart-example .grid}
::: g-col-6
```` {.python .pymd}
---
title: "Tabset (Card)"
format: dashboard
---
    
## Row {height=70%}

```{{python}}
```

## Row {height=30%}

### Column {.tabset}

```{{python}}
#| title: Chart 2
```

```{{python}}
#| title: Chart 3
```

### Column

```{{python}}
```
````
:::

::: g-col-6
![](images/chart-tabset-card.png){fig-alt="Page is split into two rows: the first higher than the second. Chart 1 is in the top row and spans the full page width. The bottom row is split into two equal width columns. The left column has a tabset: Chart 2 is selected; Chart 3 is unselected. The right column contains Chart 4. Dashboard Schematic."}
:::
:::

## Input Sidebar

This layout demonstrates how to add a sidebar to a dashboard page (Shiny or ObservableJS based dashboards will often present user input controls in a sidebar). To include a sidebar you add the `.sidebar` class to a level 2 heading

::: {.chart-example .grid}
::: g-col-6
```` {.python .pymd}
---
title: "Sidebar"
format: dashboard
---
    
## {.sidebar}

```{{python}}
```

## Column 

```{{python}}
```

```{{python}}
```
````
:::

::: g-col-6
![](images/chart-input-sidebar.png){fig-alt="Page is split into two columns. The column on the left is narrower than the right, and has a grey background representing the sidebar. The column on the right is split into two rows: Chart 1 in the top row; Chart 2 in the bottom row. Dashboard Schematic."}
:::
:::

## Global Sidebar

If you have a dashboard with [multiple pages](#multiple-pages), you may want the sidebar to be global (i.e. visible across all pages). To do this, add the `.sidebar` class to a level one heading:

```` {.python .pymd}
---
title: "Sidebar"
format: dashboard
---
    
# {.sidebar}

Sidebar content

# Page 1 

```{{python}}
```

# Page 2

```{{python}}
```
````

## Learning More


[Dashboard Components](components.qmd) shows you how to control the navigation bar, and how to arrange your content across pages, rows, columns, tabsets, sidebars, and cards.

[Data Presentation](data-presentation.qmd) shows you how to display data in your dashboard as plots, tables, value boxes, and text.

[Examples](examples/index.qmd) provides a gallery of example dashboards you can use as inspiration for your own.

[Theming](theming.qmd) describes the various way to customize the fonts, colors, layout and other aspects of dashboard appearance.

[Parameters](parameters.qmd) explains how to create dashboard variants by defining parameters and providing distinct values for them on the command line.

[Deployment](deployment.qmd) covers how to deploy both static dashboards (which require only a web host, but not a server) and Shiny dashboards (which require a Shiny Server).

Interactive dashboards are covered in the articles on using [Shiny for Python](interactivity/shiny-python/index.qmd), [Shiny for R](interactivity/shiny-r.qmd), and [Observable JS](interactivity/observable.qmd).



# quarto-web/docs/dashboards/theming.qmd

---
title: "Dashboard Theming"
tbl-colwidths: [40,60]
---

## Overview

Quarto Dashboards use same Bootstrap 5 based theming system as regular HTML documents (so themes you have built for HTML websites can also be used with dashboards). Use the `theme` option to choose a theme:

``` yaml
theme: cosmo
```

Quarto includes 25 themes from the [Bootswatch](https://bootswatch.com/) project (for example, the website uses the [cosmo](https://bootswatch.com/cosmo/) theme). Available themes include:

{{< include /docs/output-formats/_theme-list.md >}}

Use of any of these themes via the `theme` option. For example:

``` yaml
format:
  dashboard:
    theme: united
```

In the following sections we'll describe how you can customize these themes or create your own new themes.

{{< include /docs/output-formats/_theme-options.md >}}

{{< include /docs/output-formats/_theme-custom.md >}}

{{< include /docs/output-formats/_theme-variables.md >}}

# quarto-web/docs/dashboards/interactivity/shiny-r.qmd

---
title: "Dashboards with Shiny for R"
code-annotations: select
lightbox: auto
---

{{< include /docs/prerelease/1.4/_pre-release-feature.qmd >}}


## Introduction

The [Shiny](https://shiny.posit.co/r/getstarted/shiny-basics/lesson1/index.html) package provides an easy way to build web applications with R. Quarto dashboards can include embedded Shiny components (e.g. a plot with sliders that control its inputs).

This section covers integrating Shiny with Quarto and assumes that you already have basic familiarity with Shiny. To learn more about Shiny please visit <https://shiny.posit.co/r/getstarted/shiny-basics/lesson1/index.html>. If you are using Python rather than R, see the documentation on using [Shiny for Python](shiny-python/index.qmd).

## Walkthrough

Here we'll explore an in-depth example that covers many of the techniques you'll use when creating dashboards with Shiny, including factoring out setup code, reactive calculations, and more advanced layout constructs like sidebars and tabsets. Here is the interactive document we'll be building:

![](../images/shiny-diamonds.png){.border fig-alt="Screenshot of a Diamonds Explorer App. The navigation bar shows two pages: Plot (active), and Data. On the left a sidebar contains eight inputs: a sample size slider; two checkboxes for Jitter and Smooth (both checked); and a dropdown for each of X, Y, Color, Facet Row and Facet Col. On the right, a plot of cut versus carat using points colored by clarity."}

Here is the source code for this dashboard (click on the numbers on the far right for additional explanation of syntax and mechanics):

```` {.python .pymd}
---
title: "Diamonds Explorer"
author: "Barkamian Analytics"
format: dashboard
server: shiny # <1>
---

```{{r}} # <2>
#| context: setup
library(ggplot2)
dataset <- diamonds
``` # <3>

# {.sidebar} # <3>

```{{r}}
sliderInput('sampleSize', 'Sample Size', 
            min=1, max=nrow(dataset),
            value=min(1000, nrow(dataset)), 
            step=500, round=0)
br()
checkboxInput('jitter', 'Jitter')
checkboxInput('smooth', 'Smooth')
```

```{{r}} # <4>
selectInput('x', 'X', names(dataset)) 
selectInput('y', 'Y', names(dataset), names(dataset)[[2]])
selectInput('color', 'Color', c('None', names(dataset)))
```

```{{r}}
selectInput('facet_row', 'Facet Row',
  c(None='.', names(diamonds[sapply(diamonds, is.factor)])))
selectInput('facet_col', 'Facet Column',
  c(None='.', names(diamonds[sapply(diamonds, is.factor)])))
``` # <4>

# Plot # <5>

```{{r}}
plotOutput('plot')
```

# Data

```{{r}}
tableOutput('data')
``` # <5>

```{{r}}
#| context: server # <6>

dataset <- reactive({ # <7>
  diamonds[sample(nrow(diamonds), input$sampleSize),] # <7>
}) # <7>
 
output$plot <- renderPlot({  # <8>
  
  p <- ggplot(
    dataset(), 
    aes_string(x=input$x, y=input$y)) + geom_point()
  
  if (input$color != 'None')
    p <- p + aes_string(color=input$color)
  
  facets <- paste(input$facet_row, '~', input$facet_col)
  if (facets != '. ~ .')
    p <- p + facet_grid(facets)
  
  if (input$jitter)
    p <- p + geom_jitter()
  if (input$smooth)
    p <- p + geom_smooth()
  
  p
  
})

output$data <- renderTable({ # <9>
  dataset()
})
```
````


1.  The `server: shiny` option instructs Quarto to run a Shiny Server behind the document.

2.  The `context: setup` cell option indicates that this code cell should run when the application starts (as opposed to when each new client session starts). Expensive initialization code (e.g. loading data) should be placed in `context: setup`.

3.  Create global sidebars by adding the `.sidebar` class to level 1 headers. Sidebars can include code cells as well as images, narrative, and links.

4.  These select inputs have their contents dynamically driven from the available columns in the dataset.

5.   Level 1 headings (here `# Plots` and `# Data`) create pages within the dashboard.

6.  Include server code (reactives that compute values or render output) in a cell with `context: server`.

7.  The `dataset()` reactive will be called to re-sample the dataset every time the sample size changes.

8.  The `renderPlot()` function regenerates the plot whenever the `dataset()` reactive or another input option changes.

9. The `renderTable()` function regenerates the table whenever the `dataset()` reactive changes.

## Learning More

To learn more about Shiny for R interactive documents see the following articles:

-   [Running Documents](/docs/interactive/shiny/running.qmd) covers how to run interactive documents both within RStudio and at the command line, as well as how to deploy them to end users.

-   [Execution Contexts](/docs/interactive/shiny/execution.qmd) goes in depth on when different code blocks (e.g. rendering vs. serving) run as well as how to cache expensive computations for more responsive documents.

-   [External Resources](/docs/interactive/shiny/resources.qmd) describes how to make sure that Shiny can locate resources (e.g. CSS, JS, images, etc.) that you include in your document.

# quarto-web/docs/dashboards/interactivity/observable.qmd

---
title: "Dashboards with Observable JS"
code-annotations: select
lightbox: auto
---

## Introduction

Quarto includes native support for [Observable JS](https://observablehq.com/@observablehq/observables-not-javascript), a set of enhancements to vanilla JavaScript created by [Mike Bostock](https://en.wikipedia.org/wiki/Mike_Bostock) (also the author of [D3](https://d3js.org/)). Observable JS is distinguished by its [reactive runtime](https://github.com/observablehq/runtime), which is especially well suited for interactive data exploration and analysis.

The creators of Observable JS (Observable, Inc.) run a hosted service at <https://observablehq.com/> where you can create and publish notebooks. Additionally, you can use Observable JS ("OJS") in standalone documents and websites via its [core libraries](https://github.com/observablehq). Quarto uses these libraries along with a [compiler](https://github.com/asg017/unofficial-observablehq-compiler/tree/beta) that is run at render time to enable the use of OJS within Quarto documents.

## Walkthrough

Quarto Dashboards are a great way to present interactive OJS visualizations. Below we'll provide a complete example which will give you a high level view of the basics. If you want to learn more, please see the complete documentation on [Using OJS with Quarto](/docs/interactive/ojs/index.qmd).

This example covers many of the techniques you'll use when creating dashboards with OJS, including reactive calculations and more advanced layout constructs like sidebars and tabsets. Here is the interactive document we'll be building:

![](../images/penguins-ojs.png){.border fig-alt="A screenshot of a Palmer Penguins dashboard. The navigation bar shows two pages: Plot (active) and Data. On the left a sidebar with an image of penguins and two inputs: a range input for Bill length; and a set of checkboxes for Islands. On the right a plot with histgrams of body mass facetted by sex and species, with bars colored by species."}

The source code for this dashboard is below. Note that we add the <br/>
`//| output: false` option to the first cell: this is to designate the cell as having only intermediate computations (so it should not be turned into a card in the dashboard layout).

Click on the numbers on the far right for additional explanation of syntax and mechanics)

```` {.python .pymd}
---
title: "Palmer Penguins"
author: "Cobblepot Analytics"
format: dashboard
---

```{{ojs}}
//| output: false # <1>

data = FileAttachment("penguins.csv") # <2>
  .csv({ typed: true }) # <2>

filtered = data.filter(function(penguin) {  # <3>
  return bill_length_min < penguin.bill_length_mm && # <3>
         islands.includes(penguin.island); # <3>
}) # <3>
```

# {.sidebar} # <4>

![](images/penguins.png){width="80%"}

```{{ojs}} # <5>
viewof bill_length_min = Inputs.range(
  [32, 50], 
  {value: 35, step: 1, label: "Bill length (min):"}
)
viewof islands = Inputs.checkbox(
  ["Torgersen", "Biscoe", "Dream"], 
  { value: ["Torgersen", "Biscoe", "Dream"], 
    label: "Islands:"
  }
)
``` # <5>

# Plot # <6>

```{{ojs}} # <7>
Plot.rectY(filtered, 
  Plot.binX(
    {y: "count"}, 
    {x: "body_mass_g", fill: "species", thresholds: 20}
  ))
  .plot({
    facet: {
      data: filtered,
      x: "sex",
      y: "species",
      marginRight: 80
    },
    marks: [
      Plot.frame(),
    ]
  }
)
```  # <7>

# Data

```{{ojs}} # <8>
Inputs.table(filtered)
``` # <8>
````

1. We set `output: false` to indicate that this cell includes only intermediate calculations and should not have its contents printed.

2.  We read the raw penguins dataset from a CSV when the page loads.

3.  `filtered` is a value that is automatically recomputed when variables declared with `viewof` change (in this case `bill_length_min` and `islands`).

4.  Create global sidebars by adding the `.sidebar` class to a level 1 header. Sidebars can include code cells as well as images, narrative, and links.

5.  Here we define our inputs using `viewof` so that the `filtered` dataset is automatically recomputed when they change.

6. Level 1 headings (here `# Plots` and `# Data`) create pages within the dashboard.

7.  The plot is automatically redrawn whenever the `filtered` dataset changes.

8.  The tabular data display is automatically refreshed whenever the `filtered` dataset changes.

## Learning More

To learn more about using OJS with Quarto, see the following articles:

-   [Using OJS](/docs/interactive/ojs/index.qmd) provides an introduction and overview of other topics.

-   [OJS Libraries](/docs/interactive/ojs/libraries.qmd) covers using standard libraries and external JavaScript libraries.

-   [OJS Data Sources](/docs/interactive/ojs/data-sources.qmd) outlines the various ways to read and pre-process data.

-   [OJS Cells](/docs/interactive/ojs/ojs-cells.qmd) goes into more depth on cell execution, output, and layout.

-   [OJS Code Reuse](/docs/interactive/ojs/code-reuse.qmd) delves into ways to re-use OJS code across multiple documents.

# quarto-web/docs/dashboards/interactivity/shiny-python/execution.qmd

---
title: "Execution Contexts"
---

## Overview

Shiny interactive documents contain both code that executes at render time as well as code that executes on the server in response to user actions and changes in input values. A solid understanding of these execution contexts is important both to have the right mental model during development as well as to optimize the performance of your document.

## Default Execution

By default, all of the Python code in your document is executed at two different times:

1)  When you render the document using `quarto render` or `quarto preview`; and

2)  Whenever a new user connects to the Shiny application generated from the document.

If the render time of your document is short, this default execution pattern will likely serve you well and you don't need to think further about optimizing execution contexts.

## Setup Context

Many documents include setup code that loads required packages and data. If this setup code takes longer than a couple of seconds, it may make sense to explicitly designate it as setup code using the `context: setup` cell option. For example:

````python
```{{python}}
#| context: setup
import seaborn as sns
penguins = sns.load_dataset("penguins")
```
````

When you add `context: setup` to a cell, the code cell will be executed:

1)  When you render the document using `quarto render` or `quarto preview`; and

2)  At the startup of the Shiny application (this is in contrast to the default behavior which is to run the code whenever a new user connects to the application).

Explicitly designating setup code using `context: setup` is likely the only thing you'll need to do in terms of explicitly specifying execution contexts. Not only does `context: setup` address the most common performance issues, it also preserves simple and easy to reason about source code (all data and functions in the document are available at both render and serve time).

## UI Context

It's possible that you have cells in your document that _only_ contribute to the user interface and does not need to execute on the server. For example, this could be a static visualization that is never dynamically redrawn in response to changes in inputs.

To designate a call as only contributing to the user interface, specify the `context: ui` cell option. For example:

````python
```{{python}}
#| context: ui

# plot that isn't ever updated after initial rendering 
sns.lmplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm", hue="species",
    height=5
)
```
````

Cells with `context: ui` will only run during `quarto render`. Code and data created by this cell are not available when the application is served. 

## Learning More

To learn more about Shiny for Python interactive documents see the following articles:

-   [Getting Started](index.qmd) explains the basics of Shiny interactive documents.

-   [Component Browser](https://jcheng.shinyapps.io/shiny-component-browser/#outputs) enumerates the available Shiny inputs and outputs, along with code snippets you can copy and paste into your dashboard. 

-   [Running Dashboards](running.qmd) covers how to run interactive dashboards both within VS Code and at the command line, as well as how to deploy them to end users.

-   [Component Layout](/docs/interactive/layout.qmd) enumerates the various techniques you can use to layout interactive components within your documents.

-   [Shiny for Python](https://shiny.posit.co/py/) provides in-depth documentation on all of the available UI and ouput widgets, as well as conceptual discussions on how things work.




# quarto-web/docs/dashboards/interactivity/shiny-python/index.qmd

---
title: "Dashboards with Shiny for Python"
code-annotations: select
lightbox: auto
aliases: 
  - /docs/dashboards/interactivity/shiny-python.html
---

{{< include /docs/prerelease/1.4/_pre-release-feature.qmd >}}



## Introduction

The [Shiny](https://shiny.posit.co/py/) package provides an easy way to build web applications with Python. Quarto dashboards can include embedded Shiny components (e.g. a plot with sliders that control its inputs).

This section assumes you have no experience with Shiny, and will teach you the basic concepts you need to get up and running with Shiny with Quarto. <!-- You can learn much more about Shiny at the official [Shiny website](https://shiny.posit.co/py/)--although note that the documentation there is written for non-Quarto uses of Shiny, which currently involve a slightly different syntax. -->

If you are using R rather than Python, see the documentation on using [Shiny for R](../shiny-r.qmd).

{{< include _shiny-requirements.qmd >}}

## Hello, Shiny

We'll start with a very simple dashboard that consists of a single plot and some inputs to drive its display:

{{< include _shiny-sidebar.md >}}

In this dashboard, you can choose different values from the select boxes on the left, and the plot will update to reflect your choices. You can also click the checkbox to show or hide rug marks. Let's go through the construction of this Shiny-enabled dashboard one step at a time.

### Metadata

The first thing to do is add `server: shiny` to the front matter. This tells Quarto that the document should be rendered as a Shiny dashboard (which requires a Python runtime whenever the dashboard is being viewed), rather than as a static HTML page. When you run `quarto preview <filename>.qmd` on a `server: shiny` document, Quarto will start and maintain a Shiny process for you and open the dashboard in your browser.

### Adding Input Controls

Next, we use functions matching the pattern `ui.input_xxx` to create input controls. For example, `ui.input_select()` creates a select box, `ui.input_slider()` creates a slider, and so on. The values returned by these functions are then rendered into HTML and JavaScript by Quarto.

This example only uses two types of inputs, but Shiny has many more. Use the [Shiny Component Browser](https://jcheng.shinyapps.io/shiny-component-browser/) to see them all, along with code snippets you can copy and paste into your dashboard. 

The example above defined an input with the following code:


```` {.python .pymd}
```{{python}}
ui.input_select("x", label="Variable:",
                choices=["bill_length_mm", "bill_depth_mm"])
```
````

**Every input function takes an input ID as its first argument.** An input ID is string that uniquely identifies this input; it must be a simple, syntactically valid Python variable name. We will use this ID to access the input's value from other parts of the dashboard.

::: {.callout-warning}
Make sure each input ID in your Shiny dashboard is unique. If you use the same ID for two different inputs, Shiny will not be able to tell them apart, and your dashboard will not work correctly.
:::

The second argument for each input function is usually a human-readable string that will be displayed next to the input control. For example, the `ui.input_select()` function passes `"Variable:"`as the second argument, which is why the select box has the label "Variable:" next to it.

#### Sidebars

In many dashboards, it's desirable to visually gather all of your input controls into a sidebar. You can do this by adding the `.sidebar` class to a level 2 header, as we did in the example:

````{.python .pymd}
## {.sidebar}

```{{python}}
from shiny import render, reactive, ui
3ui.input_select("x", "Variable:",
                choices=["bill_length_mm", "bill_depth_mm"])
ui.input_select("dist", "Distribution:", choices=["hist", "kde"])
ui.input_checkbox("rug", "Show rug marks", value = False)
```
````

### Displaying Dynamic Output

In Shiny, dashboards can contain outputs---plots, tables, text, etc.---that dynamically update in response to user input.

The example above defined a dynamic plot with the following code:

```` {.python .pymd}
```{{python}}
@render.plot
def displot():
    sns.displot(
        data=penguins, hue="species", multiple="stack",
        x=input.x(), rug=input.rug(), kind=input.dist())
```
````

The function here is given the name `displot`. The body of the function is using typical Seaborn code to create the plot. And a `@render.plot` decorator is added to the function, to indicate to Shiny that this function should be used to create a plot. (If you haven't seen decorators before, they're a Python feature that allows you to add additional behavior to a function.)

The `input.x()`, `input.rug()`. and `input.dist()` method calls are retrieving the values of the `x`, `rug`, and `dist` inputs created earlier in the dashboard.

Note that our code never calls the `displot()` function! Just the act of defining the function, and decorating it with `@render.plot`, is enough to tell Shiny and Quarto to:

* Insert a plot into the dashboard at this location.
* Use the function body to create the plot.
* Automatically re-run the function body whenever the values of `input.x()`, `input.rug()`, or `input.dist()` change due to user interaction, and use the result to update the existing plot.

This example only contains a single `@render.plot` output, but it's possible for Shiny apps to contain multiple outputs, and outputs of different types, as you'll see in the following example. Check out the [Shiny Component Browser](https://jcheng.shinyapps.io/shiny-component-browser/#outputs) to see what types of outputs are available.

### Reactive Programming

In the previous section, we said that the `displot` function would re-run _automatically_ whenever any of the inputs it referred to changed. Shiny is a **reactive programming** framework, meaning it takes care of tracking the relationships between inputs and outputs in your app. When an input changes, only outputs that are affected by that input are re-rendered. This is a powerful feature that makes it easy to create dashboards that respond to user input efficiently.

::: {.callout-note}
The `input` object is designed to be tracked by Shiny's reactive framework, 

Shiny specifically tracks changes to _reactivity-aware_ objects like the `input` object, not to just any arbitrary Python variable. You can't just write `x = 100`, then use `x` from the `displot` function, and expect `displot` to automatically rerun whenever `x` changes.

Similarly, Shiny will only automatically re-run functions that are reactivity-aware, like ones decorated with `@render.plot`. It will not help re-execute code at the top level of the document or code in regular Python functions.
:::

## Additional Features

Next, we'll explore a more in-depth example that covers more features, including factoring out setup code, reactive calculations, and more advanced layout constructs like pages. Here is the interactive document we'll be building:

![](../../images/penguins-shiny.png){.border fig-alt="Screenshot of a Palmer Penguins dashboard. Navigation bar shows two pages: Plots and Data. On the left is a sidebar with an image of penguins followed by four inputs: a set of checkboxes for Species; a set of checkboxes for Islands; and dropdown for Distribution; and a checkbox to show rug marks. On the right the page is divided into two rows each showing a density plot: the top row of bill_depth_mm; the bottom row of bill_length_mm"}

Here is the source code for this dashboard. You can click on the numbers on the far right for additional explanation of syntax and mechanics, and we'll also explain in more detail below.

{{< include _shiny-advanced.md >}}

### Setup Cell

In static Quarto documents, `{python}` code cells run only when the document is rendered, not when it is viewed. In `server: shiny` documents, `{python}` code cells are run both during render time _and_ each time the dashboard is loaded in a browser. This is important because each visitor to the dashboard needs their own independent copies of inputs/outputs in memory, so that simultaneous users don't interfere with each other.

However, sometimes we have code that would be excessive to run for every user, and we only want the code to run once, when the document's Shiny runtime process is starting up. For example, in the example above, we import packages and load data using `sns.load_dataset("penguins")`:

````{.python .pymd}
```{{python}}
#| context: setup
import seaborn as sns
from shiny import render, reactive, ui
penguins = sns.load_dataset("penguins")
```
````

We do this in a setup cell because it would be wasteful in terms of both time and memory to load the data once for each user, instead of once for the process.

By simply adding `#| context: setup` to the code cell, we can tell Quarto to run the code only once, when the Shiny process starts up. Setup cells are a great way to factor out code that you want to run once, not on every page load. Variables you define in setup cells can be read by all other code cells in the document.

### Dashboard Pages

At the top of this dashboard, you can see "Plots" and "Data" headings. These are called **dashboard pages**. Dashboard pages are a way to organize your dashboard into multiple pages, each with its own set of outputs. You can insert dashboard pages by adding level 1 headers to your Markdown. In this case, `# Plots` and `# Data`:

```` {.python .pymd}
# Plots

# Data
````

### Data Frame Outputs

On the Data page, there's a dynamic data frame output. This is created by the following code:

```` {.python .pymd}
```{{python}}
@render.data_frame
def dataview():
    return render.DataGrid(filtered_penguins())
```
````

In a `@render.data_frame` function, you can simply return a Pandas data frame, and Shiny will automatically render it as an interactive data grid. (The `filtered_penguins()` function is a reactive calculation that returns a data frame--we'll explore that next.)

You also have the option of wrapping the data frame object in a [`render.DataGrid`](https://shiny.posit.co/py/api/render.DataGrid.html) or [`render.DataTable`](https://shiny.posit.co/py/api/render.DataTable.html#shiny.render.DataTable) constructor; in this case, we're using the former. This is not strictly necessary, but it allows you to set additional options on the data grid or table, such as filtering and selection.

The only difference between `render.DataGrid` and `render.DataTable` is the appearance of the rendered table: `render.DataGrid` uses a more compact, spreadsheet-like appearance, while `render.DataTable` uses a more traditional table appearance.

### Reactive Calculations

In this example, the user uses select boxes to filter a dataset, and the filtered dataset is displayed in three different dynamic outputs: two plots and a data frame. Remember that as inputs change, Shiny automatically re-executes functions decorated with `@render.plot` and `@render.data_frame` that are affected by those inputs. But where do we put the code that filters the dataset?

The most obvious place would be to duplicate the code in each of the three rendering functions. But this is a bad idea, both because duplicate code is annoying to maintain, and because it would be inefficient to re-run the same filtering code three times just to get the exact same results. We could extract the duplicated code into a function, which would remove the maintenance problem, but it would not be any more efficient.

Shiny has a solution: **reactive calculations**. A reactive calculation is a reactive-aware function that is re-executed whenever its inputs change, but whose return value is not rendered into the dashboard. Instead, the return value is cached, and can be accessed by rendering functions (or even by other reactive calculations). This allows us to place the filtering logic in a single reactive calculation, and then have the three rendering functions access the filtered dataset from the reactive calculation.

To create a reactive calculation, we use the `@reactive.Calc` decorator. The following code creates a reactive calculation called `filtered_penguins`:

```` {.python .pymd}
```{{python}}
@reactive.Calc
def filtered_penguins():
    data = penguins[penguins["species"].isin(input.species())]
    data = data[data["island"].isin(input.islands())]
    return data
```
````

To read the value of a reactive calc, call it like a function. For example, the `depth` plot looks like this:

```` {.python .pymd}
```{{python}}
@render.plot
def depth():
    return sns.displot(
        filtered_penguins(), x = "bill_depth_mm",
        hue = "species", kind = input.dist(),
        fill = True, rug=input.rug()
    )
```
````

Note the `filtered_penguins()` call. To reiterate, this call does not necessarily cause the `filtered_penguins` function to run. Instead, it usually returns the cached value of the function, which is automatically updated whenever the inputs it refers to change. And because the `depth` plot refers to the `filtered_penguins` calculation, it will be re-rendered whenever those inputs change.

## Learning More

To learn more about Shiny for Python interactive documents see the following articles:

-   [Component Browser](https://jcheng.shinyapps.io/shiny-component-browser/#outputs) enumerates the available Shiny inputs and outputs, along with code snippets you can copy and paste into your dashboard. 

-   [Running Dashboards](running.qmd) covers in more depth how to run Shiny dashboards both within VS Code and at the command line, as well as how to deploy them to end users.

-   [Execution Contexts](execution.qmd) goes in depth on when different code cells run (e.g. rendering vs. serving).

-   [Shiny Component Browser](https://jcheng.shinyapps.io/shiny-component-browser/) gives a preview of Shiny's built-in input and output widgets.

-   [Shiny for Python](https://shiny.posit.co/py/) provides in-depth documentation on all of the available UI and ouput widgets, as well as conceptual discussions on how things work.

# quarto-web/docs/dashboards/interactivity/shiny-python/running.qmd

---
title: "Running Dashboards"
lightbox: auto
---

## Overview

There are a number of ways to run Shiny for Python interactive documents:

1.  Use the **Quarto: Preview** command within VS Code.
2.  Use the `quarto preview` command line interface with any editor.
3.  Deploy them to a server for use by a wider audience.

We'll cover all of these scenarios in depth here.

{{< include _shiny-requirements.qmd >}}

## VS Code

The [Quarto VS Code Extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto) provides integrated support for previewing Shiny interactive documents (just use the **Quarto: Preview** command as you normally would with a static document):

![](images/preview-dashboard.png){.border fig-alt="Screenshot of VS Code with the file shiny.qmd open in the left pane. On the right is a pane labelled Quarto Preview showing the live dashboard."}

Note that you need the very latest version of the VS Code extension (v1.105.0 or greater) to preview Shiny interactive documents.

## Command Line

If you are using another notebook or text editor, you can also preview Shiny interactive documents from the command line via `quarto preview`. This works the same for notebooks (`.ipynb`) and plain text markdown (`.qmd`). For example:

``` {.bash filename="Terminal"}
quarto preview example.ipynb
quarto preview example.qmd
```

There are a number of options to the `preview` command to control the port and host of the document server as well as whether a browser is automatically opened for the running document. You can learn more about these options with `quarto preview help`.

If you want to serve your document without the features of `quarto preview` (i.e. automatic re-rendering when the document changes) you can use the `quarto serve` command:

``` {.bash filename="Terminal"}
quarto serve example.qmd
```


## Deployment

{{< include _shiny-deployment.md >}}


## Debugging

You can run an interactive debugging session for Shiny  documents by debugging the generated `.py` application file (e.g. `hello-app.py`). Use the **Debug Shiny App** menu command at the top right of the editor to launch a debugging session:

![](images/debug.png){.border fig-alt="Screenshot of VS Code with the file hello-app.py open. In the top right, a menu is open from the Run dropdown with the Debug Shiny App item selected."}

::: {.callout-caution title="Important Note"}
The file you are debugging (e.g. `hello-app.py`) is _generated_ from your interactive document. You should therefore not edit this file directly (as it will be overwritten on the next render) but rather the source document from which it is generated (e.g. `hello.qmd`).
:::

## Learning More

To learn more about Shiny for Python interactive documents see the following articles:

-   [Getting Started](index.qmd) explains the basics of Shiny interactive documents.

-   [Component Browser](https://jcheng.shinyapps.io/shiny-component-browser/#outputs) enumerates the available Shiny inputs and outputs, along with code snippets you can copy and paste into your dashboard. 

-   [Execution Contexts](execution.qmd) goes in depth on when different code cells run (e.g. rendering vs. serving).

-   [Component Layout](/docs/interactive/layout.qmd) enumerates the various techniques you can use to layout interactive components within your documents.

-   [Shiny for Python](https://shiny.posit.co/py/) provides in-depth documentation on all of the available UI and ouput widgets, as well as conceptual discussions on how things work.

# quarto-web/docs/dashboards/interactivity/shiny-python/_shiny-requirements.qmd


::: {.callout-note}
### Shiny Prerequisites

In order to use Shiny within Quarto documents you will need the latest version of the `shiny` (>=0.6) and `shinywidgets` (>=0.2.2) packages. You can install the latest version of these with:

```{.bash}
pip install --upgrade shiny shinywidgets
```
:::


# quarto-web/docs/dashboards/examples/index.qmd

---
title: "Dashboard Examples"
format: html
search: false
listing:
  - id: examples
    template: examples.ejs
    contents: examples.yml
---

::: {#examples .column-page-right style="padding-right: 60px;"}
:::


# quarto-web/docs/dashboards/_examples/valuebox.qmd

---
title: "Value Boxes"
format: dashboard
engine: knitr
---

```{r}
spam = 50
```

```{python}
articles = 45
comments = 126
```

## Row 

```{python}
#| component: valuebox
#| title: "Articles per day"
#| icon: pencil
#| color: primary

articles
```

```{python}
#| component: valuebox
#| title: "Comments per day"

dict(
  icon = "pencil",
  color = "primary",
  value = comments
)
```

```{r}
#| component: valuebox
#| title: "Spam per day"

list(
  icon = "trash",
  color = "dark",
  value = spam
)
```

## Row

Here we go

# quarto-web/docs/dashboards/_examples/shiny.qmd

---
title: "Palmer Penguins"
author: "Cobblepot Analytics"
format: dashboard
server: shiny
---

```{python}
#| context: setup
import seaborn as sns
penguins = sns.load_dataset("penguins")
species = list(penguins["species"].value_counts().index)
islands = list(penguins["island"].value_counts().index)
```

# {.sidebar}

![](images/penguins.png){width="80%"}

```{python}
from shiny import render, reactive, ui

ui.input_checkbox_group(
    "species", "Species:", 
    species, selected = species
)

ui.input_checkbox_group(
    "islands", "Islands:", 
    islands, selected = islands
)

@reactive.Calc
def filtered_penguins():
    data = penguins[penguins["species"].isin(input.species())]
    data = data[data["island"].isin(input.islands())]
    return data
```

```{python}
ui.input_select("dist", "Distribution:", choices=["kde", "hist"])
ui.input_checkbox("rug", "Show rug marks", value = False)
```

[Learn more](https://pypi.org/project/palmerpenguins/) about the 
Palmer Penguins dataset.


# Plots

```{python}
#| title: Bill Depth
@render.plot
def depth():
    return sns.displot(
        filtered_penguins(), x = "bill_depth_mm", 
        hue = "species", kind = input.dist(), 
        fill = True, rug=input.rug()
    )
```

```{python}
#| title: Bill Length
@render.plot
def length():
    return sns.displot(
        filtered_penguins(), x = "bill_length_mm", 
        hue = "species", kind = input.dist(), 
        fill = True, rug=input.rug()
    )
```

# Data

```{python}
@render.data_frame
def dataview():
    return render.DataGrid(filtered_penguins(), height = "100%")
```


# quarto-web/docs/dashboards/_examples/markdown.qmd

---
title: "Markdown"
format: dashboard
---

```{python}
import plotly.express as px
gapminder = px.data.gapminder()
```




```{python}
from itables import show
show(gapminder)
```



```{python}
from IPython.display import Markdown
Markdown(f"""The model is old""")
```


# quarto-web/docs/dashboards/_examples/_TODO.qmd

---
title: "TODO"
---

-   Fake Navigation Bar
-   `width` and `height` attributes
    -   In the presence of not all rows/columns specified, unspecified rows and columns should distribute
    -   Unitless numbers should be interpreted as pixels
    -   Percents should work as expected
    -   Cards need to be able have width and height (which means `width` and `height` cell options need to work
-   Tabsets
    -   Headings should be able to create tabsets
    -   Tabsets without titles (left align tabs)
-   Sidebars
-   Markdown cells in notebooks should be cards
-   Value Boxes (`compontent: valuebox`)
-   Real Navigation Bar

# quarto-web/docs/dashboards/_examples/penguins-obervable.qmd

---
title: "Palmer Penguins"
author: "Cobblepot Analytics"
format: dashboard
---

```{ojs}
//| output: false

data = FileAttachment("penguins.csv").csv({ typed: true })

filtered = data.filter(function(penguin) {
  return bill_length_min < penguin.bill_length_mm &&
         islands.includes(penguin.island);
})
```

# {.sidebar}

![](images/penguins.png){width="80%"}

```{ojs}
viewof bill_length_min = Inputs.range(
  [32, 50], 
  {value: 35, step: 1, label: "Bill length (min):"}
)

viewof islands = Inputs.checkbox(
  ["Torgersen", "Biscoe", "Dream"], 
  { value: ["Torgersen", "Biscoe"], 
    label: "Islands:"
  }
)
```

A simple example based on Allison Horst's [Palmer Penguins](https://
allisonhorst.github.io/palmerpenguins/) dataset. Here we look at how penguin body mass varies across both sex and species.

# Plot

```{ojs}
Plot.rectY(filtered, 
  Plot.binX(
    {y: "count"}, 
    {x: "body_mass_g", fill: "species", thresholds: 20}
  ))
  .plot({
    facet: {
      data: filtered,
      x: "sex",
      y: "species",
      marginRight: 80
    },
    marks: [
      Plot.frame(),
    ]
  }
)
```

# Data

```{ojs}
Inputs.table(filtered)
```




# quarto-web/docs/dashboards/_examples/gapminder.qmd

---
title: "Development Indicators by Continent"
author: "Gapminder Analytics Group"
format: 
  dashboard:
    expandable: false
---

```{python}
import plotly.express as px
df = px.data.gapminder()
```

## Row {height=60%}

```{python}
#| title: GDP and Life Expectancy 
#| expandable: true
px.scatter(
  df, x="gdpPercap", y="lifeExp", 
  animation_frame="year", animation_group="country",
  size="pop", color="continent", hover_name="country", 
  facet_col="continent", log_x=True, size_max=45, 
  range_x=[100,100000], range_y=[25,90]
)
```

## Row {height=40%}

```{python}
#| title: Population
px.area(df, x="year", y="pop", color="continent", line_group="country")
```


```{python}
#| title: Life Expectancy
px.line(df, x="year", y="lifeExp", color="continent", line_group="country")
```



# quarto-web/docs/dashboards/_examples/shiny-diamonds.qmd

---
title: "Diamonds Explorer"
author: "Barkamian Analytics"
format: dashboard
server: shiny
---

```{r}
#| context: setup
library(ggplot2)
dataset <- diamonds
```

## {.sidebar}

```{r}
sliderInput('sampleSize', 'Sample Size', 
            min=1, max=nrow(dataset),
            value=min(1000, nrow(dataset)), 
            step=500, round=0)
br()
checkboxInput('jitter', 'Jitter')
checkboxInput('smooth', 'Smooth')
```

```{r}
selectInput('x', 'X', names(dataset))
selectInput('y', 'Y', names(dataset), names(dataset)[[2]])
selectInput('color', 'Color', c('None', names(dataset)))
```

```{r}
selectInput('facet_row', 'Facet Row',
  c(None='.', names(diamonds[sapply(diamonds, is.factor)])))
selectInput('facet_col', 'Facet Column',
  c(None='.', names(diamonds[sapply(diamonds, is.factor)])))
```

## Column {.tabset}

```{r}
#| title: Plot
plotOutput('plot')
```

```{r}
#| title: Data
tableOutput('data')
```

```{r}
#| context: server

dataset <- reactive({
  diamonds[sample(nrow(diamonds), input$sampleSize),]
})
 
output$plot <- renderPlot({
  
  p <- ggplot(
    dataset(), 
    aes_string(x=input$x, y=input$y)) + geom_point()
  
  if (input$color != 'None')
    p <- p + aes_string(color=input$color)
  
  facets <- paste(input$facet_row, '~', input$facet_col)
  if (facets != '. ~ .')
    p <- p + facet_grid(facets)
  
  if (input$jitter)
    p <- p + geom_jitter()
  if (input$smooth)
    p <- p + geom_smooth()
  
  p
  
})

output$data <- renderTable({
  dataset()
})
```


# quarto-web/docs/dashboards/_examples/python-wide.qmd

---
title: "Wide"
format: dashboard
---

```{python}
import seaborn as sns
sns.set_theme(style="darkgrid")

# Load an example dataset with long-form data
fmri = sns.load_dataset("fmri")
```

```{python}
sns.lineplot(x="timepoint", y="signal",
             hue="region", style="event",
             data=fmri)
```


```{python}
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12, 4)
sns.lineplot(x="timepoint", y="signal",
             hue="region", style="event",
             data=fmri)
```


```{python}
# Plot the responses for different events and regions
sns.lineplot(x="timepoint", y="signal",
             hue="region", style="event",
             data=fmri)
```

# quarto-web/docs/dashboards/_examples/navigation.qmd

---
title: "Palmer Penguins"
author: "Cobblepot Analytics"
format: 
   dashboard:
      logo: penguins.png
      nav-buttons:
        - linkedin
        - twitter
        - github
---
 
# Bills 

```{python}
1
```

# Flippers {orientation="columns"}

## Column 

```{python}
1
```

## Column

```{python}
1
```

```{python}
1
```

# Data


# quarto-web/docs/dashboards/_examples/flow.qmd

---
title: "Development Indicators by Continent"
author: "Gapminder Analytics Group"
format: dashboard
---

```{python}
import plotly.express as px
df = px.data.gapminder()
```

```{python}
px.area(df, x="year", y="pop", color="continent", line_group="country")
```

```{python}
px.line(df, x="year", y="lifeExp", color="continent", line_group="country")
```

## {.flow}

Mauris quis ex leo. Duis sagittis vel odio ac interdum. Sed molestie mauris neque, sed commodo est iaculis fringilla. Curabitur molestie suscipit sem, vitae condimentum dolor feugiat eget. Cras tincidunt sem vel dolor feugiat, et vehicula mauris fermentum. Nulla iaculis libero vitae porttitor consectetur. Vivamus ultricies lectus imperdiet elit lacinia congue. Etiam efficitur tortor est, nec pharetra mi congue quis. Curabitur accumsan, ante id condimentum elementum, felis odio suscipit felis, eget pellentesque justo tortor quis odio. Quisque nec ex et enim tempor dapibus quis ut libero. Quisque feugiat justo ipsum, eu tincidunt justo posuere id. Donec non ullamcorper eros. Curabitur maximus lacus vel lectus pulvinar vehicula.

Maecenas nunc leo, molestie quis augue ac, interdum fringilla ante. Sed ut nunc diam. Etiam aliquet elit eget volutpat dignissim. Cras cursus bibendum eros, a pellentesque mauris venenatis non. In iaculis porta justo, vitae luctus lectus consectetur ut. Integer pretium dolor aliquet massa eleifend faucibus. Ut sed metus lacinia, fringilla neque eget, ultrices nunc.

# quarto-web/docs/dashboards/_examples/leaflet.qmd

---
title: "Leaflet"
format: dashboard
---


```{python}
from ipyleaflet import Map, basemaps, basemap_to_tiles
Map(basemap=basemap_to_tiles(basemaps.OpenStreetMap.Mapnik),
    center=(48.204793, 350.121558), zoom=2)
```

# quarto-web/docs/dashboards/_examples/shiny-python-simple.qmd

---
title: "Penguin Bills"
format: dashboard
server: shiny
---

```{python}
import seaborn as sns
penguins = sns.load_dataset("penguins")
```

## {.sidebar}

```{python}
from shiny import render, ui
ui.input_select("x", "Variable:",
                choices=["bill_length_mm", "bill_depth_mm"])
ui.input_select("dist", "Distribution:", choices=["hist", "kde"])
ui.input_checkbox("rug", "Show rug marks", value = False)
```

## Column

```{python}
@render.plot
def displot():
    sns.displot(
        data=penguins, hue="species", multiple="stack",
        x=input.x(), rug=input.rug(),kind=input.dist())
```

# quarto-web/docs/dashboards/_examples/cell-layout.qmd

---
title: "Cell Layout"
format: dashboard
---

```{python}
import plotly.express as px
df = px.data.tips()
```

```{python}
#| title: "Tipping Behavior"
#| layout-ncol: 2

px.box(df, x="sex", y="total_bill", color="smoker")

px.violin(df, x="sex", y="total_bill", color="smoker")
```



# quarto-web/docs/dashboards/_examples/gapminder-content.qmd

---
title: "Gapminder: Development Indicators by Continent"
format: 
  dashboard:
    orientation: columns
---

```{python}
import plotly.express as px
df = px.data.gapminder()
```

## Column

```{python}
#| title: Population
px.area(df, x="year", y="pop", color="continent", 
        line_group="country")
```


```{python}
#| title: Life Expectancy
px.line(df, x="year", y="lifeExp", color="continent", 
        line_group="country")
```

::: {.card .flow}

Gapminder combines data from multiple sources into
unique coherent time-series that can’t be found
elsewhere. Learn more about the Gampminder dataset at
 <https://www.gapminder.org/data/>.
 
:::

# quarto-web/docs/dashboards/_examples/python/python-tabulate.qmd

---
title: "Python Tabulate"
format: dashboard
---


```{python}
import pandas as pd
from IPython.display import Markdown
from tabulate import tabulate
penguins = pd.read_csv("penguins.csv")
```


```{python}
Markdown(penguins.to_markdown(index=False))
```

```{python}
Markdown(tabulate(
  penguins, 
  showindex=False,
  headers=penguins.columns
))
```



# quarto-web/docs/dashboards/_examples/python/python-itables.qmd

---
title: "Python Test"
format: dashboard
execute: 
  daemon: false
---

```{python}
import seaborn as sns
from itables import show
penguins = sns.load_dataset("penguins")

#options.classes = "display nowrap compact"
# options.dom = "ifrt"
# options.language = { "info": "Showing _TOTAL_ entries" }
# options.paging = False

```


## First

```{python}
show(penguins)
```


## Second

```{python}
show(penguins)
```



```{python}
#| classes: flow
#show(penguins, maxBytes = 1000)
```

```{python}
# sns.displot(penguins, x = "bill_depth_mm", 
#         hue = "species", fill = True, rug=True)
```



# quarto-web/docs/dashboards/_examples/r/dt.qmd

---
title: "DataTables"
format: dashboard
---

```{r}
knitr::kable(mtcars)
```


```{r}
options(DT.options = list(bPaginate = FALSE, dom = "ifrt", language = list(info = "Showing _TOTAL_ entries")))
```

```{r}
library(DT)
datatable(mtcars)
```



# quarto-web/docs/dashboards/_examples/julia/julia-plotly.qmd

---
title: "Julia Plotly"
format: dashboard
---


```{julia}
using Plots
plot(sin, 
     x->sin(3x), 
     0, 
     2π, 
     leg=false, 
     fill=(0,:lavender))
```


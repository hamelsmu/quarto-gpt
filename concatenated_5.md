# quarto-web/docs/presentations/revealjs/examples/background-no-title.qmd

---
format: revealjs
---

## {background-color="aquamarine"}

(A slide with no title)

## {background-color="black" background-image="https://placekitten.com/100/100" background-size="100px" background-repeat="repeat"}

(Another slide with no title)


# quarto-web/docs/presentations/revealjs/examples/slide-with-speaker-notes.qmd

---
format:
  revealjs
---

## Slide with speaker notes

Slide content

::: {.notes}
Speaker notes go here.
:::


# quarto-web/docs/presentations/revealjs/examples/scrollable-and-smaller.qmd

---
format:
  revealjs:
    smaller: true
    scrollable: true
---

## Slide 1

* Bullet Point 1
* Bullet Point 2
* Bullet Point 3
* Bullet Point 4
* Bullet Point 5
* Bullet Point 6
* Bullet Point 7
* Bullet Point 8
* Bullet Point 9
* Bullet Point 10
* Bullet Point 11
* Bullet Point 12
* Bullet Point 13
* Bullet Point 14
* Bullet Point 15
* Bullet Point 16

## Slide 2

* Bullet Point 1
* Bullet Point 2
* Bullet Point 3
* Bullet Point 4
* Bullet Point 5
* Bullet Point 6
* Bullet Point 7
* Bullet Point 8
* Bullet Point 9
* Bullet Point 10
* Bullet Point 11
* Bullet Point 12
* Bullet Point 13
* Bullet Point 14
* Bullet Point 15
* Bullet Point 16


# quarto-web/docs/presentations/revealjs/examples/scrollable.qmd

---
format: revealjs
---

## Non-scrollable Slide

* Bullet Point 1
* Bullet Point 2
* Bullet Point 3
* Bullet Point 4
* Bullet Point 5
* Bullet Point 6
* Bullet Point 7
* Bullet Point 8
* Bullet Point 9
* Bullet Point 10
* Bullet Point 11
* Bullet Point 12
* Bullet Point 13
* Bullet Point 14
* Bullet Point 15
* Bullet Point 16

## Scrollable Slide {.scrollable}

* Bullet Point 1
* Bullet Point 2
* Bullet Point 3
* Bullet Point 4
* Bullet Point 5
* Bullet Point 6
* Bullet Point 7
* Bullet Point 8
* Bullet Point 9
* Bullet Point 10
* Bullet Point 11
* Bullet Point 12
* Bullet Point 13
* Bullet Point 14
* Bullet Point 15
* Bullet Point 16


# quarto-web/docs/presentations/revealjs/examples/incremental-pause.qmd

## Slide with a pause

content before the pause

. . .

content after the pause


# quarto-web/docs/presentations/revealjs/examples/tabset.qmd

---
format: revealjs
---

## Title

::: {.panel-tabset}

### Tab A

Content for `Tab A`

### Tab B

Content for `Tab B`

:::


# quarto-web/docs/authoring/_kbd.qmd

{{< include ../_require-1.3.qmd >}}

The `kbd` shortcode can be used to describe keyboard shortcuts in documentation. On Javascript formats, it will attempt to detect the operating system of the format and show the correct shortcut. On print formats, it will print the keyboard shortcut information for all operating systems.

For example, writing the following markdown:

``` md
To print, press {{{< kbd Shift-Ctrl-P >}}}. To open an existing new project, press {{{< kbd mac=Shift-Command-O win=Shift-Control-O linux=Shift-Ctrl-L >}}}.
```

will render the keyboard shortcuts as:

To print, press {{< kbd Shift-Ctrl-P >}}. To open an existing new project, press {{< kbd mac=Shift-Command-O win=Shift-Control-O linux=Shift-Ctrl-L >}}.


# quarto-web/docs/authoring/variables.qmd

---
title: "Variables"
---

## Overview

There are a number of ways to include dynamic variables within documents rendered by Quarto. This is useful for externalizing content that varies depending on context, or as an alternative to repeating a value in multiple places (e.g. a version number).

For example, the following prints the `title` from document metadata:

``` {.markdown shortcodes="false"}
{{< meta title >}}
```

The `{{{< meta >}}}` syntax used here is an example of a [shortcode](../extensions/shortcodes.qmd). Quarto supports the following shortcodes for dynamic variables:

| Shortcode     | Description                          |
|---------------|--------------------------------------|
| [var](#var)   | Value from `_variables.yml` file     |
| [meta](#meta) | Value from document metadata         |
| [env](#env)   | Value of System environment variable |

## var {#var}

If you are using a Quarto project, the `var` shortcode enables you to insert content from a project-level `_variables.yml` file. Create this file alongside your `_quarto.yml` project file, and then include references to those variables within any document in your project.

Variables can be either simple values or can include arbitrary markdown content. To define variables, create a `_variables.yml` file in the root directory of your project. For example:

``` yaml
version: 1.2

email:
  info: info@example.com
  support: support@example.com

engine:
  jupyter: "[Jupyter](https://jupyter.org)"
  knitr: "[Knitr](<https://yihui.name/knitr>)"
```

Note that the `engine` variable values include markdown for hyperlinks.

To include the value of a variable, use the `{{</* var */>}}` shortcode, for example:

``` {.markdown shortcodes="false"}
Version {{< var version >}} is a minor upgrade.

Please contact us at {{< var email.info >}}.

Quarto includes {{< var engine.jupyter >}} and 
{{< var engine.knitr >}} computation engines.
```

## meta {#meta}

The `meta` shortcode allows you to insert content from Pandoc metadata (e.g. YAML at the top of the document and/or in `_quarto.yml`).

For example, the following shortcode inserts the value of the `title` field from YAML metadata:

``` {.markdown shortcodes="false"}
{{< meta title >}}
```

You can dereference sub-keys using the dot (`.)` delimiter. For example:

``` {.markdown shortcodes="false"}
{{< meta labels.description >}}
```

## env {#env}

The `env` shortcode enables you to read values from environment variables. For example:

``` {.markdown shortcodes="false"}
Version {{< env PRODUCT_VERSION >}} is a minor upgrade.
```

{{< include ../extensions/_shortcode-escaping.qmd >}}


# quarto-web/docs/authoring/_embeds-ipynb.qmd

An alternative to including computations directly in the article notebook is to embed output from other notebooks. This manuscript project includes the notebook `data-screening.ipynb` in the `notebooks/` folder.

To embed output from a notebook, you can use the `embed` shortcode. Quarto shortcodes are special markdown directives that generate content. The `embed` shortcode is used in `{{< meta tool.article-file >}}` in the line:

``` {.markdown shortcodes="false"}
{{< embed notebooks/data-screening.ipynb#fig-spatial-plot >}}
```

The double curly braces (`{{`) and angle brackets (`<`) indicate this is a shortcode. The `embed` shortcode requires a path to a notebook cell. In this case, it's the file path to `data-screening.ipynb`, followed by `#` and a cell identifier. Here, the cell identifier is the cell label, set using the Quarto cell option `label` in code cell in the `data-screening.ipynb` notebook:

``` {.python filename="data-screening.ipynb"}
#| label: fig-spatial-plot
#| fig-cap: "Locations of earthquakes on La Palma since 2017."
#| fig-alt: "A scatterplot of earthquake locations plotting latitude 
#|   against longitude."
from matplotlib import colormaps
cmap = colormaps['viridis_r']
ax = df.plot.scatter(x="Longitude", y="Latitude", 
                     s=40-df["Depth(km)"], c=df["Magnitude"], 
                     figsize=(12,10), grid="on", cmap=cmap)
colorbar = ax.collections[0].colorbar
colorbar.set_label("Magnitude")

plt.show()
```

Just like any figure, using a label starting with `fig-` allows it to be cross referenced in the text. Any other options, like the figure caption (`fig-cap`) and alt text (`fig-alt`), can also be set in the source notebook.

In this manuscript, the notebook `data-screening.ipynb` isn't reproducible: you can't regenerate all the outputs because some inputs (e.g. the data) aren't included in the project. However, you can change the Quarto cell options without rerunning the code cells in the notebook. If you edit the caption to:

``` python
#| fig-cap: "Earthquakes on La Palma since 2017."
```

When you save `data-screening.ipynb`, you'll find the preview updates and the caption is reflected in the article itself.


# quarto-web/docs/authoring/article-layout.qmd

---
title: "Article Layout"
format: html
reference-location: margin
citation-location: margin
aliases:
  - page-layout.html
---

## Overview

Quarto supports a variety of page layout options that enable you to author content that:

-   Fills the main content region
-   Overflows the content region
-   Spans the entire page
-   Occupies the document margin

Quarto uses the concept of columns to describe page layout (e.g. the "body" column, the "margin" column, etc.). Below we'll describe how to arrange content into these columns. If you need to adjust the widths of the columns, see [Page Layout - Grid Customization](/docs/output-formats/page-layout.qmd#grid-customization).

All of the layout capabilities described in this document work for HTML output and many work for PDF and LaTeX output. For details about the PDF / LaTeX output, see [PDF/LaTeX Layout].

## Body Column

By default, elements are position in the body of the document and are allowed to span the content of the document, like the below.

::: {.layout-example .column-body}
.column-body
:::

But if you'd like, you can extend content slightly outside the bounds of the body by creating a div with the .`column-body-outset` class. For example:

``` markdown
:::{.column-body-outset}
Outset content...
:::
```

::: {.layout-example .column-body-outset}
.column-body-outset
:::

## Page Column

If you need even more space for your content, you can use the `.column-page` class to make the content much wider, though stopping short of extending across the whole document.

::: {.layout-example .column-page}
.column-page
:::

For example, to create a wider image, you could use:

``` markdown
:::{.column-page}
![](images/elephant.jpg)
:::
```

::: column-page
![](images/elephant.jpg){fig-alt="Three walking elephants in silhouette against the backdrop of a sunset."}
:::

For computational output, you can specify the page column in your code cell options. For example:

```{r}
#| column: page
#| echo: fenced

knitr::kable(
  mtcars[1:6, 1:10]
)
```

In addition, you can use `.column-page-inset` to inset the element from the page slightly, like so:

::: {.layout-example .column-page-inset}
.column-page-inset
:::

## Screen Column

You can have content span the full width of the page with no margin (full bleed). For this, use the `.column-screen` class or specify `column: screen` on a code cell. For example:

``` md
::: {.column-screen}
![A full screen image](/image.png)
:::
```

::: {.layout-example .column-screen}
.column-screen
:::

The following code displays a Leaflet map across the whole page.

```{r}
#| column: screen
#| echo: fenced

library(leaflet)
leaflet() %>%
  addTiles() %>%  # Add default OpenStreetMap map tiles
  addMarkers(lng=174.768, lat=-36.852, popup="The birthplace of R")
```

### Screen Inset

If you'd like a full width appearance, but would like to retain a margin, you can use inset or inset-shaded modifiers on the column. For example:

``` md
::: {.column-screen-inset}
![A full screen image](/image.png)
:::
```

::: {.layout-example .column-screen-inset}
.column-screen-inset
:::

The inset-shaded modifier results in a block spanning the full width but wrapped with a lightly shaded background. For example:

```{r}
#| column: screen-inset-shaded
#| echo: fenced

library(leaflet)
leaflet() %>%
  addTiles() %>%  # Add default OpenStreetMap map tiles
  addMarkers(lng=174.768, lat=-36.852, popup="The birthplace of R")
```

Column layouts like `screen-inset-shaded` will work with advanced figure layout. For example, it is straightforward to create a multi column presentation of figures that spans the document:

```{r}
#| column: screen-inset-shaded
#| layout-nrow: 1
#| echo: fenced

plot(cars)
plot(iris)
plot(pressure)
```

## Margin Content

You can place content within the right margin of Quarto document. For example, here we use the `.column-margin` class to place an image in the margin:

``` md
::: {.column-margin}
![A margin image](image.png)
:::
```

::: {.layout-example .column-margin style="margin-top: 18px;"}
.column-margin
:::

This also works for text content:

``` md
::: {.column-margin}
We know from *the first fundamental theorem of calculus* that for $x$ in $[a, b]$:

$$\frac{d}{dx}\left( \int_{a}^{x} f(u)\,du\right)=f(x).$$
:::
```

::: column-margin
We know from *the first fundamental theorem of calculus* that for $x$ in $[a, b]$:

$$\frac{d}{dx}\left( \int_{a}^{x} f(u)\,du\right)=f(x).$$
:::

### Margin Figures

Figures that you create using code cells can be placed in the margin by using the `column: margin` code cell option. If the code produces more than one figure, each of the figures will be placed in the margin.

```{r}
#| label: fig-mtcars
#| fig-cap: "MPG vs horsepower, colored by transmission."
#| column: margin
#| echo: fenced

library(ggplot2)
mtcars2 <- mtcars
mtcars2$am <- factor(
  mtcars$am, labels = c('automatic', 'manual')
)
ggplot(mtcars2, aes(hp, mpg, color = am)) +
  geom_point() +
  geom_smooth(formula = y ~ x, method = "loess") +
  theme(legend.position = 'bottom')
```

### Margin Tables

You an also place tables in the margin of your document by specifying `column: margin`.

```{r}
#| column: margin
#| echo: fenced

knitr::kable(
  mtcars[1:6, 1:3]
)
```

### Multiple Outputs

You can also target specific output types (for example, figures) to be placed in the margin. For example, the following code will render a table showing part of the `mtcars` dataset and produce a plot in the margin next to the table.

```{r}
#| fig-column: margin
#| echo: fenced

mtcars2 <- mtcars
mtcars2$am <- factor(
  mtcars$am, labels = c('automatic', 'manual')
)

knitr::kable(
  mtcars[1:6, 1:6]
)

library(ggplot2)
ggplot(mtcars2, aes(hp, mpg, color = am)) +
  geom_point() +
  geom_smooth(formula = y ~ x, method = "loess") +
  theme(legend.position = 'bottom')
```

{{< include _pagebreak.qmd >}}

## Margin References

Footnotes and the bibliography typically appear at the end of the document, but you can choose to have them placed in the margin by setting the following option[^1] in the document front matter:

``` yaml
---
reference-location: margin
citation-location: margin
---
```

With these options set, footnotes and citations will (respectively) be automatically be placed in the margin of the document rather than the bottom of the page. As an example, when I cite @xie2018, the citation bibliography entry itself will now appear in the margin.

### Asides

Asides allow you to place content aside from the content it is placed in. Asides look like footnotes, but do not include the footnote mark (the superscript number). [This is a span that has the class `aside` which places it in the margin without a footnote number.]{.aside}

``` markdown
[This is a span that has the class `aside` which places it in the margin without a footnote number.]{.aside}
```

## Margin Captions

For figures and tables, you may leave the content in the body of the document while placing the caption in the margin of the document. Using `cap-location: margin` in a code cell or document front matter to control this. For example:

```{r}
#| label: fig-cap-margin
#| fig-cap: "MPG vs horsepower, colored by transmission."
#| cap-location: margin
#| echo: fenced

library(ggplot2)
mtcars2 <- mtcars
mtcars2$am <- factor(
  mtcars$am, labels = c('automatic', 'manual')
)
ggplot(mtcars2, aes(hp, mpg, color = am)) +
  geom_point() +
  geom_smooth(formula = y ~ x, method = "loess") +
  theme(legend.position = 'bottom')
```

## Overflowing Content

You can also extend content outside the body region on only the left or right side of the document by using the `right` and `left` versions of the `body`, `page`, and `screen` columns to layout your content. The `left` or `right` version of these columns are as follows:

::: {.layout-example .column-body-outset-right .left}
.column-body-outset-right
:::

::: {.layout-example .column-page-inset-right .left}
.column-page-inset-right
:::

::: {.layout-example .column-page-right .left}
.column-page-right
:::

::: {.layout-example .column-screen-inset-right .left}
.column-screen-inset-right
:::

::: {.layout-example .column-screen-right .left}
.column-screen-right
:::

::: {.layout-example .column-body-outset-left .right}
.column-body-outset-left
:::

::: {.layout-example .column-page-inset-left .right}
.column-page-inset-left
:::

::: {.layout-example .column-page-left .right}
.column-page-left
:::

::: {.layout-example .column-screen-inset-left .right}
.column-screen-inset-left
:::

::: {.layout-example .column-screen-left .right}
.column-screen-left
:::

Use a div with one of the above classes to align content into one of the overflow regions. This also works using the `column` option of executable code cells:

```{r}
#| column: screen-inset-right
#| echo: fenced

library(leaflet)
leaflet() %>%
  addTiles() %>%  # Add default OpenStreetMap map tiles
  addMarkers(lng=174.768, lat=-36.852, popup="The birthplace of R")
```

## Options Reference

### Global Options

Some layout options can be specified globally in document yaml. For example:

``` yaml
---
fig-cap-location: margin
reference-location: margin
---
```

All of the below options currently only support setting a value of `margin` which tells Quarto to place the corresponding element in the margin.

+----------------------+---------------------------------------------------------------------------------------------------------+
| Option               | Description                                                                                             |
+======================+=========================================================================================================+
| `reference-location` | Where to place footnotes. Defaults to `document`.\                                                      |
|                      | \[`document` \| `section` \| `block` \| `margin` \]                                                     |
+----------------------+---------------------------------------------------------------------------------------------------------+
| `citation-location`  | Where to place citations. Defaults to `document`.\                                                      |
|                      | \[`document` \| `margin` \]                                                                             |
+----------------------+---------------------------------------------------------------------------------------------------------+
| `cap-location`       | Where to place figure and table captions. Defaults to `bottom` for figures and `top` for tables.\ |
|                      | \[`top` \| `bottom` \| `margin`\]                                                                       |
+----------------------+---------------------------------------------------------------------------------------------------------+
| `fig-cap-location`   | Where to place figure captions. Defaults to `bottom`.\                                                  |
|                      | \[`top` \| `bottom` \| `margin`\]                                                                       |
+----------------------+---------------------------------------------------------------------------------------------------------+
| `tbl-cap-location`   | Where to place table captions. Defaults to `top`.\                                                      |
|                      | \[`top` \| `bottom` \| `margin`\]                                                                       |
+----------------------+---------------------------------------------------------------------------------------------------------+

### Code Cell Options

You can also set layout column on specific code cells. This controls the layout of content that is produced by the code cell.

```{{r}}
#| column: page

plot(cars)
```

::: column-page-right
+--------------------+------------------------------------------------------------------------------------------------------------------------------+
| Option             | Description                                                                                                                  |
+====================+==============================================================================================================================+
| `column`           | Layout column to use for code cell outputs. See column options below.                                                        |
+--------------------+------------------------------------------------------------------------------------------------------------------------------+
| `fig-column`       | Layout column to use for code cell figure outputs. See column options below.                                                 |
+--------------------+------------------------------------------------------------------------------------------------------------------------------+
| `tbl-column`       | Layout column to use for code cell table outputs. See column options below.                                                  |
+--------------------+------------------------------------------------------------------------------------------------------------------------------+
| `cap-location`     | Where to place figure and table captions produced by this code cell. Defaults to `bottom` for figures and `top` for tables.\ |
|                    | \[`top` \| `bottom` \| `margin`\]                                                                                            |
+--------------------+------------------------------------------------------------------------------------------------------------------------------+
| `fig-cap-location` | Where to place captions for figures produced by this code cell. Defaults to `inline`.\                                       |
|                    | \[`inline` \| `margin`\]                                                                                                     |
+--------------------+------------------------------------------------------------------------------------------------------------------------------+
| `tbl-cap-location` | Where to place captions for tables produced by this code cell. Defaults to `inline`.\                                        |
|                    | \[`inline` \| `margin`\]                                                                                                     |
+--------------------+------------------------------------------------------------------------------------------------------------------------------+
:::

### Using Classes

In addition to global and code cell specific options, you may use divs with layout classes (prefixed with `.column-`) to arrange content into columns:

``` md
::: {.column-margin}
This content will appear in the margin!
:::
```

### Available Columns

Here are all of the available column specifiers:

::: column-page-right
+--------------+---------------------------------+---------------------------------+
| Column       | Code Cell `column`              | Class Name                      |
+==============+=================================+=================================+
| Body         |     column: body                |     .column-body                |
|              |     column: body-outset         |     .column-body-outset         |
|              |     column: body-outset-left    |     .column-body-outset-left    |
|              |     column: body-outset-right   |     .column-body-outset-right   |
+--------------+---------------------------------+---------------------------------+
| Page         |     column: page                |     .column-page                |
|              |     column: page-left           |     .column-page-left           |
|              |     column: page-right          |     .column-page-right          |
+--------------+---------------------------------+---------------------------------+
| Screen Inset |     column: screen-inset        |     .column-screen-inset        |
|              |     column: screen-inset-shaded |     .column-screen-inset-shaded |
|              |     column: screen-inset-left   |     .column-screen-inset-left   |
|              |     column: screen-inset-right  |     .column-screen-inset-right  |
+--------------+---------------------------------+---------------------------------+
| Screen       |     column: screen              |     .column-screen              |
|              |     column: screen-left         |     .column-screen-left         |
|              |     column: screen-right        |     .column-screen-right        |
+--------------+---------------------------------+---------------------------------+
| Margin       |     column: margin              |     .column-margin              |
+--------------+---------------------------------+---------------------------------+
:::

## PDF/LaTeX Layout {data-link="PDF/LaTeX Layout"}

While most of the layout capabilities described are supported for both HTML and PDF output, some are available only for HTML output. You can use the full set of columns for HTML. Then, when you render PDF or LaTeX output, content will automatically be placed in the most appropriate related column (typically this will mean using the main column and right margin). Here is how columns are mapped:

-   Any column that uses the right margin (e.g. `page`, `screen`, `screen-right`, etc.) will be rendered as `page-right` in LaTeX.
-   Any column that uses the left margin will be rendered as normal body content.

### Page Geometry

When you render a PDF using content in the margin or content that spans the page, Quarto automatically will adjust the page geometry for the default Quarto LaTeX document classes (KOMA `scrartcl`, `scrreport`, or `scrbook`) to create a slightly narrower body content region and a slightly wider margin region. This adjustment will incorporate known paper sizes to create a reasonable page geometry for most content.

You can control the page geometry directly yourself by setting `geometry` options in your document's front matter. For example:

``` yaml
---
geometry:
  - left=.75in
  - textwidth=4.5in
  - marginparsep=.25in
  - marginparwidth=2.25in
---
```

You can use these options to control the page geometry for the built in document classes or to customize the geometry of other document classes that you may be using.

::: {.callout-tip appearance="simple"}
If you'd like to view the page geometry in your rendered PDF, you can pass `showframe` to the `geometry` option as in the below example.

``` {.yaml style="background: none;"}
---
geometry:
  - showframe
---
```
:::

### Code Blocks

When rendering a PDF that uses the margins for content, Quarto automatically adjusts the appearance of code blocks. Rather than having a solid background color, a left border treatment is used.

This enables non-breaking code to overflow into the margin without cosmetic issues created by the code block background (which does not overflow into the margin region).

You can disable this treatment by setting the following `code-block-border-left: false` in your document front matter.

[^1]: You can also position references in other location (such as the bottom of the block, section, or document).


# quarto-web/docs/authoring/diagrams.qmd

---
title: "Diagrams"
aliases:
  - /docs/prerelease/1.3/mermaid.html
---

## Overview

Quarto has native support for embedding [Mermaid](https://mermaid-js.github.io/mermaid/#/) and [Graphviz](https://graphviz.org/) diagrams. This enables you to create flowcharts, sequence diagrams, state diagrams, gantt charts, and more using a plain text syntax inspired by markdown.

For example, here we embed a flowchart created using Mermaid:

```{mermaid}
%%| echo: fenced
flowchart LR
  A[Hard edge] --> B(Round edge)
  B --> C{Decision}
  C --> D[Result one]
  C --> E[Result two]
```

As illustrated above, Mermaid diagrams are embedded using `{mermaid}` executable cells.  Graphviz diagrams are embedded using `{dot}` executable cells. Note that cell options are added with slightly different syntax: `%%|` for `{mermaid}`, and `//|` for `{dot}`. 


::: callout-note
For print output formats like `pdf` or `docx`, diagram rendering makes use of the Chrome or Edge web browser to create a high-quality PNG. Quarto can automatically use an existing version of Chrome or Edge on your system, or alternatively if you don't have either installed, can use a lighter-weight library version of Chrome (see [Chrome Install](#chrome-install) below for details).
:::

## Mermaid

Mermaid is a Javascript based diagramming and charting tool that uses Markdown-inspired text definitions and a renderer to create and modify complex diagrams.

Mermaid diagrams use `%%` as their comment syntax, and so cell options are declared using `%%|`. Cell options **must** be included directly beneath the start of the diagram code chunk.

Above we demonstrated a flowchart created with Mermaid, here is a sequence diagram (also embedded using a `{mermaid}` executable cell):

```{mermaid}
%%| echo: fenced
sequenceDiagram
  participant Alice
  participant Bob
  Alice->>John: Hello John, how are you?
  loop Healthcheck
    John->>John: Fight against hypochondria
  end
  Note right of John: Rational thoughts <br/>prevail!
  John-->>Alice: Great!
  John->>Bob: How about you?
  Bob-->>John: Jolly good!
```

Note that Mermaid output varies depending on the target format (e.g. HTML vs. print-based). See the section below on [Mermaid Formats](#mermaid-formats) for additional details.

To learn more about using Mermaid, see the [Mermaid website](https://mermaid-js.github.io/mermaid/) or the [Mermaid book](https://www.amazon.com/Official-Guide-Mermaid-js-beautiful-flowcharts-dp-1801078025/dp/1801078025) (which is written by the creator of Mermaid).

## Graphviz

The Graphviz layout programs take descriptions of graphs in a simple text language, and make diagrams in useful formats. Graphviz has many useful features for concrete diagrams, such as options for colors, fonts, tabular node layouts, line styles, hyperlinks, and custom shapes.

Graphviz diagrams use `//` as their comment syntax, and so cell options are declared using `//|`. Cell options **must** be included directly beneath the start of the diagram code chunk.

For example, here is a simple undirected graph created using graphviz:

```{dot}
//| echo: fenced
graph G {
  layout=neato
  run -- intr;
  intr -- runbl;
  runbl -- run;
  run -- kernel;
  kernel -- zombie;
  kernel -- sleep;
  kernel -- runmem;
  sleep -- swap;
  swap -- runswap;
  runswap -- new;
  runswap -- runmem;
  new -- runmem;
  sleep -- runmem;
}
```


To learn more about Graphviz, see the [Graphviz website](https://graphviz.org/), this list of simple [Graphiz Examples](https://renenyffenegger.ch/notes/tools/Graphviz/examples/index), or the [Graphviz Gallery](https://graphviz.org/gallery/).

## Authoring

There are a variety of tools available to improve your productivity authoring diagrams:

1)  The [Mermaid Live Editor](https://mermaid.live/) is an online tool for editing and previewing Mermaid diagrams in real time.

2)  [Graphviz Online](https://dreampuf.github.io/GraphvizOnline/) provides a similar tool for editing Graphviz diagrams.

3)  [RStudio](https://www.rstudio.com/products/rstudio/download/) includes support for editing and previewing `.mmd` and `.dot` files (with help from the [DiagrammeR](https://rich-iannone.github.io/DiagrammeR/) package).

4)  The Quarto [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto) supports live preview of diagrams embedded in `.qmd` files and in `.mmd` and `.dot` files:

    ![](images/vscode-graphviz.gif){.border fig-alt="A Quarto document being edited in Visual Studio Code, with a live preview of the currenly edited diagram shown in a pane to the right"}

    Note that you should be sure to have installed the [very latest](https://marketplace.visualstudio.com/items?itemName=quarto.quarto) version of the Quarto VS Code extension to try this out.

## Figures

Diagrams can be treated as figures the same way that images and plot output are. For example, if we added the following figure options to the diagram above:

```{{dot}}
//| label: fig-simple
//| fig-cap: "This is a simple graphviz graph."
```

We'd get this output:

```{dot}
//| label: fig-simple
//| fig-cap: "This is a simple graphviz graph."
graph G {
  layout=neato
  run -- intr;
  intr -- runbl;
  runbl -- run;
  run -- kernel;
  kernel -- zombie;
  kernel -- sleep;
  kernel -- runmem;
  sleep -- swap;
  swap -- runswap;
  runswap -- new;
  runswap -- runmem;
  new -- runmem;
  sleep -- runmem;
}
```

## File Include

You might find it more convenient to edit your diagram in a standalone `.dot` or `.mmd` file and then reference it from within your `.qmd` document. You can do this by adding the `file` option to a Mermaid or Graphviz cell.

For example, here we include a very complex diagram whose definition would be too unwieldy to provide inline:

```{{dot}}
//| label: fig-linux-kernel
//| fig-cap: "A diagram of the Linux kernel."
//| file: linux-kernel-diagram.dot
```

```{dot}
//| label: fig-linux-kernel
//| fig-cap: "A diagram of the Linux kernel."
//| file: images/linux-kernel-diagram.dot
```

Note that the `label` and `fig-cap` attributes still work as expected with `file` includes.

## Sizing

By default, diagrams are rendered at their natural size (i.e. they are not stretched to fit the default figure size for the current document). Within HTML output formats, diagrams are also made responsive, so that their width doesn't overflow the current page column. This is similar to the treatment given to images and dynamic JavaScript widgets.

You can disable responsive sizing by specifying the `fig-responsive: false` option. You can also specify explicit sizes via `fig-width` and `fig-height`. For example, here we want to make a mermaid diagram a bit bigger because it contains only a few elements:

```{mermaid}
%%| echo: fenced
%%| fig-width: 6.5
flowchart LR
  A[Hard edge] --> B(Round edge)
  B --> C{Decision}
```

## Mermaid Formats {#mermaid-formats}

When you include a Mermaid diagram in a document, the diagram format used is chosen automatically based on the output format:

| Format                              | Output                      |
|-------------------------------------|-----------------------------|
| HTML (`html`, `revealjs`, etc.)     | Mermaid native (JavaScript) |
| GitHub Flavored Markdown (`gfm`)    | Mermaid code block          |
| Other Formats (`pdf`, `docx`, etc.) | PNG image                   |

The Mermaid native format is used by default whenever the underlying output format supports JavaScript.

When using `format: gfm`, diagrams will be emitted as plain `mermaid` code blocks. This is because both [GitHub](https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/) and [GitLab](https://docs.gitlab.com/ee/user/markdown.html#mermaid) natively support rendering Mermaid diagrams from code.

For formats that don't do special handling of Mermaid or lack a JavaScript run-time (e.g. formats like `pdf`, `docx`, `epub`, etc.) a PNG image is created using [Chrome](#chrome-install).

You can change the default behavior using the `mermaid-format` option. For example:

``` yaml
---
format:
  gfm:
    mermaid-format: png
---
```

Valid values for `mermaid-format` include `js`, `png`, and `svg`,

## Mermaid Themes {#mermaid-theming}

{{< include _mermaid-theming.qmd >}}

## Code Echo

Note that unlike other executable cell handlers (e.g. `{python}`), cells with diagrams don't display their code in the rendered document by default. You can display code by adding an `echo: true` option in a comment at the top the cell.

To include code for `{mermaid}`, add `%%| echo: true` to the top of the cell. For example:

```{{mermaid}}
%%| echo: true
```

To include code for `{dot}`, add `//| echo: true` to the top of the cell. For example:

```{{dot}}
//| echo: true
```

## Chrome Install {#chrome-install}

For printing to output formats like `pdf` or `docx`, diagram rendering makes use of the Chrome or Edge web browser to create a high-quality PNG.

Quarto can automatically use an existing version of Chrome or Edge on your system for rendering. Alternatively, if you don't have either, you can install a minimal version of Chrome for use by Quarto with the following command:

``` {.bash filename="Terminal"}
quarto tools install chromium
```

::: callout-note
Quarto installs headless Chromium via Puppeteer. The bundled Chromium that Puppeteer installs may not work on Docker containers; please check [the Puppeteer documentation](https://github.com/puppeteer/puppeteer/blob/main/docs/troubleshooting.md#running-puppeteer-in-docker) as well as [this article](https://pptr.dev/next/troubleshooting#running-puppeteer-on-wsl-windows-subsystem-for-linux) if you are attempting to install within Windows Subsystem for Linux (WSL).
:::


# quarto-web/docs/authoring/figures.qmd

---
title: "Figures"
format: html
aliases: 
  - figures-and-layout.html
  - figure-layout.html
---

Quarto includes a number of features aimed at making it easier to work with figures and subfigures, as well as for laying out panels that contain multiple figures, tables, or other content.

## Figure Basics

In Pandoc markdown, a figure is created whenever a captioned image appears by-itself in a paragraph. For example:

``` markdown
![Elephant](elephant.png)
```

This results in the following treatment for various output types:

| HTML                                                                              | PDF                                                                  | Word                                                                  |
|---------------------------|-----------------------|-----------------------|
| ![](images/html-figure.png){fig-alt="A line drawing of an elephant." width="340"} | ![](images/pdf-figure.png){fig-alt="A line drawing of an elephant."} | ![](images/word-figure.png){fig-alt="A line drawing of an elephant."} |

Note that for LaTeX / PDF output figures are automatically numbered (you can arrange for figures to be numbered in other formats using [Cross References](cross-references.html)).

### Figure Sizing

By default figures are displayed using their actual size (subject to the width constraints imposed by the page they are rendered within). You can change the display size by adding the `width` and `height` attributes to the figure. For example:

``` markdown
![Elephant](elephant.png){width=300}
```

Note that if only `width` is specified then `height` is calculated automatically. If you need to modify the default behaviour just add an explicit `height` attribute.

The default units for `width` and `height` are pixels. You can also specify sizes using a percentage or a conventional measurement like inches or millimetres. For example:

``` markdown
![Elephant](elephant.png){width=80%}
![Elephant](elephant.png){width=4in}
```

### Linked Figures

When rendering with Quarto, you can enclose a figure within a link and it will still be treated within output as a captioned figure. For example:

``` markdown
[![Elephant](elephant.png)](https://en.wikipedia.org/wiki/Elephant)
```

### Figure Alignment

Figures are center aligned by default. Add the `fig-align` attribute to the image to use a different alignment. For example:

``` markdown
![Elephant](elephant.png){fig-align="left"}
```

Note that figure captions are left aligned to accommodate longer caption text (which looks odd when center aligned).

### Alt Text

You can add alternative text to a figure by adding the `fig-alt` attribute to the image. For example, the following Markdown...

``` markdown
![](elephant.png){fig-alt="A drawing of an elephant."}
```

... will create the following HTML with the corresponding alt tag:

``` html
<img src="elephant.png" alt="A drawing of an elephant.">
```

Note that the figure caption, title, and alt text can all be different. For example, the following code...

``` markdown
![Elephant](elephant.png "Title: An elephant"){fig-alt="A drawing of an elephant."}
```

...produces this HTML:

``` html
<img src="elephant.png" title="Title: An elephant" alt="A drawing of an elephant.">
```

### Multiformat Figures

You can write markdown that provides a distinct image file format depending on the target output format. To do this simply leave-off the extension, for example:

``` markdown
![](elephant)
```

By default this will look for `elephant.png`, however if you are rendering to PDF it will look for `elephant.pdf`. You can customize this behavior using the `default-image-extension` option. For example:

``` yaml
format:
  html:
    default-image-extension: svg
  pdf:
    default-image-extension: tex
```

### Applying Multiple Parameters 
To combine the above methods, separate arguments by a space, for example:
``` markdown
![](elephant.png){fig-alt="A drawing of an elephant." fig-align="left" width=20%}
```

## Cross References

You can cross-reference figures by adding an ID with the `fig-` prefix to them, and then referencing the figure using the `@` prefix. For example:

``` markdown
![An Elephant](elephant.png){#fig-elephant}

This is illustrated well by @fig-elephant.
```

For figures produced by executable code cells, include a `label` with a `fig-` prefix to make them cross-referenceable. For example:

```` markdown
For a demonstration of a line plot, see @fig-line-plot.

```{{python}}
#| label: fig-line-plot
#| fig-cap: "A line plot "

import matplotlib.pyplot as plt
plt.plot([1,23,2,4])
plt.show()
```
````

::: callout-important
## Label Prefix

In order for a figure to be cross-referenceable, its label must start with the `fig-` prefix.
:::

See the article on [Cross References](cross-references.qmd) for additional details.

## Subfigures

If you have several figures that appear as a group, you can create a figure div to enclose them. For example:

``` markdown
::: {#fig-elephants layout-ncol=2}

![Surus](surus.png){#fig-surus}

![Hanno](hanno.png){#fig-hanno}

Famous Elephants
:::
```

Again, the last paragraph provides the main caption, and the individual figures carry the sub-captions. Here is what this looks like when rendered as HTML:

![](images/elephant-subfigures.png){fig-alt="An artistic rendition of Surus, Hannibal's last war elephant, is on the left. Underneath this picture is the caption '(a) Surus.' On the right is a line drawing of Hanno, a famous elephant. Underneath this picture is the caption '(b) Hanno.' The words 'Figure 1: Famous elephants' are centered beneath both pictures."}

Note that the empty lines between the figures (and between the last figure and the caption) are required (it's what indicates that these images belong to their own paragraphs rather than being multiple images within the same paragraph).

Note also that we also used a `layout-ncol` attribute to specify a two-column layout. The next section delves more into customizing figure layouts.

## Figure Panels

Above we demonstrate laying out two side-by-side figures with subcaptions and a main caption. You may or may not want the caption / sub-caption treatment, and you might also want to use multiple rows of figures. All of these variations are possible.

To layout two figures with their own standalone captions (and no main caption), just eliminate the `#fig` identifiers and main caption at the bottom:

``` markdown
::: {layout-ncol=2}
![Surus](surus.png)

![Hanno](hanno.png)
:::
```

![](images/elephant-figures-no-subcaption.png){fig-alt="An artistic rendition of Surus, Hannibal's last war elephant, is on the left. Underneath this picture is the caption 'Surus.' On the right is a line drawing of Hanno, a famous elephant. Underneath this picture is the caption 'Hanno.'"}

You can also eliminate the captions entirely:

``` markdown
::: {layout-ncol=2}
![](surus.png)

![](hanno.png)
:::
```

### Multiple Rows

If you have more than 2 images, you might want to lay them out across multiple rows. You can do this using the `layout-nrow` attribute. For example:

``` markdown
::: {layout-nrow=2}
![Surus](surus.png)

![Hanno](hanno.png)

![Abdul Abbas](abdul-abbas.png)

![Lin Wang](lin-wang.png)
:::
```

![](images/elephant-rows.png){fig-alt="A 2x2 grid of pictures of elephants. There are labels underneath each of the pictures. Clockwise from the upper left, the labels say: Surus, Hanno, Lin Wang, and Abdul Abbas."}

More complex figure arrangements (e.g. rows with varying column layouts) are possible. See the [Custom Layouts](#complex-layouts) section below for more details.

## Figure Divs

You can treat any markdown content you want as a figure by enclosing it in Pandoc div block with an identifier prefaced with `#fig-`. For example, here we create a figure that includes an embedded iframe:

``` markdown
::: {#fig-elephant}

<iframe width="560" height="315" src="https://www.youtube.com/embed/SNggmeilXDQ"></iframe>

Elephant
:::
```

Note that the last paragraph in the div block is used as the figure caption.

## LaTeX Figures

This section describes some figure handling options that are specific to LaTeX output.

One very important thing to note is that using the `fig-env` and `fig-pos` options described below will trigger the creation of a LaTeX floating environment (most often `\begin{figure}`). Depending upon where this LaTeX is generated it (e.g. is it within another `\begin{figure}`) this could generate invalid LaTeX. To be on the safe side these attributes should typically only be used for images at the very top level of your document.

### Environments

There are a number of LaTeX packages that provide custom figure environments. For example, in two-column formats, the `figure*` environment spans both columns of the document. You can explicitly pass the figure environment to use as the `fig-env` attribute of the image or the fenced div:

``` markdown
![Elephant](surus.jpg){#fig-elephant fig-env="figure*"}

::: {#fig-elephant-2 fig-env="figure*"}

![](surus.jpg)

Another elephant.

:::
```

### Figure Position

The default LaTeX `figure` is a floating environment, so the specific location it appears in your document will depend on its size and the nature of the other content around it. You can exercise some control over this behavior using the `fig-pos` option. The `fig-pos` option provides a placement specifier for the `figure` environment. For example, the `ht` in this LaTeX snippet is the `fig-pos`:

``` latex
\begin{figure}[ht]

\end{figure}
```

You can specify `fig-pos` either at the document level, as a executable code block option, or within markdown. Here we do all three:

```` markdown
---
title: "My Document"
format:
  pdf:
    fig-pos: 'h'
---

```{{python}}
#| fig-pos: 't'

```

![](figure.png){fig-pos='b'}
````

See [this article](https://www.latex-project.org/publications/2014-FMi-TUB-tb111mitt-float-placement.pdf) for additional details on LaTeX figure positioning.

::: callout-note
## Figures and Code Blocks

If your figure was generated by an executable code block and the code was included in the output (`echo: true`), then `fig-pos` will be set to `H` by default (to try to keep it alongside the code that generated it). In all other cases, default LaTeX handing of figure position is used unless you specify an explicit `fig-pos`.
:::

### PGF/Ti*k*Z Graphics

If you are creating LaTeX output, Quarto will automatically emit the correct LaTeX for markdown images that reference `.tex` files containg [PGF/Ti*k*Z](https://en.wikipedia.org/wiki/PGF/TikZ) vector graphics. For example, the following markdown images:

``` markdown
![](image1.tex)

![](image2.tex){width=80%}
```

Will be written to LaTeX as:

``` tex
\input{image1.tex}

\resizebox{0.8\linewidth}{!}{\input{image2.tex}}
```

As shown above, `width` and `height` percentages are automatically converted to `\linewidth` scaled. Alternatively you can specify custom LaTeX for the `width` and `height` arguments of `\resizebox`.

## Caption Locations

By default, figure captions are positioned below figures. In HTML and PDF formats, you can modify this behavior using the `fig-cap-location` option. For example:

``` yaml
---
fig-cap-location: top
---
```

Note that this option is specified at the top level so that it can be shared by both PDF and HTML formats. If you are only targeting a single format you can place it alongside other `format` specific options.

Valid values for the caption location include:

| Value    | Description                            |
|----------|----------------------------------------|
| `top`    | Position the caption above the figure. |
| `bottom` | Position the caption below the figure. |
| `margin` | Position the caption in the margin.    |

See the article on [Article Layout](article-layout.qmd#margin-captions) for additional details on placing captions in the margin.

## Custom Layouts {#complex-layouts}

The examples above used the `layout-ncol` or `layout-nrow` attributes to create straightforward layouts where all columns are of equal sizes. The `layout` attribute enables the creation of much more complex layouts.

For example, this defines a layout with two equally sized figures in the first row, then another image that spans the entire second row:

``` markdown
::: {layout="[[1,1], [1]]"}
![Surus](surus.png)

![Hanno](hanno.png)

![Lin Wang](lin-wang.png)
:::
```

![](images/layout-attrib.png){fig-alt="Three elephant pictures arranged such that two pictures are side-by-side in the first row, and the third picture is underneath both of these. The picture on the left in the first row is captioned 'Surus' and the picture on the right is captioned 'Hanno'. The picture underneath these two is captioned 'Lin Wang' and is as as wide and tall as the other two put together."}

The `layout` attribute is a 2-dimensional array where the first dimension defines rows and the second columns. In this case `"layout="[[1,1], [1]]"` translates to: create two rows, the first of which has two columns of equal size and the second of which has a single column.

Note that the numbers in a row are arbitrary and don't need to add up to a particular total. You can therefore use whatever scheme is most natural. For example, here we define columns that occupy varying percentage widths of the row:

``` markdown
::: {layout="[[70,30], [100]]"}
![Surus](surus.png)

![Hanno](hanno.png)

![Lin Wang](lin-wang.png)
:::
```

You can also use negative values to create space between elements. For example:

``` markdown
::: {layout="[[40,-20,40], [100]]"}
![Surus](surus.png)

![Hanno](hanno.png)

![Lin Wang](lin-wang.png)
:::
```

![](images/layout-attrib-negative.png){fig-alt="Three elephant pictures arranged such that two pictures are side-by-side in the first row, and the third picture is underneath both of these. The picture on the left in the first row is captioned 'Surus' and the picture on the right is captioned 'Hanno'. The two pictures are separated by some whitespace. The picture underneath these two is captioned 'Lin Wang' and is wider and taller than the other two put together."}

### Vertical Alignment

If you have a layout with a row of images of differing heights, you can control their vertical alignment using the `layout-valign` attribute. A simple example:

``` markdown
::: {layout="[15,-2,10]" layout-valign="bottom"}
![Surus](surus.png)

![Lin Wang](lin-wang.png)
:::
```

![](images/valign.png){fig-alt="Two pictures of elephants side by side. The picture on the left has the label 'Figure 1: Surus' underneath it. The picture on the right has the label 'Figure 2: Lin Wang' underneath it. The figure on the left is more than twice the width and height of the figure on the right."}

Note that vertical alignment isn't limited to images, you can also vertically align any other elements that are included in a panel.

## Computations

Figures produced by executable code blocks are automatically included in your document. 
To set the ID, caption and link, use the chunk options `label`, `fig-cap` and `fig-link` respectively. 
Other attributes, e.g. `fig-align` and `fig-alt`, can be set using the chunk option of the same name.

You can control the default size for computational figures using the `fig-width` and `fig-height` options in the document header.  
Read more about these options in [Execution Options: Figure Options](https://quarto.org/docs/computations/execution-options.html#figure-options).

### Layout 

Note that figure layout attributes also work for figures produced by executable code blocks. Here are examples for both Jupyter and Knitr:

::: panel-tabset
#### Jupyter

```{{python}}
#| layout-ncol: 2
#| fig-cap: 
#|   - "Line Plot 1"
#|   - "Line Plot 2"

import matplotlib.pyplot as plt
plt.plot([1,23,2,4])
plt.show()

plt.plot([8,65,23,90])
plt.show()
```

![](images/jupyter-figure-layout.png){fig-alt="Two line plots rendered by Jupyter side-by-side."}

#### Knitr

```{{r}}
#| layout-ncol: 2
#| fig-cap: 
#|   - "Speed and Stopping Distances of Cars"
#|   - "Vapor Pressure of Mercury as a Function of Temperature"

plot(cars)
plot(pressure)
```

![](images/knitr-figure-layout.png){fig-alt="Two scatter plots arranged side-by-side."}
:::

Note that in these examples we also use the `fig-cap` option to apply a caption to each of the generated figures.

### Subcaptions

You can create subcaptions for computational output by combining the `fig-cap` and `fig-subcap` options. When applying captions to computational output you can optionally include a `label` with a `fig-` prefix---if you do this then the figure will be numbered and [cross-referenceable](cross-references.qmd).

::: panel-tabset
#### Jupyter

```{{python}}
#| label: fig-charts
#| fig-cap: "Charts"
#| fig-subcap: 
#|   - "First"
#|   - "Second"
#| layout-ncol: 2

import matplotlib.pyplot as plt
plt.plot([1,23,2,4])
plt.show()

plt.plot([8,65,23,90])
plt.show()
```

![](images/jupyter-figure-layout-caption.png){fig-alt="Two line plots with captions rendered by Jupyter side-by-side."}

#### Knitr

```{{r}}
#| label: fig-charts
#| fig-cap: "Charts"
#| fig-subcap: 
#|   - "Cars"
#|   - "Pressure"
#| layout-ncol: 2

plot(cars)
plot(pressure)
```

![](images/knitr-figure-layout-caption.png){fig-alt="Two scatter plots with captions arranged side-by-side."}
:::

### Custom Layout

The `layout` works the same way for figures produced by Knitr or Jupyter. For example, here's an Rmd code chunk that produces 3 plots and defines a custom layout for them:

```{{r}}
#| layout: [[45,-10, 45], [100]]

plot(cars)
plot(pressure)
plot(mtcars)
```

![](images/knitr-layout-complex.png){.preview-image fig-alt="Two plots arranged side-by-side with a large plot underneath it. The top two plots are scatter plots visualizing the `cars` and `pressure` datasets. These two plots are separated by some additional white space. The plot on the bottom visualizes the `mtcars` dataset and is wider and taller than the other two plots combined. This plot is an 11 by 11 grid plotting each of the 11 variables in the `mtcars` dataset against each other as a scatterplot. Instead of scatter plots in the diagonal starting in the upper left and going to the lower right are text labels for each of the variable names. These are: 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', and 'carb'."}

## Block Layout

While the examples above illustrate laying out figures, it's important to note that layout attributes can be used to layout any sort of block content. For example, here we layout 2 lists side-by-side:

``` markdown
::: {layout-ncol=2}
### List One

- Item A
- Item B
- Item C

### List Two

- Item X
- Item Y
- Item Z
:::
```

Note that headings are automatically combined with the block that follows them, so this markdown has a total of 2 columns to lay out. Here's an example of a paragraph next to a bullet list (without headings):

``` markdown
::: {layout-ncol=2}
- Item X
- Item Y
- Item Z

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur gravida eu erat et fring. Morbi congue augue vel eros ullamcorper, eget convallis tortor sagittis. Fusce sodales viverra mauris a fringilla. Donec feugiat, justo eu blandit placerat, enim dui volutpat turpis, eu dictum lectus urna eu urna. Mauris sed massa ornare, interdum ipsum a, semper massa. 
:::
```

For more complicated content use divs (`:::`) to divide your content into blocks for the layout. For example, here's how you could lay out a code cell along with some text, next to a figure:

````markdown
:::: {layout="[ 40, 60 ]"}

::: {#first-column}
```r
# Some code
```

Some text that should be laid out below the code
:::

::: {#second-column}
![](elephant.png)
:::

::::
````

The id attributes (`#first-column` and `#second-column`) are optional, 
but aid readability.


# quarto-web/docs/authoring/cross-references.qmd

---
title: "Cross References"
format: html
---

## Overview

Cross-references make it easier for readers to navigate your document by providing numbered references and hyperlinks to various entities like figures and tables. Every cross-referenceable entity requires a label (unique identifier prefixed with type e.g. `#fig-element`) and caption (description). For example, this is a cross-referenceable figure:

``` markdown
![Elephant](elephant.png){#fig-elephant}
```

The presence of the caption (`Elephant`) and label (`#fig-elephant`) make this figure referenceable. This enables you to use the following syntax to refer to it elsewhere in the document:

``` markdown
See @fig-elephant for an illustration.
```

Here is what this would look like rendered to HTML:

![](images/crossref-figure.png){.border fig-alt="A line drawing of an elephant. The caption 'Figure 1: Elephant' is centered beneath it." width="100%"}

Quarto enables you to create cross-references to figures, tables, equations, sections, code listings, theorems, proofs, and more. Cross references can also be applied to dynamic output from Knitr and Jupyter.

Note that cross reference identifiers must start with their type (e.g. `fig-` or `tbl-`). So the identifier `#fig-elephant` is valid for a cross-reference but the identifiers `#elephant` and `#elephant-fig` are not.

There are options available that control the text used for titles and references. For example, you could change "Figure 1" to read "Fig 1" or "fig. 1". See the [options documentation](#options) for details on how to customize the text used for crossrefs.

::: {.callout-note style="padding-bottom: 16px"}
Quarto's syntax for cross-references is based on [pandoc-crossref](https://github.com/lierdakil/pandoc-crossref) (which is in turn based on this discussion: <https://github.com/jgm/pandoc/issues/813>). There are however several differences (mostly related to handling computational output) to note:

1.  Quarto uses the prefix `#fig-` rather than `#fig:` (which is more compatible with Jupyter notebook [cell ids](https://jupyter.org/enhancement-proposals/62-cell-id/cell-id.html)).
2.  Quarto is able to reference raw HTML and LaTeX figures and tables (which are often produced by executable code blocks).
3.  Quarto has support for referencing theorems and proofs (and related types).
:::

## Figures

As described above, this is the markdown used to create a cross-referenceable figure and then refer to it:

``` markdown
![Elephant](elephant.png){#fig-elephant}

See @fig-elephant for an illustration.
```

Note again that cross-reference identifiers must start with their type (e.g. `#fig-`) and that cross reference identifiers must be all lower case.

### Subfigures

You may want to create a figure composed of multiple subfigures. To do this, enclose the figures in a div (with its own label and caption) and give each subfigure its own label and (optionally) caption. You can then refer to either the entire figure in a reference or a single subfigure:

``` markdown
::: {#fig-elephants layout-ncol=2}

![Surus](surus.png){#fig-surus}

![Hanno](hanno.png){#fig-hanno}

Famous Elephants
:::

See @fig-elephants for examples. In particular, @fig-hanno.
```

Here is what this looks like when rendered as HTML:

![](images/crossref-subfigures.png){.preview-image .border fig-alt="An artistic rendition of Surus, Hannibal's last war elephant, is on the left. Underneath this picture is the caption '(a) Surus.' On the right is a line drawing of Hanno, a famous elephant. Underneath this picture is the caption '(b) Hanno.' The words 'Figure 1: Famous elephants' are centered beneath both pictures. The text 'See fig. 1 for examples. In particular, fig. 1(b).' is underneath this text and is aligned to the left." width="100%"}

Note that we also used the `layout-ncol` attribute to specify a two-column layout. See the article on [Figures](figures.qmd) for more details on laying out panels of figures.

### Computations

Figures produced by Jupyter and Knitr can also be cross-referenced. To do this, add a `label` and `fig-cap` option at the top of the code block. For example:

::: panel-tabset
#### Jupyter

    ```{{python}}
    #| label: fig-plot
    #| fig-cap: "Plot"

    import matplotlib.pyplot as plt
    plt.plot([1,23,2,4])
    plt.show()
    ```

    For example, see @fig-plot.

![](images/crossref-figure-jupyter.png){fig-alt="A line plot with the label 'Figure 1: Plot' centered underneath it. The text 'For example, see fig. 1' is underneath this label and aligned to the left."}

#### Knitr

    ```{{r}}
    #| label: fig-plot
    #| fig-cap: "Plot"

    plot(cars)
    ```

    For example, see @fig-plot.

![](images/crossref-figure-r.png){fig-alt="A scatter plot of speed versus distance for the `cars` dataset. The label 'Figure 1: Plot' is centered beneath it. The text 'For example, see fig. 1' is aligned to the left underneath that."}
:::

You can also create multiple figures within a code cell and reference them as subfigures. To do this use `fig-cap` for the main caption, and `fig-subcap` to provide an array of subcaptions. For example:

    ```{{python}}
    #| label: fig-plots
    #| fig-cap: "Plots" 
    #| fig-subcap:
    #|   - "Plot 1"
    #|   - "Plot 2" 
    #| layout-ncol: 2

    import matplotlib.pyplot as plt
    plt.plot([1,23,2,4])
    plt.show()

    plt.plot([8,65,23,90])
    plt.show()
    ```

    See @fig-plots for examples. In particular, @fig-plots-2.

![](images/crossref-subfigures-jupyter.png){fig-alt="Two line plots side-by-side. The plot on the left has the caption '(a) Plot 1' centered underneath it. The plot on the right has the caption '(b) Plot 2' centered underneath it. The text 'Figure 1: Plots' is centered underneath both of these plots. The text 'See fig. 1 for examples. In particular, fig. 1(b)' is aligned to the left underneath that."}

Note that subfigure reference labels are created automatically based on the main chunk label (e.g. `@fig-plots-1`, `@fig-plots-2`, etc.).

If you'd like subfigure captions that include only an identifier, e.g. "(a)", and not a text caption, then specify `fig-subcap: true` rather than providing explicit subcaption text:

```{{python}}
#| label: fig-plots
#| fig-cap: "Plots" 
#| fig-subcap: true
#| layout-ncol: 2
```

## Tables

For tables produced by executable code cells, include a label with a `tbl-` prefix to make them cross-referenceable. For example:

```{python}
#| label: tbl-planets
#| tbl-cap: "Planets"
#| echo: fenced

from IPython.display import Markdown
from tabulate import tabulate
table = [["Sun",696000,1989100000],
         ["Earth",6371,5973.6],
         ["Moon",1737,73.5],
         ["Mars",3390,641.85]]
Markdown(tabulate(
  table, 
  headers=["Planet","R (km)", "mass (x 10^29 kg)"]
))
```

::: callout-important
## Label Prefix

In order for a table to be cross-referenceable, its label must start with the `tbl-` prefix.
:::

{{< include _table-crossrefs.md >}}

### Computations

You can also cross-reference tables created from code executed via computations. To do this, add the `label` and `tbl-cap` cell options. For example:

```{{r}}
#| label: tbl-iris
#| tbl-cap: "Iris Data"

library(knitr)
kable(head(iris))
```

![](/docs/authoring/images/crossref-table-knitr.png){fig-alt="Example table output." fig-align="center" width="80%"}

You can also create multiple tables within a code cell and reference them as subtables. To do this, add a `tbl-subcap` option with an array of subcaptions. For example:

```{{r}}
#| label: tbl-tables
#| tbl-cap: "Tables"
#| tbl-subcap:
#|   - "Cars"
#|   - "Pressure"
#| layout-ncol: 2

library(knitr)
kable(head(cars))
kable(head(pressure))
```

![](/docs/authoring/images/crossref-subtable-knitr.png){fig-alt="Two tables side-by-side. Each table has 2 columns and 8 rows. The table on the left is titled '(a) Cars'. The table on the right is titled '(b) Pressure'. Centered underneath both tables is the text 'Table 1: Tables.'" fig-align="center" width="80%"}

If you'd like subtable captions that include only an identifier, e.g. "(a)", and not a text caption, then specify `tbl-subcap: true` rather than providing explicit subcaption text:

```{{r}}
#| label: tbl-tables
#| tbl-cap: "Tables"
#| tbl-subcap: true
#| layout-ncol: 2

library(knitr)
kable(head(cars))
kable(head(pressure))
```

![](/docs/authoring/images/crossref-subtable-nocaption-knitr.png){fig-align="center" width="80%"}

## Equations

Provide an `#eq-` label immediately after an equation to make it referenceable. For example:

``` markdown
Black-Scholes (@eq-black-scholes) is a mathematical model that seeks to explain the behavior of financial derivatives, most commonly options:

$$
\frac{\partial \mathrm C}{ \partial \mathrm t } + \frac{1}{2}\sigma^{2} \mathrm S^{2}
\frac{\partial^{2} \mathrm C}{\partial \mathrm C^2}
  + \mathrm r \mathrm S \frac{\partial \mathrm C}{\partial \mathrm S}\ =
  \mathrm r \mathrm C 
$$ {#eq-black-scholes}
```

Black-Scholes (@eq-black-scholes) is a mathematical model that seeks to explain the behavior of financial derivatives, most commonly options:

$$
\frac{\partial \mathrm C}{ \partial \mathrm t } + \frac{1}{2}\sigma^{2} \mathrm S^{2}
\frac{\partial^{2} \mathrm C}{\partial \mathrm S^2}
  + \mathrm r \mathrm S \frac{\partial \mathrm C}{\partial \mathrm S}\ =
  \mathrm r \mathrm C 
$$ {#eq-black-scholes}

Note that the equation number is included (via `\qquad`) in the right margin of the equation.

## Sections

To reference a section, add a `#sec-` identifier to any heading. For example:

``` markdown
## Introduction {#sec-introduction}

See @sec-introduction for additional context.
```

Note that when using section cross-references, you will also need to enable the `number-sections` option (so that section numbering is visible to readers). For example:

``` yaml
---
title: "My Document"
number-sections: true
---
```

## Code Listings

To create a reference-able code block, add a `#lst-` identifier along with a `lst-cap` attribute. For example:

```` markdown
```{#lst-customers .sql lst-cap="Customers Query"}
SELECT * FROM Customers
```

Then we query the customers database (@lst-customers).
````

::: {.callout-note}

Note that code listings currently only work with _display code blocks_ (as opposed to executable code blocks). If you wish to both execute and reference a code block, use a combination of a display block and a code block with `echo: false` in the cell YAML.

:::



## Theorems and Proofs

Theorems are commonly used in articles and books in mathematics. To include a reference-able theorem, create a div with a `#thm-` label (or one of other theorem-type labels described below). You also need to specify a theorem name either via the first heading in the block. You can include any content you like within the div. For example:

``` markdown
::: {#thm-line}

## Line

The equation of any straight line, called a linear equation, can be written as:

$$
y = mx + b
$$
:::

See @thm-line.
```

![](images/crossref-theorem.png){fig-alt="A snippet of a LaTeX document. The first line reads: 'Thereom 1 (Line) The equation of any straight line, called a linear equation, can be written as:' Cenetered on a separate line is the equation 'y = mx + b'. The text 'See thm. 1' is aligned to the left underneath that."}

For LaTeX output, the [amsthm](https://ctan.org/pkg/amsthm?lang=en) package is used for typesetting theorems. For other formats an appropriate treatment is used (the above is an example of HTML output).

There are a number of theorem variations supported, each with their own label prefix:

| **Label Prefix** | **Printed Name** | **LaTeX Environment** |
|------------------|------------------|-----------------------|
| `#thm-`          | Theorem          | theorem               |
| `#lem-`          | Lemma            | lemma                 |
| `#cor-`          | Corollary        | corollary             |
| `#prp-`          | Proposition      | proposition           |
| `#cnj-`          | Conjecture       | conjecture            |
| `#def-`          | Definition       | definition            |
| `#exm-`          | Example          | example               |
| `#exr-`          | Exercise         | exercise              |

The `proof`, `remark`, and `solution` environments generally receive similar typesetting as theorems, however they are not numbered (and therefore cannot be cross-referenced). To create these environments just use them as the class name of a div:

``` markdown
::: {.solution}
The solution.
:::
```

As with theorems you can optionally include a heading as the first element of the div (or a `name` attribute) to give the environment a caption for typesetting (this typically appears in parentheses after the environment title).

For LaTeX output the [amsthm](https://ctan.org/pkg/amsthm?lang=en) package is used to typeset these environments. For other formats a similar treatment is used, but you can further customizing this using CSS.

## References

The examples above have all used the default syntax for inline references (e.g. `@fig-elephant`), which results in the reference text "Figure 1", "Table 1", etc.

You can customize the appearance of inline references by either changing the syntax of the inline reference or by setting options. Here are the various ways to compose a cross-reference and their resulting output:

| Type          | Syntax                | Output   |
|---------------|-----------------------|----------|
| Default       | `@fig-elephant`       | Figure 1 |
| Capitalized   | `@Fig-elephant`       | Figure 1 |
| Custom Prefix | `[Fig @fig-elephant]` | Fig 1    |
| No Prefix     | `[-@fig-elephant]`    | 1        |

Note that the capitalized syntax makes no difference for the default output, but would indeed capitalize the first letter if the default had been change via an option to use lower case (e.g. "fig.").

You can also group cross references using the following syntax:

``` markdown
As illustrated in [@fig-elephant; @fig-panther; @fig-rabbit].
```

There are a number of options that can be used to further customize the treatment of cross-references. See the section below on [References Options](#references-1) for additional details.

## Chapter Numbering

You can use the `crossref: chapters` option to indicate that top-level headings (H1) in your document correspond to chapters, and that cross-references should be sub-numbered by chapter. For example:

``` markdown
---
title: "My Document"
author: "Jane Doe"
number-sections: true
crossref:
  chapters: true
---

# Introduction

![Elephant](elephant.png){#fig-elephant}

See @fig-elephant for an illustration.
```

![](images/crossref-chapters.png){fig-alt="A line drawing of an elephant. Above it is the text '1 Introduction' in large, bold font. The label 'Figure 1.1: Elephant' is centered underneath it. The text 'See fig. 1.1 for an illustration' is aligned to the left underneath that."}

## Lists

For LaTeX / PDF output, you can use the raw LaTeX commands `\listoffigures`, `\listoftables` and `\listoflistings` to produce listings of all figures, tables, etc. within a document. You can use the `lof-title`, `lot-title`, and `lol-title` crossref options to customize the title of the listing.

For example:

``` markdown
---
title: "My Document"
crossref:
  lof-title: "List of Figures"
format: pdf
---

\listoffigures
```

Note that the default titles for the lists use the form displayed above (i.e. "List of \<Type\>").

## Options {#options}

There are a wide variety of options available for customizing caption labels and references. These options are all specified within the `crossref` key of document metadata.

::: {.callout-note appearance="simple"}
Note that since LaTeX does its own formatting and layout of figures and tables, not all of these options will apply when rendering to PDF. Specifically, delimiter options like `title-delim` and numbering options like `labels` don't work for PDF output. Additionally, formatting directives are not applied (e.g. italicizing the figure title) for LaTeX titles.
:::

### Titles

You can specify the title prefix used for captions using `*-title` options. You can also specify the delimiter used between the prefix and the caption using the `title-delim` option. For example:

``` yaml
---
title: "My Document"
crossref:
  fig-title: Fig     # (default is "Figure")
  tbl-title: Tbl     # (default is "Table")
  title-delim: "—"   # (default is ":")
---
```

### References {#references-1}

You can specify the prefix used for inline reference type using `*-prefix` options. You can also specify whether references should be hyper-linked using the `ref-hyperlink` option. For example:

``` yaml
---
title: "My Document"
crossref:
  fig-prefix: figure   # (default is "Figure")
  tbl-prefix: table    # (default is "Table")
  ref-hyperlink: false # (default is true)
---
```

### Numbering

There are a variety of numbering schemes available for cross-references, including:

-   `arabic` (1, 2, 3)

-   `roman` (I, II, III, IV)

-   `roman i` (i, ii, iii, iv)

-   `alpha x` (start from letter 'x')

-   `alpha X` (start from letter 'X')

You can specify the number scheme used for all types (other than sub-references) using the `labels` option. For sub-references (e.g. subfigures), you can specify the number scheme using the `subref-labels` option. For example:

``` yaml
---
title: "My Document"
crossref:
  labels: alpha a        # (default is arabic)
  subref-labels: roman i # (default is alpha a)
---
```

If you would like, you can specify the number scheme for a specific type using the `*-labels` options. For example:

``` yaml
---
title: "My Document"
crossref:
  fig-labels: alpha a    # (default is arabic)
  tbl-labels: alpha a    # (default is arabic)
  subref-labels: roman i # (default is alpha a)
---
```

If both `labels` and a type specific label option is provided, the type specific option will override the `labels` option.


# quarto-web/docs/authoring/footnotes-and-citations.qmd

---
title: Citations & Footnotes
format: html
link-citations: true
section-title-footnotes: Example Footnotes
---

## Citations

Quarto will use Pandoc to automatically generate citations and a bibliography in a number of styles. To use this capability, you will need:

-   A quarto document formatted with citations (see [Citation Markdown](#sec-citations)).

-   A bibliographic data source, for example a BibLaTeX (`.bib`) or BibTeX (`.bibtex`) file.

-   Optionally, a `CSL` file which specifies the formatting to use when generating the citations and bibliography (when not using `natbib` or `biblatex` to generate the bibliography).

### Bibliography Files

Quarto supports bibliography files in a wide variety of formats including BibLaTeX and CSL. Add a bibliography to your document using the `bibliography` YAML metadata field. For example:

``` yaml
---
title: "My Document"
bibliography: references.bib
---
```

::: callout-tip
You can provide more than one bibliography file if you would like by setting the `bibliography` field's value to a YAML array.
:::

See the [Pandoc Citations](https://pandoc.org/MANUAL.html#citations) documentation for additional information on bibliography formats.

### Citation Syntax {#sec-citations}

Quarto uses the standard Pandoc markdown representation for citations (e.g. `[@citation]`) --- citations go inside square brackets and are separated by semicolons. Each citation must have a key, composed of '\@' + the citation identifier from the database, and may optionally have a prefix, a locator, and a suffix. The citation key must begin with a letter, digit, or `_`, and may contain alphanumerics, `_`, and internal punctuation characters (`:.#$%&-+?<>~/`). Here are some examples:

+-------------------------------------------+---------------------------------------------------------------------+---------------------------------------------------------------------+
| Markdown Format                           | Output (default)                                                    | Output(`csl: diabetologia.csl`, see @sec-citations-style)           |
+===========================================+=====================================================================+=====================================================================+
|     Blah Blah [see @knuth1984, pp. 33-35; | Blah Blah [see @knuth1984, pp. 33-35; also @wickham2015, chap. 1]   | Blah Blah see [1], pp. 33-35; also [1], chap. 1                     |
|     also @wickham2015, chap. 1]           |                                                                     |                                                                     |
+-------------------------------------------+---------------------------------------------------------------------+---------------------------------------------------------------------+
|     Blah Blah [@knuth1984, pp. 33-35,     | Blah Blah [@knuth1984, pp. 33-35, 38-39 and passim]                 | Blah Blah [1], pp. 33-35, 38-39 and passim                          |
|     38-39 and passim]                     |                                                                     |                                                                     |
+-------------------------------------------+---------------------------------------------------------------------+---------------------------------------------------------------------+
|     Blah Blah [@wickham2015; @knuth1984]. | Blah Blah [@wickham2015; @knuth1984].                               | Blah Blah [1, 2].                                                   |
+-------------------------------------------+---------------------------------------------------------------------+---------------------------------------------------------------------+
|     Wickham says blah [-@wickham2015]     | Wickham says blah [-@wickham2015]                                   | Wickham says blah [1]                                               |
+-------------------------------------------+---------------------------------------------------------------------+---------------------------------------------------------------------+

You can also write in-text citations, as follows:

+-----------------------------------+-------------------------------+-------------------------------+
| Markdown Format                   | Output (author-date format)   | Output (numerical format)     |
+===================================+===============================+===============================+
|     @knuth1984 says blah.         | @knuth1984 says blah.         | [1] says blah.                |
+-----------------------------------+-------------------------------+-------------------------------+
|     @knuth1984 [p. 33] says blah. | @knuth1984 [p. 33] says blah. | [1] [p. 33] says blah.        |
+-----------------------------------+-------------------------------+-------------------------------+

See the [Pandoc Citations](https://pandoc.org/MANUAL.html#citations) documentation for additional information on citation syntax.

### Citation Style  {#sec-citations-style}


Quarto uses Pandoc to format citations and bibliographies. By default, Pandoc will use the [Chicago Manual of Style](https://chicagomanualofstyle.org/) author-date format, but you can specify a custom formatting using CSL ([Citation Style Language](https://citationstyles.org)). To provide a custom citation stylesheet, provide a path to a CSL file using the `csl` metadata field in your document, for example:

``` yaml
---
title: "My Document"
bibliography: references.bib
csl: nature.csl
---
```

You can find CSL files or learn more about using styles at the [CSL Project](https://github.com/citation-style-language/styles). You can browse the list of more than 8,500 Creative Commons CSL definitions in the CSL Project's [central repository](https://github.com/citation-style-language/styles) or Zotero's [style repository](https://www.zotero.org/styles).

`CSL` styling is only available when the `cite-method` is `citeproc` (which it is by default). If you are using another `cite-method`, you can control the formatting of the references using the mechanism provided by that method.

### Bibliography Generation

By default, Pandoc will automatically generate a list of works cited and place it in the document if the style calls for it. It will be placed in a div with the id `refs` if one exists:

``` markdown
### References

::: {#refs}
:::
```

If no such div is found, the works cited list will be placed at the end of the document. 

If your bibliography is being generated using BibLaTeX or natbib (@sec-biblatex), the bibliography will always appear at the end of the document and the `#refs` div will be ignored.

::: callout-tip
You can suppress generation of a bibliography by including `suppress-bibliography: true` option in your document metadata
:::

Here's an example of a generated bibliography:

::: {#refs}
:::

### Including Uncited Items

If you want to include items in the bibliography without actually citing them in the body text, you can define a dummy `nocite` metadata field and put the citations there:

    ---
    nocite: |
      @item1, @item2
    ---

    @item3

In this example, the document will contain a citation for `item3` only, but the bibliography will contain entries for `item1`, `item2`, and `item3`.

It is possible to create a bibliography with all the citations, whether or not they appear in the document, by using a wildcard:

    ---
    nocite: |
      @*
    ---

### Using BibLaTeX or natbib {#sec-biblatex}

{{< include ../output-formats/_pdf-citations.md >}} 


## Footnotes

Pandoc supports numbering and formatting footnotes using the following syntax:

``` markdown
Here is a footnote reference,[^1] and another.[^longnote]

[^1]: Here is the footnote.

[^longnote]: Here's one with multiple blocks.

    Subsequent paragraphs are indented to show that they
belong to the previous footnote.

        { some.code }

    The whole paragraph can be indented, or just the first
    line.  In this way, multi-paragraph footnotes work like
    multi-paragraph list items.

This paragraph won't be part of the note, because it
isn't indented.
```

#### Output

Here is a footnote reference,[^1] and another.[^2]

This paragraph won't be part of the note, because it isn't indented.

In addition, you can also write single paragraph footnotes inline using the following syntax:

``` markdown
Here is an inline note.^[Inlines notes are easier to write,
since you don't have to pick an identifier and move down to
type the note.]
```

#### Output

Here is an inline note.[^3]

The footnotes that are generated from the above examples are included in the following section. See the [Pandoc Footnotes](https://pandoc.org/MANUAL.html#footnotes) for additional information.

[^1]: Here is the footnote.

[^2]: Here's one with multiple blocks.

    Subsequent paragraphs are indented to show that they belong to the previous footnote.

        { some.code }

    The whole paragraph can be indented, or just the first line. In this way, multi-paragraph footnotes work like multi-paragraph list items.

[^3]: Inlines notes are easier to write, since you don't have to pick an identifier and move down to type the note.


# quarto-web/docs/authoring/title-blocks.qmd

---
title: Title Blocks
---

## Overview

HTML pages rendered with Quarto include a formatted title block at the start of the article. The title block contains the title, subtitle, authors, date, doi, and abstract.

A simple example title block looks like:

![](images/document-title-block.png){.border fig-alt="Document with header reading: Summarizing Output for Reproducible Documents. Below is Author (Nora Jones), Affiliation (Spacely Sprockets), Published (5/4/2018). Below that is a description which reads: A summary of best practices for summarizing output of reproducible scientific documents."}

The title block will automatically layout elements from the front matter of the document. If you'd like, you can control the behavior using `title-block-style`.

There are three options available:

`default`

:   The default title-block treatment create a smaller font face and gathers the various title elements into stylized groups in the title block of the document.

`plain`

:   The plain treatment will do all the title element processing (gathering and organizing the elements), but will not apply the default title block styling.

`none`

:   `none` disables title block processing altogether. Content will not be processed or organized and the title block will be emitted verbatim from Pandoc.

## Title Banners

In addition, if you'd like a more prominent title block, you can use `title-block-banner` to create a banner style title block. A banner style title block will position the title, subtitle, description, and categories in a banner above the article. For example:

``` yaml
---
title-block-banner: true
---
```

will render a title block like:

![](images/document-title-block-banner.png){.border fig-alt="Title block with title and description against a blue background up top, and below a section with author, affilitation, and date published."}

### Custom Backgrounds

In this case, the color of the banner is automatically determined based upon the theme. However, you can control the banner background by providing either a CSS color (e.g. `"#FFDDFF"`, or `red`) or the path to an image which will be used the background. For example, to use a banner image, you might write:

``` yaml
---
title-block-banner: images/banner.jpeg
---
```

which would render a banner title block like:

![](images/document-title-block-banner-custom.png){.border fig-alt="Title block with title and description against an image background up top, and below a section with author, affilitation, and date published."}

When you provide an explicit background color or image, Quarto assumes that the color of the background will contrast with the body background color and automatically uses the body background color as the text color over the banner.

### Foreground Color

You can specify the color the for the text of the banner as well, using `title-block-banner-color` and providing a CSS color (e.g. `"#FFDDFF"`, or `red`) .

## Date

Quarto includes the document's `date` in the title block. In addition to writing a standard date, you may also use a few special keywords which will generate a date for you. `today` will provide the current date with the current time set to 0, `now` will provide the current date and time, and `last-modified` will provide the file modification date and time of the document itself.

### Formatting

When your title block is output using the `default` or `plain` styles, Quarto will automatically format the date based upon the document locale (`lang`). You can control formatting by specifying a `date-format` in the document front matter. For example:

``` yaml
---
title: Summarizing Output for Reproducible Documents
date: 2018-05-04
date-format: short
---
```

For more about date formats, see the Quarto [date format reference](/docs/reference/dates.qmd).

## Metadata Labels

The labels for the metadata included in the title block have default values that are properly localized, but you may want to provide your own labels for metadata. You can use the following to customize the labels:

| Option              | Label          | Styles                     |
|---------------------|----------------|----------------------------|
| `author-title`      | Authors        | `plain`, `default`         |
| `affiliation-title` | Affiliations   | `plain`, `default`         |
| `abstract-title`    | Abstract       | `plain`, `default`, `none` |
| `description-title` | Description    | `plain`, `default`         |
| `published-title`   | Date Published | `plain`, `default`         |
| `doi-title`         | DOI            | `plain`, `default`         |

## Custom Title Pages

To learn more about providing a complete custom title block, see the [documentation on template partials](../journals/templates.qmd#template-partials).


# quarto-web/docs/authoring/callouts.qmd

---
title: Callout Blocks
format: html
---

Callouts are an excellent way to draw extra attention to certain concepts, or to more clearly indicate that certain content is supplemental or applicable to only some scenarios.

## Callout Types

There are five different types of callouts available.

-   `note`
-   `warning`
-   `important`
-   `tip`
-   `caution`

The color and icon will be different depending upon the type that you select. Here are what the various types look like in HTML output:

::: callout-note
Note that there are five types of callouts, including: `note`, `tip`, `warning`, `caution`, and `important`.
:::

::: callout-warning
Callouts provide a simple way to attract attention, for example, to this warning.
:::

::: callout-important
## This is Important

Danger, callouts will really improve your writing.
:::

::: callout-tip
## Tip With Title

This is an example of a callout with a title.
:::

::: {.callout-caution collapse="true"}
## Expand To Learn About Collapse

This is an example of a 'collapsed' caution callout that can be expanded by the user. You can use `collapse="true"` to collapse it by default or `collapse="false"` to make a collapsible callout that is expanded by default.
:::

## Markdown Syntax

Create callouts in markdown using the following syntax (note that the first markdown heading used within the callout is used as the callout heading):

``` markdown
::: {.callout-note}
Note that there are five types of callouts, including:
`note`, `warning`, `important`, `tip`, and `caution`.
:::

::: {.callout-tip}
## Tip with Title

This is an example of a callout with a title.
:::

::: {.callout-caution collapse="true"}
## Expand To Learn About Collapse

This is an example of a 'folded' caution callout that can be expanded by the user. You can use `collapse="true"` to collapse it by default or `collapse="false"` to make a collapsible callout that is expanded by default.
:::
```

Note that above callout titles are defined by using a heading at the top of the callout. If you prefer, you can also specify the title using the `title` attribute. For example:

```markdown
::: {.callout-tip title="Tip with Title"}
This is a callout with a title.
:::
```

## Customizing Appearance

### Collapse

You can create 'folded' callouts that can be expanded by the user by settings the `collapse` attribute on the callout. If you set `collapse=true`, the callout will be expandable, but will be collapsed by default. If you set `collapse=false`, the callout will be expandable, but will be expanded by default.

### Appearance

Callouts have 3 different looks you can use.

|           |                                                                                                                 |
|-----------|-----------------------------------------------------------------------------------------------------------------|
| `default` | The default appearance with colored header and an icon.                                                         |
| `simple`  | A lighter weight appearance that doesn't include a colored header background.                                   |
| `minimal` | A minimal treatment that applies borders to the callout, but doesn't include a header background color or icon. |

You can set the callout appearance either globally in the document (or project yaml):

``` yaml
callout-appearance: simple
```

or by setting the `appearance` attribute on the callout. For example

``` markdown
::: {.callout-note appearance="simple"}

## Pay Attention

Using callouts is an effective way to highlight content that your reader give special consideration or attention.

:::
```

which appears as:

::: {.callout-note appearance="simple"}
## Pay Attention

Using callouts is an effective way to highlight content that your reader give special consideration or attention.
:::

### Icons

In addition to controlling the appearance of the callout, you can also choose to directly suppress the icon by setting the global option in your document (or project) yaml:

``` yaml
callout-icon: false
```

or by setting an attribute directly on the callout:

``` markdown
::: {.callout-note icon=false}

## Pay Attention

Using callouts is an effective way to highlight content that your reader give special consideration or attention.

:::
```

Which will appear as:

::: {.callout-note icon="false"}
## Pay Attention

Using callouts is an effective way to highlight content that your reader give special consideration or attention.
:::

## Format Support

The following formats render callouts as illustrated above:

-   HTML
-   PDF
-   MS Word
-   EPUB
-   revealjs

Note that callout rendering for HTML is not available when you disable the standard HTML theme (e.g. if you specify the `theme: none` option). Also, some features are specific to document using Bootstrap, like collapsible callouts, and won't work in other documents.

When the target format doesn't support callouts, they are rendered as a simple blockquote with the title in bold.


# quarto-web/docs/authoring/conditional.qmd

---
title: "Conditional Content"
---

In some cases you may want to create content that only displays for a given output format (or only displays when *not* rendering to a format). You can accomplish this by creating divs, spans and code blocks with the `.content-visible` and `.content-hidden` classes.

## .content-visible

To make content visible only for a given format, you can create a div (`:::`) with the `.content-visible` class. For example, here we mark content as only visible in HTML:

``` markdown
::: {.content-visible when-format="html"}

Will only appear in HTML.

:::
```

You can also set conditions on non-executable code blocks:

```` markdown
```{.python .content-visible when-format="html"}
# code shown only in HTML
2+2
```
````

To apply a condition only to a part of a paragraph, use a span (`[]{}`):

``` markdown
Some text
[in HTML.]{.content-visible when-format="html"}
[in PDF.]{.content-visible when-format="pdf"}
```

You can also mark content as visible for all formats *except* a specified format. For example:

``` markdown
::: {.content-visible unless-format="pdf"}

Will not appear in PDF.

:::
```

Then `when-format` and `unless-format` attributes match the current Pandoc output format with some additional intelligence to alias related formats (e.g. html, html4, and html5). Details are provided below in [Format Matching](#format-matching)

`when-format` and `unless-format` can also be combined to create more complex conditions:

``` markdown
::: {.content-visible when-format="html" unless-format="revealjs"}

Will only appear in HTML and not in Reveal.js, but actually it appears.

:::

::: {.content-visible when-format="revealjs"}

Will only appear in Reveal.js and not in HTML or other formats.

:::
```

## .content-hidden

To prevent content from being displayed when rendering to a given format, use the `.content-hidden` class. For example, here we mark content as hidden in HTML:

``` markdown
::: {.content-hidden when-format="html"}

Will not appear in HTML.

:::
```

You can also mark content as hidden for all formats *except* a specified format. For example:

``` markdown
::: {.content-hidden unless-format="pdf"}

Will only appear in PDF.

:::
```

## Format Matching {#format-matching}

Then `when-format` and `unless-format` clauses do some aliasing of related formats to make it more straightforward to target content. The following aliases are implemented:

{{< include _format-aliases.md >}}


# quarto-web/docs/authoring/notebook-embed.qmd

---
title: Embedding Jupyter Notebook Cells
aliases:
  - /docs/prerelease/1.3/embed.html
---

{{< include ../_require-1.3.qmd >}}

## Overview

You can include the output of an external Jupyter notebook in a Quarto document with the `embed` shortcode. To embed a notebook cell, provide the path to a Jupyter Notebook and a cell identifier. For example, this notebook called `penguins.ipynb` has a cell labelled `fig-bill-scatter`:

![](images/notebook-simple.png){fig-alt="A screenshot of a Jupyter Notebook with the name 'penguins.ipynb', with a cell highlighted that has the code chunk option label set to fig-bill-scatter. Below the cell is the resulting plot."}

You can use the following shortcode to embed the output of this cell:

```{.markdown shortcodes=false}
{{< embed penguins.ipynb#fig-bill-scatter >}}
```

This will embed the plot as follows:

{{< embed penguins.ipynb#fig-bill-scatter >}}

A link to the source notebook is automatically provided beneath the plot. Following the link takes users to a rendered version of the notebook, allowing them to explore the notebook without having to download and run it locally. For example, clicking on the link to `penguins.ipynb` gets you to a page that looks like the following:

![](images/notebook-view.png){.border fig-alt="A screenshot of webpage with the title 'penguins.ipynb', a large blue button labelled 'Download Notebook', followed by the notebook contents."}

Beyond this basic usage, you can also:

-   Specify cells in multiple ways, see [Specifying Cells](#specifying-cells).

-   Control the output using code cell options in the source Notebook, including things like figure captions, figure layout, and code display, see [Code Cell Options](#code-cell-options).

-   Include the cell code along with the output by adding an `echo` option to the shortcode, see [Embedding Code](#embedding-code).

-   Customize or exclude the link to the the source notebooks, see [Links to Source Notebooks](#linked-source-notebooks).

## Specifying Cells {#specifying-cells}

The `embed` shortcode specifies target notebooks using a relative path followed by a cell identifier (e.g. `penguins.ipynb#fig-bill-scatter`). If the cell identifier is omitted, all of the cells in the notebook will be embedded in the document.

The cell identifier is used to locate the proper cell using the following heuristics:

1.  **Cell `id`**\
    First, the cell metadata will be checked for a matching `id`. ([Cell IDs](https://jupyter.org/enhancement-proposals/62-cell-id/cell-id.html) are a newer feature of Jupyter Notebooks that are not yet well supported in Jupyter front ends, but `id` is checked first to allow for future compatibility as they become more common).
2.  **Label**\
    If no cell with a matching `id` is found, Quarto will use a cell that has a `label` in the code metadata which matches the cell identifier.
3.  **Tags**\
    If no cell has been found, Quarto will use a cell or cell(s) whose tag matches the cell identifier.

### Cell Tags

For example, to embed the output of a cell that you have given the tag `bill-ratio` within Jupyter Lab:

![](images/notebook-tag.png){.border fig-alt="Screenshot of a code cell in a Jupyter Notebook with the cell tags open in the cell toolbar and displaying the tag 'bill-ratio'."}

You would use the following embed:

```{.markdown shortcodes=false}
{{< embed penguins.ipynb#bill-ratio >}}
```

Which results in the following output:

{{< embed penguins.ipynb#bill-ratio >}}

## Code Cell Options {#code-cell-options}

Code cell options from the source Jupyter Notebook are propagated to the document in which they are embedded. For instance, you may specify code cell options like `fig-cap`, `fig-alt` and `layout-ncol`, to control aspects of embedded figures. For example, this cell in the Notebook specifies figure options including a caption, sub-caption, alt text and layout:

```{.python filename="penguins.ipynb"}
#| label: fig-bill-marginal
#| fig-cap: "Marginal distributions of bill dimensions"
#| fig-subcap: 
#|   - "Gentoo penguins tend to have thinner bills,"
#|   - "and Adelie penguins tend to have shorter bills."
#| fig-alt:
#|   - "Density plot of bill depth by species."
#|   - "Density plot of bill length by species."
#| layout-ncol: 2

sns.displot(penguins, 
            x = "bill_depth_mm", 
            hue = "species", 
            kind = "kde", fill = True, aspect = 2, height = 3)
plt.show()
sns.displot(penguins, 
            x = "bill_length_mm", 
            hue = "species", 
            kind = "kde", fill = True, aspect = 2, height = 3)
plt.show()
```

When this cell is embedded:

```{.markdown shortcodes=false}
{{< embed penguins.ipynb#fig-bill-marginal >}}
```

The following output is produced:

{{< embed penguins.ipynb#fig-bill-marginal >}}

## Embedding Code {#embedding-code}

You may include the code from a cell along with the output by using the `echo=true` option. For example, to include the code and the plot from the cell labelled `species-counts` the embed would be:

```{.markdown shortcodes=false}
{{< embed penguins.ipynb#species-counts echo=true >}}
```

The result in the document is both the code and output for the cell:

{{< embed penguins.ipynb#species-counts echo=true >}}

Like figure options, options for displaying the code will propagate from the source Jupyter Notebook. For example, to fold the code for this cell, you could add `code-fold: true` to the options for the `species-counts` cell:

```{.python filename="penguins.ipynb"}
#| label: species-counts
#| code-fold: true
penguins.groupby("species").size().reset_index(name = "count")
```

The options set in the YAML header for the document in which these cells are embedded will also control these code cells. For example, to fold all the code, including the code embedded from `penguins.ipynb`, you could add `code-fold: true` to the document YAML:

```{.yaml filename="sample.qmd"}
title: Exploration of penguin characteristics
author: Norah Jones
toc: true
format:
  html:
    code-fold: true
```

## Links to Source Notebooks {#linked-source-notebooks}

When you embed the contents of Notebooks in a Quarto document and render the document to HTML, Quarto will automatically include links to the source Notebooks that provided the embedded content. These links will by default appear both inline below the embedded content as well as below the table of contents. For example, the following document embeds content from the notebook `penguins.ipynb`. You can see the links in the rendered HTML document below:

![](images/notebook-links.png){.border fig-alt="Screenshot of a rendered page with an embedded plot. A link to the Source 'penguins.ipynb' is shown directly below the plot. A similar link is shown below the table of contents under the heading 'Notebooks'."}

### Link Placement

You can control the placement of the links to source notebooks by specifying the option `notebook-links`{spellcheck="false"} in the document YAML with one of the following values:

`true`{spellcheck="false"} (default)

:   Display links to source notebooks inline below the embedded content, and alongside the table of contents.

`false`{spellcheck="false"}

:   Do not display any links to source notebooks.

`inline`{spellcheck="false"}

:   Display only the links inline below the embedded content.

`global`{spellcheck="false"}

:   Display only the links alongside the table of contents. 

### Notebook Views

By default, the link to the source notebook goes to an automatically generated HTML render of the notebook. This makes it easier for users to view the Notebook contents without needing to download and run the Notebook locally. This notebook view displays the contents of the notebook and includes a button to download the notebook.  For example:

![](images/notebook-view.png){.border fig-alt="A screenshot of webpage with the title 'penguins.ipynb', a large blue button labelled 'Download Notebook', followed by the notebook contents."}

As an example, you can view the [live preview for the \`penguins.ipynb\` notebook](penguins.ipynb.html) used in this document.

### View Options

You can control the behavior of notebook views using `notebook-view`. For each source notebook, you can provide a `title` and a `url`. The `title` will be used as the text of the any links to the source notebook and will also appear at the top of the rendered notebook view. The `url`, if provided, will be used as the `href` of any links to the source notebook. This is useful if you have deployed a copy of the source notebook to a site like Github, Google Colab, or Kaggle and would rather link to that instead.

For example:

``` {.markdown style="whitespace: pre-wrap;"}
notebook-view:
  - notebook: penguins.ipynb
    title: "Plots and Computations"
    url: https://colab.research.google.com/drive/12GsIPQ644SI4vkEEHiZn-Qqfbr-bD1__
```

will result in links to the source notebook like so:

![](images/notebook-links-updated.png){.border fig-alt="Screenshot of a rendered page with an embedded plot. A link to the Source 'Plots and Computations' is shown directly below the plot. A similar link is shown below the table of contents under the heading 'Notebooks'."}

To disable the notebook views, and instead link directly to the Jupyter notebook (so the user may download the notebook with no intermediary view), set `notebook-view` to `false`.


# quarto-web/docs/authoring/appendices.qmd

---
title: Appendices
---

## Overview

HTML pages rendered with Quarto include a formatted appendix at the end of the article. The appendix includes sections for citations and footnotes in the document, as well the attribution information (if specified) for the document itself.

A simple example document appendix looks like:

![](images/document-appendix-simple.png){.border fig-alt="Appendix with two sections: References, and Footnotes."}

To learn more about including document attribution information in the appendix, see [Creating Citeable Articles](/docs/authoring/create-citeable-articles.qmd).

## Custom Appendix Sections

Sections of your document can be added to the Appendix that appears at the end of your article by adding the `.appendix` class to any header. For example:

``` yaml
## Acknowledgments {.appendix}

I am grateful for the insightful comments offered by the anonymous peer reviewers at Books & Texts. The generosity and expertise of one and all have improved this study in innumerable ways and saved me from many errors; those that inevitably remain are entirely my own responsibility.
```

Any sections marked with the `.appendix` class will be included at the front of the appendix in the order in which they appear in the document. A more complete example appendix including attribution and the above custom appendix section looks like:

![](images/document-appendix-full.png){.border fig-alt="Appendix with Acknowledgements, References, Footnes, and Citation sections. The Citation section contains both BibTex citation, and plain text for attribution."}

## License

If you include a license in the front matter or citation information for your document, a 'Reuse' section will automatically be added to the appendix. Read more about specifying a license in [Front Matter](/docs/authoring/front-matter.qmd#license).

Here is an example of a complete appendix including all the fields with an Attribution-ShareAlike Creative Commons license.

![](images/document-appendix-reuse.png){.border fig-alt="Appendix with Acknowledgements, References, Footnotes, Reuse, and Citation sections. The Reuse section contains a link to the Attribution-ShareAlike Creative Commons license."}


## Appendix Style

You can control how Quarto process the appendix of your document using the `appendix-style` option. There are three options available:

`default`

:   The default appendix treatment create a smaller font face and gathers the various sections into stylized groups at the end of the document.

`plain`

:   The plain treatment will do all the appendix processing (gathering and organizing the sections at the end of the document, creating sections like 'Reuse'), but will not apply the default appendix styling.

`none`

:   `none` disables appendix processing altogether. Content will not be processed or organized and information like 'Citation' and 'Reuse' will not be included in the document.


# quarto-web/docs/authoring/_pagebreak.qmd

## Page Breaks

The `pagebreak` shortcode enables you to insert a native pagebreak into a document (.e.g in LaTeX this would be a `\newpage`, in MS Word a docx-native pagebreak, in HTML a `page-break-after: always` CSS directive, etc.):

```{.markdown shortcodes="false"}
page 1

{{< pagebreak >}}

page 2
```

Native pagebreaks are supported for HTML, LaTeX, Context, MS Word, Open Document, and ePub (for other formats a form-feed character `\f` is inserted).



# quarto-web/docs/authoring/create-citeable-articles.qmd

---
title: Creating Citeable Articles
---

You can make it easier for others to cite your work by providing additional metadata with the YAML front-matter of your article. Citations can be provided for both articles published to the web or for articles published in journals (with or without a DOI).

## Web Articles

To provide a citation for an article published to the web, include author and date metadata as well as a citation url. For example:

``` yaml
---
title: "Summarizing Output for Reproducible Documents"
description: | 
  A summary of the best practices for summarizing output of reproducible scientific documents.
date: 5/4/2018
author:
  - name: Nora Jones 
    url: https://example.com/norajones
    affiliation: Spacely Sprockets
    affiliation-url: https://example.com/spacelysprockets
citation:
  url: https://example.com/summarizing-output
bibliography: biblio.bib
---
```
Name particles can be further defined in the `name` key following the [Citation Style Language (CSL) specification for naming particles](https://docs.citationstyles.org/en/stable/specification.html#name-particles). If you omit the citation url, Quarto will attempt to generate a citation url by using the `site-url` and the current page's location. If you'd like to allow Quarto to generate the citation url, you can omit the citation url and simply enable citation output on the page. For example:

``` yaml
---
title: "Summarizing Output for Reproducible Documents"
description: | 
  A summary of the best practices for summarizing output of reproducible scientific documents.
date: 5/4/2018
author:
  - name: Nora Jones 
    url: https://example.com/norajones
    affiliation: Spacely Sprockets
    affiliation-url: https://example.com/spacelysprokets
citation: true
bibliography: biblio.bib
---
```

When this metadata is available, a citation appendix is automatically added to the article. The citation appendix will present both a copy-able `bibtex` representation of the document and a formatted representation of the citation (based upon the document's CSL file, if specified). For example:

![](images/appendix-citation.png){.border fig-alt="Appearance of a citation appendix contains both BibTeX citation and plain text citation for attribution."}

By default both the `bibtex` and formatted representations are displayed. You can use the `appendix-cite-as` option to control this behavior:

+-----------------------------+------------------------------------------------+
| `appendex-cite-as: false`   | Do not include any citations in the appendix.  |
+-----------------------------+------------------------------------------------+
| `appendix-cite-as: bibtex`  | Show only the BibTeX version of the citation.  |
+-----------------------------+------------------------------------------------+
| `appendix-cite-as: display` | Show only the display version of the citation. |
+-----------------------------+------------------------------------------------+

: {tbl-colwidths="\[50,50\]"}

## Journal Articles

If your article is published within a Journal, you can add the following the additional fields to generate the appropriate citation entry:

``` yaml
---
title: "Summarizing Output for Reproducible Documents"
description: | 
  A summary of the best practices for summarizing output of reproducible scientific documents.
date: 5/4/2018
author:
  - name: Nora Jones 
    url: https://example.com/norajones
    affiliation: Spacely Sprockets
    affiliation-url: https://example.com/spacelysprokets
citation:
  type: article-journal
  container-title: "Journal of Data Science Software"
  doi: "10.23915/reprodocs.00010"
  url: https://example.com/summarizing-output
bibliography: biblio.bib
---
```

This is how the citation is presented in the appendix:

![](images/appendix-citation-journal.png){.border fig-alt="Appearance of a journal citation in document appendix with both BibTex and plain text citations given for attribution."}

## Other Types of Documents

The BibTeX and formatted attribution displayed in the document will be generated based upon the complete citation information that is present in the `citation` key, which is based upon the [Citation Style Language (CSL) specification for items](https://docs.citationstyles.org/en/stable/specification.html). You can learn more about the available options in the [Citation Metadata Reference](/docs/reference/metadata/citation.qmd).

## Google Scholar

Quarto documents can include metadata compatible with the format indexed by [Google Scholar](https://scholar.google.com). This makes it easy for indexing engines (Google Scholar or otherwise) to extract not only a citation for your article but also information on other sources which you cited. To enable this use the `google-scholar` option:

``` yaml
title: "Summarizing Output for Reproducible Documents"
description: | 
  A summary of the best practices for summarizing output of reproducible scientific documents.
date: 5/4/2018
author:
  - name: Nora Jones 
    url: https://example.com/norajones
    affiliation: Spacely Sprockets
    affiliation-url: https://example.com/spacelysprokets
citation:
  type: article-journal
  container-title: "Journal of Data Science Software"
  doi: "10.23915/reprodocs.00010"
  url: https://example.com/summarizing-output
bibliography: biblio.bib 
google-scholar: true
```

For example, here is the Google Scholar metadata automatically included for a document created with the above metadata:

``` {.html style="font-size: 0.9em;"}
<meta name="citation_title" content="Summarizing Output for Reproducible Documents">
<meta name="citation_author" content="Nora Jones">
<meta name="citation_online_date" content="2018-05-04">
<meta name="citation_fulltext_html_url" content="https://example.com/summarizing-output">
<meta name="citation_publication_date" content="2018-05-04">
<meta name="citation_journal_title" content="Journal of Data Science Software">
<meta name="citation_reference" content="citation_title=Donald knuth;,citation_fulltext_html_url=http://dx.doi.org/10.7551/mitpress/
5485.003.0041;,citation_publication_date=1989;,citation_journal_title
=undefined;">
```

In the addition to the citation metadata from this document described above, Quarto will automatically generate a `citatation_reference` entry for each of the entries included in the document's bibliography.

## Citation Fields

Quarto's approach to emitting scholarly metadata is to take the standard CSL fields and make them into the corresponding Google Scholar / Zotero / Highwire metadata tags as appropriate. The following fields, when specified under the `citation` key of the document metadata, will generate scholarly meta tags in the rendered HTML document as described. These fields comprise the required Google Scholar fields as well as additional, optional fields that may also be included.

+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Document Yaml                                                                                                                                 | Metadata Tag                                                                            |
+===============================================================================================================================================+=========================================================================================+
| `title`\                                                                                                                                      | `citation_title`                                                                        |
| <sub>Document `title` will be used if not provided.</sub>                                                                                     |                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `author`\                                                                                                                                     | `citation_author`                                                                       |
| <sub>One or more authors[^1]. Document `author` will be used if not provided as a citation subkey.</sub>                                      |                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `editor`\                                                                                                                                     | `citation_editor`                                                                       |
| <sub>One or more editors[^2].</sub>                                                                                                           |                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `abstract`\                                                                                                                                   | `citation_abstract`                                                                     |
| <sub>Document `abstract` will be used if not provided.</sub>                                                                                  |                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `keyword`[^3]\                                                                                                                                | `citation_keywords`                                                                     |
| <sub>Document `keywords` will be used if not provided.</sub>                                                                                  |                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `issued`\                                                                                                                                     | `citation_publication_date`                                                             |
| <sub>Document `date` will be used if not provided.</sub>                                                                                      |                                                                                         |
|                                                                                                                                               | <sub>In addition, the issued date will be used to populate the following fields:</sub>\ |
|                                                                                                                                               | \                                                                                       |
|                                                                                                                                               | `citation_cover_date`\                                                                  |
|                                                                                                                                               | `citation_year`                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `available-date`\                                                                                                                             | `citation_online_date`                                                                  |
| <sub>Document `date` will be used if not provided.</sub>                                                                                      |                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `url`\                                                                                                                                        | `citation_fulltext_html_url`                                                            |
| <sub>`url` will be synthesized for current document if a [`site-url`](../websites/website-tools.qmd#preview-images) has been specified.</sub> |                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `pdf-url`                                                                                                                                     | `citation_pdf_url`                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `language`\                                                                                                                                   | `citation_language`                                                                     |
| <sub>Document `lang` will be used if not provided.</sub>                                                                                      |                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `type`\                                                                                                                                       | `<none>`                                                                                |
| <sub>A valid CSL type. See <https://docs.citationstyles.org/en/stable/specification.html#appendix-iii-types></sub>.                           |                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `doi`\                                                                                                                                        | `citation_doi`                                                                          |
| <sub>Document `doi` will be used if not provided.</sub>                                                                                       |                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `isbn`                                                                                                                                        | `citation_isbn`                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `issn`                                                                                                                                        | `citation_issn`                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `eissn`                                                                                                                                       | `citation_eissn`                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `pmid`                                                                                                                                        | `citation_pmid`                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `issue`                                                                                                                                       | `citation_issue`                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `volume`                                                                                                                                      | `citation_volume`                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `page`\                                                                                                                                       | `citation_firstpage`                                                                    |
| <sub>Will be split on `-` to create appropriate page metadata.</sub>                                                                          |                                                                                         |
|                                                                                                                                               | `citation_lastpage`                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `page-first`                                                                                                                                  | `citation_firstpage`                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `page-last`                                                                                                                                   | `citation_lastpage`                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `abstract-url`                                                                                                                                | `citation_abstract_html_url`                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `container-title`                                                                                                                             | `citation_journal_title`                                                                |
|                                                                                                                                               |                                                                                         |
|                                                                                                                                               | <small> For specific types, other meta tags will be produced:                           |
|                                                                                                                                               |                                                                                         |
|                                                                                                                                               | -   type: paper-conference\                                                             |
|                                                                                                                                               |     `citation_conference_title`                                                         |
|                                                                                                                                               |                                                                                         |
|                                                                                                                                               | -   type: book\                                                                         |
|                                                                                                                                               |     `citation_book_title`                                                               |
|                                                                                                                                               |                                                                                         |
|                                                                                                                                               | -   type: chapter\                                                                      |
|                                                                                                                                               |     `citation_inbook_title` </small>                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `number`                                                                                                                                      | `citation_technical_report_number`                                                      |
|                                                                                                                                               |                                                                                         |
|                                                                                                                                               | <sub>`citation_technical_report_number` will be created if the type is report.</sub>    |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `publisher`                                                                                                                                   | `citation_publisher`                                                                    |
|                                                                                                                                               |                                                                                         |
|                                                                                                                                               | <small>For specific types, other meta tags will be produced:                            |
|                                                                                                                                               |                                                                                         |
|                                                                                                                                               | -   type: paper-conference\                                                             |
|                                                                                                                                               |     `citation_conference`                                                               |
|                                                                                                                                               |                                                                                         |
|                                                                                                                                               | -   type: thesis\                                                                       |
|                                                                                                                                               |     `citation_dissertation_institution`                                                 |
|                                                                                                                                               |                                                                                         |
|                                                                                                                                               | -   type:report\                                                                        |
|                                                                                                                                               |     `citation_technical_report_institution`                                             |
|                                                                                                                                               |                                                                                         |
|                                                                                                                                               | </small>                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `container-title-short`                                                                                                                       | `citation_journal_abbrev`                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| `collection-title`                                                                                                                            | `citation_series_title`                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+

[^1]: Specify one or more authors using one of the following:

    ``` yaml
    author: Norah Jones
    ```

    or multiple values like:

    ``` yaml
    author:
    -   Norah Jones
    -   Nick Fury
    ```

    The list of authors provded under the citation key will be used instead of the document authors when generating the html metadata.

[^2]: Specify one or more editors using one of the following:

    ``` yaml
    editors: Norah Jones
    ```

    or multiple values like:

    ``` yaml
    editors:
    -   Norah Jones
    -   Nick Fury
    ```

[^3]: Note that the `keyword` citation field is a comma separated string of keywords (consistent with CSL).

For example, citation data for a published conference paper defined as such in the document front matter:

``` yaml
title: A Published Conference Paper
author:
  - name: Norah Jones
    affiliation: School of Hard Knocks
    orcid: 0000-0001-8715-9476
citation:
  type: paper-conference
  container-title: "Proceedings of the annual conference of the Society for Research"
  publisher: "Society for Research"
  issued: 2020/09/23
  volume: 2
  doi: "10.23915/reprodocs.00010"
  url: https://example.com/summarizing-output
  page-first: 46
  page-last: 53
  editor:
  - Don Draper
  - Nick Fury
google-scholar: true  
```

provides HTML metadata like:

``` html
<meta name="citation_title" content="A Published Conference Paper">
<meta name="citation_author" content="Norah Jones">
<meta name="citation_editor" content="Nick Cage">
<meta name="citation_editor" content="Don Draper">
<meta name="citation_publication_date" content="2020-09-23">
<meta name="citation_cover_date" content="2020-09-23">
<meta name="citation_year" content="2020">
<meta name="citation_fulltext_html_url" content="https://example.com/summarizing-output">
<meta name="citation_doi" content="10.23915/reprodocs.00010">
<meta name="citation_volume" content="2">
<meta name="citation_language" content="en">
<meta name="citation_conference_title" content="Proceedings of the annual conference of the Society for Research">
<meta name="citation_conference" content="Society for Research">
```


# quarto-web/docs/authoring/language.qmd

---
title: "Document Language"
---

## Overview

Document language plays a role in Pandoc's processing of most formats, and controls hyphenation in PDF output when using LaTeX (through [`babel`](https://ctan.org/pkg/babel) and [`polyglossia`](https://ctan.org/pkg/polyglossia)) or ConTeXt.

Additonally, Quarto, Pandoc, and LaTeX will sometimes generate textual output that requires localization. For example, "Figure" or "List of Figures" for cross references, callout captions like "Note" or "Warning", or the "Code" caption for folded code chunks.

## `lang` Option

The [`lang`](https://pandoc.org/MANUAL.html#language-variables) document option identifies the main language of the document using IETF language tags (following the [BCP 47](https://tools.ietf.org/html/bcp47) standard), such as `en` or `en-GB`. The [Language subtag lookup](https://r12a.github.io/app-subtags/) tool can look up or verify these tags.

For example, this document specifies the use of French:

``` yaml
---
title: "My Document"
lang: fr    
---
```

This will result in the use of French translations as well as the application of other language specific rules to document processing. The following languages currently have full translations available:

-   English (`en`, used by default)
-   Chinese (`zh`)
-   Spanish (`es`)
-   French (`fr`)
-   Japanese (`ja`)
-   German (`de`)
-   Portuguese (`pt`)
-   Russian (`ru`)
-   Czech (`cs`)
-   Finnish (`fi`)
-   Dutch (`nl`)
-   Italian (`it`)
-   Polish (`pl`)
-   Korean (`ko`)

## Alternate Language

If you aren't happy with the default language used for a given part of a document you can provide alternate language via the `language` key (this can be used at a document or project level). For example, to override the values for the "Author" and "Published" captions used within title blocks you could do this:

``` yaml
---
title: "My Document"
author: "Norah Jones"
date: 5/22/2022
language: 
  title-block-author-single: "Writer"
  title-block-published: "Updated"
---
```

As described below, you can also provide these translations in a standalone YAML file and reference it as follows:

``` yaml
---
title: "My Document"
author: "Norah Jones"
date: 5/22/2022
language: custom.yml
---
```

You can discover all of the `language` values that can be customized by referencing this file: <https://github.com/quarto-dev/quarto-cli/blob/main/src/resources/language/_language.yml>.

### Per-Language Alternates

Alternate values can be restricted to a particular target language using subkeys of the `language` key. This way, distinct values can be defined for each language. For example, you can override the English and French versions of the "Published" caption:

``` yaml
---
title: "My Document"
author: "Norah Jones"
date: 5/22/2022
lang: fr
language:
  en:
    title-block-published: "Updated"
  fr:
    title-block-published: "Mis à jour"
---
```

In this case the French "Mis à jour" will be used since `lang` is set to `fr`.

These language-specific alternate values can also be provided in a standalone YAML file. For example, the following file could be used by setting `language: custom-language.yml` in the metadata:

``` {.yaml filename="custom-language.yml"}
en:
  title-block-published: "Updated"
fr:
  title-block-published: "Mis à jour"
```

## Custom Translations

You can create and use a custom translation for a new language not supported by Quarto as follows:

1.  Make a copy of the default `_language.yml` file (<https://github.com/quarto-dev/quarto-cli/blob/main/src/resources/language/_language.yml>).

2.  Provide translations from the default English values.

3.  Specify the custom translation file using the `language` option. For example:

    ``` yaml
    ---
    language: custom.yml
    ---
    ```

The `language` option can be specified at a project or document level. Additionally, if you include a `_language.yml` file in the root of your project alongside your `_quarto.yml` config file it will be automatically used.

If you create a language translation file please consider contributing it so others can benefit from it. See the documentation on [contributing language translations](https://github.com/quarto-dev/quarto-cli/tree/main/src/resources/language) for additional details.


# quarto-web/docs/authoring/includes.qmd

---
title: "Includes"
---

## Overview

Includes are a convenient way to re-use content across documents. Includes work for plain markdown content as well as for `.qmd` files with executable code cells (note however that the cells must all use the same engine -- i.e. knitr or jupyter, but not both).

To include a file, add the `{{{< include >}}}` shortcode at the location in your document where you want it included.

``` markdown
{{{< include _content.qmd >}}}
```

::: callout-important

Include shortcodes are equivalent to copying and pasting the text from the included file into the main file. This means that relative references (links, images, etc.) inside the included file resolve based on the directory of the main file not the included file.

:::

::: callout-important

Include shortcodes need to appear by themselves in a line, and they need to be surrounded by empty lines. This means that you cannot use an include shortcode inside markdown syntax (such as an item in a bulleted list).

:::

## Content

A concrete example would be if you have several articles about a topic that share a common introduction. Here we have an article titled "Revealjs Presentations" that wants to include some basic information on presentations not specific to Revealjs (we do that by including `_basics.qmd`):

``` markdown
---
title: "Revealjs Presentations"
---

## Overview

Revealjs Presentations are a great way to
present your ideas to others!

{{{< include _basics.qmd >}}}

## Revealjs Options

More content here...
```

Note that we use an underscore (`_`) prefix for the included file. You should always use an underscore prefix with included files so that they are automatically ignored (i.e. not treated as standalone files) by a `quarto render` of a project.

## Computations

You can also include files with computational cells. For example, here we include a `.qmd` that does some data preprocessing that we want shared across multiple documents:

``` markdown
---
title: "My Document"
---

{{{< include _data.qmd >}}}


Use the data...
```

A couple of important things to remember when using computational includes:

1)  All computations still share a single engine (e.g. knitr or jupyter)

2)  Computational includes work only in `.qmd` files (they don't work in `.ipynb` notebook files)

```{=html}
<style type="text/css">
code span.in {
  font-style:  normal;
}
</style>
```


# quarto-web/docs/authoring/tables.qmd

---
title: Tables
engine: jupyter
---

## Overview

Quarto includes a number of features aimed at making it easy to to author and customize markdown table output, including:

-   Specifying column alignment and widths.
-   Providing captions, subcaptions, and cross-references.
-   Generating tables dynamically from executable code cells.

This article covers using these features in-depth.

## Markdown Tables

The most commonly used markdown table is known as a pipe table. Pipe tables support specifying per column alignment as well as captions. For example:


::: {layout-ncol="2"}

:::: {}

``` markdown
| Default | Left | Right | Center |
|---------|:-----|------:|:------:|
| 12      | 12   |    12 |   12   |
| 123     | 123  |   123 |  123   |
| 1       | 1    |     1 |   1    |

: Demonstration of pipe table syntax
```

::::

:::: {}

| Default | Left | Right | Center |
|---------|:-----|------:|:------:|
| 12      | 12   |    12 |   12   |
| 123     | 123  |   123 |  123   |
| 1       | 1    |     1 |   1    |

: Demonstration of pipe table syntax

::::

:::

The beginning and ending pipe characters are optional, but pipes are required between all columns. The colons indicate column alignment as shown. The header cannot be omitted, however you can simulate a headerless table by including a header with blank cells.

Since the pipes indicate column boundaries, columns need not be vertically aligned, as they are in the above example. So, this is a perfectly legal (though ugly) pipe table:

``` markdown
fruit| price
-----|-----:
apple|2.05
pear|1.37
orange|3.09
```

The cells of pipe tables cannot contain block elements like paragraphs and lists, and cannot span multiple lines. If a pipe table contains a row whose markdown content is wider than the column width (see `columns` option), then the table will take up the full text width and the cell contents will wrap, with the relative cell widths determined by the number of dashes in the line separating the table header from the table body.

For example `---|-` would make the first column 3/4 and the second column 1/4 of the full text width. On the other hand, if no lines are wider than column width, then cell contents will not be wrapped, and the cells will be sized to their contents.

### Using Bootstrap classes

Bootstrap table classes given as attributes next to a table caption are inserted into the `<table>` element.
The classes permitted are those that apply expressly to the entire table, and these are:
`"primary"`, `"secondary"`, `"success"`, `"danger"`, `"warning"`, `"info"`, `"light"`, `"dark"`, `"striped"`, `"hover"`, `"active"`, `"bordered"`, `"borderless"`, `"sm"`, `"responsive"`, `"responsive-sm"`, `"responsive-md"`, `"responsive-lg"`, `"responsive-xl"`, `"responsive-xxl"`.
For example, the following Markdown table will be rendered with row stripes and the rows will also be highlighted on hover:

::: {layout-ncol="2"}

:::: {}


``` markdown
| fruit  | price  |
|--------|--------|
| apple  | 2.05   |
| pear   | 1.37   |
| orange | 3.09   |

: Fruit prices {.striped .hover}
```

::::

:::: {}

| fruit  | price  |
|--------|--------|
| apple  | 2.05   |
| pear   | 1.37   |
| orange | 3.09   |

: Fruit prices {.striped .hover}

::::

:::

### Authoring

For simple tables with only a few cells it's straightforward to create them directly in markdown. As tables get larger, it makes sense to use an authoring tool. Some table authoring tools to consider include:

+------------------------------------------------------------------------+---------------------------------------------------------------+
| [TablesGenerator](https://tablesgenerator.com/markdown_tables)         | Online tool for generating markdown tables                    |
+------------------------------------------------------------------------+---------------------------------------------------------------+
| [Emacs TableMode](https://www.emacswiki.org/emacs/TableMode)           | Text based table creation and editing capabilities for Emacs. |
+------------------------------------------------------------------------+---------------------------------------------------------------+
| [Quarto Visual Editor](/docs/visual-editor/content.qmd#editing-tables) | Visual editor for `.qmd` files with table editing support.    |
+------------------------------------------------------------------------+---------------------------------------------------------------+

: {tbl-colwidths="\[35,65\]"}

## Column Widths

Above we describe a means of specifying column widths using the relative number of dashes in each column header (_e.g._, `---|-` to get a 75% / 25% split for a two-column table).

You can also explicitly specify columns widths using the `tbl-colwidths` attribute or document-level option. For an individual markdown table, add the attribute after the caption. For example:

::: {layout-ncol="2"}

:::: {}

``` markdown
| fruit  | price  |
|--------|--------|
| apple  | 2.05   |
| pear   | 1.37   |
| orange | 3.09   |

: Fruit prices {tbl-colwidths="[75,25]"}
```

::::

:::: {}

| fruit  | price  |
|--------|--------|
| apple  | 2.05   |
| pear   | 1.37   |
| orange | 3.09   |

: Fruit prices {tbl-colwidths="[75,25]"}

::::

:::

If your table doesn't have a caption, then you can still specify only `tbl-colwidths`:

::: {layout-ncol="2"}

:::: {}

``` markdown
| fruit  | price  |
|--------|--------|
| apple  | 2.05   |
| pear   | 1.37   |
| orange | 3.09   |

: {tbl-colwidths="[75,25]"}
```

::::

:::: {}

| fruit  | price  |
|--------|--------|
| apple  | 2.05   |
| pear   | 1.37   |
| orange | 3.09   |

: {tbl-colwidths="[75,25]"}

::::

:::

Column widths can also be specified at the document level (_e.g._, to have uniform widths across a set of tables):

``` yaml
---
title: "My Document"
format: html
tbl-colwidths: [75,25]
---
```

## Cross References

For tables produced by executable code cells, include a label with a `tbl-` prefix to make them cross-referenceable.
For example:

```{python}
#| label: tbl-planets
#| tbl-cap: "Astronomical object"
#| echo: fenced

from IPython.display import Markdown
from tabulate import tabulate
table = [["Sun","696,000",1.989e30],
         ["Earth","6,371",5.972e24],
         ["Moon","1,737",7.34e22],
         ["Mars","3,390",6.39e23]]
Markdown(tabulate(
  table, 
  headers=["Astronomical object","R (km)", "mass (kg)"]
))
```

::: callout-important
## Label Prefix

In order for a table to be cross-referenceable, its label must start with the `tbl-` prefix.
:::

{{< include _table-crossrefs.md >}}

## Caption Location

By default, table captions are positioned above tables. You can modify this behavior using the `tbl-cap-location` option. For example:

``` yaml
---
tbl-cap-location: top
---
```

Note that this option is specified at the top level so that it can be shared by both PDF and HTML formats. If you are only targeting a single format you can place it alongside other `format` specific options.

Valid values for the caption location include:

| Value    | Description                           |
|----------|---------------------------------------|
| `top`    | Position the caption above the table. |
| `bottom` | Position the caption below the table. |
| `margin` | Position the caption in the margin.   |

See the article on [Article Layout](article-layout.qmd#margin-captions) for additional details on placing captions in the margin.

## Computations

All of the options described above work for tables produced by executable code cells. For example, here we use the Python [tabulate](https://pypi.org/project/tabulate/) package along with the `Markdown()` function from the IPython [display](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html#) module to print a markdown table:

```{python}
#| label: tbl-planet-measures
#| tbl-cap: "Astronomical object"
#| echo: fenced

from IPython.display import Markdown
from tabulate import tabulate
table = [["Sun","696,000",1.989e30],
         ["Earth","6,371",5.972e24],
         ["Moon","1,737",7.34e22],
         ["Mars","3,390",6.39e23]]
Markdown(tabulate(
  table, 
  headers=["Astronomical object","R (km)", "mass (kg)"]
))
```

Here we apply the `tbl-cap` and `tbl-colwidths` options to a code cell that uses the knitr `kable()` function to write a markdown table:

```{{r}}
#| label: tbl-cars
#| tbl-cap: "Cars"
#| tbl-colwidths: [60,40]

kable(head(cars))
```

If your code cell produces multiple tables, you can also specify subcaptions and layout using cell options:

::: {.panel-tabset group="language"}

## Python

````python
```{{python}}
#| label: tbl-example
#| tbl-cap: "Example"
#| tbl-subcap: 
#|   - "MPG"
#|   - "Taxis"
#| layout-ncol: 2

import seaborn as sns
from IPython.display import Markdown, display
mpg = sns.load_dataset("mpg").head(10)
taxis = sns.load_dataset("taxis").head(10)

display(Markdown(mpg.to_markdown(index = False)))
display(Markdown(taxis.to_markdown(index = False)))
```
````

Note that we use the [`display()`](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html#IPython.display.display) function imported from `IPython` so that we can render multiple outputs from a single cell (by default cells only output their last expression).

## R

````python
```{{r}}
#| label: tbl-example
#| tbl-cap: "Example"
#| tbl-subcap: 
#|   - "Cars"
#|   - "Pressure"
#| layout-ncol: 2

library(knitr)
kable(head(cars))
kable(head(pressure))
```
````


:::

## Grid Tables

Grid tables are a more advanced type of markdown tables that allow arbitrary block elements (multiple paragraphs, code blocks, lists, etc.). For example:

::: {layout-ncol="2"}

:::: {}

``` markdown
+-----------+-----------+--------------------+
| Fruit     | Price     | Advantages         |
+===========+===========+====================+
| Bananas   | $1.34     | - built-in wrapper |
|           |           | - bright color     |
+-----------+-----------+--------------------+
| Oranges   | $2.10     | - cures scurvy     |
|           |           | - tasty            |
+-----------+-----------+--------------------+

: Sample grid table.
```

::::

:::: {}

+-----------+-----------+--------------------+
| Fruit     | Price     | Advantages         |
+===========+===========+====================+
| Bananas   | $1.34     | - built-in wrapper |
|           |           | - bright color     |
+-----------+-----------+--------------------+
| Oranges   | $2.10     | - cures scurvy     |
|           |           | - tasty            |
+-----------+-----------+--------------------+

: Sample grid table.

::::

:::

The row of `=`s separates the header from the table body, and can be omitted for a headerless table. Cells that span multiple columns or rows are not supported.

Alignments can be specified as with pipe tables, by putting colons at the boundaries of the separator line after the header:

::: {layout-ncol="2"}

:::: {}

``` markdown
+---------+--------+------------------+
| Right   | Left   | Centered         |
+========:+:=======+:================:+
| Bananas | $1.34  | built-in wrapper |
+---------+--------+------------------+
```

::::

:::: {}

+---------+--------+------------------+
| Right   | Left   | Centered         |
+========:+:=======+:================:+
| Bananas | $1.34  | built-in wrapper |
+---------+--------+------------------+

::::

:::

For headerless tables, the colons go on the top line instead:

::: {layout-ncol="2"}

:::: {}

``` markdown
+----------:+:----------+:--------:+
| Right     | Left      | Centered |
+-----------+-----------+----------+
```

::::

:::: {}
+----------:+:----------+:--------:+
| Right     | Left      | Centered |
+-----------+-----------+----------+
::::

:::

Note that grid tables are quite awkward to write with a plain text editor (because unlike pipe tables, the column indicators must align). Here are some tools that can assist with creating grid tables:

-   Emacs' [table-mode](https://www.gnu.org/software/emacs/manual/html_node/emacs/Text-Based-Tables.html) (`M-x table-insert`)
-   Quarto [Visual Editor](https://quarto.org/docs/visual-editor/content.html#editing-tables)
-   Tables Generator's [Plain Text mode](https://www.tablesgenerator.com/text_tables) with `Use reStructuredText syntax` enabled

## HTML Tables

Quarto can process HTML tables in `html` `RawBlock` nodes (_i.e._, `{=html}`) and convert them to Markdown tables, regardless of the output format (intentionally including non-HTML formats).
As a result, you can use HTML table syntax in your documents and it will be converted to Markdown syntax for all formats.
Additionally, libraries that emit computational tables in HTML format can work in other output formats.

For example, consider the following raw HTML block:

````markdown
```{=html}
<table>
  <caption>As described in the section above, Quarto tables are great.</caption>
  <thead>
    <tr>
      <th>Header 1</th>
      <th>Header 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
    <td><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/African_Bush_Elephant.jpg/220px-African_Bush_Elephant.jpg" alt="African Bush Elephant" /></td>
      <td>Regular output</td>
    </tr>
  </tbody>
</table>
```
````

When rendered, this results in the following output for HTML and PDF formats:

::: {layout-ncol=2}

:::: {}
### HTML Output

```{=html}
<table>
  <caption>As described in the section above, Quarto tables are great.</caption>
  <thead>
    <tr>
      <th>Header 1</th>
      <th>Header 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
    <td><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/African_Bush_Elephant.jpg/220px-African_Bush_Elephant.jpg" alt="African Bush Elephant" /></td>
      <td>Regular output</td>
    </tr>
  </tbody>
</table>
```
::::

:::: {}
### PDF Output

![](images/raw-table-pdf.png){.border fig-alt="Screenshot of PDF output showing a table with a caption and two columns. The column headers are Header 1 and Header 2, and the cell contents are an image of an elephant and text that reads Regular Output."}
::::

:::

In addition, Quarto supports the specification of embedded Markdown content in tables.
This is done by providing a data attribute `qmd` or `qmd-base64` in an embedded `span` or `div` node.
These nodes can appear anywhere that such content is allowed: table headers, footers, cells, captions, _etc._ 

For example, the following table includes a cross reference, markdown formatting and a shortcode:

:::: {layout-nrow="2"}

::: {}

```` markdown
## HTML Tables Example {#sec-html-tables}

```{=html}
<table>
  <caption><span data-qmd="As described in [Section -@sec-html-tables], Quarto are great."></span></caption>
  <thead>
    <tr>
      <th><span data-qmd="_Header 1_"></span></th>
      <th><span data-qmd="_Header 2_"></span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span data-qmd="{{{< video https://www.youtube.com/embed/wo9vZccmqwc >}}}"></span></td>
      <td>Regular output</td>
    </tr>
  </tbody>
</table>
```
````

:::

::: {}

Which renders as follows:

## HTML Tables Example {#sec-html-tables}

```{=html}
<table>
  <caption><span data-qmd="As described in [Section -@sec-html-tables], Quarto are great."></span></caption>
  <thead>
    <tr>
      <th><span data-qmd="_Header 1_"></span></th>
      <th><span data-qmd="_Header 2_"></span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span data-qmd="{{< video https://www.youtube.com/embed/wo9vZccmqwc >}}"></span></td>
      <td>Regular output</td>
    </tr>
  </tbody>
</table>
```

:::

::::


## Disabling Quarto Table Processing

It's possible that Quarto's processing of HTML tables interferes with your library's processing.
If this is the case, you can disable Quarto's processing of HTML tables by adding the attribute `data-quarto-disable-processing="true"` to your table, for example:

```html
<table data-quarto-disable-processing="true">
  ...
</table>
```


# quarto-web/docs/authoring/_mermaid-theming.qmd

{{< include ../_require-1.3.qmd >}}

The following sections describe the ways in which you can control the color theme of Mermaid diagrams:

- Using the current document theme.
- Using one of Mermaid's own color themes via a YAML option.
- Using SCSS and CSS variables.

### Default Colors for Mermaid Diagrams

If you use Quarto's [bootswatch built-in themes](../output-formats/html-themes.qmd), including the default theme, or a custom theme that uses the same SCSS variables, your Mermaid diagrams will automatically follow your theme.

The following examples demonstrate this with a few of Quarto's built-in bootswatch themes.

::: panel-tabset

## Darkly

![](images/mermaid-darkly.png){fig-alt="A screenshot of a Mermaid flowchart in a document using bootswatch's Darkly theme."}

## Sandstone

![](images/mermaid-sandstone.png){fig-alt="A screenshot of a Mermaid flowchart in a document using bootswatch's Sandstone theme."}

## Vapor

![](images/mermaid-vapor.png){fig-alt="A screenshot of a Mermaid flowchart in a document using bootswatch's Vapor theme."}
:::

You can read more about the correspondence between Bootstrap's SCSS variables and Quarto's Mermaid SCSS variables, and how to change it, below in [Customizing the Mermaid Theme](#customizing-mermaid).

### Using Mermaid's Built-in Themes

If you want to use Mermaid's own themes, you can do so by configuring the `mermaid` option in your YAML front matter:

``` yml
format:
  html:
    mermaid:
      theme: forest
```

The available themes from mermaid are: `default`, `dark`, `forest`, and `neutral`.

::: panel-tabset
## default

![](images/mermaid-default.png){fig-alt="A screenshot of a Mermaid flowchart using the Mermaid's default theme."}

## dark

![](images/mermaid-dark.png){fig-alt="A screenshot of a Mermaid flowchart using the Mermaid's dark theme."}

## forest

![](images/mermaid-forest.png){fig-alt="A screenshot of a Mermaid flowchart using the Mermaid's forest theme."}

## neutral

![](images/mermaid-neutral.png){fig-alt="A screenshot of a Mermaid flowchart using the Mermaid's neutral theme."}

:::

### Customizing the Mermaid Theme {#customizing-mermaid}

Quarto provides its own Mermaid SCSS and CSS variables that can be overwritten to allow some customization of the diagram theme. The SCSS variables, together with their default values, are:

<!-- This comes from quarto-dev/quarto-cli/src/resources/formats/html/_quarto-rules.scss -->

``` scss
$mermaid-bg-color: $body-bg;
$mermaid-edge-color: $secondary;
$mermaid-node-fg-color: $body-color;
$mermaid-fg-color: $body-color;
$mermaid-fg-color--lighter: lighten($body-color, 10%);
$mermaid-fg-color--lightest: lighten($body-color, 20%);
$mermaid-font-family: $font-family-sans-serif;
$mermaid-label-bg-color: $body-bg;
$mermaid-label-fg-color: $primary;
$mermaid-node-bg-color: rgba($primary, 0.1);
$mermaid-node-fg-color: $primary;

```

Their CSS variable counterparts are:

``` css
:root {
  --mermaid-bg-color: #{$mermaid-bg-color};
  --mermaid-edge-color: #{$mermaid-edge-color};
  --mermaid-node-fg-color: #{$mermaid-node-fg-color};
  --mermaid-fg-color: #{$mermaid-fg-color};
  --mermaid-fg-color--lighter: #{$mermaid-fg-color--lighter};
  --mermaid-fg-color--lightest: #{$mermaid-fg-color--lightest};
  --mermaid-font-family: #{$mermaid-font-family};
  --mermaid-label-bg-color: #{$mermaid-label-bg-color};
  --mermaid-label-fg-color: #{$mermaid-label-fg-color};
  --mermaid-node-bg-color: #{$mermaid-node-bg-color};
  --mermaid-node-fg-color: #{$mermaid-node-fg-color};
}
```

For example, to provide a custom color for the background of the nodes you could [add a custom CSS stylesheet](../../output-formats/html-basics.html#css-styles) containing:

```css
:root {
  --mermaid-node-bg-color: #375a7f;
}
```

You can find the correspondence between Quarto's variables and Mermaid's native CSS classes in Quarto's source code in the file  [embed-mermaid.css](https://github.com/quarto-dev/quarto-cli/blob/main/src/resources/formats/html/mermaid/embed-mermaid.css).

# quarto-web/docs/authoring/markdown-basics.qmd

---
title: Markdown Basics
format: html
aliases: 
  - /docs/authoring/
---

## Overview

Quarto is based on Pandoc and uses its variation of markdown as its underlying document syntax. Pandoc markdown is an extended and slightly revised version of John Gruber's [Markdown](https://daringfireball.net/projects/markdown/) syntax.

Markdown is a plain text format that is designed to be easy to write, and, even more importantly, easy to read:

> A Markdown-formatted document should be publishable as-is, as plain text, without looking like it's been marked up with tags or formatting instructions. -- [John Gruber](https://daringfireball.net/projects/markdown/syntax#philosophy)

This document provides examples of the most commonly used markdown syntax. See the full documentation of [Pandoc's Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown) for more in-depth documentation.

## Text Formatting

+-----------------------------------------+-----------------------------------------+
| Markdown Syntax                         | Output                                  |
+=========================================+=========================================+
| ``` markdown                            | *italics*, **bold**, ***bold italics*** |
| *italics*, **bold**, ***bold italics*** |                                         |
| ```                                     |                                         |
+-----------------------------------------+-----------------------------------------+
| ``` markdown                            | superscript^2^ / subscript~2~           |
| superscript^2^ / subscript~2~           |                                         |
| ```                                     |                                         |
+-----------------------------------------+-----------------------------------------+
| ``` markdown                            | ~~strikethrough~~                       |
| ~~strikethrough~~                       |                                         |
| ```                                     |                                         |
+-----------------------------------------+-----------------------------------------+
| ``` markdown                            | `verbatim code`                         |
| `verbatim code`                         |                                         |
| ```                                     |                                         |
+-----------------------------------------+-----------------------------------------+

## Headings {#headings}

+-----------------+-----------------------------------+
| Markdown Syntax | Output                            |
+=================+===================================+
| ``` markdown    | # Header 1 {.heading-output}      |
| # Header 1      |                                   |
| ```             |                                   |
+-----------------+-----------------------------------+
| ``` markdown    | ## Header 2 {.heading-output}     |
| ## Header 2     |                                   |
| ```             |                                   |
+-----------------+-----------------------------------+
| ``` markdown    | ### Header 3 {.heading-output}    |
| ### Header 3    |                                   |
| ```             |                                   |
+-----------------+-----------------------------------+
| ``` markdown    | #### Header 4 {.heading-output}   |
| #### Header 4   |                                   |
| ```             |                                   |
+-----------------+-----------------------------------+
| ``` markdown    | ##### Header 5 {.heading-output}  |
| ##### Header 5  |                                   |
| ```             |                                   |
+-----------------+-----------------------------------+
| ``` markdown    | ###### Header 6 {.heading-output} |
| ###### Header 6 |                                   |
| ```             |                                   |
+-----------------+-----------------------------------+

```{=html}
<style type="text/css">
.heading-output {
  border-bottom: none;
  margin-top: 0;
  margin-bottom: 0;
}
</style>
```
## Links & Images

+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Markdown Syntax                                              | Output                                                                                                 |
+==============================================================+========================================================================================================+
| ``` markdown                                                 | <https://quarto.org>                                                                                   |
| <https://quarto.org>                                         |                                                                                                        |
| ```                                                          |                                                                                                        |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``` markdown                                                 | [Quarto](https://quarto.org)                                                                           |
| [Quarto](https://quarto.org)                                 |                                                                                                        |
| ```                                                          |                                                                                                        |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``` markdown                                                 | ![Caption](elephant.png){fig-alt="A line drawing of an elephant."}                                     |
| ![Caption](elephant.png)                                     |                                                                                                        |
| ```                                                          |                                                                                                        |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``` markdown                                                 | [![Caption](elephant.png)](https://quarto.org)                                                         |
| [![Caption](elephant.png)](https://quarto.org)               |                                                                                                        |
| ```                                                          |                                                                                                        |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``` markdown                                                 | [![Caption](elephant.png "An elephant"){fig-alt="A line drawing of an elephant."}](https://quarto.org) |
| [![Caption](elephant.png)](https://quarto.org "An elephant") |                                                                                                        |
| ```                                                          |                                                                                                        |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``` markdown                                                 | [![](elephant.png){fig-alt="A line drawing of an elephant."}](https://quarto.org)                      |
| [![](elephant.png){fig-alt="Alt text"}](https://quarto.org)  |                                                                                                        |
| ```                                                          |                                                                                                        |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

## Lists

+-----------------------------------+---------------------------------+
| Markdown Syntax                   | Output                          |
+===================================+=================================+
| ``` markdown                      |                                 |
| * unordered list                  | * unordered list                |
|     + sub-item 1                  |     + sub-item 1                |
|     + sub-item 2                  |     + sub-item 2                |
|         - sub-sub-item 1          |         - sub-sub-item 1        |
| ```                               |                                 |
+-----------------------------------+---------------------------------+
| ``` markdown                      |                                 |
| *   item 2                        | -   item 2                      |
|                                   |                                 |
|     Continued (indent 4 spaces)   |     Continued (indent 4 spaces) |
| ```                               |                                 |
+-----------------------------------+---------------------------------+
| ``` markdown                      |                                 |
| 1. ordered list                   |  1. ordered list                |
| 2. item 2                         |  2. item 2                      |
|     i) sub-item 1                 |      i) sub-item 1              |
|          A.  sub-sub-item 1       |           A.  sub-sub-item 1    |
| ```                               |                                 |
|                                   |                                 |
+-----------------------------------+---------------------------------+
| ``` markdown                      |                                 |
| (@)  A list whose numbering       |  (1) A list whose numbering     |
|                                   |                                 |
| continues after                   |  continues after                |
|                                   |                                 |
| (@)  an interruption              |  (2) an interruption            |
| ```                               |                                 |
+-----------------------------------+---------------------------------+
| ``` markdown                      |                                 |
| ::: {}                            | ::: {}                          |
| 1. A list                         | 1. A list                       |
| :::                               | :::                             |
|                                   |                                 |
| ::: {}                            | ::: {}                          |
| 1. Followed by another list       | 1. Followed by another list     |
| :::                               | :::                             |
| ```                               |                                 |
+-----------------------------------+---------------------------------+
| ``` markdown                      |                                 |
| term                              | term                            |
| : definition                      | : definition                    |
| ```                               |                                 |
+-----------------------------------+---------------------------------+

Note that unlike other Markdown renderers (notably Jupyter and GitHub), lists in Quarto require an entire blank line above the list. Otherwise the list will not be rendered in list form, rather it will all appear as normal text along a single line.

## Tables

#### Markdown Syntax

``` markdown
| Right | Left | Default | Center |
|------:|:-----|---------|:------:|
|   12  |  12  |    12   |    12  |
|  123  |  123 |   123   |   123  |
|    1  |    1 |     1   |     1  |
```

#### Output

| Right | Left | Default | Center |
|------:|:-----|---------|:------:|
|    12 | 12   | 12      |   12   |
|   123 | 123  | 123     |  123   |
|     1 | 1    | 1       |   1    |

Learn more in the article on [Tables](tables.qmd).

## Source Code

Use ```` ``` ```` to delimit blocks of source code:

```` markdown
```
code
```
````

Add a language to syntax highlight code blocks:

```` markdown
```python
1 + 1
```
````

Pandoc supports syntax highlighting for over [140 different languages](https://github.com/jgm/skylighting/tree/master/skylighting-core/xml). If your language is not supported then you can use the `default` language to get a similar visual treatment:

```` markdown
```default
code
```
````

If you are creating HTML output there is a wide variety of options available for code block output. See the article on [HTML Code](../output-formats/html-code.qmd) for additional details.

## Equations

Use `$` delimiters for inline math and `$$` delimiters for display math. For example:

+---------------------------+-------------------------+
| Markdown Syntax           | Output                  |
+===========================+=========================+
| ``` markdown              |                         |
| inline math: $E = mc^{2}$ | inline math: $E=mc^{2}$ |
| ```                       |                         |
+---------------------------+-------------------------+
| ``` markdown              |                         |
| display math:             | display math:           |
|                           |                         |
| $$E = mc^{2}$$            | $$E = mc^{2}$$          |
| ```                       |                         |
+---------------------------+-------------------------+

If you want to define custom TeX macros, include them within `$$` delimiters enclosed in a `.hidden` block. For example:

``` tex
::: {.hidden}
$$
 \def\RR{{\bf R}}
 \def\bold#1{{\bf #1}}
$$
:::
```

For HTML math processed using [MathJax](https://docs.mathjax.org/) (the default) you can use the `\def`, `\newcommand`, `\renewcommand`, `\newenvironment`, `\renewenvironment`, and `\let` commands to create your own macros and environments.  

## Diagrams

Quarto has native support for embedding [Mermaid](https://mermaid-js.github.io/mermaid/#/) and [Graphviz](https://graphviz.org/) diagrams. This enables you to create flowcharts, sequence diagrams, state diagrams, Gantt charts, and more using a plain text syntax inspired by markdown.

For example, here we embed a flowchart created using Mermaid:

```{mermaid}
%%| echo: fenced
flowchart LR
  A[Hard edge] --> B(Round edge)
  B --> C{Decision}
  C --> D[Result one]
  C --> E[Result two]
```

Learn more in the article on [Diagrams](diagrams.qmd).

## Videos

You can include videos in documents using the `{{{< video >}}}` shortcode. For example, here we embed a YouTube video:

``` {.markdown shortcodes="false"}
{{< video https://www.youtube.com/embed/wo9vZccmqwc >}}
```

Videos can refer to video files (e.g. MPEG) or can be links to videos published on YouTube, Vimeo, or Brightcove. Learn more in the article on [Videos](videos.qmd).

{{< include _pagebreak.qmd >}}

## Divs and Spans

You can add classes, attributes, and other identifiers to regions of content using Divs and Spans (you'll see an example of this below in [Callout Blocks]).

For example, here we add the "border" class to a region of content using a div (`:::`):

``` markdown
::: {.border}
This content can be styled with a border
:::
```

Once rendered to HTML, Quarto will translate the markdown into:

``` html
<div class="border">
  <p>This content can be styled with a border</p>
</div>
```

Divs start with a fence containing at least three consecutive colons plus some attributes. The attributes may optionally be followed by another string of consecutive colons. The Div ends with another line containing a string of at least three consecutive colons. The Div should be separated by blank lines from preceding and following blocks. Divs may also be nested. For example

``` markdown
::::: {#special .sidebar}

::: {.warning}
Here is a warning.
:::

More content.
:::::
```

Once rendered to HTML, Quarto will translate the markdown into:

``` html
<div id="special" class="sidebar">
  <div class="warning">
    <p>Here is a warning.</p>
  </div>
  <p>More content.</p>
</div>
```

Fences without attributes are always closing fences. Unlike with fenced code blocks, the number of colons in the closing fence need not match the number in the opening fence. However, it can be helpful for visual clarity to use fences of different lengths to distinguish nested divs from their parents.

A bracketed sequence of inlines, as one would use to begin a link, will be treated as a `Span` with attributes if it is followed immediately by attributes:

``` markdown
[This is *some text*]{.class key="val"}
```

Once rendered to HTML, Quarto will translate the markdown into:

``` html
<span class="class" data-key="val">
  This is <em>some text</em>
</span>
```

Typically, you'll use CSS and/or a [Filter](/docs/extensions/filters.qmd) along with Divs and Spans to provide styling or other behavior within rendered documents.

### Ordering of Attributes

Both divs and spans in Pandoc can have any combination of identifiers, classes, and (potentially many) key-value attributes. In order for these to be recognized by Pandoc, they have to be provided in a specific order: identifiers, classes, and then key-value attributes. Any of these can be omitted, but must follow that order if they are provided. For example, the following is valid:

``` markdown
[This is good]{#id .class key1="val1" key2="val2"}
```

However, the following *will not be recognized by Pandoc*:

``` markdown
[This does *not* work!]{.class key="val" #id}
```

This ordering restriction applies to both divs and spans. See Pandoc's documentation on [Divs and Spans](https://pandoc.org/MANUAL.html#divs-and-spans) for additional details.

## Callout Blocks

#### Markdown Syntax

``` markdown
:::{.callout-note}
Note that there are five types of callouts, including: 
`note`, `tip`, `warning`, `caution`, and `important`.
:::
```

#### Output

::: callout-note
Note that there are five types of callouts, including `note`, `tip`, `warning`, `caution`, and `important`.
:::

Learn more in the article on [Callout Blocks](callouts.qmd).

## Other Blocks

+--------------------------+--------------------------+
| Markdown Syntax          | Output                   |
+==========================+==========================+
| ``` markdown             | > Blockquote             |
| > Blockquote             |                          |
| ```                      |                          |
+--------------------------+--------------------------+
| ``` markdown             | ::: classname            |
| ::: {.classname}         | Div                      |
| Div                      | :::                      |
| :::                      |                          |
| ```                      |                          |
+--------------------------+--------------------------+
| ``` markdown             | | Line Block             |
| | Line Block             | |    Spaces and newlines |
| |   Spaces and newlines  | |    are preserved       |
| |   are preserved        |                          |
| ```                      |                          |
+--------------------------+--------------------------+

## Special Characters

+-----------------+---------------+
| Markdown Syntax | Output        |
+=================+===============+
| ``` markdown    | endash: --    |
| endash: --      |               |
| ```             |               |
+-----------------+---------------+
| ``` markdown    | emdash: ---   |
| emdash: ---     |               |
| ```             |               |
+-----------------+---------------+

## Keyboard Shortcuts {#keyboard-shortcuts}

{{< include _kbd.qmd >}}


# quarto-web/docs/authoring/front-matter.qmd

---
title: Front Matter
---

## Overview

Scholarly articles require much more detail in their front matter than simply a title and an author. Quarto provides a rich set of YAML metadata keys to describe these details. On this page, you'll learn how to specify authors and their affiliations, article summaries like an abstract and keywords, and how to include information on copyright, licensing and funding.

This YAML header includes examples of all the top level keys discussed on this page:

``` {.yaml filename="document.qmd"}
---
title: "Toward a Unified Theory of High-Energy Metaphysics: Silly String Theory"
date: 2008-02-29
author:
  - name: Josiah Carberry
    id: jc
    orcid: 0000-0002-1825-0097
    email: josiah@psychoceramics.org
    affiliation: 
      - name: Brown University
        city: Providence
        state: RI
        url: www.brown.edu
abstract: > 
  The characteristic theme of the works of Stone is 
  the bridge between culture and society. ...
keywords:
  - Metaphysics
  - String Theory
license: "CC BY"
copyright: 
  holder: Josiah Carberry
  year: 2008
citation: 
  container-title: Journal of Psychoceramics
  volume: 1
  issue: 1
  doi: 10.5555/12345678
funding: "The author received no specific funding for this work."
---
```

The documents produced by the above metadata for the HTML and JATS formats are shown below.

::: panel-tabset
## JATS

![](images/scholarly-front-matter-jats.png){fig-alt="Screenshot of the JATS preview from the document with the above metadata."}

## HTML

![](images/scholarly-front-matter-html.png){fig-alt="Screenshot of the HTML preview from the document with the above metadata."}
:::

Not all of the metadata keys are used in every format. For example, the HTML format does not display the `keywords`. However, the tags described on this page will generally be supported in [journal article formats](/docs/extensions/listing-journals.html). Currently the JATS format makes use of the broadest set of metadata tags, so if you want to check how things render we recommend previewing with `format: jats`.

## Authors & Affiliations {#authors-and-affiliations}

The simplest way to describe an author is with a string directly to the `author` key:

``` yaml
---
author: Norah Jones
---
```

However, the `author` key has a number of sub-keys that provide the additional detail required for scholarly articles. For instance, you can add an author's affiliation by using the `affiliation` key. In the simplest form, an author along with their affiliation can be described by passing a string to each of `name` and `affiliation`:

``` yaml
---
author:
  name: Norah Jones
  affiliation: Carnegie Mellon University
---
```

You can read about the other keys you can provide to `author` and `affiliation` in the corresponding [Author](#author) and [Affiliation](#affiliation) sections below.

Both `author` and `affiliation` can take multiple elements to describe multiple authors, or authors with multiple affiliations. As an example, here is the YAML to describe a document with two authors, the first of which has two affiliations:

``` yaml
---
author:
  - name: Norah Jones
    affiliation: 
      - Carnegie Mellon University
      - University of Chicago
  - name: Josiah Carberry
    affiliation: Brown University
---
```

Notice that each element of `author` and `affiliation` is prefaced by a `-` and indented appropriately. You can read more about shortcuts to avoid repetition when authors share affiliations in the [Multiple Authors](#multiple-authors) section below.

::: callout-note
## Singular or Plural?

Both of these keys can be specified using a singular (`author` and `affiliation`) or plural (`authors` and `affiliations`) form.
:::

### Author {#author}

Beyond `name` and `affiliation`, `author` can also take any of the following:

+----------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `email`\             | string         | Contact details for the author. Converted to hyperlinks in many formats.                                                                                            |
| `phone`\             |                |                                                                                                                                                                     |
| `fax`\               |                |                                                                                                                                                                     |
| `url`                |                |                                                                                                                                                                     |
+----------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `orcid`              | string         | Author's Open Researcher and Contributor ID ([ORCID](https://orcid.org/)), in the form `0000-0000-0000-0000`. Creates a link to the author's ORCID in many formats. |
+----------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `note`\              | string         | Notes to attach to an author, such as contribution details;\                                                                                                        |
| `acknowledgements`   |                | Author's acknowledgements.                                                                                                                                          |
+----------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `roles`              | string(s)      | Author's roles. Read more in [Author Roles](#roles) below.                                                                                                          |
+----------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `corresponding`\     | `true`/`false` | Set this author as:\                                                                                                                                                |
| `equal-contributor`\ |                | the corresponding author;\                                                                                                                                          |
| `deceased`           |                | as having contributed equally with all other contributors;\                                                                                                         |
|                      |                | and/or deceased.                                                                                                                                                    |
+----------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `id`                 | string         | An identifier to be used to refer to this author in other fields. See an example in [Funding].                                                                      |
+----------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Available keys to `author`

An `affiliations-url` key can also be provided to `author`, and will be propagated to the `url` key of `affiliation`.

As an example, a more complete description of an author might look like:

``` yaml
---
author:
  - name: Josiah Carberry
    orcid: 0000-0002-1825-0097
    url: https://en.wikipedia.org/wiki/Josiah_S._Carberry
    email: josiah@psychoceramics.org
    corresponding: true
---
```

#### Name Components

Quarto will automatically parse the `name` key into its components. 
However, if this parsing is incorrect you can specify the components, `given`, `family`, `dropping-particle`, and `non-dropping-particle` directly, for example:

``` yaml
---
author: 
  - name: 
      given: Charles
      family: Gaulle
      non-dropping-particle: de
  - name: 
      given: Ludwig
      family: Beethoven
      dropping-particle: van
---
```

#### Author Roles {#roles}

Use `roles` to describe an author's contributions to the work. You can use free form text as a string:

``` yaml
author:
  - name: Josiah Carberry
    roles: "Conceived and designed the study, analysed the results and wrote the manuscript."
```

Or alternatively, make use of the [Contributor Roles Taxonomy (CRediT)](https://credit.niso.org). 
To use CRediT roles provide one of the [14 contributor](#credit-roles) roles, e.g.:

``` yaml
author:
  - name: Josiah Carberry
    roles: conceptualization
```

Or, an array of roles:

``` yaml
author:
  - name: Josiah Carberry
    roles: [investigation, data curation]
```

Or specify the role along with a degree of contribution:
```yaml
author:
  - name: Josiah Carberry
    roles: 
      - investigation: lead 
      - data curation: supporting
```

::: {.callout-tip collapse="true" #credit-roles}

## Expand to see the 14 Contributor Roles

| Value                                                                                        | Alias |
|----------------------------------------------------|----------|
| [conceptualization](https://credit.niso.org/contributor-roles/conceptualization/)               |          |
| [data curation](https://credit.niso.org/contributor-roles/data-curation/)                       |          |
| [formal analysis](https://credit.niso.org/contributor-roles/formal-analysis/)                   | analysis |
| [funding acquisition](https://credit.niso.org/contributor-roles/funding-acquisition/)           | funding  |
| [investigation](https://credit.niso.org/contributor-roles/investigation/)                       |          |
| [methodology](https://credit.niso.org/contributor-roles/methodology/)                           |          |
| [project administration](https://credit.niso.org/contributor-roles/project-administration/)     |          |
| [resources](https://credit.niso.org/contributor-roles/resources/)                               |          |
| [software](https://credit.niso.org/contributor-roles/software/)                                 |          |
| [supervision](https://credit.niso.org/contributor-roles/supervision/)                           |          |
| [validation](https://credit.niso.org/contributor-roles/validation/)                             |          |
| [visualization](https://credit.niso.org/contributor-roles/visualization/)                       |          |
| [writing – review & editing](https://credit.niso.org/contributor-roles/writing-review-editing/) | editing  |
| [writing – original draft](https://credit.niso.org/contributor-roles/writing-original-draft/)   | writing  |

: CRediT contributor values available in `roles` 



:::


### Affiliation {#affiliation}

Like `author`, you can provide a string is directly to `affiliation`, as in:

``` yaml
---
author:
  name: Norah Jones
  affiliation: Carnegie Mellon University
---
```

Alternatively, you can provide the name explicitly to the `name` key, like:

``` yaml
---
author:
  name: Norah Jones
  affiliation: 
    name: Carnegie Mellon University
---
```

In addition to `name`, `affiliation` can take any of the following:

+-------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `department`            | String    |                                                                                                    |
+-------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `address`\              | String    | Affiliation's location. Provide one of `region` or `state`, and any combination of the other keys. |
| `city`\                 |           |                                                                                                    |
| `region` or `state`\    |           |                                                                                                    |
| `country`\              |           |                                                                                                    |
| `postal-code`           |           |                                                                                                    |
+-------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `url`                   | String    | Affiliation's website. Converted to a link in many formats.                                        |
+-------------------------+-----------+----------------------------------------------------------------------------------------------------+
|  \                      | \         | Affiliation IDs:\                                                                                  | 
| `isni`\                 | Numeric\  | 16 digit [International Standard Name Identifier (ISNI)](https://isni.org/); \                     |
| `ringgold`\             | Numeric\  | 4-6 digit [Ringgold ID](https://www.ringgold.com/ringgold-identifier/);\                           |
| `ror`                   | String    | [Research Organization Registry (ROR) ID](https://ror.org/), starting with `https://ror.org/`,     |
|                         |           | followed by a 9 digit alphanumeric identifier.                                                     |
+-------------------------+-----------+----------------------------------------------------------------------------------------------------+

: Available keys to `affiliation`

For example, a more complete `affiliation` for an author might look like:

``` yaml
---
author:
  name: Josiah Carberry
  orcid: 0000-0002-1825-0097
  url: https://en.wikipedia.org/wiki/Josiah_S._Carberry
  email: josiah@psychoceramics.org
  corresponding: true
  affiliation: 
    - name: Brown University
      department: Psychoceramics
      city: Providence
      state: RI
      country: US
      url: www.brown.edu
      ringgold: 6752
      isni: 0000000419369094
---
```

### Multiple Authors {#multiple-authors}

When there are multiple authors of a document, it is common that they share affiliations. To avoid repeating an affiliation's details, you can describe an affiliation once, assign it an id, and then refer to the id in other fields.

One approach is to assign an `id` to each affiliation where they are described within an author. For example, here we assign the author's affiliations the ids `cmu` and `chicago`:

``` yaml
---
author:
  - name: Norah Jones
    affiliation:
      - id: cmu
        name: Carnegie Mellon University
      - id: chicago
        name: University of Chicago
---
```

Then, when adding additional authors, you can refer to affiliations using `ref:`:

``` yaml
---
author:
  - name: Norah Jones
    affiliation:
      - id: cmu
        name: Carnegie Mellon University
      - id: chicago
        name: University of Chicago
  - name: John Hamm
    affiliation:
      - ref: cmu
---
```

An alternative approach is to define affiliations at the top level, as opposed to within an `author`:

``` yaml
---
author:
  - name: Norah Jones
    affiliation:
      - ref: cmu
      - ref: chicago
  - name: John Hamm
    affiliation:
      - ref: cmu
affiliations:
  - id: cmu
    name: Carnegie Mellon University
  - id: chicago
    name: University of Chicago
---
```

This approach may be more convenient in cases where you also want to refer to affiliations in fields other than `author`, e.g. `funding`.

## Abstract

You can add an abstract with the `abstract` key. Since abstracts are generally longer than a line, and may contain markdown, you'll need to provide it using YAML's literal block style. That is, place a `|` on the same line as `abstract:` and indent your raw abstract text by two spaces.

For example:

``` yaml
---
abstract: |
  This article evaluates novel approaches to do
  some really important things.
---
```

## Keywords

Keywords can be added with `keywords`:

``` yaml
---
keywords: 
  - open-source 
  - scientific publishing
  - reproducible research
---
```

## Copyright

You can specify copyright in two ways. Either directly as a string to `copyright`:

``` yaml
---
copyright: "Copyright Acme, Inc. 2021. All Rights Reserved"
---
```

Which is equivalent to providing the same string to the `statement` sub-key:

``` yaml
---
copyright: 
  statement: "Copyright Acme, Inc. 2021. All Rights Reserved"
---
```

Or, alternatively, by specifying a `holder` and `year`:

``` yaml
---
copyright: 
  holder: Acme, Inc
  year: 2021
---
```

When specifying `year` you can also use a range (`year: 2021 - 2023`) or an array (`year: [2021, 2022, 2023]`).

## License

To specify a license, you can pass a string directly to `license`:

``` yaml
---
license: "This work is dedicated to the Public Domain"
---
```

This is equivalent to specifying the `text` sub-key directly:

``` yaml
---
license:
  text: "This work is dedicated to the Public Domain"
---
```

You can add additional details by providing the `type` and `url` sub-keys:

``` yaml
---
license:
  text: > 
    Permission is granted to copy, distribute and/or 
    modify this document under the terms of the GNU Free 
    Documentation License, Version 1.3 or any later version 
    published by the Free Software Foundation; with no 
    Invariant Sections, no Front-Cover Texts, and no 
    Back-Cover Texts. A copy of the license is included in 
    the section entitled "GNU Free Documentation License
  type: open-access
  url: https://www.gnu.org/licenses/fdl-1.3-standalone.html
---
```

If you are choosing a Creative Commons license you may simply pass an abbreviation:

``` yaml
---
license: "CC BY"
---
```

The available abbreviations are covered in the [Creative Commons](cc) section below.

### Creative Commons {#cc}

The Creative Commons copyright licenses and tools forge a balance inside the traditional "all rights reserved" setting that copyright law creates. These tools give everyone from individual creators to large companies and institutions a simple, standardized way to grant copyright permissions to their creative work.

Here are some of the common forms of Creative Commons content license:

+---------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| License       | Name                                    | Description                                                                                                                                                                                                                                                                                                                                                                           |
+===============+=========================================+=======================================================================================================================================================================================================================================================================================================================================================================================+
| `CC BY`       | Attribution                             | This license lets others distribute, remix, tweak, and build upon your work, even commercially, as long as they credit you for the original creation. This is the most accommodating of licenses offered.                                                                                                                                                                             |
+---------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `CC BY-SA`    | Attribution-ShareAlike                  | This license lets others remix, tweak, and build upon your work even for commercial purposes, as long as they credit you and license their new creations under the identical terms. This license is often compared to "copyleft" free and open source software licenses. All new works based on yours will carry the same license, so any derivatives will also allow commercial use. |
+---------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `CC BY-ND`    | Attribution-NoDerivs                    | This license allows for redistribution, commercial and non-commercial, as long as it is passed along unchanged and in whole, with credit to you.                                                                                                                                                                                                                                      |
+---------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `CC BY-NC`    | Attribution-NonCommercial               | This license lets others remix, tweak, and build upon your work non-commercially, and although their new works must also acknowledge you and be non-commercial, they don't have to license their derivative works on the same terms.                                                                                                                                                  |
+---------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `CC BY-NC-SA` | Attribution-NonCommercial-ShareAlike    | This license lets others remix, adapt, and build upon your work non-commercially, as long as they credit you and license their new creations under the identical terms.                                                                                                                                                                                                             |
+---------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `CC BY-NC-ND` | Attribution-NonCommercial-NoDerivs      | This license is the most restrictive of the six main licenses, only allowing others to download your works and share them with others as long as they credit you, but they can't change them in any way or use them commercially.                                                                                                                                                     |
+---------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

If you specify a Creative Commons license for your content, Quarto will automatically include the relevant link to the appropriate license.

## Citation

The `citation` key allows you to specify additional metadata that is used to create a citation for the document. You can read more about this in [Creating Citeable Articles](/docs/authoring/create-citeable-articles.qmd).

## Funding

The `funding` key can directly take a string:

``` yaml
---
funding: "The author(s) received no specific funding for this work."
---
```

This is equivalent to providing the `statement` sub-key directly:

``` yaml
---
funding: 
  statement: "The author(s) received no specific funding for this work."
---
```

The `funding` key can also take the sub-keys `source`, `recipient` and `investigator`. Both `recipient` and `investigator` can take a string, or a reference to an author or affiliation using `ref:`. For example, this front matter adds funding where the investigator is specified using an author id:

``` yaml
---
author:
  - name: Norah Jones
    id: nj
funding:
  - source: "NIH (Grant #: 1-R01-MH99999-01A1)"
    investigator: 
      - ref: nj
---
```


# quarto-web/docs/authoring/videos.qmd

---
title: "Videos"
---

## Overview

You can embed videos in documents using the `{{{< video >}}}` shortcode. For example, here we embed a YouTube video:

``` {.markdown shortcodes="false"}
{{< video https://www.youtube.com/embed/wo9vZccmqwc >}}
```

Videos can refer to video files (e.g. `.mp4`) or can be links to videos published on YouTube, Vimeo, or Brightcove.

Here are some additional examples that demonstrate using various video sources and options:

``` {.default shortcodes="false"}
{{< video local-video.mp4 >}}

{{< video https://www.youtube.com/embed/wo9vZccmqwc >}}

{{< video https://vimeo.com/548291297 >}}

{{< video https://youtu.be/wo9vZccmqwc width="400" height="300" >}}

{{< video https://www.youtube.com/embed/wo9vZccmqwc
    title="What is the CERN?"
    start="116"
    aspect-ratio="21x9" 
>}}
```

In HTML formats the video will be embedded within the document. For other formats, a simple link to the video will be rendered.

Next, we'll cover the various options available for video embedding. For additional details on using videos within Revealjs presentations (including how to create slides with full-screen video backgrounds), see the [Revealjs](#revealjs) section below.

## Video URL

The video URL can specify either a path to a video file (e.g. a `.mp4`) alongside the document, a remote URL to a video file, or a URL to a video service (YouTube, Vimeo, or Brightcove).

These are valid URLs for video files:

``` {.default shortcodes="false"}
{{< video local-video.mp4 >}}
{{< video https://videos.example.com/video.mp4 >}}
```

For video services, a variety of URL forms are supported. For example, the following video service URLs are all valid:

``` {.default .code-overflow-scroll shortcodes="false"}
{{< video https://youtu.be/wo9vZccmqwc >}}
{{< video https://www.youtube.com/watch?v=wo9vZccmqwc >}}
{{< video https://www.youtube.com/embed/wo9vZccmqwc >}}
{{< video https://vimeo.com/548291297 >}}
{{< video https://players.brightcove.net/1460825906/default_default/index.html?videoId=5988531335001 >}}
```

Note that YouTube videos support both the URL that is available in the address bar when watching a video as well as the standard URLs used for linking and embedding. Brightcove videos are embedded using the standard [iframe embed code](https://studio.support.brightcove.com/publish/choosing-correct-embed-code.html).

## Options

### Aspect Ratio

Videos are automatically rendered responsively using the full width of the document's main text column. The `aspect-ratio` specifies how the height should vary with changes in width. For example:

``` {.default shortcodes="false"}
{{< video https://youtu.be/wo9vZccmqwc aspect-ratio="4x3" >}}
```

Available [aspect ratios](https://getbootstrap.com/docs/5.0/helpers/ratio/#aspect-ratios) include `1x1`, `4x3`, `16x9` (the default), and `21x9`.

#### Width and Height

You can disable responsive sizing by providing explicit `width` and `height` attributes. For example:

``` {.default shortcodes="false"}
{{< video https://youtu.be/wo9vZccmqwc width="250" height="175" >}}
```

This will produce a video that renders at the specified dimensions and is not responsive. Note that when no `height` or `width` are specified, videos will size responsively given the space available to them.

### Start Time

For YouTube videos, you can specify a `start` option to indicate how many seconds into the video you want to start playing:

``` {.default shortcodes="false"}
{{< video https://youtu.be/wo9vZccmqwc start="10" >}}
```

### Frame Title

The `title` option adds a `title` attribute to the video `<iframe>`:

``` {.default shortcodes="false"}
{{< video https://www.youtube.com/embed/wo9vZccmqwc 
    title='What is the CERN?' 
>}}
```

## Revealjs {#revealjs}

You can include videos within [Revealjs](/docs/presentations/revealjs/index.qmd) presentations in one of two ways:

-   A video that appears within the contents of a slide.

-   A video that occupies the entire background of a slide.

### Slide Content

Here's a video on a slide without a title:

``` {.default shortcodes="false"}
---

{{< video https://youtu.be/wo9vZccmqwc width="100%" height="100%" >}}
```

Note that we set the `width` and `height` explicitly to 100% so that the video fills the slide.

Here's a video on a slide with a title.

``` {.default shortcodes="false"}
## Video Slide 

{{< video https://youtu.be/wo9vZccmqwc width="100%" height="85%" >}}
```

Note that we set the `height` to 85% to leave room for the title.

### Backgrounds

For videos on slides without titles, you might prefer to have the video fill the entire background of the slide. You can do this using the `background-video` attribute. For example:

``` markdown
## {background-video="intro-cern.mp4"}

## {background-video="https://videos.example.com/intro-cern.mp4"}

## {background-video="https://youtu.be/wo9vZccmqwc?autoplay=1"}

## {background-video="https://vimeo.com/548291297"}
```

Note that when using `background-video` for video files (as distinct from services like YouTube) you can specify a number of other attributes, including:

{{< include ../presentations/revealjs/_background-video.md >}}


# quarto-web/docs/authoring/code-annotation.qmd

---
title: Code Annotation
code-annotations: below
aliases:
  - /docs/prerelease/1.3/code-annotation.html
---

{{< include ../_require-1.3.qmd >}}

## Overview

Code blocks and executable code cells in Quarto can include line-based annotations. Line-based annotations provide a way to attach explanation to lines of code much like footnotes. 

For example, this code uses annotation to describe the steps in an R dplyr pipeline in plain language:

```r
library(tidyverse)
library(palmerpenguins)
penguins |>                                            # <1>
  mutate(                                              # <2>
    bill_ratio = bill_depth_mm / bill_length_mm,       # <2>
    bill_area  = bill_depth_mm * bill_length_mm        # <2>
  )                                                    # <2>
```
1. Take `penguins`, and then,
2. add new columns for the bill ratio and bill area.

The default HTML annotation style displays annotations in a list below the code block. Clicking on the annotation number in the list highlights the relevant lines in the code. Other [HTML styles](#html-styles) hide the annotations, revealing them in a tooltip when a user hovers or selects a marker, as illustrated in this example of a Revealjs presentation:

```{.yaml code-preview="code-annotation-example/revealjs.qmd"}
format: revealjs
```

The PDF format also allows for annotations, numbering, and displaying the annotation text below the code. In other formats, like Word and GitHub Markdown, annotations are instead labeled with the line of code (or lines of code) to which the annotation text applies.

::: panel-tabset
#### PDF

![](images/annote-pdf.png){fig-alt="Screenshot of output in PDF format showing code annotation."}

#### GitHub Flavored Markdown

````markdown
``` r
library(tidyverse)
library(palmerpenguins)
penguins |>
  mutate(
    bill_ratio = bill_depth_mm / bill_length_mm,
    bill_area  = bill_depth_mm * bill_length_mm
  )
```

Line 3  
Take `penguins`, and then,

Lines 4-7  
add new columns for the bill ratio and bill area.
````
:::


To add code annotation to a code block, you need to add two things: specially formatted code comments in your code cell, and an ordered list below the code cell with the annotation text. Read more in [Annotation Syntax](#annotation-syntax).

The `code-annotations` option controls how annotations appear in the HTML format (`below` (default), `hover` or `select`), and in all formats, whether annotation is disabled (`false`), or if annotations should be removed from the output (`none`).

## Annotation Syntax {#annotation-syntax}

Annotations for a code cell consist of two related elements:

1.  Each annotated line should be terminated with a comment (using the code cell's language comment character) followed by a space and then an annotation number enclosed in angle brackets (e.g. `# <2>`). You may repeat an annotation number if the annotation spans multiple lines.

2.  An ordered list that appears immediately after the code cell which includes the contents of each annotation. Each numbered item in the ordered list will correspond to the line(s) of code with the same annotation number.

For example, the annotations in the overview were produced with the following:

```` markdown
```r
library(tidyverse)
library(palmerpenguins)
penguins |>                                      # <1>
  mutate(                                        # <2>
    bill_ratio = bill_depth_mm / bill_length_mm, # <2>
    bill_area  = bill_depth_mm * bill_length_mm  # <2>
  )                                              # <2>
```
1. Take `penguins`, and then,
2. add new columns for the bill ratio and bill area.
````

## Annotation Style {#html-styles}

For HTML output, there are three annotation styles you can set with the `code-annotations` document option:

`below`

:   By default (or if `code-annotations: below` is specified), code annotation text will appear below the code cell.

`hover`

:   Code annotation text will be displayed when the user hovers over the annotation marker for a line of code. 

`select`

:   Code annotation text will be displayed when the user clicks on an annotation marker (selecting it). The annotation text can be dismissed by clicking the annotation marker once again.

For example, to set the display style to hover, the complete Quarto file would be:

```` markdown
---
code-annotations: hover
---

```r
library(tidyverse)
library(palmerpenguins)
penguins |>                                      # <1>
  mutate(                                        # <2>
    bill_ratio = bill_depth_mm / bill_length_mm, # <2>
    bill_area  = bill_depth_mm * bill_length_mm  # <2>
  )                                              # <2>
```
1. Take `penguins`, and then,
2. add new columns for the bill ratio and bill area.
````



## Removing Annotations

For some formats, you may prefer to remove annotations from the output. In this case, you can set `code-annotations: none`, which will remove the annotation comments from your code and suppress the output of the ordered list which contains the annotation text.

## Disabling Annotation

You can disable code annotation by including the option `code-annotations: false` in your document. This will stop the processing of code annotations and leave your code (including the annotation comments) and the original ordered list as is.

# quarto-web/docs/authoring/_mermaid-examples/forest.qmd

---
format:
  html:
    mermaid:
      theme: forest
---

```{mermaid}
flowchart LR
  qmd --> J([Jupyter])
  qmd --> K([knitr])
  J --> md
  K --> md
  md --> P([pandoc])
  P --> pdf
  P --> html
  P --> docx
```


# quarto-web/docs/authoring/_mermaid-examples/neutral.qmd

---
format:
  html:
    mermaid:
      theme: neutral
---

```{mermaid}
flowchart LR
  qmd --> J([Jupyter])
  qmd --> K([knitr])
  J --> md
  K --> md
  md --> P([pandoc])
  P --> pdf
  P --> html
  P --> docx
```


# quarto-web/docs/authoring/_mermaid-examples/sandstone.qmd

---
format:
  html:
    theme: sandstone
---

## Quarto Render

```{mermaid}
flowchart LR
  qmd --> J([Jupyter])
  qmd --> K([knitr])
  J --> md
  K --> md
  md --> P([pandoc])
  P --> pdf
  P --> html
  P --> docx
```

Read more on the [Quarto documentation site](https://quarto.org)


# quarto-web/docs/authoring/_mermaid-examples/darkly.qmd

---
format:
  html:
    theme: darkly
---

## Quarto Render

```{mermaid}
flowchart LR
  qmd --> J([Jupyter])
  qmd --> K([knitr])
  J --> md
  K --> md
  md --> P([pandoc])
  P --> pdf
  P --> html
  P --> docx
```

Read more on the [Quarto documentation site](https://quarto.org) 




# quarto-web/docs/authoring/_mermaid-examples/dark.qmd

---
format:
  html:
    mermaid:
      theme: dark
---

```{mermaid}
flowchart LR
  qmd --> J([Jupyter])
  qmd --> K([knitr])
  J --> md
  K --> md
  md --> P([pandoc])
  P --> pdf
  P --> html
  P --> docx
```


# quarto-web/docs/authoring/_mermaid-examples/default.qmd

---
format:
  html:
    mermaid:
      theme: default
---

```{mermaid}
flowchart LR
  qmd --> J([Jupyter])
  qmd --> K([knitr])
  J --> md
  K --> md
  md --> P([pandoc])
  P --> pdf
  P --> html
  P --> docx
```


# quarto-web/docs/authoring/_mermaid-examples/vapor.qmd

---
format:
  html:
    theme: vapor
---

## Quarto Render

```{mermaid}
flowchart LR
  qmd --> J([Jupyter])
  qmd --> K([knitr])
  J --> md
  K --> md
  md --> P([pandoc])
  P --> pdf
  P --> html
  P --> docx
```

Read more on the [Quarto documentation site](https://quarto.org) 




# quarto-web/docs/authoring/_mermaid-examples/solar.qmd

---
format:
  html:
    theme: sandstone
---

## Quarto Render

```{mermaid}
flowchart LR
  qmd --> J([Jupyter])
  qmd --> K([knitr])
  J --> md
  K --> md
  md --> P([pandoc])
  P --> pdf
  P --> html
  P --> docx
```

Read more on the [Quarto documentation site](https://quarto.org) 




# quarto-web/docs/authoring/_mermaid-examples/customize.qmd

---
format:
  html:
    css: custom.css
---

```{mermaid}
flowchart LR
  qmd --> J([Jupyter])
  qmd --> K([knitr])
  J --> md
  K --> md
  md --> P([pandoc])
  P --> pdf
  P --> html
  P --> docx
```


# quarto-web/docs/authoring/_figure-examples/_examples.qmd

---
title: Examples used in `../figures.qmd`
fontsize: 1.5em
---

``` {.bash filename="Terminal"}
quarto render _examples.qmd
quarto render _examples.qmd --to pdf
quarto render _examples.qmd --to docx
quarto run take-screenshots.R
```

## Figure Basics

![Elephant](elephant.png){width="400px"}


## Subfigures

::: {#fig-elephants layout-ncol=2}

![Surus](surus.png){#fig-surus}

![Hanno](hanno.png){#fig-hanno}

Famous Elephants
:::

## Figure Panels

::: {#elephant-figures-no-subcaption layout-ncol=2}
![Surus](surus.png)

![Hanno](hanno.png)
:::

## Multiple Rows

::: {#elephant-rows layout-nrow=2}
![Surus](surus.png)

![Hanno](hanno.png)

![Abdul Abbas](abdul-abbas.png)

![Lin Wang](lin-wang.png)
:::

## Custom Layouts

::: {#layout-attrib layout="[[1,1], [1]]"}
![Surus](surus.png)

![Hanno](hanno.png)

![Lin Wang](lin-wang.png)
:::

::: {#layout-attrib-negative layout="[[40,-20,40], [100]]"}
![Surus](surus.png)

![Hanno](hanno.png)

![Lin Wang](lin-wang.png)
:::

## Vertical Alignment

::: {#valign layout="[15,-2,10]" layout-valign="bottom"}
![Surus](surus.png)

![Lin Wang](lin-wang.png)
:::




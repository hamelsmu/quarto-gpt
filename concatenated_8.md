# quarto-web/docs/output-formats/_ssg-intro.qmd


## Overview

{{< meta ssg-description >}}. Pages in {{< meta ssg-name >}} websites are typically written in plain markdown, so don't have a straightforward way to automatically and reproducibly incorporate computational output.

Using the Quarto `{{< meta format-name >}}-md` format, you can incorporate computational output (e.g. R or Python code that produces plots) into {{< meta ssg-name >}} websites. This article explains how.

It's important to note that many of the Quarto features related to theming, page layout, and navigation are not applicable when you are using Quarto with {{< meta ssg-name >}}. {{< meta ssg-name >}} has its own theming system, syntax highlighting, table of contents, page layout, navigational menus, and full text search. You'll use Quarto to execute code and generate markdown that is rendered within the {{< meta ssg-name >}} HTML publishing framework rather than Quarto's own.


# quarto-web/docs/output-formats/pdf-engine.qmd

---
title: "PDF Engines"
format: html
---

## Overview

Pandoc supports the use of a wide range of TeX distributions and PDF compilation engines including pdflatex, xelatex, lualatex, tectonic, and latexmk.

While you can employ whatever toolchain you like for LaTeX compilation, we strongly recommend the use of [TinyTeX](https://yihui.org/tinytex/), which is a distribution of [TeX Live](https://tug.org/texlive/) that provides a reasonably sized initial download (\~100 MB) that includes the 200 or so most commonly used TeX packages for Pandoc documents.

We also recommend the use of Quarto's built in PDF compilation engine, which among other things performs automatic installation of any missing TeX packages.

## Installing TeX

To install TinyTeX, use the following command:

``` {.bash filename="Terminal"}
quarto install tinytex
```

TinyTeX is not installed to the system `PATH` so will not affect other applications that use TeX. If you want to use TinyTeX with other applications, add the `--update-path` flag when installing (this will add TinyTex to the system path):

``` {.bash filename="Terminal"}
quarto install tinytex --update-path
```

If you already have another installation of TeX that you prefer to use with Quarto, add the `latex-tinytex: false` in your project or document front matter to prevent Quarto from using its internal version.

If you prefer TeX Live, you can find instructions for installing it here: <https://tug.org/texlive/>.

Note that Quarto's automatic installation of missing TeX packages will work for TinyTeX and TeX Live, but not for other TeX distributions (as it relies on TeX Live's [tlmgr](https://www.tug.org/texlive/tlmgr.html) command).

## Managing TeX

In addition to installing TinyTeX, you may also update or remove the installation of TinyTex. To see the currently installed version of TinyTex, use the command:

``` {.bash filename="Terminal"}
quarto list tools
```

which will provide a list of available tools, the installed versions, and the latest available version:

``` bash
[✓] Inspecting tools

Tool         Status            Installed     Latest
chromium     Not installed     ---           869685
tinytex      Up to date        v2022.10      v2022.10
```

To update to the latest version, use the command:

``` {.bash filename="Terminal"}
quarto update tinytex
```

which will download and install the latest version of TinyTex (following the same behavior as described for installing TinyTex above).

To remove TinyTex altogether, use the command:

``` {.bash filename="Terminal"}
quarto uninstall tinytex
```

::: callout-tip
Each year in April, TeXlive updates their remote package repository to the new year's version of TeX. When this happens, previous year installations of TeX will not be able to download and install packages from the remote repository. When this happens, you may see an error like:

*Your TexLive version is not updated enough to connect to the remote repository and download packages. Please update your installation of TexLive or TinyTex.*

When this happens, you can use `quarto update tinytex` to download and install an updated version of tinytex.
:::

## Quarto PDF Engine

Quarto's built-in PDF compilation engine handles running LaTeX multiple times to resolve index and bibliography entries, and also performs automatic LaTeX package installation. This section describes customizing the built-in engine (see the [Alternate PDF Engines](#alternate-pdf-engines) section below for docs on using other engines).

### PDF Compilation

The following options are available for customizing PDF compilation:

| Option                 | Description                                                         |
|------------------------|---------------------------------------------------------------------|
| `latex-min-runs`       | Number (minimum number of compilation passes)                       |
| `latex-max-runs`       | Number (maximum number of compilation passes)                       |
| `latex-clean`          | Boolean (clean intermediates after compilation, defaults to `true`) |
| `latex-output-dir`     | String (output directory for intermediates and PDF)                 |
| `latex-makeindex`      | String (program to use for `makeindex`)                             |
| `latex-makeindex-opts` | Array (options for `makeindex`program)                              |

### Package Installation

The following options are available for customizing automatic package installation:

| Option               | Description                                                         |
|----------------------|---------------------------------------------------------------------|
| `latex-auto-install` | Boolean (enable/disable automatic package installation)             |
| `latex-tlmgr-opts`   | Array (options for [tlmgr](https://www.tug.org/texlive/tlmgr.html)) |

## Alternate PDF Engines {#alternate-pdf-engines}

You can use the `pdf-engine` and `pdf-engine-opts` to control the PDF engine that Quarto uses to compile the LaTeX output into a PDF. For example:

``` yaml
title: "My Document"
pdf-engine: lualatex
pdf-engine-opt: -outdir=out
```

The above example will use the `lualatex` PDF engine rather than the default `xelatex`.

## Latexmk

Quarto includes a built in Latexmk engine, which will run the `pdf-engine` more than once to generate your PDF (for example if you're using cross references or a bibliography). In addition, this engine will detect and attempt to install missing packages, fonts, or commands if TeX Live is available.

You can disable Quarto's built in Latexmk engine by settng the `latex-auto-mk` option to `false`. For example:

``` yaml
title: "My Document"
latex-auto-mk: false
```


# quarto-web/docs/output-formats/gfm.qmd

---
title: GitHub (GFM)
format: html 
format-name: gfm
---

## Overview

While markdown is the input format for Quarto, it can also in some cases be an output format (for example, if you have a website or CMS that accepts markdown as input and want to incorporate computations from Python or R).

This article covers using Quarto to generate [GitHub Flavored Markdown](https://github.github.com/gfm/) (GFM). You might want to do this in order to:

-   Generate a GitHub README.md from a Jupyter notebook

-   Create pages for a GitHub wiki that include computations (e.g. plot output).

## GFM Format

Use the `gfm` format to create GitHub Flavored Markdown from Quarto. For example:

``` yaml
---
title: "My Project"
format: gfm
---
```

See the GFM [format reference](../reference/formats/markdown/gfm.qmd) for a complete list of all options available for GFM output.

To create a `README.md` using Quarto, start with a notebook (.ipynb) or computational markdown file (.qmd) that has README as its file name stem, for example:

````{.markdown filename="README.qmd"}
---
title: "My Project"
format: gfm
jupyter: python3
---

This is a GitHub README that has content dynamically generated from Python:
    
```{{python}}
1 + 1
```
````

Render the README with:

```{.bash filename="Terminal"}
quarto render README.qmd
```

Which will create `README.md` alongside your input file.

## Preview Mode

When you `quarto preview` a GitHub Flavored Markdown document, by default an HTML preview that approximates the look of markdown rendered on GitHub is shown. If you'd prefer to see the raw generated markdown, use the `preview-mode: raw` option. For example:

``` yaml
---
title: "My Project"
format: 
  gfm:
    preview-mode: raw
---
```

{{< include _webtex.md >}}


## GitHub Wikis

If you want to use Quarto to incorporate computations into a GitHub wiki start by [cloning the wiki for local editing](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages#adding-or-editing-wiki-pages-locally).

Then, simply create a computational markdown file (.ipynb, .qmd) for each page in the wiki. You can render all of these files at once into their corresponding .md files using [Quarto Projects](../projects/quarto-projects.qmd). For example:

```{.bash filename="Terminal"}
quarto render
```

You don't even strictly need a Quarto project file to do this as `quarto render` will render all input files in a directory by default if there is no project file.


# quarto-web/docs/output-formats/html-multi-format.qmd

---
title: Including Other Formats
format: 
  html: default
  ipynb: default
  docx: default
aliases:
  - /docs/prerelease/1.3/multi-format.html
---

{{< include ../_require-1.3.qmd >}}

## Overview

HTML pages (either standalone or in a website) can automatically include links to other formats specified in the document front matter. For example, the following document front matter:

``` yaml
title: Sample Page
author: Norah Jones
date: last-modified
toc: true
format: 
  html: default
  ipynb: default
```

Results in an HTML page that includes a link to the additional notebook format in the right margin below the table of contents:

![](images/other-format.png){.border fig-alt="Screenshot of a HTML page that includes a link to the Jupyter format below the table of contents under the heading Other Formats."}

If a table of contents is enabled for the page, the additional formats will be automatically placed within the table of contents as a new section. If no table of contents is displayed, the additional formats will be displayed in the right margin at the top of the document.

Links to additional formats are displayed by default, but you can control whether they are shown or even which specific formats are included with the `format-links` YAML option.

::: callout-note
## Rendering All Formats in Standalone HTML Documents

The Render buttons in RStudio and VS Code will not automatically render all formats if the document isn't part of a Quarto website. To render all formats use `quarto render` on the command line:

``` {.bash filename="Terminal"}
quarto render multi-format.qmd
```
:::

## Rendering Formats with the Same Extension

If your formats share a file extension, for example, both HTML pages and Revealjs presentations use `.html`, their outputs will overwrite each other. To include formats with the same extension, use `output-file` to distinguish one. For example, to include a link to a RevealJS presentation provide a distinct `output-file`:

``` {.yaml filename="document.qmd"}
title: Sample Page
format: 
  html: default
  revealjs: 
    output-file: document-revealjs.html
```

## Specifying Formats to Link

You can provide an explicit list of formats to include in the **Other Formats** section by providing a list as the value for `format-links`. For example, this document front matter will result in only the link to the Jupyter notebook format, excluding the PDF format:

``` yaml
title: Sample Page
author: Norah Jones
date: last-modified
toc: true
format: 
  html: default
  ipynb: default
  pdf: default
format-links: [ipynb]
```

## Hiding All Links

To prevent format links from being shown at all, specify `format-links: false` in your document front matter. For example this front matter will not display the **Other Formats** links:

``` yaml
title: Sample Page
author: Norah Jones
date: last-modified
toc: true
format: 
  html: default
  ipynb: default
format-links: false
```

## Controlling Formats at a Project Level

In a Quarto Project, to control the formats and their behavior for a specific folder, provide the `format`{spellcheck="false"} and `format-links`{spellcheck="false"} options in a `_metadata.yml`{spellcheck="false"} file. Similarly, you can specify these options for an entire project by including them in the `_quarto.yml` project file. See [Directory Metadata](/docs/projects/quarto-projects.qmd#directory-metadata) or [Project Metadata](/docs/projects/quarto-projects.html#project-metadata) for additional details.

The `format`{spellcheck="false"} option isn't merged like all other [metadata](https://quarto.org/docs/projects/quarto-projects.html#metadata-merging) across `_quarto.yml`{spellcheck="false"}, `_metadata.yml`{spellcheck="false"}, and the document YAML. If you have some formats specified at a project or directory level, you'll also need to explicitly list them in the document YAML. For example, suppose you have HTML options set at the project level:

``` {.yaml filename="_quarto.yml"}
format:
  html:
    toc: true
```

In order to get an HTML document with a link to the PDF format, you'll need to list both formats in the YAML header:

``` {.yaml filename="document.qmd"}
format: 
  html: default
  pdf: default
```


# quarto-web/docs/output-formats/pdf-basics.qmd

---
title: PDF Basics
format: html
---

## Overview

Use the `pdf` format to create PDF output. For example:

``` yaml
---
title: "My document"
format:
  pdf:
    toc: true
    number-sections: true
    colorlinks: true
---
```

This example highlights a few of the options available for PDF output. This article covers these and other options in detail. See the PDF [format reference](../reference/formats/pdf.qmd) for a complete list of all available options.

If you want to produce raw LaTeX output (a .tex file) rather than a PDF, all of the options documented here are still available (see the [LaTeX Output] section below for additional details).

::: callout-note
Note that while we will focus here exclusively on the use LaTeX to create PDFs, Pandoc also has support for creating PDFs using ConTeXt, roff ms, or HTML (via wkhtmltopdf). See the Pandoc documentation on [Creating a PDF](https://pandoc.org/MANUAL.html#creating-a-pdf) for additional details.
:::

### Prerequisites

In order to create PDFs you will need to install a recent distribution of TeX. We recommend the use of TinyTeX (which is based on TexLive), which you can install with the following command:

```{.bash filename="Terminal"}
quarto install tinytex
```

See the article on [PDF Engines](pdf-engine.qmd) for details on using other TeX distributions and PDF compilation engines.

## Document Class

Quarto uses [KOMA Script](https://ctan.org/pkg/koma-script) document classes by default for PDF documents and books. KOMA-Script classes are drop-in replacements for the standard classes with an emphasis on typography and versatility.

For PDF documents this results in the following Pandoc options set by default:

``` yaml
format:
  pdf:
    documentclass: scrartcl
    papersize: letter
```

You can set `documentclass` to the standard `article`, `report` or `book` classes, to the KOMA Script equivalents `scrartcl`, `scrreprt`, and `scrbook` respectively, or to any other class made available by LaTeX packages you have installed.

::: callout-note
Setting your `documentclass` to either `book` or `scrbook` will automatically handle many of the common needs for printing and binding PDFs into a physical book (i.e., chapters start on odd pages, alternating margin sizes, etc).
:::

See the [Output Options] section below for additional details on customizing LaTeX document options.

{{< include _document-options-begin.md >}}


## Output Options

There are numerous options available for customizing PDF output, including:

-   Specifying document classes and their options

-   Including lists of figures and tables

-   Using the `geometry` and `hyperref` packages

-   Numerous options for customizing fonts and colors.

For example, here we use a few of these options:

``` yaml
---
title: "My Document"
format: 
  pdf: 
    documentclass: report
    classoption: [twocolumn, landscape]
    lof: true
    lot: true
    geometry:
      - top=30mm
      - left=20mm
      - heightrounded
    fontfamily: libertinus
    colorlinks: true
---
```

See the Pandoc documentation on metadata [variables for LaTeX](https://pandoc.org/MANUAL.html#variables-for-latex) for documentation on all available options.

## Citations

{{< include _pdf-citations.md >}}


## Raw LaTeX

When creating a PDF document, Pandoc allows the use of [raw LaTeX](https://pandoc.org/MANUAL.html#extension-raw_tex) directives intermixed with markdown. For example:

``` tex
\begin{tabular}{|l|l|}\hline
Age & Frequency \\ \hline
18--25  & 15 \\
26--35  & 33 \\
36--45  & 22 \\ \hline
\end{tabular}
```

Raw LaTeX commands will be preserved and passed unchanged to the LaTeX writer.

::: callout-warning
While it's very convenient to use raw LaTeX, raw LaTeX is ignored when rendering to other formats like HTML and MS Word. If you plan on rendering to other formats then the example above would be better written using native [markdown tables](../authoring/markdown-basics.qmd#tables).
:::

In some cases raw LaTeX will require additional LaTeX packages. The [LaTeX Includes] section below describes how to include `\usepackage` commands for these packages in your document.

## LaTeX Includes

{{< include _document-options-includes.md >}}

For example:

``` yaml
format:
  pdf:
    include-in-header:
      - text: |
          \usepackage{eplain}
          \usepackage{easy-todo}
      - file: packages.tex
      - macros.tex 
```

Any packages specified using includes that you don't already have installed locally will be installed by Quarto during the rendering of the document.

## LaTeX Output

If you want Quarto to produce a LaTeX file (.tex) rather than a PDF (for example, if you want to do your own processing of the PDF) there are two ways to accomplish this:

1.  Use the `latex` format rather than the `pdf` format. For example:

    ``` yaml
    format:
      latex:
        documentclass: report
        classoption: [twocolumn, landscape]
        lof: true
        lot: true
    ```

    Note that all of the PDF format options documented above will also work for the `latex` format.

2.  Use the `pdf` format along with the `keep-tex` option. For example:

    ``` yaml
    format:
      pdf:
        documentclass: report
        keep-tex: true
    ```

    This technique will produce a PDF file for preview, but will also create a .tex file alongside it that you can do subsequent processing on.

## Unicode Characters

By default, Quarto uses the `xelatex` engine to produce PDFs from LaTeX. `xelatex` has native support for unicode characters, but it is possible some customization will be required in order to properly typeset specific unicode characters. In particular, it is important that you use a font that supports the characters that you using in your document. To identify fonts on your system that support specific language characters, you can use the following command:

```{.bash filename="Terminal"}
fc-list :lang=<lang>
```

For example, to see a list of fonts that support Japanese characters, use:

```{.bash filename="Terminal"}
fc-list :lang=ja
```

Select a font name from the list and use that as the document's main font, like:

``` markdown
---
title: Unicode test
format: pdf
mainfont: "Hiragino Sans GB"
---

## Test Document

青黑體簡體中文,ヒラギノ角
```


# quarto-web/docs/output-formats/ms-word-templates.qmd

---
title: Word Templates
format: html
---

## Using Templates

If you want to customize the appearance of MS Word output, Pandoc supports a special type of template called a *reference document*. Here's an example of specifying a custom reference document for `docx`:

``` yaml
format:
  docx:
    reference-doc: custom-reference-doc.docx
```

Reference documents include sample text that uses all of the output styles used by Pandoc.

To use a reference doc template, just copy it to your document's directory and reference it as shown above.

## Creating Templates

To create a new reference doc based on the Pandoc default, execute the following command:

    $ quarto pandoc -o custom-reference-doc.docx \
       --print-default-data-file reference.docx

Then, open `custom-reference-doc.docx` in MS Word and modify styles as you wish:

![You can open the Styles pane from the HOME tab in the MS Word toolbar.](images/word-styles.png){.preview-image fig-alt="Screenshot of Microsoft Word document open with Styles pane open in a pane over the left side of the document."}

When you move the cursor to a specific element in the document, an item in the styles list will be highlighted. If you want to modify the style of any type of element, you can click the drop-down menu on the highlighted item, and you will see a dialog box like this:

![](images/word-modify-styles.png){fig-alt="Modify Style dialog box with a properties section for selecting what is to be styled, and a formatting section for selecting the style settings. The color selection dropdown in the formatting section is open."}

After you finish modifying the styles, you can save the document and use it as the template for future Word documents.


# quarto-web/docs/output-formats/page-layout.qmd

---
title: Page Layout
format: html
page-layout: full
aliases:
  - /docs/prerelease/1.3/grid.html
---

## Overview

Quarto provides a default layout for HTML pages that should work well for many documents. However, if the default layout isn't working for your content, you can adjust it. 

On this page, learn about:

* The three high level layout options for your pages in [Page Layout](#page-layout).

* How to adjust the width of the individual layout components (sidebar, body, margins, and gutter) to fit your content in [Grid Customization](#grid-customization). 

## Page Layout {#page-layout}

By default Quarto HTML documents display content centered at a width optimized for readability (typically from 600px to 900px wide). While this is a sound default layout for traditional articles, for other types of pages (e.g. landing or index pages) you may want to use other layouts.

The `page-layout` option can be use to control the layout used. For example:

``` yaml
format: 
  html:
    page-layout: full
```

The various `page-layout` options are described below.

### Article

```
page-layout: article
```

Article layout provides a content area with a page based grid layout that provides margins, areas for sidebars, and a reading width optimized body region. The precise size of the document regions will vary slightly depending upon the sidebar (if present) and the presence or absence of margin or complex layout elements. To learn more, checkout the guide to [Article Layout](../authoring/article-layout.qmd).

### Full

```
page-layout: full
```

Full layout uses the article grid system, but automatically expands the content area to use the sidebar and margin region if no content is placed within those regions. This is useful for layouts that don't need to be constrained to reading width and that will benefit from additional horizontal space (e.g. landing or index pages)

### Custom

```
page-layout: custom
```

Custom layout provides a simple HTML content container with no default grid system, padding, or margins. The default HTML framing provided will look this this:

``` html
<div class="page-layout-custom">
  <!-- body content here -->
</div>
```

In websites, custom layouts do not include navigation sidebars but do include the site navbar and footer.

#### CSS Grid

If you are using `page-layout: custom`, you'll likely want to utilize the [Bootstrap CSS Grid](https://getbootstrap.com/docs/5.1/layout/css-grid/) layout system (which is available by default in Quarto documents) for creating more sophisticated layouts.

For example, here's a simple 2-column grid:

```markdown
::: {.grid}

::: {.g-col-4}
This column takes 1/3 of the page
:::

::: {.g-col-8}
This column takes 2/3 of the page
:::

:::
```

Bootstrap's CSS Grid system includes facilities for responsiveness, wrapping, nesting, and fine grained customization of column behavior.

Note that this isn't the traditional Bootstrap grid used in older versions of Bootstrap -- rather, it's a brand new layout system introduced in Bootstrap 5.1 based on the CSS Grid standard. Quarto uses this newer system because it has more sophisticated layout capabilities akin to what LaTeX offers for print documents.

See the [Bootstrap CSS Grid](https://getbootstrap.com/docs/5.1/layout/css-grid/) documentation for additionals details.

## Grid Customization {#grid-customization}

{{< include ../_require-1.3.qmd >}}

You can control the width of the layout components in HTML documents with YAML options and SCSS. For example, if long entries in a sidebar are being wrapped, it may make sense to increase the width of sidebar: 

::: {layout-ncol=2}
![Default Layout](images/grid-default.png){fig-alt="Screenshot of a Quarto website displaying the default layout of the sidebar, body and margin."}

![Wider Sidebar](images/grid-wide-sidebar.png){fig-alt="Screenshot of a Quarto website with altered layout, devoting more space to the sidebar."}
:::

This change can be made by adding the `grid` option to the `_quarto.yml` file, increasing the `sidebar-width` from its default of 250px:

```{.yaml filename="_quarto.yml"}
format:
  html:
    grid:
      sidebar-width: 350px
```

There are four variables to control the four components of the layout: the sidebar, the body, the margin, and the gutters. 

The rest of this section describes these components, and their default values, as well as how to customize them either with YAML or SCSS  variables. You can also find [Additional Examples](#more-examples) of customization in action.

### HTML Page Layout

Quarto HTML documents are arranged in a structure composed of a sidebar on the left, the body of the document, the margin of the document on the right, and the space between these elements, known as gutters. This is illustrated below:

![](images/grid.png){fig-alt="A screenshot of a page in the Quarto documentation site, with rectangles drawn around the sidebar, body and margin, and arrows indicating the gutters between them."}

The width of these four components is controlled by four variables. These variables, along with their default values are:

::: {style="width: 60%; margin: auto;"}
| Element                             | Size  |
|-------------------------------------|-------|
| `sidebar-width`{spellcheck="false"} | 250px |
| `body-width`{spellcheck="false"}    | 800px |
| `margin-width`{spellcheck="false"}  | 250px |
| `gutter-width`{spellcheck="false"}  | 1.5em |

: Default values for the width of layout components
:::

The values of these variables don't directly specify the display width of the corresponding component, instead they specify a maximum base value. The maximum values are scaled to create minimum values, and together they are used to compute the size and position of each component across different layout types (fixed vs. floating), responsive sizes (large screen vs. mobile size), and page contents (margin vs. no margin content). 

### Customizing Component Widths

You can control the component width variables using YAML or SCSS variables. To set these options in YAML, you may use the `grid` option :

```{.yaml filename="_quarto.yml"}
format:
  html: 
    grid:
      sidebar-width: 300px
      body-width: 900px
      margin-width: 300px
      gutter-width: 1.5rem
```

::: {.callout-note}
## Websites vs. Standalone HTML Pages

Customizing the layout of pages that are part of a Quarto website with YAML should happen at the site level in `_quarto.yml`. For HTML documents that aren't part of a website, these options could also be set in the YAML at the top of the document.

:::


Similarly, in a [custom theme `scss` file](https://quarto.org/docs/output-formats/html-themes.html#theme-options), you may set variables like:

``` css
// The left hand sidebar
$grid-sidebar-width: 300px !default;

// The main body
$grid-body-width: 900px !default;

// The right hand margin bar
$grid-margin-width: 300px !default;

// The gutter that appears between the above columns
$grid-column-gutter-width: 1.5rem !default;
```

`sidebar-width`, `body-width`, and `margin-width` should be specified in pixels (`px`) as the values will be used when computing other sizes. Requiring pixel sizing is a limitation of our approach to the Quarto's layout, but also typically makes sense since the overall document width is usually tied to the browser size and responsive breakpoints rather than font size or other relative measures. 

`gutter-width` may be specified in pixels or other units such as `em` or `rem` which are responsive to the document font size.

### Additional Examples {#more-examples}

Increasing the margin width may make sense on a website that has many figures or tables in the margin. For example, this YAML increases the `margin-width` by 200px over the default value:

```yaml
format:
  html:
    grid:
      margin-width: 450px
```

::: {layout-ncol=2}
![Default Layout](images/grid-default.png){fig-alt="Screenshot of a Quarto website displaying the default layout of the sidebar, body and margin."}

![Wider Margin](images/grid-wide-margin.png){fig-alt="Screenshot of a Quarto website with altered layout, devoting more space to the margin."}
:::

The effect of changing `margin-width` without changing `body-width` is to increase the overall page width (there is less white space on the far left and right of the page). Alternatively, to keep the overall page width the same `body-width` can be decreased by the same amount as `margin-width` increased:

```yaml
format:
  html:
    grid:
      margin-width: 450px
      body-width: 600px
```

::: {layout-ncol=2}
![Default Layout](images/grid-default.png){fig-alt="Screenshot of a Quarto website displaying the default layout of the sidebar, body and margin."}

![Wider Margin, Narrower Body](images/grid-wide-margin-narrow-body.png){fig-alt="Screenshot of a Quarto website with altered layout, devoting more space to the margin and less to the body."}
:::



# quarto-web/docs/output-formats/_ssg-workflow.qmd



## Workflow

The basic concept of using Quarto with {{< meta ssg-name >}} is that you take *computational* markdown documents (`.qmd`) or Jupyter notebooks (`.ipynb`) and use them to generate plain markdown files (`.md`) that are rendered to HTML by {{< meta ssg-name >}}.

**index.qmd**   *quarto =\>*   **index.md**   *{{< meta format-name >}} =\>*   **index.html**

The `quarto render` and `quarto preview` commands are used to transform `.qmd` or `.ipynb` files to {{< meta ssg-name >}} compatible markdown (`.md`). The computational files are located in the same place you would also locate ordinary markdown files (e.g. the `blog` directory).

After rendering, a plain `.md` file is written right alongside the computational document. This markdown file is then processed by {{< meta ssg-name >}}.

### Live Preview

The `quarto preview` command will automatically recognize when it is run from a directory that contains a {{< meta ssg-name >}} website:

``` {.bash filename="Terminal"}
cd my-{{< meta format-name >}}-website
quarto preview
```

This will automatically run `{{< meta ssg-preview >}}` on your behalf to bring up a local preview server. In addition, it will monitor the filesystem for changes to `.qmd` and `.ipynb` inputs and automatically re-render them to {{< meta ssg-name >}} compatible `.md` files when they change.

Note that this also works for the integrated Render/Preview command within the [Quarto VS Code Extension](/docs/tools/vscode.qmd).

### Rendering

If you are not previewing and want to render all of the Quarto documents (`.qmd`) and notebooks (`.ipynb`) in your site, call `quarto render` from the root directory of the site:

``` {.bash filename="Terminal"}
cd my-{{< meta format-name >}}-website
quarto render 
```

Typically you'll want to do a `quarto render` at the site level before you build the site for publishing:

``` {.bash filename="Terminal"}
quarto render && {{< meta ssg-build >}}
```

You can also render individual documents or notebooks:

``` {.bash filename="Terminal"}
quarto render blog/2022-07-26/hello-quarto/index.qmd
```

If you have computationally expensive documents you may want to consider using Quarto's [freeze](/docs/projects/code-execution.qmd#freeze) feature to only re-execute code when your document source code changes.

Note that if aren't ever rendering at the project level and just have individual files that you want to render with Quarto, you should specify the `{{< meta format-name >}}-md` format as follows:

``` yaml
---
title: "My Blog Post"
format: {{< meta format-name >}}-md
---
```

### Configuration

While Quarto works well within a {{< meta ssg-name >}} site that has no `_quarto.yml` project config file, you can add one if you want to customize the default behavior, add a bibliography, etc. For example, here is what a simple customized `_quarto.yml` file might look like:

``` {.yaml filename="_quarto.yml"}
project:
  type: {{< meta format-name >}}
      
format: 
  {{< meta format-name >}}-md:
    code-fold: true
  
execute: 
  warning: false

biliography: references.lib
```

It's important to note that if you do provide an explicit `_quarto.yml` file you need to explicitly specify the project type (`type: {{< meta format-name >}}`) as shown above.

#### External Directory

You might decide that you prefer to keep all of your Quarto documents and/or notebooks in their own directory, separate from the {{< meta ssg-name >}} website. In this configuration you would mirror the directory structure of your site in the Quarto directory, and then set the `output-dir` in the project file to point to the {{< meta ssg-name >}} directory. For example:

``` {.yaml filename="_quarto.yml"}
project:
  type: {{< meta format-name >}}
  output-dir: ../{{< meta format-name >}}-site
```


# quarto-web/docs/output-formats/docusaurus.qmd

---
title: Docusaurus
format-name: docusaurus  
ssg-name: Docusaurus
ssg-description: |
  [Docusaurus](https://docusaurus.io) is a popular markdown documentation system
ssg-preview: docusaurus start
ssg-build: npm run build
---

{{< include _ssg-intro.qmd >}}

{{< include _ssg-workflow.qmd >}}

## Code Blocks

Code blocks in Docusaurus are very similar to Quarto. One important thing to keep in mind is that the syntax highlighting theme comes from Docusaurus rather than Quarto. See the [theming](https://docusaurus.io/docs/markdown-features/code-blocks#theming) documentation for additional details.

If you use the `filename` attribute in Quarto, it will automatically become the code block `title` in Docusaurus:

```` markdown
```{.python filename="hello.py"}
1 + 1
```
````

![](images/docusaurus-code-title.png)

Code folding is also automatically applied. So, for example the following executable code block:

``` python
```{{python}}
#| code-fold: true
1 + 1
```

Is rendered as a collasable block in Docusaurus:

![](images/docusaurus-code-fold.png)

## Callouts & Tabsets

Like Quarto, Docusaurus includes support for [Callouts](/docs/authoring/callouts.qmd) and [Tabsets](/docs/output-formats/html-basics.qmd#tabsets). When including these components in a document, you should use the Quarto standard markdown syntax, which will be automatically translated to the appropriate Docusaurus constructs.

For example, here is a Quarto callout:

``` markdown
::: {.callout-important}
Note the Quarto callout syntax is used here.
:::
```

Which renders in Docusaurus as:

![](images/docusaurus-callout.png)

Here is a Quarto tabset:

``` markdown
::: {.panel-tabset group="fruits"}

## Apple
This is an apple 🍎

## Orange
This is an orange 🍊

## Banana
This is a banana 🍌

:::
```

Which renders in Docusaurus as:

![](images/docusaurus-tabs.png){.border}

## HTML and MDX

Docusaurus websites use a flavor of markdown ([MDX](https://mdxjs.com/)) that has some major differences from Pandoc (Quarto's native markdown renderer), the biggest of which is that while Quarto allows embedding of HTML, MDX does not. Rather, MDX allows direct embedding of JavaScript code and React JSX components (which look like HTML but have some significant differences in behavior).

Quarto's support for Docusaurus accounts for these differences, and enables you to embed raw HTML as well as use MDX components and JavaScript when required.

### HTML Blocks

Docusaurus websites don't allow arbitrary HTML content. Rather, JSX is used to emit HTML tags. While these JSX tags look and act like HTML tags most of the time, there are some important caveats and constraints, most notably that the `class` attribute must be written as `className`, and `style` attributes need to be specified as JavaScript objects rather than CSS strings.

If you need to include raw HTML that doesn't conform to JSX, you should use a raw ```` ```{=html} ```` code block. For example:

```` html
```{=html}
<p style="color: green;">Paragraph</p>
```
````

If you need to embed HTML code (e.g. a badge, video, or tweet) you should definitely use raw HTML blocks as shown above to avoid errors which will occur if JSX encounters tags it can't parse.

Note that HTML produced by computations (e.g. a Pandas data frame displayed in a notebook) often use raw HTML with `class` and/or `style` tags. This computational output is automatically included in a raw ```` ```{=html} ```` code block so that it renders correctly in Docusaurus.

### MDX Blocks

You can also use MDX components and JavaScript within Quarto documents that target Docusaurus. To do this, enclose them in an ```` ```{=mdx} ```` raw code block. For example:

```` html
```{=mdx}
export const Highlight = ({children, color}) => (
  <span
    style={{
      backgroundColor: color,
      borderRadius: '2px',
      color: '#fff',
      padding: '0.2rem',
    }}>
    {children}
  </span>
);

<Highlight color="#25c2a0">Docusaurus GREEN</Highlight> and <Highlight color="#1877F2">Rams blue</Highlight> are my favorite colors.

I can write **Markdown** alongside my _JSX_!
```
````

Which is rendered as follows:

![](images/docusaurus-mdx.png){.border}

Note that ordinary markdown content can also be included in `mdx` blocks alonside JavaScript and React components.

## LaTeX Math

By default, Quarto renders LaTeX math within Docusaurus projects using [WebTeX](https://github.com/KTHse/webtex), a service that creates PNG images for publishing on the web given TeX expressions as input.

{{< include _webtex-detail.md >}}

### KaTeX

It is possible to configure Docusaurus to use KaTeX for math rendering. See the Docusaurus documentation on [using KaTeX](https://docusaurus.io/docs/markdown-features/math-equations) to learn more about this option.

Once you've confirmed that KaTeX is rendering equations correctly in your site, you should update your `_quarto.yml` file to specify that `katex` rather than `webtex` should be used for rendering equations:

``` {.yaml filename="_quarto.yml"}
format:
  docusaurus-md:
    html-math-method: katex
```


# quarto-web/docs/output-formats/html-publishing.qmd

---
title: "Publishing HTML"
---

## Overview

This article covers the various ways you can publish Quarto HTML documents, including publishing to a hosting service or sharing a standalone HTML file using E-mail, Dropbox, etc.

Note that it's also possible to publish collections of Quarto documents as a website. See the article on [Publishing Basics](../publishing/index.qmd) for additional details.

## Publish Command

The `quarto publish` command provides a straightforward way to publish documents to [Quarto Pub](../publishing/quarto-pub.qmd), [GitHub Pages](../publishing/github-pages.qmd), [Netlify](../publishing/netlify.qmd), and [Posit Connect](../publishing/rstudio-connect.qmd).

For example, here are the commands to publish `document.qmd` to each of these services:

```{.bash filename="Terminal"}
quarto publish quarto-pub document.qmd
quarto publish gh-pages document.qmd
quarto publish netlify document.qmd
quarto publish connect document.qmd
```

For simple publishing of individual documents there's not much more to learn than `quarto publish`.

Here's a brief overview of the various supported services and when they might be an appropriate choice:

| Destination                                                | Description                                                                                                                                                                                     |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Quarto Pub](../publishing/quarto-pub.html)                | Publishing service for Quarto documents, websites, and books. Use Quarto Pub when you want a free, easy to use service for publicly available content.                                          |
| [GitHub Pages](../publishing/github-pages.html)            | Publish content based on source code managed within a GitHub repository. Use GitHub Pages when the source code for your document or site is hosted on GitHub.                                   |
| [Posit Connect](../publishing/rstudio-connect.html)        | Publishing platform for secure sharing of data products within an organization. Use Posit Connect when you want to publish content within an organization rather than on the public internet. |
| [Netlify](../publishing/netlify.html)                      | Professional web publishing platform. Use Netlify when you want support for custom domains, authentication, previewing branches, and other more advanced capabilities.                          |
| [Other Services](../publishing/other.html)                 | Content rendered with Quarto uses standard formats (HTML, PDFs, MS Word, etc.) that can be published anywhere. Use this if one of the methods above don't meet your requirements.               |

: {tbl-colwidths="\[25,75\]"}

Note that the documentation linked to above generally references publishing an entire project (website or book) but all of the commands work just the same if you publish an individual document or presentation as demonstrated above.

## Standalone HTML

You can optionally render Quarto documents into self contained HTML, whereby all of the content required to render the article (images generated by plots, required CSS and JavaScript, etc.) are bundled into a single HTML file. Use the `embed-resources` option to do this:

``` yaml
format:
  html:
    embed-resources: true
```

Then, you can share this HTML file using the same means you use to share other document types like spreadsheets, presentations, and PDFs (e.g by uploading it to Dropbox or any other file sharing service).

Note that when using `embed-resources: true`, math libraries like [MathJax](https://www.mathjax.org/) and [KaTeX](https://katex.org/) are not embedded by default because they are quite large and often time consuming to download. If you do want to embed math libraries, add the `self-contained-math: true` option:

``` yaml
format:
  html:
    embed-resources: true
    self-contained-math: true
```


# quarto-web/docs/output-formats/html-themes.qmd

---
title: "HTML Theming"
tbl-colwidths: [40,60]
---

## Overview

HTML documents rendered with Quarto use Bootstrap 5 by default. This can be disabled or customized via the `theme` option:

``` yaml
theme: default # bootstrap 5 default
theme: cosmo   # cosmo bootswatch theme
theme: pandoc  # pandoc default html treatment
theme: none    # no theme css added to document
```

Quarto includes 25 themes from the [Bootswatch](https://bootswatch.com/) project (for example, the website uses the [cosmo](https://bootswatch.com/cosmo/) theme). Available themes include:

{{< include _theme-list.md >}}


Use of any of these themes via the `theme` option. For example:

``` yaml
format:
  html:
    theme: united
```

You can also customize these themes or create your own new themes. Learn how to do this below in [Theme Options].

## Basic Options

If you are using a Bootstrap theme or the Pandoc theme, there are a set of options you can provide in document metadata to customize its appearance. These include:

+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option                                                       | Description                                                                                                                                                    |
+==============================================================+================================================================================================================================================================+
| `max-width`                                                  | The maximum width occupied by page content. Defaults to 1400px for bootstrap themes and 36em for the pandoc theme.                                             |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `mainfont`                                                   | Sets the [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family) property for the document.                                              |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `fontsize`                                                   | Sets the base CSS [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size) for the document.                                                  |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `fontcolor`                                                  | Sets the default text [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/color) for the document.                                                      |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `linkcolor`                                                  | Sets the default text [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/color) for hyperlinks.                                                        |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `monofont`                                                   | Sets the [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family) property for `<code>` elements.                                         |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `monobackgroundcolor`                                        | Sets the [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/background-color) property for `<code>` elements.                               |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `linestretch`                                                | Sets the CSS [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/line-height) property (affects distance between lines of text, defaults to 1.5). |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `backgroundcolor`                                            | Sets the [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/background-color) for the document.                                             |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `margin-left`, `margin-right`, `margin-top`, `margin-bottom` | Sets the CSS [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/margin) properties for the document body.                                             |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

For example. here we set the font-size a bit larger and specify that we want a bit more space between lines of text:

``` yaml
title: "My Document"
format:
  html: 
    theme: cosmo
    fontsize: 1.1em
    linestretch: 1.7
```

{{< include _theme-options.md >}}

{{< include _theme-custom.md >}}


## Dark Mode

In addition to providing a single theme for your html output, you may also provide a light and dark theme. For example:

``` yaml
theme:
  light: flatly
  dark: darkly
```

Setting the above themes in your `_quarto.yml` results in both a dark and light version of your output being available. For example:

------------------------------------------------------------------------

##### Flatly Themed Output

![](images/html-light.png){fig-alt="A screenshot of the header of the light version of this page showcasing the Flatly theme."}

------------------------------------------------------------------------

##### Darkly Themed Output

![](images/html-dark.png){fig-alt="A screenshot of the header of the dark version of this page showcasing the Darkly theme."}

------------------------------------------------------------------------

When providing both a dark and light mode for your html output, Quarto will automatically create a toggle to allow your reader to select the desired dark or light appearance. The toggle will automatically appear in the top right corner of your html output. When possible, the toggle will use browser local storage to maintain the user's preference across sessions.

The first appearance (light or dark) elements in the theme to determine the default appearance for your html output. For example, since the `light` option appears first in the above example, a reader will see the light appearance by default.

Quarto will automatically select the appropriate light or dark version of the text highlighter that you have specified when possible. For more information, see [Code Highlighting](html-code.html#highlighting).

### Customizing Themes

As when providing a single theme, you may provide a custom theme for dark and light mode, or a list of `scss` files to customize the light and dark appearance. This website, for example uses the following to use a light `cosmo` theme and then customizes the `cosmo` theme with additional Sass variables when in dark mode:

``` yaml
theme:
  light: cosmo
  dark: [cosmo, theme-dark.scss]
```

The contents of `theme-dark.scss` which is customizing the cosmo document appearance is:

``` css
/*-- scss:defaults --*/
// Base document colors
$body-bg: #181818;
$body-color: white;
$link-color: #75AADB;

// Code blocks
$code-block-bg-alpha: -.8;
```

For more information about available Sass variables, see [HTML Customization Using Sass Variables](html-themes-more.qmd).

{{< include _theme-variables.md >}}

# quarto-web/docs/output-formats/html-themes-more.qmd

---
title: "More About Quarto Themes"
---

As a part of Quarto, we've developed a simple single file format that describes declarations, variables, and rules that should be layered into Scss files when compiling them into css. The basic structure of a theme file is:

-   A single text file that contains valid Scss

-   Special comments are used to denote regions of functions, defaults, mixins, and rules (region decorators).

-   At least one of these region decorators must be present in order for the theme file to be valid.

-   More than one of each type of region decorator are permitted. If more than one of any type is present, all regions of a given type will be merged into a single block of that type in the order in which they are encountered in the file.

-   When compiling, the sections will be layered according to type, functions first, then variables, then mixins, then rules.

-   The directory that contains your theme file will be added to the load path, allowing `@use` or `@import` statements to be resolved using the same directory that contains the theme file.

Here is an example file:

``` css
/*-- scss:functions --*/
@function colorToRGB ($color) {
  @return "rgb(" + red($color) + ", " + green($color) + ", " + blue($color)+ ")";
}

/*-- scss:defaults --*/
$h2-font-size:          1.6rem !default;
$headings-font-weight:  500 !default;
$body-color:            $gray-700 !default;

/*-- scss:rules --*/
h1, h2, h3, h4, h5, h6 {
  text-shadow: -1px -1px 0 rgba(0, 0, 0, .3);
}
```

## Bootswatch Sass Theme Files

We've merged Bootswatch themes for Bootstrap 5 into this single file theme format in our repo here:

<https://github.com/quarto-dev/quarto-cli/tree/main/src/resources/formats/html/bootstrap/themes>

From time to time, as the Bootswatch themes are updated, we will update these merged theme files.

## Bootstrap / Bootswatch Layering

When using the Quarto HTML format, we allow the user to specify theme information in the document front matter (or project YAML). The theme information consists of a list of one or more of

-   A valid built in Bootswatch theme name

-   A theme file (valid as described above).

For example the following would use the cosmo Bootswatch theme and provide customization using the custom.scss file:

``` yaml
theme:
  - cosmo
  - custom.scss
```

When compiling the CSS for a Quarto website or HTML page, we merge any user provided theme file(s) or Bootswatch themes with the Bootstrap Scss in the following layers:

    Uses
        Bootstrap
        Theme(s)       /*-- scss:uses --*/
        
    Functions
        Bootstrap
        Theme(s)       /*-- scss:functions --*/

    Variables
        Themes(s)      /*-- scss:defaults --*/
        Bootstrap
        
    Mixins                 
        Bootstrap
        Theme(s)       /* -- scss:mixins --*/

    Rules
        Bootstrap
        Theme(s)       /*-- scss:rules --*/

We order the themes according to the order that they are specified in the YAML, maintaining the order for declarations and rules and reversing the order for variables (allowing the files specified later in the list to provide defaults variable values to the files specified earlier in the list). Layering of the example themes above would be as follows:

    Uses
        Bootstrap
        cosmo           /*-- scss:uses --*/
        custom.scss     /*-- scss:uses --*/

    Functions
        Bootstrap
        cosmo           /*-- scss:functions --*/
        custom.scss     /*-- scss:functions --*/

    Variables
        custom.scss     /*-- scss:defaults --*/
        cosmo           /*-- scss:defaults --*/
        Bootstrap

    Mixins
        Bootstrap
        cosmo            /* -- scss:mixins --*/
        custom.scss      /* -- scss:mixins --*/

    Rules
        Bootstrap
        cosmo           /*-- scss:rules --*/
        custom.scss     /*-- scss:rules --*/


# quarto-web/docs/output-formats/hugo.qmd

---
title: Hugo
format-name: hugo
ssg-name: Hugo
ssg-description: |
  [Hugo](https://gohugo.io/) is a very popular open source website publishing system
ssg-preview: hugo serve
ssg-build: hugo
---

{{< include _ssg-intro.qmd >}}

## Site Config

There are a couple of changes you should make to your Hugo `config.toml` in preparation for using Quarto with Hugo. First, make sure that `.qmd` and `.ipynb` files and other source code or data files are not published as part of the site. For example:

``` toml
ignoreFiles = [ "\\.qmd$", "\\.ipynb$", "\\.py$" ]
```

Next, configure Hugo's markdown renderer to allow raw HTML (as many R and Python packages will produce computational output using raw HTML rather than markdown):

``` toml
[markup.goldmark.renderer]
unsafe= true
```

## Creating a Page

Hugo articles and posts that use Quarto should live in their own directory (taking advantage of the Hugo [Page Bundles](https://gohugo.io/content-management/page-bundles/) feature). This allows any content generated/referenced by the page (e.g. plot output) to live right alongside the markdown source.

To add Quarto documents to a Hugo site:

1.  Create a directory within `content` that will hold your Quarto article.

2.  Add an `index.qmd` document to the directory. When rendered this will create an `index.md`, which in turn will ensure that Hugo treats it as a [Page Bundle](https://gohugo.io/content-management/page-bundles/) (automatically copying images and other referenced resources to the publish directory).

3.  Add the requisite Hugo [front matter](https://gohugo.io/content-management/front-matter/), then also specify `format: hugo-md` and any other required Quarto options.

For example, let's say we wanted to create a new article named `hello-quarto` within the `content` directory. The filesystem would look like this:

``` ini
mysite/
  content/
    hello-quarto/
      index.qmd
```

Here's what the source code of `index.qmd` might look like:

    ---
    title: Hello, Quarto
    date: "2012-04-06"
    categories: 
      - Matplotlib
      - Coordinates
    format: hugo-md
    jupyter: python3
    ---

    ## Polar Axis

    For a demonstration of a line plot on a polar axis, see @fig-polar.

    ```{{python}}
    #| label: fig-polar
    #| fig-cap: "A line plot on a polar axis"

    import numpy as np
    import matplotlib.pyplot as plt

    r = np.arange(0, 2, 0.01)
    theta = 2 * np.pi * r
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r)
    ax.set_rticks([0.5, 1, 1.5, 2])
    ax.grid(True)
    plt.show()
    ```

{{< include _ssg-workflow.qmd >}}


## Shortcodes

Note that Hugo [shortcodes](https://gohugo.io/content-management/shortcodes/) and Quarto [shortcodes](../extensions/shortcodes.qmd) share the same basic syntax (e.g. `{{{< var foo >}}}`). This is normally not a problem as shortcodes not recognized by Quarto are passed through unmodified to Hugo.

However, in some cases the use of a Hugo shortcode throws off Pandoc markdown processing, and its necessary to "protect" the Hugo shortcode from processing by Pandoc. This can typically be handled by escaping the shortcode with an extra brace. For example:

``` default
{{{{< ref "foo/index.md" >}}}}
```

It's possible that this won't be enough if the presence of the shortcode changes how Pandoc processes the surrounding markdown (e.g. this is currently known to occur for links). In this case you need to use a markdown raw block around the entire construct. For example:

```` default
```{=markdown}
[click here]({{< ref "foo/index.md" >}})
```
````

Or for inline content, use a markdown raw inline:

``` default
For more info, `[click here]({{< ref "foo/index.md" >}})`{=markdown}
```

{{< include _webtex.md >}}




# quarto-web/docs/reference/dates.qmd

---
title: Quarto Dates and Date Formatting
search: true
aliases: 
  - /reference/date-format.html
---

## Date Parsing

When you write a date for Quarto document, Quarto will attempt to parse a date string by trying a number of standard forms before ultimately attempting to infer the date format. Quarto will try dates formatted as follows, in the following order:

-   `MM/dd/yyyy`
-   `MM-dd-yyyy`
-   `MM/dd/yy`
-   `MM-dd-yy`
-   `yyyy-MM-dd`
-   `dd MM yyyy`
-   `MM dd, yyyy`
-   `YYYY-MM-DDTHH:mm:ssZ`

In addition, you may also provide date keywords, which will provide a dynamic date.

| Keyword         | Date                                                             |
|-----------------|-------------------------------------------------------|
| `today`         | The current local date, with the time portion set to 0.          |
| `now`           | The current local date and time.                                 |
| `last-modified` | The last modified date and time of the input file containing the date. |

## Date Formatting

When specifying a date format in Quarto, there are two ways to represent the format that you'd like.

### Using a Date Style

You can specify a simple date style which will be used to format the date.

For example:

``` yaml
---
date: 03/07/2005
date-format: long
---
```

Valid styles and examples of the formatted output are as follows:

| Style    | Description                                 | Example               |
|----------------|--------------------------------------|-------------------|
| `full`   | A full date that includes the weekday name  | Monday, March 7, 2005 |
| `long`   | A long date that includes a wide month name | March 7, 2005         |
| `medium` | A medium date                               | Mar 7, 2005           |
| `short`  | A short date with a numeric month           | 3/7/05                |
| `iso`    | A short date in ISO format                  | 2005-03-07            |

### Using a Date Format

You can also specify a date format string that will be used to format the date. For example:

``` yaml
---
date: 03/07/2005
date-format: "MMM D, YYYY"
```

The permissible values in this string include:

| **Format String** | **Output**            | **Description**                                                                                               |
|------------------|------------------|------------------------------------|
| `YY`              | 18                    | Two-digit year                                                                                                |
| `YYYY`            | 2018                  | Four-digit year                                                                                               |
| `M`               | 1-12                  | The month, beginning at 1                                                                                     |
| `MM`              | 01-12                 | The month, 2-digits                                                                                           |
| `MMM`             | Jan-Dec               | The abbreviated month name                                                                                    |
| `MMMM`            | January-December      | The full month name                                                                                           |
| `D`               | 1-31                  | The day of the month                                                                                          |
| `DD`              | 01-31                 | The day of the month, 2-digits                                                                                |
| `d`               | 0-6                   | The day of the week, with Sunday as 0                                                                         |
| `dd`              | Su-Sa                 | The min name of the day of the week                                                                           |
| `ddd`             | Sun-Sat               | The short name of the day of the week                                                                         |
| `dddd`            | Sunday-Saturday       | The name of the day of the week                                                                               |
| `H`               | 0-23                  | The hour                                                                                                      |
| `HH`              | 00-23                 | The hour, 2-digits                                                                                            |
| `h`               | 1-12                  | The hour, 12-hour clock                                                                                       |
| `hh`              | 01-12                 | The hour, 12-hour clock, 2-digits                                                                             |
| `m`               | 0-59                  | The minute                                                                                                    |
| `mm`              | 00-59                 | The minute, 2-digits                                                                                          |
| `s`               | 0-59                  | The second                                                                                                    |
| `ss`              | 00-59                 | The second, 2-digits                                                                                          |
| `SSS`             | 000-999               | The millisecond, 3-digits                                                                                     |
| `Z`               | +05:00                | The offset from UTC, ±HH:mm                                                                                   |
| `ZZ`              | +0500                 | The offset from UTC, ±HHmm                                                                                    |
| `A`               | AM PM                 |                                                                                                               |
| `a`               | am pm                 |                                                                                                               |
| `Q`               | 1-4                   | Quarter                                                                                                       |
| `Do`              | 1st 2nd ... 31st      | Day of Month with ordinal                                                                                     |
| `k`               | 1-24                  | The hour, beginning at 1                                                                                      |
| `kk`              | 01-24                 | The hour, 2-digits, beginning at 1                                                                            |
| `X`               | 1360013296            | Unix Timestamp in second                                                                                      |
| `x`               | 1360013296123         | Unix Timestamp in millisecond                                                                                 |
| `w`               | 1 2 ... 52 53         | Week of year ( dependent [`WeekOfYear` ](https://day.js.org/docs/en/plugin/week-of-year)plugin )              |
| `ww`              | 01 02 ... 52 53       | Week of year, 2-digits ( dependent [`WeekOfYear` ](https://day.js.org/docs/en/plugin/week-of-year)plugin )    |
| `W`               | 1 2 ... 52 53         | ISO Week of year ( dependent [`IsoWeek` ](https://day.js.org/docs/en/plugin/iso-week)plugin )                 |
| `WW`              | 01 02 ... 52 53       | ISO Week of year, 2-digits ( dependent [`IsoWeek` ](https://day.js.org/docs/en/plugin/iso-week)plugin )       |
| `wo`              | 1st 2nd ... 52nd 53rd | Week of year with ordinal ( dependent [`WeekOfYear` ](https://day.js.org/docs/en/plugin/week-of-year)plugin ) |
| `gggg`            | 2017                  | Week Year ( dependent [`WeekYear` ](https://day.js.org/docs/en/plugin/week-year)plugin )                      |
| `GGGG`            | 2017                  | ISO Week Year ( dependent [`IsoWeek` ](https://day.js.org/docs/en/plugin/iso-week)plugin )                    |
| `z`               | EST                   | Abbreviated named offset ( dependent [`Timezone` ](https://day.js.org/docs/en/plugin/timezone)plugin )        |
| `zzz`             | Eastern Standard Time | Unabbreviated named offset ( dependent [`Timezone`](https://day.js.org/docs/en/plugin/timezone)plugin )       |

To escape characters, wrap them in square brackets (e.g. `[MM]`).

Example formats and outputs include:

| Format                                 | Output                                |
|------------------------------------|------------------------------------|
| `MMM D, YYYY`                          | Mar 7, 2005                           |
| `DD/MM/YYYY`                           | 07/03/2005                            |
| `[YYYYescape] YYYY-MM-DDTHH:mm:ssZ[Z]` | YYYYescape 2005-03-07T00:00:00-05:00Z |
| `YYYY-MM-DDTHH:mm:ssZ`                 | 2005-03-07T00:00:00-05:00             |
| `dddd MMM D, YYYY`                     | Monday Mar 7, 2005                    |


# quarto-web/docs/reference/index.qmd

---
title: "Reference"
subtitle: Options reference for formats, code cells, and projects. See the [user guide](../guide/index.qmd) for   more in-depth documentation on usage. 
toc: false
tbl-colwidths: [30, 70]
anchor-sections: false
listing:
  id: reference-links
  template: ../../ejs/links.ejs
  contents: ./reference.yml
image: /images/hero_right.png  
---

::: {#reference-links .column-screen-inset-right style="max-width: 850px;"}
:::


# quarto-web/docs/reference/globs.qmd

---
title: Quarto Glob Syntax
search: true
---

## Overview

Quarto sometimes allows you to provide a path or paths using glob syntax, providing wildcard expansion and other behavior that makes it simple to match a list of files without having to specify each file individually. Globs may be used:

-   When specifying render targets in Quarto projects (see [Render Targets](/docs/projects/quarto-projects.qmd#render-targets)).
-   When defining resources for Quarto websites (see [Site Resources](/docs/websites/website-tools.qmd#site-resources)).
-   When defining documents to include in a listing (see [Listing Contents](/docs/websites/website-listings.qmd#listing-contents)).
-   When automatically creating navigation for sidebars (see [Auto Navigation](/docs/websites/website-navigation.qmd#auto-generation)).

## Glob Syntax

The below is a general reference of the syntax used for globs in Quarto. Note that globs match the filesystem recursively. If you prefer that they don't, then prefix the pattern with a `/` (for example, use `/*.qmd` rather than `*.qmd`).

-   `*` - Matches everything.
-   `{foo,bar}` - Matches `foo` or `bar`.
-   `[abcd]` - Matches `a`, `b`, `c` or `d`.
-   `[a-d]` - Matches `a`, `b`, `c` or `d`.
-   `[!abcd]` - Matches any single character besides `a`, `b`, `c` or `d`.
-   `[[:<class>:]]` - Matches any character belonging to `<class>`.
    -   `[[:alnum:]]` - Matches any digit or letter.
    -   `[[:digit:]abc]` - Matches any digit, `a`, `b` or `c`.
    -   See <https://facelessuser.github.io/wcmatch/glob/#posix-character-classes> for a complete list of supported character classes.
-   `\` - Escapes the next character for an `os` other than `"windows"`.
-   \` - Escapes the next character for `os` set to `"windows"`.
-   `/` - Path separator.
-   `\` - Additional path separator only for `os` set to `"windows"`.
-   `?(foo|bar)` - Matches 0 or 1 instance of `{foo,bar}`.
-   `@(foo|bar)` - Matches 1 instance of `{foo,bar}`. They behave the same.
-   `*(foo|bar)` - Matches *n* instances of `{foo,bar}`.
-   `+(foo|bar)` - Matches *n \> 0* instances of `{foo,bar}`.
-   `!(foo|bar)` - Matches anything other than `{foo,bar}`.
-   `**` - Matches any number of any path segments.
    -   Must comprise its entire path segment in the provided glob.
    -   See <https://www.linuxjournal.com/content/globstar-new-bash-globbing-option>.


# quarto-web/docs/reference/cells/cells-jupyter.qmd

---
title: "Code Cells: Jupyter"
---

[Jupyter](https://jupyter.org) is an open document format that supports computations in many languages including Python, R, and Julia. Learn more about using Jupyter with Quarto in the articles on [Using Python](../../computations/python.qmd) and [Using Julia](../../computations/julia.qmd).

## Overview

Cell options affect the execution and output of executable code blocks. They are specified within comments at the top of a block. For example:

```{{python}}
#| label: fig-polar
#| echo: false
#| fig-cap: "A line plot on a polar axis"
```


# quarto-web/docs/reference/cells/index.qmd

---
title: Code Cells
toc: false
anchor-sections: false
listing:
  id: reference-links
  template: ../../../ejs/links.ejs
  contents: ./reference.yml
---

The options available in an executable code cell depend on the engine used to process them. The engine is chosen automatically, as outlined in the [Guide](https://quarto.org/docs/computations/execution-options.html#engine-binding).

::: {#reference-links .column-screen-inset-right style="max-width: 850px;"}
:::


# quarto-web/docs/reference/cells/cells-knitr.qmd

---
title: "Code Cells: Knitr"
---

[Knitr](https://yihui.org/knitr/) is an R package for dynamic document generation. Learn more about using Knitr in the article on [Using R](../../computations/r.qmd).

## Overview

Cell options affect the execution and output of executable code blocks. They are specified within comments at the top of a block. For example:

``` {{r}}
#| label: fig-polar
#| echo: false
#| fig-cap: "A line plot on a polar axis"
```


# quarto-web/docs/reference/cells/cells-ojs.qmd

---
title: "Code Cells: Observable JS"
---

[Observable JS](https://observablehq.com/@observablehq/observables-not-javascript) is a set of enhancements to vanilla JavaScript created by [Mike Bostock](https://en.wikipedia.org/wiki/Mike_Bostock) (also the author of [D3](https://d3js.org/)). Observable JS is distinguished by its [reactive runtime](https://github.com/observablehq/runtime), which is especially well suited for interactive data exploration and analysis.

Learn more about using Observable JS with Quarto in the articles on [Interactive Documents with Observable JS](../../interactive/ojs/index.qmd).

## Overview

Cell options affect the execution and output of executable code blocks. They are specified within comments at the top of a block. For example:

```{{ojs}}
//| label: fig-polar
//| echo: false
//| fig-cap: "A line plot on a polar axis"
```


# quarto-web/docs/reference/formats/opml.qmd

---
title: "OPML Options"
spec: https://en.wikipedia.org/wiki/OPML
---

OPML (Outline Processor Markup Language) is an XML format for outlines. To learn more about OPML see <https://en.wikipedia.org/wiki/OPML>.


# quarto-web/docs/reference/formats/rtf.qmd

---
title: "RTF Options"
spec: https://en.wikipedia.org/wiki/Rich_Text_Format
---

The Rich Text Format (RTF) is a proprietary document file format with published specification developed by Microsoft Corporation from 1987 until 2008 for cross-platform document interchange with Microsoft products. Learn more about RTF at <https://en.wikipedia.org/wiki/Rich_Text_Format>.


# quarto-web/docs/reference/formats/docx.qmd

---
title: "MS Word Options"
spec: https://en.wikipedia.org/wiki/Office_Open_XML
search: true
---

MS Word is the word processor included with Microsoft Office. Word uses the OpenXML document format, which you can learn more about at <https://en.wikipedia.org/wiki/Office_Open_XML>.

See the MS Word format [user guide](../../output-formats/ms-word.qmd) for more details on creating MS Word output with Quarto.


# quarto-web/docs/reference/formats/org.qmd

---
title: "Emacs Org-Mode Options"
spec: https://orgmode.org/
---

Org-Mode is an Emacs major mode for keeping notes, authoring documents, computational notebooks, literate programming, maintaining to-do lists, planning projects, and more. To learn more about Org-Mode see <https://orgmode.org/>.


# quarto-web/docs/reference/formats/ms.qmd

---
title: "Groff Manuscript Options"
spec: hhttps://www.gnu.org/software/groff/groff.html
---

The Groff (GNU troff) manuscript format consists of plain text mixed with formatting commands that produces PostScript, PDF, or HTML. Learn more about Groff at <https://www.gnu.org/software/groff/groff.html>.


# quarto-web/docs/reference/formats/rst.qmd

---
title: "reStructuredText Options"
spec: https://docutils.sourceforge.io/rst.html
---

reStructuredText is an easy-to-read, what-you-see-is-what-you-get plaintext markup syntax and parser system. It is useful for in-line program documentation (such as Python docstrings), for quickly creating simple web pages, and for standalone documents. You can learn more about reStructuredText at <https://docutils.sourceforge.io/rst.html>.


# quarto-web/docs/reference/formats/fb2.qmd

---
title: "FictionBook Options"
spec: https://en.wikipedia.org/wiki/FictionBook
---

FictionBook is an open XML-based e-book format. You can learn more about FictionBook at <https://en.wikipedia.org/wiki/FictionBook>.


# quarto-web/docs/reference/formats/tei.qmd

---
title: "TEI Options"
spec: https://github.com/TEIC/TEI-Simple
---

TEI Simple aims to define a new *highly-constrained* and *prescriptive* subset of the Text Encoding Initiative (TEI) Guidelines suited to the representation of early modern and modern books, a formally-defined set of processing rules which permit modern web applications to easily present and analyze the encoded texts, mapping to other ontologies, and processes to describe the encoding status and richness of a TEI digital text. Learn more about TEI at <https://github.com/TEIC/TEI-Simple>.


# quarto-web/docs/reference/formats/ipynb.qmd

---
title: "Jupyter Notebook Options"
spec: https://nbformat.readthedocs.io/
---

Jupyter Notebooks are used to combine software code, computational output, explanatory text and multimedia resources in a single document. Learn more about the Jupyter Notebook format at <https://nbformat.readthedocs.io/>.


# quarto-web/docs/reference/formats/docbook.qmd

---
title: "DocBook Options"
spec: https://www.docbook.org/
---

DocBook is an XML schema particularly well suited to books and papers about computer hardware and software (though it is by no means limited to these applications). You can learn more about DocBook at <https://www.docbook.org/>.


# quarto-web/docs/reference/formats/odt.qmd

---
title: "OpenDocument Options"
spec: https://en.wikipedia.org/wiki/OpenDocument
---

OpenDocument, is an open standard file format for word processing documents It was developed with the aim of providing an open, XML-based file format specification for office applications. To learn more about OpenDocument see <https://en.wikipedia.org/wiki/OpenDocument>.


# quarto-web/docs/reference/formats/epub.qmd

---
title: "ePub Options"
spec: https://en.wikipedia.org/wiki/EPUB
---

ePub is an e-book file format that is supported by many e-readers, and compatible software is available for most smartphones, tablets, and computers. You can learn more about ePub at <https://en.wikipedia.org/wiki/EPUB>.


# quarto-web/docs/reference/formats/pdf.qmd

---
title: "PDF Options"
spec: https://en.wikipedia.org/wiki/PDF
search: true
---

Portable Document Format (PDF) is a file format developed by Adobe in 1992 to present documents, including text formatting and images, in a manner independent of application software, hardware, and operating systems. To learn more about PDF see <https://en.wikipedia.org/wiki/PDF>.

See the PDF format [user guide](../../output-formats/pdf-basics.qmd) for more details on creating PDF output with Quarto.


# quarto-web/docs/reference/formats/icml.qmd

---
title: "InDesign Options"
spec: https://wwwimages.adobe.com/content/dam/acom/en/devnet/indesign/sdk/cs6/idml/idml-specification.pdf
---

ICML is an XML representation of an Adobe InDesign document. You can learn more about ICML at <https://wwwimages.adobe.com/content/dam/acom/en/devnet/indesign/sdk/cs6/idml/idml-specification.pdf>.


# quarto-web/docs/reference/formats/dashboards.qmd

---
title: "Dashboard Options"
tbl-colwidths: [25,75]
---

## Format

The following document and format options are either dashboard-specific or have special behavior within dashboards (note that in addition to these options all standard [HTML Format](/docs/reference/formats/html.qmd) options are available):

| Option        | Description                                                                                                                                                                                                     |
|--------------------------|----------------------------------------------|
| `title`       | Title (displayed in top left of navigation bar)                                                                                                                                                                 |
| `author`      | Author (displayed alongside title in smaller font)                                                                                                                                                              |
| `logo`        | Logo (displayed left of the title in the navigation bar)                                                                                                                                                        |
| `orientation` | `rows` or `columns` (default: `rows`)                                                                                                                                                                           |
| `scrolling`   | Use scrolling rather than fill layout? (default: `false`)                                                                                                                                                       |
| `expandable`  | Make card content expandable (default: `true`)                                                                                                                                                                  |
| `theme`       | Dashboard theme (built in or custom scss)                                                                                                                                                                       |
| `nav-buttons` | Buttons to appear on the right side of the navigation bar. Use `linkedin`, `facebook`, `reddit`, `twitter`, `github`, or a custom [Nav Item](/docs/reference/projects/websites.html#nav-items). |


For example:

``` yaml
---
title: "Dashboard"
author: "Acme, Inc."
logo: images/acme.png
format:
  dashboard:
     theme: default
     orientation: rows
     expandable: true
     scrolling: false
     nav-buttons:
      - reddit
      - icon: gitlab
        href: https://gitlab.com/
---
```

## Pages

[Pages](/docs/dashboards/components.qmd#pages) can specify a custom orientation that is distinct from the global orientation:

| Option        | Description                                         |
|---------------|-----------------------------------------------------|
| `orientation` | `rows` or `columns` (default to global orientation) |

For example:

``` {.python .pymd}
---
title: "Dashboard"
format: dashboard
---

# Plots {orientation="columns"}
```

## Sidebars

Create [Sidebars](/docs/dashboards/components.qmd#sidebars) by applying the `.sidebar` attribute to a level 1 heading (for global sidebars) or level 2 heading (for page level sidebars).

| Class      | Description                                 |
|------------|---------------------------------------------|
| `.sidebar` | Contents should be arranged into a sidebar  |

For example:

``` {.python .pymd}
---
title: "Dashboard"
format: dashboard
---

# Plots {.sidebar}
```

## Rows & Columns

Rows and columns support options for customizing their layout and sizing behavior. The following classes can be used to modify layout behavior:

| Class     | Description                                                                           |
|--------------------|----------------------------------------------------|
| `.tabset` | Contents should be arranged into a [Tabset](/docs/dashboards/components.qmd#tabsets)  |
| `.fill`   | Contents should fill available layout space                                           |
| `.flow`   | Contents should flow to their natural size                                            |

Note that in most dashboards, `.fill` and `.flow` are determined automatically based on the contents of cards and don't need to be specified manually.

The following attributes can be used for explicit sizing:

| Option   | Description                                                                                         |
|--------------------------|----------------------------------------------|
| `width`  | Percentage or absolute pixel width (default distributes space evenly across elements in a row)      |
| `height` | Percentage or absolute pixel height (default distributes space evenly across elements in a column)  |

For example:

``` {.python .pymd}
---
title: "Dashboard"
format: dashboard
---

## Row {height="65%"}

## Row {height="35%"}
```

Note that if some components specify an explicit `width` or `height` and others do not, then remaining space will be distributed evenly across those elements.

## Cards

Card options enable you to specify a title and various layout behaviors:

| Option       | Description                                                                                        |
|--------------------------|----------------------------------------------|
| `title`      | Title displayed in card header                                                                     |
| `padding`    | Padding around card content (default: `8px`)                                                       |
| `expandable` | Make card content expandable (default: `true`)                                                     |
| `width`      | Percentage or absolute pixel width (default distributes space evenly across elements in a row)     |
| `height`     | Percentage or absolute pixel height (default distributes space evenly across elements in a column) |

For example:

```` {.python .pymd}
```{{python}}
#| title: "Life Expectancy"
#| padding: 3px
#| expandable: false
#| width: 70%
```
````

These same options can be applied to `.card` divs. For example:

``` {.python .pymd}
::: {.card title="Life Expectancy" padding="3px"}
This is the content.
:::
```

## Value Boxes

[Value Boxes](/docs/dashboards/data-presentation.qmd#value-boxes) support the following options:

| Option  | Description                                                                                          |
|--------------------------|----------------------------------------------|
| `title` | Title displayed above value                                                                          |
| `icon`  | Icon identifier from [bootstrap icons](https://icons.getbootstrap.com)                               |
| `color` | Background color---this can be any CSS color or one of the theme specific color aliases (see below)  |
| `value` | Main display value                                                                                   |

Available themed aliases for `color` include:

{{< include /docs/dashboards/_valuebox-colors.md >}}

Note that value box options can be specified either as cell options or by printing a `dict()` (for Python) or `list()` (for R) (this is helpful when options need to be dynamic). See the [Value Boxes](/docs/dashboards/data-presentation.qmd#value-boxes) component documentation for details.

# quarto-web/docs/reference/formats/context.qmd

---
title: "Context Options"
spec: http://www.pragma-ade.nl/
---

Context is a system for typesetting documents based on TEX and METAPOST. You can learn more about Context at <http://www.pragma-ade.nl/>.


# quarto-web/docs/reference/formats/asciidoc.qmd

---
title: "AsciiDoc Options"
spec: https://asciidoc.org/
---

AsciiDoc is a text document format for writing documentation, articles, and books, ebooks, slideshows, web pages, man pages and blogs. You can learn more about AsciiDoc at <https://asciidoc.org/>.

``` yaml
format: asciidoc
format: asciidoctor
```

::: callout-note
## Asciidoc vs Asciidoctor Format

Pandoc includes support for both the `asciidoc` and `asciidoctor` formats. The `asciidoc` format produces older style syntax that is no longer typically used, while the `asciidoctor` format produces the more current markdown syntax that is part of the formal AsciiDoc specification.

In Quarto, both `asciidoc` and `asciidoctor` are aliases for the `asciidoctor` format.
:::

# quarto-web/docs/reference/formats/man.qmd

---
title: "Groff Man Page Options"
spec: https://www.gnu.org/software/groff/groff.html
---

The Groff (GNU troff) man page document formats consists of plain text mixed with formatting commands that produce ASCII/UTF8 for display at the terminal. Learn more about Groff at <https://www.gnu.org/software/groff/groff.html>.


# quarto-web/docs/reference/formats/haddock.qmd

---
title: "Haddock Options"
spec: https://haskell-haddock.readthedocs.io/
---

Haddock is a tool for automatically generating documentation from annotated Haskell source code. You can learn more about Haddock at <https://haskell-haddock.readthedocs.io/>.



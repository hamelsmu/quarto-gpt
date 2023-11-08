# quarto-web/docs/blog/posts/2023-05-22-quarto-for-academics/index.qmd

---
title: Quarto for Academics
subtitle: A potpourri of Quarto features useful for academics
description: |
  A video highlighting some of Quarto's features that are especially useful for academics, as educators and as researchers.
categories:
  - Learn
author: Mine Çetinkaya-Rundel
date: "05/22/2023"
image: "quarto-for-academics-video-cover.png"
image-alt: "Quarto logo on a blue background and the title of the video - Quarto for Academics"
---

Quarto offers a myriad of features that are especially useful for academics, as educators and as researchers. These range from chunk options that enable automatic linking of code to documentation, to article templates for manuscript submission to multiple journals. The following video walks you through some of these features.

{{< video "https://www.youtube.com/embed/EbAAmrB0luA" >}}

Select highlights include:

-   Linking to documentation from code with [`code-link`](/docs/output-formats/html-code.html#code-linking).
-   Informative YAML errors and YAML completion.
-   Creating Quarto slides with [revealjs](/docs/presentations/revealjs/).
-   [PDF export](/docs/presentations/revealjs/presenting.html#print-to-pdf) of HTML slides.
-   Annotating slides with [`chalkboard`](/docs/presentations/revealjs/presenting.html#chalkboard).
-   Advancing slides for your audience with [`multiplex`](/docs/presentations/revealjs/presenting.html#multiplex).
-   Highlighting code with [`code-line-numbers`](/docs/presentations/revealjs/#line-highlighting).
-   Customizing output location with [`output-location`](/docs/presentations/revealjs/index.html#output-location).
-   Showing code chunk fences with [`echo: fenced`](/docs/computations/execution-options.html#fenced-echo).
-   [Code annotation](/docs/authoring/code-annotation.html).
-   Authoring manuscripts with Quarto [journal templates](/docs/journals/index.html).
-   [Inserting citations](/docs/visual-editor/technical.html#citations) from Zotero or from a DOI with the [RStudio Visual Editor](/docs/visual-editor/).

If you would like to follow along as you watch, you can find the source code for everything created in the video in [this GitHub repository](https://github.com/mine-cetinkaya-rundel/quarto-for-academics).


# quarto-web/docs/blog/posts/2023-03-15-multi-format/index.qmd

---
title: Multi-format Publishing
subtitle: Automatically link to other formats in HTML documents
description: |
  In Quarto 1.3, additional formats listed in HTML documents will automatically be linked in an "Other Formats" section near the top of the page.
categories:
  - Features
  - Authoring
  - Quarto 1.3
author: Charlotte Wickham
date: "03/15/2023"
image: multi-format.png
image-alt: "Screenshot of a Quarto webpage showing a section entitled 'Other Formats' with items Jupyter and MS Word"
format:
  html: default
  ipynb: default
  docx: default
---

{{< include ../_quarto-1.3-feature.qmd >}}

Starting in Quarto 1.3, HTML pages (either standalone or in a website) can automatically include links to other formats specified in the document front matter. For example, the following document front matter:

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

![](other-format.png){.border fig-alt="Screenshot of a HTML page that includes a link to the Jupyter format below the table of contents under the heading Other Formats."}

If a table of contents is enabled for the page, the additional formats will be automatically placed within the table of contents as a new section. If no table of contents is displayed, the additional formats will be displayed in the right margin at the top of the document.

Links to additional formats are displayed by default, but you can control whether they are shown or even which specific formats are included with the `format-links` YAML option.

Read more about this feature on the [Multi-format page](/docs/prerelease/1.3/multi-format.html) of the pre-release highlights.


# quarto-web/docs/blog/posts/2023-03-13-code-annotation/index.qmd

---
title: Code Annotation
subtitle: Add line based annotations to your code chunks
description: |
  In Quarto 1.3, you can add line based annotations to code chunks to highlight or explain parts of your code.
categories:
  - Features
  - Authoring
  - Quarto 1.3
author: Charlotte Wickham
date: "03/13/2023"
image: annotation.png
image-alt: "Screenshot a code chunk with annotations. Annotations appear in the code chunk as numbers within circles, and repeat below the code chunk along with the text content of the annotations."
code-annotations: below
---

{{< include ../_quarto-1.3-feature.qmd >}}

Code blocks and executable code cells in Quarto may now include line-based annotations. Line-based annotations provide a way to attach explanation to lines of code much like footnotes.

For example, this code uses annotation to describe the steps in an R dplyr pipeline in plain language:

``` r
library(tidyverse)
library(palmerpenguins)
penguins |>                                            # <1>
  mutate(                                              # <2>
    bill_ratio = bill_depth_mm / bill_length_mm,       # <2>
    bill_area  = bill_depth_mm * bill_length_mm        # <2>
  )                                                    # <2>
```

1.  Take `penguins`, and then,
2.  add new columns for the bill ratio and bill area.

The default HTML annotation style displays annotations in a list below the code block. Clicking on the annotation number in the list highlights the relevant lines in the code. Other HTML styles hide the annotations, revealing them in a tooltip when a user hovers or selects a marker.

The PDF format also allows for annotations, numbering, and displaying the annotation text below the code. In other formats, like Word and GitHub Markdown, annotations are instead labeled with the line of code (or lines of code) to which the annotation text applies.

::: panel-tabset
#### PDF

![](annote-pdf.png){fig-alt="Screenshot of output in PDF format showing code annotation."}

#### GitHub Flavored Markdown

```` markdown
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

To add code annotation to a code block, you need to add two things: specially formatted code comments in your code cell, and an ordered list below the code cell with the annotation text:

1.  **Code Comments**: Each annotated line in the code cell should be terminated with a comment (using the code cell's language comment character) followed by a space and then an annotation number enclosed in angle brackets (e.g. `# <2>`). You may repeat an annotation number if the annotation spans multiple lines.

2.  **Ordered List**: An ordered list should appear immediately after the code cell, and include the contents of each annotation. Each numbered item in the ordered list will correspond to the line(s) of code with the same annotation number.

For example, the annotations above were produced by including the following in the Quarto document:

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

You can read more about how to control the annotation style, and whether annotations appear at all on the [Code Annotation page](/docs/prerelease/1.3/code-annotation.html) of the pre-release highlights.


# quarto-web/docs/blog/posts/2023-05-15-get-started/index.qmd

---
title: Get Started with Quarto
subtitle: A video to jumpstart your Quarto journey
description: |
  A new video for getting started with Quarto using R and RStudio.
categories:
  - Learn
author: Mine Çetinkaya-Rundel
date: "05/15/2023"
image: "get-started-video-cover.png"
image-alt: "Quarto logo on a blue background and the title of the video - Get started with Quarto"
---

Have you been hearing about Quarto but didn't give it a try yet? Perused the [Get Started](/docs/get-started/) pages but would like another intro? Or have about 20 minutes to spare and want to pick up a few Quarto tips? You've come to the right place!

{{< video "https://www.youtube.com/embed/_f3latmOhew" >}}

In this video, I walk you through creating documents, presentations, and websites and publishing with Quarto. The video features authoring Quarto documents with executable R code chunks using the [RStudio Visual Editor](/docs/visual-editor/).

Select highlights include:

-   Inserting [cross references](/docs/authoring/cross-references.html) to tables and figures
-   Adding a [citation](/docs/visual-editor/technical.html#citations) from a DOI
-   Seamlessly switching between output formats as well as creating [multi-format documents](/docs/output-formats/html-multi-format.html)
-   Customizing the [output location](/docs/presentations/revealjs/#output-location) of code in presentations
-   Creating a [website](/docs/websites/) from scratch
-   Publishing the website to [QuartoPub](/docs/publishing/quarto-pub.html)

If you would like to follow along as you watch the video, you can find the source code for everything created in the video in [this GitHub repository](https://github.com/mine-cetinkaya-rundel/get-started-quarto) and the published [website on QuartoPub](https://mine.quarto.pub/welcome-to-quarto/).


# quarto-web/docs/extensions/listing-formats.qmd

---
title: "Quarto Extensions"
listing: 
  id: listing-formats
  contents: 
    - listings/custom-formats.yml
    - listings/revealjs-formats.yml
metadata-files: 
  - listings/_metadata.yml
---

{{< include _listing-preamble.qmd >}}

### Custom Formats {.unlisted}

::: {#listing-formats .column-body-outset-right}
:::

{{< include _listing-footer.qmd >}}




# quarto-web/docs/extensions/_shortcode-escaping.qmd

## Escaping

If you are writing documentation about using variable shortcodes (for example, this article!) you might need to prevent them from being processed. You can do this in two ways:

1.  Escape the shortcode reference with extra braces like this:

    ``` {.default shortcodes="false"}
    {{{< var version >}}}
    ```

2.  Add a `shortcodes=false` attribute to any code block you want to prevent processing of shortcodes within:

    ```` default
    ```{{shortcodes=false}}
    {{{< var version >}}}
    ```
    ````


# quarto-web/docs/extensions/filters.qmd

---
title: "Creating Filters"
aliases: 
  - /docs/authoring/shortcodes-and-filters.qmd
  - /docs/authoring/filters.qmd
---

{{< include _extension-version.qmd >}}

## Overview

If the base features of Pandoc and Quarto don't do exactly what you need, you can very likely create a [Pandoc Filter](https://pandoc.org/filters.html) that bridges the gap.

Pandoc consists of a set of readers and writers. When converting a document from one format to another, text is parsed by a reader into pandoc's intermediate representation of the document---an "abstract syntax tree" or AST---which is then converted by the writer into the target format. The pandoc AST format is defined in the module [`Text.Pandoc.Definition`](https://hackage.haskell.org/package/pandoc-types-1.22/docs/Text-Pandoc-Definition.html) in the pandoc-types package.

A "filter" is a program that modifies the AST, between the reader and the writer.

    INPUT --reader--> AST --filter--> AST --writer--> OUTPUT

Pandoc's built-in citation processing is implemented as a filter, as are many of Quarto's internal extensions (e.g. cross-references, figure layout, etc.).

You can write Pandoc filters using Lua (via Pandoc's built-in Lua interpreter) or using any other language using a JSON representation of the Pandoc AST piped to/from an external process. We strongly recommend using Lua Filters, which have the following advantages:

-   No external dependencies
-   High performance (no serialization or process execution overhead)
-   Access to the [Pandoc](https://pandoc.org/lua-filters.html#pandoc-module) and [Quarto](lua.qmd) libraries of Lua helper functions.

## Activating Filters

If you've developed a filter and want to use it within a document you need to add it to the list of `filters` for the document. For example, here we arrange for the [spellcheck](https://github.com/pandoc/lua-filters/tree/master/spellcheck) filter to run:

``` yaml
---
filters:
  - spellcheck.lua
---
```

By default, user filters are run before Quarto's built-in filters. For some filters you'll want to modify this behavior. For example, here we arrange to run `spellcheck` before Quarto's filters and `lightbox` after:

``` yaml
filters:
  - spellcheck.lua
  - quarto
  - lightbox
```

You'll notice that one of the extensions (`spellcheck.lua`) has a file extension and the other (`lightbox`) does not. This difference stems from how the extensions are distributed: an extension distributed as a plain Lua file uses `.lua` whereas a filter distributed as a [Quarto Extension](index.qmd) does not. The next section explores how to create filters as extensions.


## Filter Extensions 

### Quick Start

Here we'll describe how to create a simple filter extension. We'll use the `quarto create` command to do this. If you are using VS Code or RStudio you should execute `quarto create` within their respective integrated Terminal panes. 

To get started, execute `quarto create extension filter` within the parent directory where you'd like the filter extension to be created:

```{.bash filename="Terminal"}
$ quarto create extension filter
 ? Extension Name › fancy-header
```

As shown above, you'll be prompted for an extension name. Type `fancy-header` and press Enter---the filter extension is then created:

```bash
Creating extension at /Users/jjallaire/quarto/dev/fancy-header:
  - Created README.md
  - Created _extensions/fancy-header/_extension.yml
  - Created _extensions/fancy-header/fancy-header.lua
  - Created .gitignore
  - Created example.qmd
```

If you are running within VS Code or RStudio a new window will open with the extension project. 

Here's what the contents of the files in `_extensions/fancy-header/` look like:

``` {.yaml filename="_extensions/fancy-header/_extension.yml"}
title: Fancy-header
author: J.J. Allaire
version: 1.0.0
quarto-required: ">=99.9.0"
contributes:
  filters:
    - fancy-header.lua
```

``` {.lua filename="_extensions/fancy-header/fancy-header.lua"}
-- Reformat all heading text 
function Header(el)
  el.content = pandoc.Emph(el.content)
  return el
end
```

Finally, the `example.qmd` file includes code that exercises the extension. For example:

``` {.markdown filename="example.qmd"}
---
title: "Fancy-header Example"
filters:
  - fancy-header
---

## Heading

This filter adds formatting to heading text.
```

To develop your filter, render/preview `example.qmd`, and then make changes to `fancy-header.lua` (the preview will automatically refresh when you change `fancy-header.lua`).

### Development

To learn more about developing filter extensions:

1.  If necessary, brush up on [Lua Development](lua.qmd) (Lua is the language used to create filters).

2.  Review the Pandoc documentation on [Writing Lua Filters](https://pandoc.org/lua-filters.html).

3.  Read the [Lua API Reference](lua-api.qmd), which describes the Lua extension API for Quarto.

If you want to write a JSON filter, see the documentation on [Writing JSON filters](https://pandoc.org/filters.html).

To create a new filter extension, use the `quarto create extension filter` command as described above.

### Distribution

if your extension source code it located within a GitHub repository, then it can be added to a project by referencing the GitHub organization and repository name. For example:

``` {.bash filename="Terminal"}
# target the current HEAD of the extension
quarto add cooltools/output-folding

# target a branch or tagged release of the extension
quarto add cooltools/output-folding@v1.2
quarto add cooltools/output-folding@bugfix-22
```

Note that it is possible to bundle and distribute extensions as simple gzip archives (as opposed to using a GitHub repository as described above). See the article on [Distributing Extensions](distributing.qmd) for additional details.

### Examples

You might also find it instructive to examine the source code of these filter extensions authored by the Quarto team:

| **Extension name**                                                   | **Description**                                               |
|--------------------------------------|----------------------------------|
| [latex-environment](https://github.com/quarto-ext/latex-environment) | Quarto extension to output custom LaTeX environments.         |
| [lightbox](https://github.com/quarto-ext/lightbox)                   | Create lightbox treatments for images in your HTML documents. |

: {tbl-colwidths="\[35,65\]"}


# quarto-web/docs/extensions/starter-templates.qmd

---
title: "Starter Templates"

---

{{< include _extension-version.qmd >}}

## Overview

Starter templates provide a straightforward way for users to get started with new Quarto projects by providing example content and options. You might use starter templates to:

1.  Create a working initial document for [Journal Articles](../journals/index.qmd) or [Custom Formats](formats.qmd).

2.  Provide the initial content for a custom [Project Type](project-types.qmd). 

3.  Scaffold a standard form of data analysis project used by your organization.

Starter templates are essentially just GitHub repositories that are copied to a new directory on the user's system. As we'll describe below in [Extensions & Templates], often times the repository for a custom format is also used as a starter template.

## Creating a Template

To create a starter template, just create a GitHub repository that includes the files you want copied into projects created with the template. All of the files in the repository are copied save for:

1.  Hidden files (any file or directory name that starts with `.` (e.g. `.gitignore`).

2.  Common GitHub repository files like `README.md` and `LICENSE`.

If you'd like, you can also include a `.quartoignore` file in the root of your repository listing other files or directories you'd like to exclude. Each line of the file should be a glob describing file(s) to ignore (using syntax like a `.gitignore` file).

### template.qmd

There is one special file you'll typically want to include in templates that target creation of documents (as opposed to projects): `template.qmd`. There are two reasons to include a `template.qmd`:

1. It provides an easy way to test that your template is working as expected.

2. When the template is copied into the target directory, the `template.qmd` will automatically be renamed to match the name that the user provided for the directory.

If you are creating a template that targets creation of a website or book, a `template.qmd` is generally not necessary (as the `index.qmd` file already serves this purpose).

## Using a Template

Once you've created the template repository and pushed it to GitHub, it can be instantiated with the following command:

``` {.bash filename="Terminal"}
quarto use template cooltools/cool-project
```

This command copies the contents of the GitHub repository at `https://github.com/cooltools/cool-project` to the local system (excluding selected files as discussed above).

If the command is run in an empty directory, the user will be prompted whether they'd like to use the existing directory or create a new directory. If the command is run in a directory which contains other files or directories, they'll be prompted for the name of a directory to create.

## Extensions & Templates

When creating [Journal Articles](../journals/index.qmd), [Custom Formats](formats.qmd), or [Project Type](project-types.qmd) extensions, we recommend that you additionally provide a starter template to make it easy for users to get started.

This is generally as easy as adding a `template.qmd` file to your extension that demonstrates its use. With this configuration, users can either begin using your extension via the template or by a conventional `quarto install` of the extension. 

For example, consider the [ACM](https://github.com/quarto-journals/acm) Journal Article extension. The extension repository supports _either_ getting started with a template:

```{.bash filename="Terminal"}
quarto use template quarto-journals/acm
```

Alternatively, you can add the format (without the template) into an existing project or directory:

```{.bash filename="Terminal"}
quarto add quarto-journals/acm
```





# quarto-web/docs/extensions/listing-journals.qmd

---
title: "Quarto Extensions"
listing: 
  id: listing-journals
  contents: listings/journal-articles.yml
metadata-files: 
  - listings/_metadata.yml
---

{{< include _listing-preamble.qmd >}}

### Journal Articles {.unlisted}

::: {#listing-journals .column-body-outset-right}
:::

{{< include _listing-footer.qmd >}}



# quarto-web/docs/extensions/lua.qmd

---
title: Lua Development
resources: 
  - luarefv51.pdf
---

{{< include _extension-version.qmd >}}

## Overview

The programming language used to create [filters](filters.qmd) and [shortcodes](shortcodes.qmd) is Lua, a lightweight, high-level scripting language. [Lua](https://www.lua.org/) is the extension language for Pandoc (which includes an embedded Lua interpreter). This means that Quarto extensions have no additional runtime dependencies or requirements.

This article will start by providing an orientation to learning Lua for those new to the language. Then, we'll provide some tips for productive Lua development.

See the [Lua API Reference](lua-api.qmd) for additional details on the APIs available for developing extensions.

## Learning Lua

Lua is a scripting language similar to Python, R, Julia, and JavaScript. If you are familiar with one or more of those languages you won't have trouble picking up Lua.

Here is a recommended approach for learning Lua for use with Quarto:

1.  Read [Learn Lua in 15 Minutes](https://learnxinyminutes.com/docs/lua/) for a quick overview of the language and its syntax.

2.  Check out the first two sections of the [Pandoc Lua Filters](https://pandoc.org/lua-filters.html) documentation then skip ahead to the [Filter Examples](https://pandoc.org/lua-filters.html#macro-substitution) section to make things a bit more concrete.

3.  Once you have the basic idea of Lua and filters, get a more complete picture by skimming the full [Pandoc Lua Filters](https://pandoc.org/lua-filters.html) documentation. You won't understand everything, but its a good orientation to all of the moving parts.

4.  Finally, check out the source code of the extensions published in the [Quarto Extensions](https://github.com/quarto-ext) GitHub organization (these are extensions maintained by the Quarto core team). Once you are able to read and understand that code you are ready to start developing your own extensions!

Some additional learning resources you might find useful include:

1.  [Lua Quick Reference](luarefv51.pdf), a PDF with a compact summary of the language and base library.

2.  [Programming in Lua](https://www.amazon.com/exec/obidos/ASIN/8590379868/lua-pilindex-20), a book by Roberto Ierusalimschy, the chief architect of the language.

3.  [Lua Reference Manual](https://www.lua.org/manual/5.3/), a complete definition of the language and base library.

## Development Tools

### Quarto Preview

Quarto preview, `quarto preview`, is aware of Lua source files within extensions, and will automatically reload the preview whenever a Lua source file changes.

This makes it very easy to incrementally develop and debug Lua code (especially when combined with the [native](#native-format) format a described below). Live reloading for Lua files will work no matter what source code editor you are using (VS Code, RStudio, Neovim, etc.).

### VS Code

While you can use any text editor along with `quarto preview` for developing Lua extensions, we strongly recommend that you consider using VS Code, as it provides a number of additional tools including:

1.  Code completion and type checking.

2.  Diagnostics for various common problems with code.

3.  The ability to add types to your own functions.

Code completion covers the Lua base library as well as the Pandoc and Quarto Lua APIs, and also provides documentation on hover:

![](images/vscode-lua-completions.png){.border fig-alt="Screenshot of Lua file open in VS Code with code completion popup showing for Lua function." width="95%"}

Diagnostics check for many common errors including failing to check for `nil`, undefined global values, shadowing of local variables, unused functions, etc.

![](images/vscode-lua-diagnostics.png){.border fig-alt="Screenshot of Lua file open in VS Code with diagnostic errors shown in Problems pane below the code editor." width="95%"}

#### Installation

To get started with using VS Code for Lua extension development, install the following software:

1.  Install the latest version (v1.2 or greater) of [Quarto](https://quarto.org/docs/download/)

2.  Install the latest version (v1.40.0 or greater) of the [Quarto VS Code Extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto).

3.  For Lua code intelligence, install the [Lua LSP VS Code Extension](https://marketplace.visualstudio.com/items?itemName=sumneko.lua).

Once you've installed these components you should see the features described above appear automatically in your Quarto workspaces that include Lua code.

There are many options available for configuring Lua completion and diagnostics. It's also possible to provide type information for your own functions. See the section on [Lua in VS Code](#lua-in-vs-code) below for details.

## Diagnostic Logging

Use the functions in the `quarto.log` module to add diagnostic logging to your extension. You can use both temporary logging calls to debug a particular problem as well as add logging calls that are always present but only activated when the `--trace` flag is passed to `quarto render` or `quarto preview`.

The `quarto.log` module is based on the [pandoc-lua-logging](https://github.com/wlupton/pandoc-lua-logging) project from [\@wlupton](https://github.com/wlupton). You'll recognize the functions described below from that module (e.g. `logging.output()`, `logging.warning()`, etc). For documentation on using all of the logging functions see the project [README](https://github.com/wlupton/pandoc-lua-logging) file.

### quarto.log.output

To log any object (including Pandoc AST elements), you the `quarto.log.output()` function. For example, here we log the `Div` passed to us in our filter callback function as well as some diagnostic text:

``` {.lua filename="filter.lua"}
function Header(el)
  quarto.log.output("=== Handling Header ===")
  quarto.log.output(el)
end
```

This is log output you'd see in the terminal when the filter is executed:

``` default
=== Handling Header ===
Header {
  attr: Attr {
    attributes: AttributeList {}
    classes: List {}
    identifier: "section-one"
  }
  content: Inlines {
    [1] Str "Section"
    [2] Space
    [3] Str "One"
  }
  level: 2
}
```

### quarto.log.warning

Use the `quarto.log.warning()` function to output warnings that can be suppressed with the `--quiet` flag:

``` {.lua filename="filter.lua"}
function RawBlock(el)
  if el.format == "html" then
    quarto.log.warning("Raw HTML not supported")
    return pandoc.Null()
  end
end
```

For example, the warning above will not appear for this call to `quarto render`:

``` bash
quarto render document.qmd --quiet
```

### quarto.log.debug

Use the `quarto.log.debug()` function to write output whenever the `--trace` flag is present:

``` {.lua filename="filter.lua"}
function Header(el)
  quarto.log.debug("Header: " .. el.identifier)
end
```

For example, the debug message will appear for this call to `quarto preview`:

``` bash
quarto preview document.qmd --trace
```

You can keep these calls in your filter since they won't produce output unless `--trace` is specified.

## Native Format {#native-format}

A great tool for understanding the behavior of a Lua filter or shortcode in more depth is to target the `native` format (as opposed to `html`, `pdf`, etc.). The `native` format will show you the raw contents of the Pandoc AST. For example, here's a simple markdown document alongside it's `native` output:

::: {layout-ncol="2"}
<div>

``` {.markdown filename="document.qmd"}
---
format: native
---

## Heading

Some text below




```

</div>

<div>

``` border
Pandoc
  Meta
    { unMeta = fromList [] }
  [ Header
      2
      ( "heading" , [] , [] )
      [ Str "Heading" ]
  , Para
      [ Str "Some"
      , Space
      , Str "text"
      , Space
      , Str "below"
      ]
  ]
```

</div>
:::

Here we add a simple filter to the document that wraps all headers in `pandoc.Emph` (italics). You can see that the `Emph` AST element now wraps the heading text in the `native` output:

::: {layout-ncol="2"}
<div>

``` {.markdown filename="document.qmd"}
---
format: native
filters: [filter.lua]
---

## Heading

Some text below
```

``` {.lua filename="filter.lua"}
function Header(el)
  el.content = { 
    pandoc.Emph(el.content)
  }
  return el
end
```

</div>

::: {.font-monospace .border}
::: {style="font-size: 0.875em; padding: 4px;"}
| Pandoc
|   Meta
|     { unMeta = fromList \[\] }
|   \[ Header
|       2
|       ( "heading" , \[\] , \[\] )
|       **\[ Emph \[ Str "Heading" \]**
|       \]
|   , Para
|       \[ Str "Some"
|       , Space
|       , Str "text"
|       , Space
|       , Str "below"
|       \]
|   \]
| 
| 
| 
:::
:::
:::

## Lua in VS Code {#lua-in-vs-code}

### Type Hints

While Quarto provides type information for the Pandoc and Quarto Lua APIs, this doesn't cover functions that you write within your own extensions. You can however add type information using [Annotations](https://github.com/sumneko/lua-language-server/wiki/Annotations). For example, here we indicate that a function takes a `string` and a `pandoc.List()` and returns either a `pandoc.List()` or `nil`:

``` lua
---@param text string
---@param blocks pandoc.List
---@return pandoc.List|nil
function check_for_text(text, blocks)
  -- implementation
end
```

With these type declarations, any attempt to call the function without the correct types will result in a diagnostic message. Further, if a caller fails to check for `nil` before using the return value a diagnostic will also occur.

You can learn more about all of the available type annotations in the [Annotations Reference](https://github.com/sumneko/lua-language-server/wiki/Annotations) for the Lua Language Server.

### Settings

The [Lua Language Server](https://marketplace.visualstudio.com/items?itemName=sumneko.lua) extension includes a wide variety of options to customize its behavior (e.g. what diagnostics to show, which completions to offer, etc.).

All of the available options are documented in the [Settings Reference](https://github.com/sumneko/lua-language-server/wiki/Settings) for the Lua Language Server.

Quarto provides a default configuration file (`.luarc.json`) within the root of any workspace that includes Quarto Lua extensions. This file is necessary because it provides a reference to the Lua type definitions for Pandoc and Quarto within your currently installed version of Quarto. Without it, the Lua extension wouldn't know anything about Quarto and would report errors for "unknown" Pandoc modules.

If, for example, Quarto is installed at `/opt/quarto/`, the default contents of the configuration file will be:

``` {.json filename=".luarc.json"}
{
  "Generator": ["Quarto"],
  "Lua.runtime.version": "Lua 5.3",
  "Lua.workspace.checkThirdParty": false,
  "Lua.workspace.library": ["/opt/quarto/share/lua-types"],
  "Lua.runtime.plugin": "/opt/quarto/share/lua-plugin/plugin.lua",
  "Lua.completion.showWord": "Disable",
  "Lua.completion.keywordSnippet": "Both",
  "Lua.diagnostics.disable": ["lowercase-global", "trailing-space"]
}
```

The `.luarc.json` file will also be automatically added to `.gitignore` since it points to the absolute path of Quarto on the local system.

You can change any of the settings within this file save for the `Lua.workspace.library` and `Lua.runtime.plugin` (these are automatically maintained by the Quarto extension based on where Quarto is installed). See the [Settings Reference](https://github.com/sumneko/lua-language-server/wiki/Settings) for all available settings.

If you prefer to mange this file manually, simply remove the `Generator` key and Quarto will no longer update the `Lua.workspace.library` and `Lua.runtime.plugin` settings automatically.

You can also globally disable the automatic creation of `.luarc.json` using the **Quarto \> Lua: Provide Types** VS Code setting.


# quarto-web/docs/extensions/shortcodes.qmd

---
title: "Creating Shortcodes"
aliases: 
  - /docs/authoring/shortcodes.qmd
---

{{< include _extension-version.qmd >}}

## Overview

Shortcodes are special markdown directives that generate various types of content. Quarto shortcodes are similar in form and function to [Hugo shortcodes](https://gohugo.io/content-management/shortcodes/) and [WordPress shortcodes](https://codex.wordpress.org/Shortcode).

For example, the following shortcode prints the `title` from document metadata:

``` {.markdown shortcodes="false"}
{{< meta title >}}
```

Quarto supports several shortcodes natively:

| Shortcode                                                 | Description                            |
|-------------------------------------|-----------------------------------|
| [var](../authoring/variables.qmd#var)                     | Print value from `_variables.yml` file |
| [meta](../authoring/variables.qmd#meta)                   | Print value from document metadata     |
| [env](../authoring/variables.qmd#url)                     | Print system environment variable      |
| [pagebreak](../authoring/markdown-basics.qmd#page-breaks) | Insert a native page-break             |
| [kbd](../authoring/markdown-basics.qmd#keyboard-shortcuts) | Describe keyboard shortcuts            |
| [video](/docs/authoring/videos.qmd)                       | Embed a video in a document            |
| [include](../authoring/includes.qmd)                      | Include contents of another qmd        |
| [embed](../authoring/notebook-embed.qmd)                  | Embed cells from a Jupyter Notebook    |

This article describes how to create your own shortcodes.

## Quick Start

Here we'll describe how to create a simple shortcode extension. We'll use the `quarto create` command to do this. If you are using VS Code or RStudio, you should execute `quarto create` within their respective integrated terminal panes. 

To get started, execute `quarto create extension shortcode` within the parent directory where you'd like the shortcode extension to be created:

```{.bash filename="Terminal"}
$ quarto create extension shortcode
 ? Extension Name › shorty
```

As shown above, you'll be prompted for an extension name. Type `shorty` and press Enter---the shortcode extension is then created:

```bash
Creating extension at /Users/jjallaire/extensions/shorty/shorty:
  - Created README.md
  - Created _extensions/shorty/shorty.lua
  - Created _extensions/shorty/_extension.yml
  - Created .gitignore
  - Created example.qmd
```

If you are running within VS Code or RStudio, a new window will open with the extension project. 

Here's what the contents of the files in `_extensions/shorty/` look like:

``` {.yaml filename="_extensions/shorty/_extension.yml"}
title: Shorty
author: J.J. Allaire
version: 1.0.0
quarto-required: ">=1.2.222"
contributes:
  shortcodes:
    - shorty.lua
```

``` {.lua filename="_extensions/shorty/shorty.lua"}
return {
  ['shorty'] = function(args, kwargs, meta) 
    return pandoc.Str("Hello from Shorty!")
  end
}
```

Finally, the `example.qmd` file includes code that exercises the extension. For example:

``` {.markdown filename="example.qmd"}
---
title: "Shorty Example"
---

{{< shorty >}}
```

To develop your shortcode, render/preview `example.qmd`, and then make changes to `shorty.lua` (the preview will automatically refresh when you change `shorty.lua`).

## Development 

Shortcodes are created using Lua. If you aren't familar with Lua (or with Pandoc filters), here are some resources to help you along:

- [Lua Development](lua.qmd) (Lua is the language used to create shortcodes).

- [Lua API Reference](lua-api.qmd), which describes the Lua extension API for Quarto.

Shortcodes are implemented as Lua functions that take one or more arguments and return a Pandoc AST node (or list of nodes).

Here's the implementation of the `env` shortcode that is built in to Quarto:

``` {.lua filename="env.lua"}
function env(args)
  local var = pandoc.utils.stringify(args[1])
  local value = os.getenv(var)
  if value ~= nil then
    return pandoc.Str(value)
  else
    return pandoc.Null()
  end
end
```

Note that arguments to shortcodes are provided in `args` (a 1-dimensional array), and that each argument is a list of Pandoc inlines (i.e. markdown AST parsed from the text).

We use the `pandoc.utils.stringify()` function to convert the inlines to an ordinary string, and then the `os.getenv()` function to get its value.

You would use this shortcode as follows:

``` markdown
{{{< env HOME >}}}
```

## Distribution

If your extension source code is located within a GitHub repository, then it can be installed by referencing the GitHub organization and repository name. For example:

``` {.bash filename="Terminal"}
# install the current HEAD of the extension
quarto add cooltools/shorty

# install a branch or tagged release of the extension
quarto add cooltools/shorty@v1.2
quarto add cooltools/shorty@bugfix-22
```

Note that it is possible to bundle and distribute extensions as simple gzip archives (as opposed to using a GitHub repository as described above). See the article on [Distributing Extensions](distributing.qmd) for additional details.

## Examples

You might find it instructive to examine the source code of these shortcode extensions authored by the Quarto team:

| **Extension**                                                                                     | **Description**                                                                                 |
|---------------------------|---------------------------------------------|
| [fancy-text](https://github.com/quarto-ext/fancy-text)                                            | Output nicely formatted versions of fancy strings such as LaTeX and BibTeX in multiple formats. |
| [fontawesome](https://github.com/quarto-ext/fontawesome)                                          | Use Font Awesome icons in HTML and PDF documents.                                               |
| [video](https://github.com/quarto-dev/quarto-cli/tree/main/src/resources/extensions/quarto/video) | Embed videos in HTML documents and Revealjs presentations.                                      |

: {tbl-colwidths="\[30,70\]"}

Some additional annotated examples are provided below.

### Raw Output

Shortcodes can tailor their output to the format being rendered to. This is often useful when you want to conditionally generate rich HTML output but still have the same document render properly to PDF or MS Word.

The `pagebreak` shortcode generates "native" pagebreaks in a variety of formats. Here's the implementation of `pagebreak`:

``` {.lua filename="pagebreak.lua"}
function pagebreak()
 
  local raw = {
    epub = '<p style="page-break-after: always;"> </p>',
    html = '<div style="page-break-after: always;"></div>',
    latex = '\\newpage{}',
    ooxml = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>',
    odt = '<text:p text:style-name="Pagebreak"/>',
    context = '\\page'
  }

  if quarto.doc.isFormat('docx') then
    return pandoc.RawBlock('openxml', raw.ooxml)
  elseif quarto.doc.isFormat('pdf')  then
    return pandoc.RawBlock('tex', raw.latex)
  elseif quarto.doc.isFormat('odt')  then
    return pandoc.RawBlock('opendocument', raw.odt)
  elseif quarto.doc.isFormat('epub') then
    return pandoc.RawBlock('html', raw.epub)
  elseif quarto.doc.isFormat('html') then
    return pandoc.RawBlock('html', raw.html)
  elseif quarto.doc.isFormat('context') then
    return pandoc.RawBlock('context', raw.context)
  else
    -- fall back to insert a form feed character
    return pandoc.Para{pandoc.Str '\f'}
  end

end
```

We use the `pandoc.RawBlock()` function to output the appropriate raw content for the target format. Note that raw blocks are passed straight through to the output file and are not processed as markdown.

You'd use this shortcode as follows:

``` markdown
{{{< pagebreak >}}}
```

### Named Arguments

The examples above use either a single argument (`env`) or no arguments at all (`pagebreak`). Here we demonstrate named argument handling by implementing a `git-rev` shortcode that prints the current git revision, providing a `short` option to determine whether a short or long SHA1 value is displayed:

``` {.lua filename="git.lua"}
-- run git and read its output
function git(command)
  local p = io.popen("git " .. command)
  local output = p:read('*all')
  p:close()
  return output
end

-- return a table containing shortcode definitions
-- defining shortcodes this way allows us to create helper 
-- functions that are not themselves considered shortcodes 
return {
  ["git-rev"] = function(args, kwargs)
    -- command line args
    local cmdArgs = ""
    local short = pandoc.utils.stringify(kwargs["short"])
    if short == "true" then
      cmdArgs = cmdArgs .. "--short "
    end
    
    -- run the command
    local cmd = "rev-parse " .. cmdArgs .. "HEAD"
    local rev = git(cmd)
    
    -- return as string
    return pandoc.Str(rev)
  end
}
```

There are some new things demonstrated here:

1.  Rather than defining our shortcode functions globally, we return a table with the shortcode definitions. This allows us to define helper functions that are not themselves registered as shortcodes. It also enables us to define a shortcode with a dash (`-`) in its name.

2.  There is a new argument to our shortcode handler: `kwargs`. This holds any named arguments to the shortcode. As with `args`, values in `kwargs` will always be a list of Pandoc inlines (allowing you to accept markdown as an argument). Since `short` is a simple boolean value we need to call `pandoc.utils.stringify()` to treat it as a string and then compare it to `"true"`.

We'd use this shortcode as follows:

``` {.markdown shortcodes="false"}
---
title: "My Document"
---

{{< git-rev >}}
{{< git-rev short=true >}}
```

### Metadata Options

In some cases you may want to provide options that affect how your shortcode behaves. There is a third argument to shortcode handlers (`meta`) that provides access to document and/or project level metadata.

Let's implement a different version of the `git-rev` shortcode that emits the revision as a link to GitHub rather than plain text. To do this, we make use of `github.owner` and `github.repo` metadata values:

``` {.lua filename="git.lua"}
function git(command)
  local p = io.popen("git " .. command)
  local output = p:read('*all')
  p:close()
  return output
end

return {
  
  ["git-rev"] = function(args, kwargs, meta)
    -- run the command
    local rev = git("rev-parse HEAD")
    
    -- target repo
    local owner = pandoc.utils.stringify(meta["github.owner"])
    local repo = pandoc.utils.stringify(meta["github.repo"])
    local url = "https://github.com/" 
                .. owner .. "/" .. repo .. "/" .. rev 
    
    -- return as link
    return pandoc.Link(pandoc.Str(rev), url)
  end
}
```

As with `args` and `kwargs`, `meta` values are always provided as a list of Pandoc inlines, so often need to be converted to string using `pandoc.utils.stringify()`.

To use this shortcode in a document, we provide the GitHub info as document options, then include the shortcode where we want the link to be:

``` {.markdown shortcodes="false"}
---
title: "My Document"
github:
  owner: quarto-dev
  repo: quarto-cli
---

{{< git-rev >}}
```

The shortcode registration and GitHub metadata could just as well been provided in a project-level `_quarto.yml` file or a directory-level `_metadata.yml` file.

## Raw Arguments

In Quarto >= 1.3 you can also access the raw stream of inlines passed to a shortcode by adding a `raw_args` parameter. For example:

```lua
function shorty(args, kwargs, meta, raw_args)

end
```

{{< include _shortcode-escaping.qmd >}}


# quarto-web/docs/extensions/distributing.qmd

---
title: "Distributing Extensions"
---

{{< include _extension-version.qmd >}}

## Overview

Quarto extensions are directories that contain an `_extensions` sub-directory with one or more extensions. The files above the `_extensions` directory are not installed, so typically contain README and LICENSE files, examples, test cases, etc.

There are two distinct ways to distribute extensions to end users:

1.  Publish your extension in a public GitHub repository.

2.  Bundle your extension into a `.zip` or `.tar.gz` archive.

Each method has benefits and drawbacks that will be explored below. First we'll cover the basic file structure and contents of an extension.

## Extension Contents

Quarto Extensions are directories that contain an `_extensions` folder that contains one or more extension contributions. While the most common case is the distribution of a single extension, it is possible to create a single extension directory that includes multiple shortcodes, multiple filters, or a combination of both.

Here is the contents of an extension named `my-filter`:

``` default
README.md
LICENSE
example.qmd
_extensions/
  my-filter/
    _extension.yml
    my-filter.lua
```

Note that the only thing strictly required is the `_extensions` directory (anything above that is for your own purposes and is ignored during installation). Even so, it's good practice to include a `README.md` and `LICENSE` file, and the `example.qmd` will be useful for developing your extension.

### \_extension.yml

Each extension is defined by its `_extension.yml` file which contains the metadata about the extension as well as the what items it contributes when used. For example, here is the `_extension.yml` for a filter extension:

``` yaml
title: My Filter
author: Cooltools
version: 1.0.0
quarto-required: ">=1.2.0"
contributes:
  filters:
    - my-filter.lua
```

Here are all of the fields that can be specified in the `_extension.yml` file:

`title`

:   The extension's name

`author`

:   The author of the extension

`version`

:   A semantic version number this release. When installing, updating, or releasing an extension, this version number will be used to present a summary of actions to the user.

`quarto-required`

:  A semantic version number indicating the minimum quarto version required to run this extension.

`contributes`

:   The items that this extension will contribute to the render. These are allowed subkeys:

::: {style="margin-left: 1em;"}

`shortcodes`

:   A list of shortcode files that should be loaded when this extension is installed.

`filters`

:   A list of filters that should be loaded when this extension is included in the list of filters used to render a document or project. The order of the filters in this list will be preserved.

`formats`

:   A record containing the key value pairs of output formats and the metadata associated with that output format.
:::

## GitHub Distribution

Distributing extensions on GitHub has a number of benefits, including compact syntax (e.g. `quarto add org-name/extension`), the use of organizations as a "namespace" for managing name conflicts, and the ability to target specific releases or tags.

For example, the extensions in the [`quarto-ext`](https://github.com/quarto-ext/) GitHub organization can be added to a project with these commands:

``` {.bash filename="Terminal"}
quarto add quarto-ext/lightbox
quarto add quarto-ext/fontawesome
```

By default, extensions are added from the `HEAD` of the `main` branch of the repository. You can also target tags and/or branches in your repository by including an `@` after the repository name. For example:

``` {.bash filename="Terminal"}
quarto add quarto-ext/lightbox@v1.2
quarto add quarto-ext/lightbox@bugfix-22
```

Extensions added from GitHub have another special property: the GitHub organization can be used as a namespace qualifier to disambiguate extensions that have the same name. For example, if you have two different `lightbox` extensions in your project, you explicitly specify the `quarto-ext` one as follows:

``` yaml
---
filters:
  - quarto-ext/lightbox
---
```

You can also add an extension from a subdirectory of a GitHub repository. For example, here we install two different extensions from the `cooltools/icons` repository:

``` {.bash filename="Terminal"}
quarto add cooltools/icons/fontawesome
quarto add cooltools/icons/iconify
```

## Archive Distribution

Distributing extensions as a `.zip` or `.tar.gz` archive has the benefit of not requiring public distribution. These extensions can also be added directly from non-GitHub version control services using the archive URLs normally provided for repositories.

Note that unlike GitHub hosted extensions, extensions installed from archives do not have an organizational namespace (they all share a single namespace).

### Git Repositories

To add an extension to a project from a GitLab repository you could do this:

``` {.bash filename="Terminal"}
quarto add https://gitlab.com/cooltools/shorty/-/archive/main/shorty-main.zip
```

You'll note that the above URL references the `main` branch. You can similarly target any other branch, tag, or release. For example, to add an extension using the `v1.0` tag:

``` {.bash filename="Terminal"}
quarto add https://gitlab.com/cooltools/shorty/-/archive/v1.0/shorty-main.zip
```

If you are using BitBucket, Azure DevOps, or another Git hosting provider, consult the appropriate service documentation to learn how to form archive URLs for repositories.

### Archive Files

The above examples demonstrate adding an extension from a Git repository, you can also add an extension from an archive published to an ordinary web host. For example:

``` {.bash filename="Terminal"}
quarto add https://cooltools.org/quarto/shorty.zip
```

Or alternatively from a local archive file or even ordinary uncompressed directory:

``` {.bash filename="Terminal"}
quarto add ~/Downloads/shorty.zip
quarto add /share/quarto/extensions/shorty
```


# quarto-web/docs/extensions/index.qmd

---
title: "Quarto Extensions"
listing: 
  id: listing-filters
  contents: listings/shortcodes-and-filters.yml
metadata-files: 
  - listings/_metadata.yml
---

{{< include _listing-preamble.qmd >}}

### Shortcodes and Filters {.unlisted}

::: {#listing-filters .column-body-outset-right}
:::

{{< include _listing-footer.qmd >}}


# quarto-web/docs/extensions/listing-revealjs.qmd

---
title: "Quarto Extensions"
listing: 
  id: listing-revealjs
  contents: 
    - listings/revealjs.yml
    - listings/revealjs-formats.yml
metadata-files: 
  - listings/_metadata.yml
---

{{< include _listing-preamble.qmd >}}

### Revealjs Extensions {.unlisted}

::: {#listing-revealjs .column-body-outset-right}
:::

{{< include _listing-footer.qmd >}}



# quarto-web/docs/extensions/_extension-version.qmd



# quarto-web/docs/extensions/_listing-preamble.qmd

::: column-body-outset-right
{{< include _extension-version.qmd >}}

Extensions are a powerful way to modify and extend the behavior of Quarto. Below is a listing of available extensions (please [let us know](https://github.com/quarto-dev/quarto-web/tree/main/docs/extensions/listings) if you have an extension you'd like to see added to the list).

See the articles on [Creating Extensions](creating.qmd) to learn how to develop your own extensions.
:::

{{< include _listing-chooser.qmd >}}


# quarto-web/docs/extensions/formats.qmd

---
title: "Custom Formats"
example-org: lexcorp
example-format: lexconf
---

{{< include _extension-version.qmd >}}


## Overview

Quarto format extensions enable you to add new formats to the built-in formats (e.g. `html`, `pdf`, `docx`) already available. Custom formats can provide default document options, style-sheets, header, footer, or logo elements, and even bundle other extensions like [filters](filters.qmd) and [shortcodes](shortcodes.qmd). They are a great way to provide a common baseline for authoring documents or presentations within an organization, for a particular type of project or analysis, or for a specific publication.

You can specify a custom format beneath the `format` key just like a built-in format. For example:

``` yaml
---
title: "My Document"
format:
   acm-pdf: 
     toc: true
---
```

Custom formats all derive from one of the base formats, and include that base format as a suffix. Formats can also provide multiple variations that derive from distinct base formats. For example:

``` yaml
---
title: "My Document"
toc: true
format:
   acm-pdf: default
   acm-html: default
---
```

Note that we moved the `toc` option to the top level since it is shared between both of the formats.

Custom formats can also be used with the `--to` argument to `quarto render`. For example:

``` {.bash filename="Terminal"}
quarto render document.qmd --to acm-html
```

 Note that if you are specifically interested in using or creating custom formats for journals and manuscripts, you may want to proceed instead to the documentation on [Journal Articles](../journals/index.qmd).

## Quick Start

Here we'll describe how to create a simple HTML-based format extension. We'll use the `quarto create` command to do this. If you are using VS Code or RStudio you should execute `quarto create` within their repsective integrated Terminal panes. 

To get started, execute `quarto create extension format:html` within the parent directory where you'd like the format to be created:

```{.bash filename="Terminal"}
$ quarto create extension format:html
 ? Extension Name › lexdoc
```

As shown above, you'll be prompted for an extension name. Type `lexdoc` (a document format for a fictional company named LexCrop) and press Enter---the custom format extension is then created:

```bash
Creating extension at /Users/jjallaire/quarto/dev/lexdoc:
  - Created README.md
  - Created _extensions/lexdoc/custom.scss
  - Created _extensions/lexdoc/_extension.yml
  - Created template.qmd
```

If you are running within VS Code or RStudio a new window will open with the extension project. 

::: {.callout-note appearance="simple"}
Note that this example creates a format that is derivative of the Quarto base `html` format. You can similarly create formats that are derivative of `pdf`, `docx`, and `revealjs` as follows:

```{.bash filename="Terminal"}
quarto create extension format:pdf
quarto create extension format:docx
quarto create extension format:revealjs
```
:::

Here's what the contents of the files in `_extensions/lexdoc/` look like:

``` {.yaml filename="_extensions/lexdoc/_extension.yml"}
title: Lexdoc
author: J.J. Allaire
version: 1.0.0
quarto-required: ">=1.2.222"
contributes:
  formats:
    html:
      toc: true
      theme: [yeti, custom.scss]
```

The custom HTML format defined here is very simple. It takes the base `html` format, turns on the table of contents by default, and sets the theme as `yeti` along with a `custom.scss` file for additional customizations:

```{.css filename="_extensions/lexdoc/custom.css"}
/*-- scss:defaults --*/

/* TODO: Customize appearance with SCSS variables */
/* See https://quarto.org/docs/output-formats/html-themes.html#theme-options */

/*-- scss:rules --*/

/* TODO: Provide custom CSS rules */
```

Finally, the `template.qmd` provides a base example article for users of the format:

``` {.markdown filename="template.qmd"}
---
title: "Lexdoc Example"
format:
  lexdoc-html: default
author: J.J. Allaire
date: last-modified
---

## Introduction

*TODO* Create an example file that demonstrates the formatting and features of your format.

## More Information

You can learn more about controlling the appearance of HTML output here: <https://quarto.org/docs/output-formats/html-basics.html>
```

To develop your format, render/preview `template.qmd`, and then make changes to the various files in the `_extensions` directory (the preview will automatically refresh when you change these files).


## Example: Revealjs

Next, we'll walk through the creation of a custom format that extends the `revealjs` presentation format. Here is what the source code repository of the format extension might look like:

``` default
README.md
LICENSE
template.qmd
_extensions/
  lexconf/
    _extension.yml
    theme.scss
    logo.png
    title.png
```

Note that the format suffix (`revealjs`) is excluded from the directory name (this is to account for the possibility of multiple formats e.g. `lexconf-revealjs`, `lexconf-pptx`, etc.)

As with other types of extensions, the only thing strictly required is the `_extensions` directory (anything above that is for your own purposes and is ignored during format installation). Even so, it's good practice to include a `README.md` and `LICENSE` file. The `template.qmd` file serves a couple of purposes:

1.  It can be rendered as you develop your format to ensure that things work as expected.
2.  It can serve as the basis for a format template (which helps users gets started with using your format).

Here is what the contents of `_extension.yml` might look like:

``` yaml
title: LexConf 2022 Presentation
author: LexCorp
version: 1.0.0
quarto-required: ">=1.2.0"
contributes:
  formats:
    revealjs:
       theme: [default, theme.scss]
       logo: logo.png
       footer: | 
         Copyright 2022 (c) LexCorp, Inc.
       title-slide-attributes:
          data-background-image: title.png
          data-background-size: contain
       preview-links: auto
       
```

This format mostly provides organization-level content and theming. As mentioned above, formats can also include filters which allow for adding custom markdown constructs and rendering behavior.

Here is what the contents of `template.qmd` might look like:

``` markdown
---
title: "Presentation"
subtitle: "LexConf 2022"
author: "Your Name"
date: today
format: lexconf-revealjs
---

# Overview
```

Extension repositories are structured in such a way that you can test your extension and the template by simply rendering the `template.qmd` file right in the root of your repository. The `template.qmd` will be able to load your extension just as it would when installed, so testing and iterating should be as simple as working within your extension directory until you're satisfied (without the need to repeatedly install or update the extension in order to test it).

## Format Templates

Above we described including a `template.qmd` alongside your extension and then installing the template and format together with:

``` {.bash filename="Terminal"}
quarto use template <gh-organization>/<extension>
```

The `template.qmd` should demonstrate the functionality of the format and serve as a sound starting point for the user. When the extension template is copied into the target directory, the `template.qmd` will automatically be renamed to match the name that the user provided for the directory.

You can also include other files alongside `template.qmd` and they will be copied as well. Note that by default, Quarto will exclude common Github repository files when copying an extension template. This includes any file name or directory starting with a `.` (e.g. `.gitignore`), `README.md`, `LICENSE`, etc.. If you'd like, you can place a `.quartoignore` file in the root of your repository with each line of the file being a glob describing file(s) to ignore (using syntax like a `.gitignore` file).

{{< include _formats-common.qmd >}}


# quarto-web/docs/extensions/lua-api.qmd

---
title: "Lua API Reference"
---

{{< include _extension-version.qmd >}}

## Overview

This article provides documentation on the standard APIs available when implementing Lua filters and shortcodes. There are three major sets of APIs available:

-   **Lua Base API**---Base functions provided for string handling, pattern matching, table manipulation, and file input and output.

-   **Pandoc Lua API**---Core API provided by Pandoc for filter development, and includes both core AST types (e.g. `pandoc.Div`, `pandoc.CodeBlock`, etc.) as well as a wide variety of helper functions for common tasks.

-   **Quarto Lua API**---Additional functions used for debugging, format detection, encoding (e.g. JSON), and adding dependencies to documents (e.g. JavaScript libraries or LaTeX packages).

To get started with programming in Lua and learn about some recommended tools and workflow, see the article on [Lua Development](lua.qmd).

## Lua Base API

The Lua standard library provides core functions for low-level string, math, table, and file operations. Here we provide links to a few of the more useful standard libaries (complete documentation can be found in the [Lua Reference Manual](https://www.lua.org/manual/5.3/)).

| Library                                                                                                      | Description                                                                                                                         |
|---------------------------------|---------------------------------------|
| [string](https://www.lua.org/manual/5.3/manual.html#6.4)                                                     | This library provides generic functions for string manipulation, such as finding and extracting substrings, and pattern matching.   |
| [utf8](https://www.lua.org/manual/5.3/manual.html#6.5)                                                       | This library provides basic support for UTF-8 encoding.                                                                             |
| [table](https://www.lua.org/manual/5.3/manual.html#6.6)                                                      | This library provides generic functions for table manipulation.                                                                     |
| [math](https://www.lua.org/manual/5.3/manual.html#6.7)                                                       | This library provides basic mathematical functions.                                                                                 |
| [io](https://www.lua.org/manual/5.3/manual.html#6.8), [file](https://www.lua.org/manual/5.3/manual.html#6.8) | The I/O library provides two different styles for file manipulation: one uses implicit file handles and the other explicit handles. |
| [os](https://www.lua.org/manual/5.3/manual.html#6.9)                                                         | Date/time, locales, environment variables, etc.                                                                                     |

: {tbl-colwidths="\[30,70\]"}

## Pandoc Lua API

Complete documentation for the Pandoc Lua API can be found in the [Lua Filters](https://pandoc.org/lua-filters.html) article available on the Pandoc website. Here are the various components of the API along with links to their reference documentation:

| Lua Module                                                                    | Description                                                                                                                                               |
|--------------------------|----------------------------------------------|
| [pandoc](https://pandoc.org/lua-filters.html#module-pandoc) (ast)             | Constructors for document tree elements (e.g. `pandoc.Div()`, `pandoc.Strong()`, etc.) as well as core components (e.g. `pandoc.Attr()`)                  |
| [pandoc](https://pandoc.org/lua-filters.html#helper-functions) (functions)    | Functions to parse text in a given format, filter and modify a sub-tree, and run child processes.                                                         |
| [pandoc.text](https://pandoc.org/lua-filters.html#module-text)                | UTF-8 aware text manipulation functions (e.g. `upper()`, `lower()`, etc.)                                                                                 |
| [pandoc.List](https://pandoc.org/lua-filters.html#module-pandoc.list)         | This module defines pandoc's list type. It comes with useful methods and convenience function (e.g `find_if()`, `includes()`, `filter()`, `map()`, etc.)  |
| [pandoc.utils](https://pandoc.org/lua-filters.html#module-pandoc.utils)       | Internal pandoc functions and utility functions (e.g. `blocks_to_inlines()`, `stringify()`, `citeproc()`, etc.)                                           |
| [pandoc.path](https://pandoc.org/lua-filters.html#module-pandoc.path)         | Module for file path manipulations (e.g. `is_absolute()`, `is_relative()`, `join()`, etc.                                                                 |
| [pandoc.system](https://pandoc.org/lua-filters.html#module-pandoc.system)     | Access to system information and functionality (e.g. `get_working_directory()`, `list_directory()`, etc.                                                  |
| [pandoc.mediabag](https://pandoc.org/lua-filters.html#module-pandoc.mediabag) | Access to pandoc's media storage. The "media bag" is used when pandoc is called with the `--extract-media` or (for HTML only) `--embed-resources` option. |
| [pandoc.template](https://pandoc.org/lua-filters.html#module-pandoc.template) | Compile and access defualt pandoc templates (e.g. `compile()`)                                                                                            |
| [pandoc.types](https://pandoc.org/lua-filters.html#module-pandoc.types)       | Constructors for types which are not part of the pandoc AST (e.g. `Version()`)                                                                            |

: {tbl-colwidths="\[30,70\]"}

## Quarto Lua API

### Utility Functions

Various utility functions are provided:

| Function                          | Description                                                                                                                                                                                    |
|-------------------|-----------------------------------------------------|
| `quarto.version()`                | Return the current Quarto version as a `pandoc.Version` object.                                                                                                                                |
| `quarto.utils.dump(obj)`          | Dump a text representation of the passed object to stdout.                                                                                                                                     |
| `quarto.utils.resolve_path(path)` | Compute the full path to a file that is installed alongside your extension's Lua script. This is useful for *internal* resources that your filter needs but should not be visible to the user. |

Quarto includes the [pandoc-lua-logging](https://github.com/wlupton/pandoc-lua-logging) library, which should be used in preference to the dump function. For example, you can examine an element passed to a filter function as follows:

``` lua
function Div(el)
  quarto.log.output(el)
end
```

### Format Detection

Extensions will often need to detect the current format to create custom content depending on the target output medium. The `quarto.doc.is_format()` function

| Function                     | Description                                                                                                                                                                                                 |
|-------------------|-----------------------------------------------------|
| `quarto.doc.is_format(name)` | Detect if the current format matches `name`.                                                                                                                                                                |
| `quarto.doc.has_bootstrap()` | Query whether [Bootstrap CSS](https://getbootstrap.com/) is available within the current document (it is by default for standard `html` documents but this may have been overridden by e.g. `theme: none`). |

The `name` parameter can match an exact Pandoc format name (e.g. `docx`, `latex`, etc. or can match based on an alias that groups commonly targeted formats together. The following values format aliases are handled specially by `quarto.doc.is_format()`:

{{< include ../authoring/_format-aliases.md >}}

For example, here we check for PDF and HTML output:

``` lua
if quarto.doc.is_format("pdf") then
  -- pdf specific output
elseif quarto.doc.is_format("html") then
  -- html specific output
else
  -- output for other formats
end
```

For LaTeX output, you may need to additionally detect which citation utility and pdf engine are being used for the current render. You can use these functions to do that detection:

| Function                   | Description                                                                                                                      |
|--------------------|----------------------------------------------------|
| `quarto.doc.cite_method()` | Returns a string (`citeproc`, `natbib`, or `biblatex)` indicating the cite method in use.                                        |
| `quarto.doc.pdf_engine()`  | Returns a string (`pdflatex`, `xelatex`, `lualatex`, or `tectonic`) indicating the PDF engine being used to render the document. |

### Includes

Sometimes extensions need to inject content into the target document. There are three locations that content can be included (pass one of these locations as the first argument of the include functions):

| Location      | Description                                                         |
|--------------------|----------------------------------------------------|
| `in-header`   | In the header of the document (HTML `<head>` tag or LaTeX preamble) |
| `before-body` | Before the document body                                            |
| `after-body`  | After the document body                                             |

Note that the included content should use the *raw target format* (e.g. HTML or LaTeX) rather than markdown. You can use these functions to include text or the contents of a file:

| Function                                  | Description                                                                                                                                                           |
|--------------------|----------------------------------------------------|
| `quarto.doc.include_text(location, text)` | Include text at the specified location (`in-header`, `before-body`, or `after-body`)                                                                                  |
| `quarto.doc.include_file(location, file)` | Include file at the specified location (`in-header`, `before-body`, or `after-body`). The path to the file should *relative* to the Lua script calling this function. |

For example the following code includes an HTML file after the body in the rendered document:

``` lua
quarto.doc.include_file("after-body", "comments.html")
```

### Dependencies

Extensions will sometimes want to add external dependencies (for example, a JavaScript library and related CSS, or the usage of a LaTeX package). This can be accomplished with the following functions:

| Function                                        | Description                                                                                                                                                                                                                                               |
|-------------------|-----------------------------------------------------|
| `quarto.doc.add_html_dependency(dep)`           | Add an HTML dependency (additional resources and content) to a document. See docs on the [HTML Dependencies](#html-dependencies) below for additional details.                                                                                            |
| `quarto.doc.attach_to_dependency(name, attach)` | Attach a file to an existing dependency. `attach` is a file path relative to the Lua filter or table with \`path\` and \`name\` for renaming the file as its copied.                                                                                      |
| `quarto.doc.use_latex_package(pkg, opt)`        | Adds a `\usepackage` statement to the LaTeX output (along an options string specified in `opt`)                                                                                                                                                           |
| `quarto.doc.add_format_resource(path)`          | Add a format resource to the document. Format resources will be copied into the directory next to the rendered output. This is useful, for example, if your format references a `bst` or `cls` file which must be copied into the LaTeX output directory. |

For example, here we add a LaTeX package dependency:

``` lua
quarto.doc.use_latex_package("gamebook")
```

#### HTML Dependencies {#html-dependencies}

HTML Dependencies can bundle together JavaScript, CSS, and even arbitrary content to inject into the `<head>` of the document. These dependencies have a name and a version, which is used to ensure that the same dependency isn't bundled into the document more than once.

The `dep` object passed to `quarto.doc.add_html_dependency()` has the following fields:

| Field            | Description                                                                                                                                                                                        |
|-------------------|-----------------------------------------------------|
| `name`           | Unique name. Required.                                                                                                                                                                             |
| `version`        | Version number (as a string). Required.                                                                                                                                                            |
| `scripts`        | List of scripts to include (paths can be absolute or relative to the Lua file calling the function). Scripts can be either a simple path or a [script object](#script-object).                     |
| `stylesheets`    | List of CSS style-sheets to include (paths can be absolute or relative to the Lua file calling the function). Stylesheets can either be a simple path or a [stylesheet object](#stylesheet-object) |
| `links`          | List of link tags to add to the document. Each tag should be a table with `rel` and `ref` (required) and optionally `type`                                                                         |
| `resources`      | Additional files to copy to the input directory (each resource is an object with `name` (target file name in input directory) and `path` (source file name relative to Lua script).                |
| `serviceworkers` | JavaScript serviceworker files that should be copied to the root output directory (can be a simple string file name or table with \`path\` and \`name\` for renaming the file as its copied).      |
| `meta`           | Table of optional `key = value` meta tags to insert into the document `<head>`                                                                                                                     |
| `head`           | Arbitrary string to include in document `<head>`                                                                                                                                                   |

For example, here we add a dependency to a JavaScript library:

``` lua
quarto.doc.add_html_dependency({
  name = "glightbox",
  version = "3.2.0",
  scripts = {"glightbox.min.js"},
  stylesheets = {"glightbox.min.css"}
})
```

#### Script Object {#script-object}

The easiest way to specify `scripts` is with simple paths. However, in some cases you may need to add attributes to the `<script>` tag or specify that the script should go after the body. In those cases pass a script object:

| Field       | Description                                                       |
|--------------------|----------------------------------------------------|
| `path`      | Path to the script (relative to the calling Lua script)           |
| `attribs`   | Table with `key = value` attributes to add to the `<script>` tag  |
| `afterBody` | Specify that the `<script>` tag should be inserted after the body |

For example, here update the previous example to add an `integrity` attribute to the script:

``` lua
quarto.doc.add_html_dependency({
  name = "glightbox",
  version = "3.2.0",
  scripts = {
    { path = "glightbox.min.js ", attribs = {integrity = "R9GqQ8K/uxy9rx"} }
  },
  stylesheets = {"glightbox.min.css"}
})
```

#### Stylesheet Object {#stylesheet-object}

The easiest way to specify `stylesheets` is with simple paths. However, in some cases you may need to add attributes to the `<link>` tag generated for the stylesheet. In those cases pass a stylesheet object:

| Field     | Description                                                    |
|-------------------|-----------------------------------------------------|
| `path`    | Path to the stylesheet (relative to the calling Lua script)    |
| `attribs` | Table with `key = value` attributes to add to the `<link>` tag |

For example, here we update the previous example to add an `integrity` attribute to the stylesheet:

``` lua
quarto.doc.add_html_dependency({
  name = "glightbox",
  version = "3.2.0",
  scripts = {
    { 
      path = "glightbox.min.js ", 
      attribs = {integrity = "R9GqQ8K/uxy9rx"} 
    }
  },
  stylesheets = {
    { 
      path = "glightbox.min.css ", 
      attribs = {integrity = "GYl1kPzQho1wx"} 
    }
  }
})
```

### JSON Encoding

Quarto includes a copy of [json.lua](https://github.com/rxi/json.lua). a lightweight JSON library for Lua. You can access the JSON functions as follows:

| Function                    | Description                            |
|-----------------------------|----------------------------------------|
| `quarto.json.encode(input)` | Encode a Lua table into a JSON string. |
| `quarto.json.decode(str)`   | Parse a JSON string into a Lua table.  |

For example, here we encode and then decode a table:

``` lua
local json = quarto.json.encode({foo = "bar"})
local obj = quarto.json.decode(json)
```

### Base64 Encoding

Quarto includes a copy of [lbase64](https://github.com/iskolbin/lbase64), a pure Lua implementation of Base64 encoding. You can access the Base 64 encoding functions as follows:

| Function                       | Description                   |
|--------------------------------|-------------------------------|
| `quarto.base64.encode(str)`    | Encode a string into Base 64. |
| `quarto.base64.decode(b64str)` | Decode a Base 64 string.      |

# quarto-web/docs/extensions/managing.qmd

---
title: "Managing Extensions"
---

{{< include _extension-version.qmd >}}

## Installation

If you want to use an extension within a document or project you need to add it to a project or directory. Rather than installing into a global library, Quarto extensions are stored locally, directly alongside the document or project they are used within. For example, if you have a project in a directory named `myblog`, you could add some extensions for use with that the project as follows:

``` {.bash filename="Terminal"}
cd myblog
quarto add quarto-ext/fontawesome
quarto add quarto-ext/video
```

This will result in an `_extensions` folder being created at the root of your project, and the `fontawesome` and `video` extensions being placed within it.

Note that a project isn't strictly required for using extensions---if you add extensions in a directory that isn't a project then any document located directly alongside the `_extensions` folder can use the extensions.

{{< include _extension-trust.qmd >}}

### Version Control

If you are using version control you should check the `_extensions` directory in to your repo along with your other code. Extensions used by a document or project are treated as source code to ensure very long term reproducibility---your project doesn't need to rely on the availability of an external package manager (or the maintenance of older extension versions) to successfully render now and far into the future.

## Repositories

The extensions in the example above were prefixed with `quarto-ext` because they were distributed from the [quarto-ext](https://github.com/quarto-ext/) GitHub organization. Extensions can be similarly distributed from **any** GitHub organization. So for example the following might also be valid command to add extensions to a project:

``` {.bash filename="Terminal"}
quarto add cooltools/lightbox
quarto add bigstateu/fancytweet
```

While it's convenient to distribute extensions using GitHub, you can also bundle them into a `.zip` or `.tar.gz` archive and distribute them using a URL or a local file. See the article on [Distributing Extensions](distributing.qmd) for additional details.

## Updating

You can list and update configured extensions for a given project with the following commands:

``` {.bash filename="Terminal"}
quarto list extensions
quarto update quarto-ext/fontawesome
```

Note that when updating an extension you'll be prompted to confirm the update based on the version you have and the version you are attempting to update to.

## Removing

Use this command to remove an extension from a project:

``` {.bash filename="Terminal"}
quarto remove quarto-ext/fontawesome
```

If you run the `quarto remove extension` command with no `extension-id`, you will be presented with a list of extensions that are present and you may select which extensions to remove.


# quarto-web/docs/extensions/_listing-chooser.qmd

::: column-page-inset-right
```{=html}

<style type="text/css">
.nav-tabs {
  margin-top: 0.5rem;
  border-bottom: none;
}

.callout {
  margin-top: 0;
}

.nav-tabs .nav-link {
  text-align: center;
  margin-right: 15px;
  margin-top: 10px;
  width: 147px;
  font-size: 0.8em;
  font-weight: 600;
}


.nav-tabs .nav-link, 
.nav-tabs .nav-link.active, 
.nav-tabs .nav-item.show .nav-link {
  border: 1px solid  rgb(222, 226, 230);
  border-radius: 10px;
  color: rgb(80,146,221);
}
.nav-tabs .nav-link:hover {
   border-color: rgb(80,146,221);
   border-width: 1px;
} 

.nav-tabs .nav-link.active, 
.nav-tabs .nav-item.show .nav-link {
  border-color: rgb(80,146,221);
  border-width: 2px;
}


.nav-tabs .nav-link i {
  display: block;
  font-size: 3rem;
  color: rgb(80,146,221);
  margin-bottom: 5px;
}

.quarto-listing {
  margin-top: 2em;
}

.quarto-listing .listing-name,
.quarto-listing .listing-author {
  white-space: nowrap;
}

.quarto-listing .listing-actions-group h3 {
  margin-top: 0;
}

 
</style>

<ul id="index-chooser" class="nav nav-tabs" role="tablist">
  <li class="nav-item" role="presentation">
    <a class="nav-link" href="listing-filters.html">
      <i class="bi bi-gear"></i>Shortcode/Filter
    </a>
  </li>
  <li class="nav-item" role="presentation">
    <a class="nav-link" href="listing-journals.html">
      <i class="bi bi-journal-text"></i>Journal Articles
    </a>
  </li>
  <li class="nav-item" role="presentation">
    <a class="nav-link" href="listing-formats.html">
      <i class="bi bi-file-earmark-richtext"></i>Custom Formats
    </a>
  </li>
  <li class="nav-item" role="presentation">
    <a class="nav-link" href="listing-revealjs.html">
      <i class="bi bi-easel3"></i>Revealjs
    </a>
  </li>
</ul>

<script type="text/javascript">
document.addEventListener("DOMContentLoaded", function() {
  // get file name
  const filename = window.location.pathname.split("/").slice(-1)[0];

  // latch active
  const toolLinks = window.document.querySelectorAll("#index-chooser a");
  for (const tool of toolLinks) {
    if (filename && filename !== "index.html") {
      if (tool.href.endsWith(filename)) {
        tool.classList.add("active");
      } 
    } else {
      if (tool.href.endsWith("listing-filters.html")) {
        tool.classList.add("active");
      }
    }
  }
  
  // move heading into table
  document.querySelector(".listing-actions-group").prepend(document.querySelector("h3.unlisted"));
});

</script>
```
:::


# quarto-web/docs/extensions/_listing-footer.qmd


::: {.column-body-outset-right}



:::


# quarto-web/docs/extensions/creating.qmd

---
title: Creating Extensions
---

{{< include _extension-version.qmd >}}

## Overview

Quarto Extensions are a powerful way to modify or extend the behavior of Quarto, and can be created and distributed by anyone. There are several types of extensions available:

| Extension                                   | Description                                                                                                                                                                                                                                                   |
|----------------------------------|-----------------------------------------------------------------------------------|
| [Shortcodes](shortcodes.qmd)                | Special markdown directives that generate various types of content. For example, you could create shortcodes to embed tweets or videos in a document.                                                                                                         |
| [Filters](filters.qmd)                      | A flexible and powerful tool for introducing new global behaviors and/or new markdown rendering behaviors. For example, you could create filters to implement output folding, an image carousel, or just about anything you can imagine!                      |
| [Journal Articles](../journals/formats.qmd) | Enable authoring of professional Journal articles using markdown, and produce both LaTeX (PDF) and HTML versions of the articles.                                                                                                                             |
| [Custom Formats](formats.qmd)               | Create new output formats by bundling together document options, templates, style sheets, and other content.                                                                                                                                                  |
| [Revealjs Plugins](revealjs.qmd)            | Extend the capabilities of HTML presentations created with Revealjs.                                                                                                                                                                                          |
| [Project Types](project-types.qmd)          | Create new project project types that bundle together standard content and options, or make it easy to create a website for a custom HTML format.                                                                                                             |
| [Starter Templates](starter-templates.qmd)  | Help users get started with new projects by providing a template and example content. Starter templates aren't strictly extensions (i.e. they aren't installed in the `_extensions` directory) but they are often used with custom formats and project types. |

: {tbl-colwidths="\[30,70\]"}

## Development

Each type of extension has its own development requirements: in some cases an extension can be created with YAML metadata alone, however in many cases you'll end up doing some custom scripting using Lua.

These articles provide in-depth documentation on learning and using Lua for extension development:

-   [Lua Development](lua.qmd) helps you get started with Lua (the language used to create extensions)

-   [Lua API Documentation](lua-api.qmd) provides documentation on the Pandoc and Quarto Lua APIs used for creating extensions.

## Distribution

There are two distinct ways to distribute extensions to end users:

-   Publish your extension in a public GitHub repository.

-   Bundle your extension into a `.zip` or `.tar.gz` archive.

[Distributing Extensions](distributing.qmd) goes into more depth on how to package and distribute extensions, both on GitHub and using plain gzip archives.

## Examples

The documentation linked to above provides simple motivating examples for each type of extension. Once you understand these, check out the following for more sophisticated examples of each type of extension:

The [Quarto Extensions](https://github.com/quarto-ext/) GitHub organization provides a set of extensions developed by the core Quarto team. Many of these extensions implement frequently requested features, and all of them provide sound examples of how to implement extensions.

The [Quarto Journals](https://github.com/quarto-journals/) GitHub organization contains a set of Journal Article formats developed by the core Quarto team or contributed by third parties.

Finally, most [published extensions](index.qmd) are hosted on GitHub and therefore have source code available that you can learn from.


# quarto-web/docs/extensions/listing-filters.qmd

---
title: "Quarto Extensions"
listing: 
  id: listing-filters
  contents: listings/shortcodes-and-filters.yml
metadata-files: 
  - listings/_metadata.yml
---

{{< include _listing-preamble.qmd >}}

### Shortcodes and Filters {.unlisted}

::: {#listing-filters .column-body-outset-right}
:::

{{< include _listing-footer.qmd >}}



# quarto-web/docs/extensions/nbfilter.qmd

---
title: "Notebook Filters"
---

## Overview

If you are rendering existing Jupyter notebooks that were not created with Quarto in mind, you may wish to do some pre-processing on the notebook prior to its conversion to markdown. This can be accomplished by specifying one or more `ipynb-filters`. These filters are passed the [JSON representation](https://nbformat.readthedocs.io/en/latest/format_description.html) of the notebook on `stdin` and should write a transformed JSON representation to `stdout`.

::: callout-note
The purpose of notebook filters is to adapt existing `.ipynb` files for use with Quarto. Consequently, notebook filters are only run when the original input is an `.ipynb` file (they are not run for `.qmd` files).
:::

## Example

For example, this notebook filter uses the [nbformat](https://nbformat.readthedocs.io/en/latest/index.html) package to read a notebook, prepend a comment to the source of each code cell, and then write it back to `stdout`:

``` python
import sys
import nbformat

# read notebook from stdin
nb = nbformat.reads(sys.stdin.read(), as_version = 4)

# prepend a comment to the source of each cell
for index, cell in enumerate(nb.cells):
  if cell.cell_type == 'code':
     cell.source = "# comment\n" + cell.source
  
# write notebook to stdout 
nbformat.write(nb, sys.stdout)
```

You can arrange for this filter to be run using the `ipynb-filters` option (specified at either the document or project level):

``` yaml
---
ipynb-filters:
  - filter.py
---
```

Note that the current working directory for the filter will be set to the location of the input notebook.


# quarto-web/docs/extensions/revealjs.qmd

---
title: "Revealjs Plugins"
---

{{< include _extension-version.qmd >}}

## Overview

Revealjs plugins enable you to extend the capabilities of HTML presentations created with [Revealjs](../presentations/revealjs/). The Reveal Plugin API is very rich, and many of the built-in capabilities of Quarto Revealjs presentations are implemented as plugins, including [Menu](https://github.com/quarto-dev/quarto-cli/tree/main/src/resources/formats/revealjs/plugins/menu), [Chalkboard](https://github.com/quarto-dev/quarto-cli/tree/main/src/resources/formats/revealjs/plugins/chalkboard), and [PDF Export](https://github.com/quarto-dev/quarto-cli/tree/main/src/resources/formats/revealjs/plugins/pdfexport).

Here are some examples of Revealjs plugins packaged as Quarto extensions:

| Extension                                                | Description                                                                          |
|----------------------------------------------------------|--------------------------------------------------------------------------------------|
| [Pointer](https://github.com/quarto-ext/pointer)         | Adds support for switching the cursor to a 'pointer' style element while presenting. |
| [Attribution](https://github.com/quarto-ext/attribution) | Display attribution text along the right edge of slides.                             |

: {tbl-colwidths="\[30,70\]"}

## Quick Start

Here we'll describe how to create a simple Revealjs plugin extension. We'll use the `quarto create` command to do this. If you are using VS Code or RStudio you should execute `quarto create` within their repsective integrated Terminal panes. 

To get started, execute `quarto create extension revealjs-plugin` within the parent directory where you'd like the plugin extension to be created:

```{.bash filename="Terminal"}
$ quarto create extension revealjs-plugin
 ? Extension Name › shuffler
```

As shown above, you'll be prompted for an extension name. Type `shuffler` and press Enter---the Revealjs plugin extension is then created:

```bash
Creating extension at /Users/jjallaire/quarto/dev/shuffler:
  - Created README.md
  - Created _extensions/shuffler/_extension.yml
  - Created _extensions/shuffler/shuffler.css
  - Created _extensions/shuffler/shuffler.js
  - Created .gitignore
  - Created example.qmd
```

If you are running within VS Code or RStudio a new window will open with the extension project. 

Here's what the contents of the files in `_extensions/shuffler/` look like:

``` {.yaml filename="_extensions/shuffler/_extension.yml"}
title: Shuffler
author: J.J. Allaire
version: 1.0.0
quarto-required: ">=1.2.222"
contributes:
  revealjs-plugins:
    - name: RevealShuffler
      script:
        - shuffler.js
      stylesheet:
        - shuffler.css
```

``` {.lua filename="_extensions/shuffler/shuffler.js"}
window.RevealShuffler = function () {
  return {
    id: "RevealShuffler",
    init: function (deck) {
      // TODO: Implement your plugin functionality
      // Learn more at https://revealjs.com/creating-plugins/
      
      // This example shuffles the deck when the 'T' key is pressed
      deck.addKeyBinding({ keyCode: 84, key: "T" }, () => {
        deck.shuffle();
      });
    },
  };
};
```

There is also a `shuffler.css` file for providing any styles required by your plugin.

Finally, the `example.qmd` file includes code that exercises the extension. For example:

``` {.markdown filename="example.qmd"}
---
title: "Shuffler Example"
format:
  revealjs: default
revealjs-plugins:
  - shuffler
---

## Breakfast

- Eat eggs
- Drink coffee

## Dinner

- Eat spaghetti
- Drink wine
```

To develop your plugin, render/preview `example.qmd`, and then make changes to `shuffler.js` and `shuffler.css` (the preview will automatically refresh when you change these files).

## Installation and Use

If your extension source code it located within a GitHub repository, then it can be added by referencing the GitHub organization and repository name. For example, you can install the `attribution` extension with the following:

``` {.bash filename="Terminal"}
quarto add quarto-ext/attribution
```

Note that it is possible to bundle and distribute extensions as simple gzip archives (as opposed to using a GitHub repository as described above). See the article on [Distributing Extensions](distributing.qmd) for additional details.

Once an extension has been added, you can use the Reveal plugin by adding it to the `reveal-plugins` key. For example:

``` yaml
---
title: "My Presentation"
format: revealjs
revealjs-plugins:
  - attribution
---
```

## Plugin Packaging

Note that the plugins listed above were not initially developed for use with Quarto. Rather, they were developed intially as native Revealjs plugins and then packaged as Quarto extensions.

For example, you can find the original implementation of the attribution plugin here: <https://github.com/rschmehl/reveal-plugins/tree/main/attribution>. The plugin is implemented with a JavaScript file and a CSS file. To make the plugin available as a Quarto extension, we package these files along with an `_extension.yml` config file that registers the plugin. Here are the files in the Quarto extension:

``` bash
LICENSE
README.md
example.qmd
_extensions/
   attribution/
     _extension.yml
     attribution.js
     attribution.css
```

Note that the `LICENSE` and `README.md` are standard documentation files and the `example.qmd` is used for development and documentation of the extension. None of those files are actually installed by end users (rather only the contents of the `_extensions` directory is installed).

You can see the full source code of the Quarto version here: <https://github.com/quarto-ext/attribution> (we'll also walk through the code in detail below).

## Plugin Development

You can develop either entirely new Revealjs plugins from scratch or you can package existing Revealjs extensions as described above.

Here is a list of existing 3rd party plugins for Revealjs that you might consider packaging as Quarto extensions: <https://github.com/hakimel/reveal.js/wiki/Plugins,-Tools-and-Hardware>.

If you want to develop new plugins, check out the Quarto Reveal extensions listed above as well as the code of other 3rd party Reveal Plugins. The following documentation on the Revealjs website provides additional important technical details:

-   [API Methods](https://revealjs.com/api/)

-   [Reveal Events](https://revealjs.com/events/)

## Plugin Configuration

Some Revealjs plugins make available various user options. If you are developing a plugin from scratch, you should use a distinct key for your plugin's configuration. Users can use this key alongside other `revealjs` options. For example the `pointer` extension can be configured as follows:

``` yaml
---
title: "Example Presentation"
format:
  revealjs: 
    pointer:
      pointerSize: 18
      color: '#32cd32'
revealjs-plugins:
  - pointer
---
```

The extension accesses options using the `deck.getConfig()` function:

``` javascript
return {
  id: "pointer",
  init: (deck) => {
    const config = deck.getConfig();
    const options = config.pointer || {};
    // etc
  }
}
```

Note that when packaging an existing Revealjs plugin, you can override its default configuration using the `config` key within your `_extension.yml` file. For example, these are the overrides provided by the `pointer` extension:

``` yaml
title: Pointer
author: Charles Teague
contributes:
  revealjs-plugins:
    - name: RevealPointer
      script:
        - pointer.js
      stylesheet:
        - pointer.css
      config:
        pointer:
          key: "q"
          color: "red"
          pointerSize: 16
          alwaysVisible: false
```

## Example: Attribution

Here we'll walk through the complete source code for the [attribution](https://github.com/quarto-ext/attribution/) extension. This extension enables you to display attribution text sideways along the right edge of Revealjs slides.

Here are source files used to develop the extension:

``` bash
LICENSE
README.md
example.qmd
_extensions/
   attribution/
     _extension.yml
     attribution.js
     attribution.css
```

The `example.qmd` and documentation files are used for development of the the extension only (it is not installed by end users). The other files provide extension registration (`_extension.yml`) and the actual implementation of the Revealjs plugin (`attribution.js` and `attribution.css`).

The `example.qmd` is a simple one-slide presentation that includes an image along with a a div with class `.attribution`:

``` {.markdown filename="example.qmd"}
---
title: "Attribution Extension"
format: revealjs
revealjs-plugins:
  - attribution
---

## Forest Image

![](ingtotheforest.jpg)

::: {.attribution)
Photo courtesy of [@ingtotheforest](https://unsplash.com/@ingtotheforest)
:::
```

Note that the `revealjs-plugins` key references the `attribution` extension, which will implemented in the `_extensions/attribution` directory.

The `_extension.yml` file indicates that the extension is making available a Revealjs plugin along with the plugin name, script, and style-sheets (note that the plugin name is not arbitrary, it will be whatever name is used within the script that implements the plugin, in this case `RevealAttribution`):

``` {.yaml filename="_extensions/attribution/_extension.yml"}
title: Attribution
author:  Roland Schmehl
version: 0.1.0
quarto-required: ">=1.2.0"
contributes:
  revealjs-plugins:
    - name: RevealAttribution
      script:
        - attribution.js
      stylesheet:
        - attribution.css
```

The `attribution.js` file contains the implementation of the Plugin using the Revealjs Plugin API:

``` {.javascript filename="_extensions/attribution/attribution.js"}
window.RevealAttribution = window.RevealAttribution || {
  id: 'RevealAttribution',
  init: function(deck) {
      initAttribution(deck);
  }
};

const initAttribution = function(Reveal){

var ready = false;
var resize = false;
var scale = 1;

window.addEventListener( 'ready', function( event ) {

  var content;

  // Remove configured margin of the presentation
  var attribution = document.getElementsByClassName("attribution");
  var width = window.innerWidth;
  var configuredWidth = Reveal.getConfig().width;
  var configuredHeight = Reveal.getConfig().height;

  scale = 1/(1-Reveal.getConfig().margin);

  for (var i = 0; i < attribution.length; i++) {
    content = attribution[i].innerHTML;
    attribution[i].style.width = configuredWidth + "px";
    attribution[i].style.height = configuredHeight + "px";
    attribution[i].innerHTML = "<span class='content'>" + content + "</span>";
    attribution[i].style.transform = 'translate( -50%, -50% ) scale( ' + scale*100 + '% ) rotate(-180deg)';
  }

  // Scale with cover class to mimic backgroundSize cover
  resizeCover();

});

window.addEventListener( 'resize', resizeCover );

function resizeCover() {

  // Scale to mimic backgroundSize cover
  var attribution = document.getElementsByClassName("attribution");
  var xScale = window.innerWidth / Reveal.getConfig().width;
  var yScale = window.innerHeight / Reveal.getConfig().height;
  var s = 1;

  if (xScale > yScale) {
      // The div fits perfectly in x axis, stretched in y
      s = xScale/yScale;
  }
  for (var i = 0; i < attribution.length; i++) {
    attribution[i].style.transform = 'translate( -50%, -50% ) scale( ' + s*scale*100 + '% ) rotate(-180deg)';
  }
}

};
```

Finally, `attribution.css` includes the CSS that repositions and rotates the element with class `.attribution` on the far right side of the slide:

``` {.css filename="_extensions/attribution/attribution.css"}
/* Attribution plugin: text along the right edge of the viewport */
.attribution{
  position: absolute;
  top: 50%;
  bottom: auto;
  left: 50%;
  right: auto;
  font-size: 0.4em;
  pointer-events: none;
  text-align: center;
  writing-mode: vertical-lr;
  transform: translate( -50%, -50% ) scale( 100% ) rotate(-180deg);
}

/* Attribution plugin: activate pointer events for attribution text only */
.attribution .content{
  pointer-events: auto;
}
```


# quarto-web/docs/extensions/_formats-common.qmd

## Distributing Formats

You can distribute format extensions in one of two ways:

1.  As a template that includes both the format in the `_extensions` directory and the `template.qmd` (which is automatically renamed to match the name of the enclosing directory).

2.  As a plain format with no template scaffolding (this is useful for adding the format to an existing document or project).

If you have a GitHub repository containing the files enumerated above in the `{{< meta example-format >}}` example, users could install your extension and associated template as follows (where `{{< meta example-org >}}` is the GitHub organization hosting the repo):

``` {.bash filename="Terminal"}
quarto use template {{< meta example-org >}}/{{< meta example-format >}}
```

This is often the preferred way to get started with a format as it provides the user with a working document right out of the box. It's also possible to install *only* the format if you are working with an existing project:

``` {.bash filename="Terminal"}
quarto add {{< meta example-org >}}/{{< meta example-format >}}
```

Note that it is possible to bundle and distribute extensions as simple gzip archives (as opposed to using a GitHub repository as described above). See the article on [Distributing Extensions](../extensions/distributing.qmd) for additional details.

## Common Metadata

If you have metadata that is common to any output format when your format extension is targeted, you can place that metadata under the `common` key. For example:

``` yaml
contributes:
  format:
    common:
      filters:
        - filter.lua
      shortcodes:
        - quarto-ext/fancy-text
    html:
      # html-specifc
    pdf:
      # pdf-specifc
```

## Format Resources

You can usually include other files and resources within a format extension by placing those files within the extension directory and using relative paths to reference them in your `_extension.yml` metadata file. These relative paths will be properly handled as your extension's metadata is merged with the rendered document metadata.

If there are resources that you need to have copied to the input directory as a part of rendering the document (for example, a `bst` file for LaTeX bibliographies or a logo or other file referenced from a LaTeX template), you can provide `format-resources`, which is a list of file paths[^_formats-common-1]. Each of these files will be copied into the directory containing the input that is being rendered when the document is rendered. For example:

``` yaml
contributes:
  format:
    pdf:
      format-resources:
        - plos2015.bst
```

## Extension Embedding

In some cases format extensions will want to make use of other extensions. This is permitted, but adding extensions for use within a custom format must be done with a special command line flag to ensure they are embedded correctly.

``` {.bash filename="Terminal"}
quarto create extension format:pdf myformat
cd myformat
quarto add quarto-ext/fancy-text --embed myformat
```

For example, here we want to make the [fancy-text](https://github.com/quarto-ext/fancy-text) extension (which provides special formatting for the words {{< latex >}} and {{< bibtex >}}) available for users of the [jss](https://github.com/quarto-journals/jss) custom format:

``` {.bash filename="Terminal"}
quarto add quarto-ext/fancy-text --embed jss
```

This will produce the following output:

``` {.bash filename="Output"}
quarto-journals/jss
└── _extensions
    └── jss
        ├── _extensions
        │   └── quarto-ext
        │       └── fancy-text
        └── partials
```

This will add the `quarto-ext/fancy-text` extension into the `jss` extension in the `_extensions` folder. By embedding an extension you make it available without creating the potential for conflict with other versions of the extension that users might already have installed.

[^_formats-common-1]: This is most common in the the case of PDF based formats which have a secondary step of converting the LaTeX produced by Pandoc into a PDF. If there are files that are referenced indirectly by the LaTeX, they will need to be discoverable and should typically be copied into the same directory that contains the LaTeX input.


# quarto-web/docs/extensions/_extension-trust.qmd

::: {.callout-warning appearance="simple"}
### Extension Trust

Quarto extensions may execute code when documents are rendered. Therefore, if you do not trust the author of an extension, we recommend that you do not install or use the extension.
:::




# quarto-web/docs/extensions/project-types.qmd

---
title: "Project Types"
---

{{< include _extension-version.qmd >}}

## Overview

Custom project types provide the ability to tailor projects for a particular purpose. This could be used to create a project type that implements an organization-level standard for creating documentation or conducting analyses.

For example, if you created a project type extension called `lexdocs`, it could be used with:

``` {.yaml filename="_quarto.yml"}
project:
  type: lexdocs
```

This single line of configuration could provide:

-   Navigational elements
-   Headers and footers
-   Document filters
-   Graphical elements
-   HTML options and styles

If you additionally include some basic scaffolding as a [Starter Template](starter-templates.qmd) for using the project type, and host it within a GitHub repository, then users could get a new project up and running as simply as:

``` {.bash filename="Terminal"}
quarto use template lexcorp/lexdocs
```

Note that it is possible to bundle and distribute project type extensions as simple gzip archives (as opposed to using a GitHub repository as described above). See the article on [Distributing Extensions](http://localhost:7603/docs/extensions/distributing.html) for additional details.

## Development Tools

If you are using custom project types within VS Code or RStudio, only the very latest versions of these tools handle custom project types correctly:

-   For the Quarto VS Code Extension, use [version 1.45](https://marketplace.visualstudio.com/items?itemName=quarto.quarto) or greater.

-   For RStudio, use [version 2022.12](https://posit.co/download/rstudio-desktop/) or higher.

Please be sure to update your version(s) of these tools before proceeding.

## Complete Example

In this section we'll describe exactly what a project type extension should include by providing a complete example of the `lexdocs` project type alluded to above. Here are the files contained in our `lexdocs` project type:

``` bash
_quarto.yml
index.qmd
team.qmd
_extensions
  lexdocs/
    _extension.yml
    lexcorp.png
    theme.scss
    filter.lua
```

Note that this repository provides both:

1.  The project type extension (contained in the `_extensions` directory).

2.  A starter template for using the project type (the `_quarto.yml`, `index.qmd`, and `team.qmd` files in the root of the repository).

### Project Type Extension

Let's explore the code for the extension first. Here is the main `_extension.yml` file:

``` {.yaml filename="_extensions/lexdocs/_extension.yml"}
title: Lexdocs Project
author: Lexcorp, Inc.
version: 1.0.0
quarto-version: ">=1.2.0"
contributes:
  project:
    project:
      type: website
    website:
      sidebar: 
        contents: auto
        search: true
        style: docked
        background: light
        logo: lexcorp.png
      page-footer: |
        "Copyright 2022, Lexcorp, Inc." 
    format: lexdocs-html
  formats:
    html:
      theme: [default, theme.scss]
      code-overflow: wrap
      code-line-numbers: true
      filters:
        - filter.lua
```

The `contributes` key includes a `project` entry, which in turn defines the default values for the `_quarto.yml` configuration file when this project type is used.

Note that custom project types always need to inherit from one of the base project types built into Quarto (`default`, `website`, or `book`). Here we specify `project: type: website`.

You'll also note that we additionally define a `lexdocs-html` [Custom Format](formats.qmd) within the extension (and then make that the default format for the project). This enables us to reference that format explicitly within documents (e.g. if you want to include a document that renders both `pdf` and `lexdocs-html` variations).

There are three additional files referenced in the custom `project` definition in `_extension.yml`. We won't show their source code, but here's a rundown on the role they play:

-   `lexcorp.png` is a logo added to the `sidebar`.
-   `theme.scss` provides a [custom theme](../output-formats/html-themes.qmd) for HTML output.
-   `filter.lua` provides some additional transformations required by the format.

### Starter Template

This repository also provides a starter template by including these files at the root of the repository:

-   `_quarto.yml` is the project configuration file
-   `index.qmd` is an empty default home page
-   `team.qmd` is a page where users of the project type are encouraged to list the team members who contributed.

Here's what `_quarto.yml` might look like:

``` {.yaml filename="_quarto.yml"}
project:
  title: "Docs Site"
  type: lexdocs
  
format:
  lexdocs-html:
    toc: true
```

Users of the template will natually change the default `title`, and can add whatever other project, website, or format level options they require (these options will be merged with the defaults provided by the extension).

## Markdown Publishing

If you are using Quarto to produce markdown for another publishing system, you can use a project type extension to tailor the markdown output created by Quarto, as well as integrate with the native preview capabilities of the other system.

Quarto includes a couple of built-in project-types for integrating with the [Hugo](../output-formats/hugo.qmd) and [Docusaurus](../output-formats/docusaurus.qmd) publishing systems. You can see the source code for these project types here:

-   [`hugo`](https://github.com/quarto-dev/quarto-cli/blob/main/src/resources/extensions/quarto/hugo/_extension.yml) project type

-   [`docusaurus`](https://github.com/quarto-dev/quarto-cli/blob/main/src/resources/extensions/quarto/docusaurus/_extension.yml) project type

### Hugo Example

Here is the the `_extension.yml` file for the Hugo project type (this demonstrates a few of the additional options you'd typically specify when creating a project type for markdown publishing, we'll describe these options below):

``` {.yaml filename="_extension.yml"}
title: Hugo
author: RStudio, PBC
organization: quarto
contributes:
  project:
    project:
      type: default
      detect:
        - ["config.toml", "content"]
        - ["config/_default/config.toml", "content"]
      render:
        - "**/*.qmd"
        - "**/*.ipynb"
      preview:
        serve:
          cmd: "hugo serve --port {port} --bind {host} --navigateToChanged"
          env: 
            HUGO_RELATIVEURLS: "true"
          ready: "Web Server is available at"
    format: hugo-md
  formats:
    md:
      variant: gfm+yaml_metadata_block+definition_lists
      prefer-html: true
      fig-format: retina
      fig-width: 8
      fig-height: 5
      wrap: preserve
```

Let's look specifically at some project options provided for Hugo that you may not have seen before:

``` yaml
project:
  type: default
  detect:
    - ["config.toml", "content"]
    - ["config/_default/config.toml", "content"]
  render:
    - "**/*.qmd"
    - "**/*.ipynb"
  preview:
    serve:
      cmd: "hugo serve --port {port} --bind {host} --navigateToChanged"
      env: 
        HUGO_RELATIVEURLS: "true"
      ready: "Web Server is available at"
```

The `detect` option enables Quarto to automatically detect when to activate this project type based on the presence of one or more files.

The `render` option indicates which files Quarto should render (note that by default Quarto will render `.md` files, but this would interfere with Hugo's native rendering of `.md` files so we exclude them here).

The `preview` option enables `quarto preview` to launch the native preview server for Hugo. The `cmd` indicates the shell command to use (with spots to interpolate the `{port}` and `{host`}); the `env` option specifies values for environment variables; and the `ready` option is a sequence of characters to look for to indicate that the preview server has started and is ready to handle requests.

### Markdown Formats

When creating a project type for a markdown publishing system you'll always need to define a custom format along with it which defines what flavor of markdown to produce. In the case of Hugo we define the markdown flavor using the `variant` option:

``` yaml
formats:
  md:
    variant: gfm+yaml_metadata_block+definition_lists+smart
```

This results in GitHub Flavored Markdown w/ YAML metadata blocks (which Hugo requires for tags/categories/etc) in addition to support for definition lists and smart typography.

Note that for some systems you'll need to do more than just declare a variant. For example, in the case of Docusaurus we declare the variant as well as a Lua filter that deals with Docusaurus-specific constructs like MDX, Callouts, and Tabsets:

``` yaml
formats:
  md:
    variant: +yaml_metadata_block+pipe_tables+tex_math_dollars+header_attributes-all_symbols_escapable
    filters:
      - docusaurus.lua
```

A project type for any given markdown publishing system will have its own variant, and will often also require a filters to deal with non-standard constructs and other vagaries of the target system.


# quarto-web/docs/journals/index.qmd

---
title: "Journal Articles"
---

## Overview

Quarto supports the creation of custom formats that extend base formats like `pdf`, `html`, and `docx`. The custom format system is very flexible, and has been designed to accommodate the creation of articles for publishing in professional Journals.

A major focus is single-source publishing: the same Quarto document source should be capable of producing both HTML and LaTeX output, and should also be capable of creating the LaTeX required for submission to multiple Journals. Key capabilities that enable this include:

-   The ability to flexibly adapt the native LaTeX templates provided by Journals for use with Pandoc.

-   The use of spans and divs to apply formatting (which enables targeting by CSS for HTML output and LaTeX macros/environments for PDF output).

-   A standardized schema for authors and affiliations so that you can express this data once and then have it automatically formatted according to the styles required for various Journals.

-   The use of Citation Style Language (CSL) to automate the formatting of citations and bibliographies according to whatever style is required by various Journals.

## Journal Formats

The Quarto team has developed several Journal formats and made them available within the [quarto-journals](https://github.com/quarto-journals/) GitHub organization. These formats include:

-   [ACM](https://github.com/quarto-journals/acm) [(preview)](https://quarto-journals.github.io/acm/)
-   [PLOS](https://github.com/quarto-journals/plos) [(preview)](https://quarto-journals.github.io/plos/)
-   [ASA](https://github.com/quarto-journals/jasa) [(preview)](https://quarto-journals.github.io/jasa/)
-   [Elsevier](https://github.com/quarto-journals/elsevier) [(preview)](https://quarto-journals.github.io/elsevier/)
-   [Biophysical](https://github.com/quarto-journals/biophysical-journal) [(preview)](https://quarto-journals.github.io/biophysical-journal/)
-   [ACS](https://github.com/quarto-journals/acs) [(preview)](https://quarto-journals.github.io/acs/)
-   [JSS](https://github.com/quarto-journals/jss) [(preview)](https://quarto-journals.github.io/jss/)

Many more formats will be added over time and we welcome proposals from the community for contributed formats (please post an issue at <https://github.com/quarto-journals/article-format-template/issues> if you are interested in contributing a format).

The `quarto use template` command can be used to create an article from one these formats. For example:

```{.bash filename="Terminal"}
quarto use template quarto-journals/acm
quarto use template quarto-journals/plos
quarto use template quarto-journals/elsevier
quarto use template quarto-journals/acs
quarto use template quarto-journals/jss
```

Note that the above commands will create a brand new article with default contents. In some cases you may want to use a Journal format in an existing document or project without copying the entire template. In that case you can just add the format extension by itself. For example:

```{.bash filename="Terminal"}
quarto add quarto-journals/acm
quarto add quarto-journals/plos
```

Follow the links for any of the formats above to learn more about how to use them with your own articles.

## Creating Formats

While the list of supported journals on [quarto-journals](https://github.com/quarto-journals/) will grow over time, it's likely that many users will want to create their own Journal formats. Creating a new format typically involves:

1.  Adapting the LaTeX template typically provided by Journals for use with Quarto.
2.  Selecting the appropriate citation processing and style for use with the format.
3.  Creating a `template.qmd` that demonstrates using the format.
4.  Optionally, ensuring that both HTML and LaTeX articles are well supported.

See the article on [Journal Formats](formats.qmd) for additional details on creating your own formats.


# quarto-web/docs/journals/templates.qmd

---
title: "Article Templates"
---

{{< include ../extensions/_extension-version.qmd >}}

## Overview

Journal article formats often require fine grained control of generated output as well as the ability to use Journal-specific commands and directives. This can be achieved for Quarto formats by providing custom Pandoc templates (LaTeX and/or HTML). Often these templates are a mix of Journal-specific LaTeX and standard directives required by Pandoc. This article describes how to create custom Journal templates that behave well with Pandoc and produce high-fidelity publisher ready output.

## Templates

Quarto uses [Pandoc templates](https://pandoc.org/MANUAL.html#templates) to generate the rendered output from a markdown file. A Pandoc template is a mix of format specific content and variables. The variables will be replaced with their values from a rendered document. For example, the most basic template looks like:

``` {.latex filename="mytemplate.tex"}
\documentclass{scrartcl}
\begin{document}
$body$
\end{document}
```

In the above template, the `$body$` variable will be replaced with the LaTeX that is generated from the body of the document. If the body text is `Hello **world**!` in Markdown, the value of `$body$` will be `Hello \textbf{world}!`.

By providing your own custom template used when rendering, you have complete control of the final output. You can provide this custom template to be used when rendering like this:

``` yaml
format:
  pdf:
    template: mytemplate.tex
```

For more complete information about template syntax, see [Template syntax](https://pandoc.org/MANUAL.html#template-syntax).

## Template Partials

Replacing an entire template gives you complete control of the rendered output, but many features of Pandoc and Quarto depend upon code and variables that appear in the built in templates. If you replace the entire template and omit these variables, features will not work properly.

It's therefore recommended that you take one of two approaches when authoring templates:

1.  Selectively [replace partials](#replacing-partials) that exist within the master LaTeX or HTML template.

2.  Replace the entire LaTeX or HTML template, but then [include partials](#including-partials) provided with Quarto to ensure that your template takes advantage of all Pandoc and Quarto features.

Below we'll cover both of these approaches. Note that after reviewing this documentation you may also want to check out the source code of formats published on [quarto-journals](https://github.com/quarto-journals/) for additional examples.

### Replacing Partials {#replacing-partials}

For LaTeX / PDF and HTML output, Quarto provides built in templates that are composed of a set of 'partial' template files. For these formats, you may replace portions of Quarto's built in template, allowing you to customize just a portion of the template without needing to replace the whole thing. A simple partial to provide custom handling of the document title in LaTeX looks like:

``` {.latex filename="title.tex"}
\title{$title$}
\author{$for(author)$$author$$sep$ \and $endfor$}
\date{$date$}
```

You provide this partial to Quarto like:

``` yaml
format:
  pdf:
    template-partials:
      - title.tex
```

When Quarto renders a document with a partial, it will use the built in template but replace a portion of the template with the provided partial. In the above case, the LaTeX title will be replaced with the implementation provided as the partial, while the rest of the built in template will be used.

Note that the name of the partial files is important. You choose which portion of the template to replace by providing a partial with that name. You can see the list of partials available in [HTML Partials] and [LaTeX Partials] below.

### Including Partials {#including-partials}

In addition to replacing built in partials with your own, you may also choose to use built in partials when composing your own template. This allows you to create a template that takes advantage of the capabilities and options provided by Quarto and Pandoc without copying and maintaining the entire template code. For example, you can use the `$pandoc.tex()$` partial to include pandoc configuration for text highlighting, tables, graphics, tight lists, citations, and header includes:

``` {.latex filename="my-template.tex"}
\documentclass{scrartcl}
$pandoc.tex()$
\begin{document}
$body$
\end{document}
```

This modular approach means that is easier to implement templates that:

-   Include required elements of Pandoc templates

-   Support general Pandoc features and options

-   Provide only the minimal LaTeX or HTML rather than being required to provide all of it

## LaTeX Partials

View the Quarto LaTeX template and partials [source code here](https://github.com/quarto-dev/quarto-cli/tree/main/src/resources/formats/pdf/pandoc). Note that latex.template is a copy of the complete Pandoc template that the Quarto template and partials is based upon.

template.tex

:   The core LaTeX template which includes the basic document skeleton plus the following partials. This can't be replaced as a `partial`, instead use the `template` option to provide your own template.

doc-class.tex

:   Contains the document class declaration and options. By default we provide the identical document class that Pandoc provides, implementing many features. If you override this (which will be common), you will need to either implement support for the document class options or be aware that those options (e.g. font-size, paper-size, classoption, etc...) will not be supported in your output.

title.tex

:   Provides configuration of document metadata for writing the title block. Note that in addition to these templates and partials, Quarto will also make normalized authors and affiliations data available to the template, making is easy to write custom title blocks against a standard schema.

before-body.tex

:   Implements the frontmatter, title page, and abstract.

after-body.tex

:   Provides a placeholder to attach content at the end of the body.

toc.tex

:   Creates the table of contents, list of figures, and list of tables.

before-bib.tex

:   Placed after the content of the document, but before the bibliography. By default contains nothing. (Placed here as a couple of templates seemed to have commands here, but I think we may be able to remove).

biblio.tex

:   Creates the bibliography.

pandoc.tex

:   This includes configuration for text highlighting, tables, graphics, tight lists, citations, and header includes. In general, this partial must always be included within your custom template. In some circumstances, you may know that certain capabilities will not be needed, so you this partial is further composed of the following partials, which could be used if sensible:

::: {style="margin-left: 2em;"}

tightlist.tex

:   Provides the tight list command.

tables.tex

:   Provides configuration for the output of tables, table captioning, and footnotes within tables.

graphics.tex

:   Provides image scaling and placement configuration.

citations.tex

:   When using CSL references, provides configuration and commands for outputting the bibliography.
:::

See the [full source code](https://github.com/quarto-dev/quarto-cli/blob/main/src/resources/formats/pdf/pandoc/template.tex) for the Quarto LaTeX template to see how these partials are invoked by default.

## HTML Partials

View the Quarto html template and partials [source code here](https://github.com/quarto-dev/quarto-cli/tree/main/src/resources/formats/html/pandoc). Note that `html.template` is a copy of the complete Pandoc template that the Quarto template and partials is based upon.

Quarto's HTML template is broken down into the following components:

template.html

:   The core HTML template which includes the basic document skeleton plus the following partials. This can't be replaced as a `partial`, instead use the `template` option to provide your own template.

metadata.html

:   Populates basic document metadata into the HTML document head. More advanced metadata elements are not currently implemented within this template (e.g. social media, academic metadata) but are implemented as post processors.

title-block.html

:   Provides the title block for the document. 

toc.html

:   Provide the table of contents target for the document

## Revealjs Partials

View the Quarto Revealjs template and partials [source code here](https://github.com/quarto-dev/quarto-cli/tree/main/src/resources/formats/revealjs/pandoc). Note that `revealjs.template` is a copy of the complete Pandoc template that the Quarto template and partials is based upon.

template.html

:   The core Revealjs templates which includes the basic presentation skeleton plus the following partials. This can't be replaced as a `partial`, instead use the `template` option to provide your own template.

title-slide.html

:   HTML used for the presentation title slide.

toc-slide.html

:   HTML used for the presentation table of contents.


# quarto-web/docs/journals/formats.qmd

---
title: "Journal Formats"
example-org: quarto-journals
example-format: acm
---

{{< include ../extensions/_extension-version.qmd >}}

## Overview

This article provides a guide to creating your own custom Journal formats. As a supplement to this guide we also recommend the following learning resources:

-   The source code for the Journal article formats available from the [quarto-journals](https://github.com/quarto-journals/) GitHub organization.

-   The [GitHub template repository](https://github.com/quarto-journals/article-format-template) for creating new Journal formats. The code in the template repository is heavily annotated so creating a new repository using this template and experimenting with it is an excellent way to learn.

Journal custom formats can be used just like normal Quarto formats (e.g. `pdf` and `html`):

You can specify a custom format beneath the `format` key just like a built-in format. For example:

``` yaml
----
title: "My Document"
format:
   acm-pdf: 
     toc: true
---
```

Custom formats all derive from one of the base formats, and include that base format as a suffix. Formats can also provide multiple variations that derive from distinct base formats. For example:

``` yaml
----
title: "My Document"
toc: true
format:
   acm-pdf: default
   acm-html: default
---
```

Note that we moved the `toc` option to the top level since it is shared between both of the formats.

Custom formats can also be used with the `--to` argument to `quarto render`. For example:

``` {.bash filename="Terminal"}
quarto render document.qmd --to acm-pdf
```

## Quick Start

Here we'll describe how to create a simple Journal article format extension. We'll use the `quarto create` command to do this. If you are using VS Code or RStudio you should execute `quarto create` within their respective integrated Terminal panes. 

To get started, execute `quarto create extension journal` within the parent directory where you'd like the format to be created:

```{.bash filename="Terminal"}
$ quarto create extension journal
 ? Extension Name › aps
```

As shown above, you'll be prompted for an extension name. Type `aps` (an acronym for a fictional academic association) and press Enter---the Journal format extension is then created:

```bash
Creating extension at /Users/jjallaire/quarto/dev/aps:
  - Created README.md
  - Created template.qmd
  - Created _extensions/aps/aps.lua
  - Created _extensions/aps/styles.css
  - Created _extensions/aps/_extension.yml
  - Created _extensions/aps/header.tex
  - Created bibliography.bib
```

If you are running within VS Code or RStudio a new window will open with the extension project. 

Here's what the contents of the files in `_extensions/aps/` look like:

``` {.yaml filename="_extensions/aps/_extension.yml"}
title: Aps
author: J.J. Allaire
version: 1.0.0
quarto-required: ">=1.2.222"
contributes:
  formats:
    common:
      toc: true
      filters:
        - aps.lua
    pdf:
      include-in-header: header.tex
    html:
      css: styles.css
```

The main `_extension.yml` config file defines the output formats available for this Journal. Here we defined `pdf` and `html` formats, which will be available to Quarto documents as `aps-pdf` and `aps-html`, respectively.

The config file also points to a number of other files that are used to customize the appearance of the Journal article:

- `header.tex` --- Custom LaTeX header directives

- `styles.css` --- Custom CSS for HTML output

- `aps.lua` --- Lua filter for various custom transformations

Finally, the `template.qmd` provides a base example article for users of the format:

``` {.markdown filename="template.qmd"}
---
title: Aps Template
format:
  aps-pdf:
    keep-tex: true  
  aps-html: default
author:
  - name: Sarah Malloc
    affiliations:
      - name: An Organization
        department: The Department
        address: 1 Main St
        city: Boston
        country: USA
        postal-code: 02210-1022
      - A second affilication
    orcid: 0000-0000-0000-0000
    email: sm@example.org
    url: https://example.org/
  - name: Eliza Dealloc
    affiliations:
      - Another Affiliation
abstract: |
  This document is a template demonstrating the Aps format.
keywords: [template, demo]
bibliography: bibliography.bib  
---

## Introduction {#sec-intro}

*TODO* Create a template that demonstrates the appearance, formatting, layout, and functionality of your format. Learn more about journal formats at <https://quarto.org/docs/journals/>.
```

To develop your format, render/preview `template.qmd`, and then make changes to the various files in the `_extensions` directory (the preview will automatically refresh when you change these files).


## Example: ACM Format

The Quick Start above creates a very simple Journal article format. Here we'll walk through some of the code for a more complex example, the [ACM Format](https://github.com/quarto-journals/) available from [quarto-journals](https://github.com/quarto-journals/).

Before proceeding to the example we recommend you review these articles which cover some foundations that will be made use of in the example:

-   [Article Templates](templates.qmd)

-   [Authors & Affiliations](authors.qmd)

### Format Components

Here is what the source code repository for the ACM extension looks like:

``` default
.gitignore
.quartoignore
LICENSE
README.md
bibliography.bib
template.qmd
_extensions/
  acm/
    _extension.yml
    acm_proc_article-sp.cls
    sensys-abstract.cls
    include-in-header.tex
    acm-sig-proceedings.csl
    partials/
      doc-class.tex
      title.tex
      before-bib.tex
```

For the time being we'll ignore all of the files above the `_extensions` directory (those files aren't strictly part of the extension but rather provide documentation and a starter template---we'll describe their usage below).

-   The `_extensions` directory contains one or more extensions---in this case it contains the `acm` format extension.

-   The `_extension.yml` file declares the format extension and provides default metadata and options for articles created for the format (we'll do a deep dive into its contents below).

-   The `acm_proc_article-sp.cls` and `sensys-abstract.cls` files are LaTeX class files used by the ACM.

-   The `include-in-header.tex` file provides some standard content included in the preamble of ACM articles.

-   The `acm-sig-proceedings.csl` is a Citation Style Language (CSL) file that enables rendering of citations and bibliographies according to the standards of the ACM.

-   The `partials` directory contains some `.tex` files that override various parts of the standard Pandoc LaTeX template (see [Article Templates](templates.qmd) to learn more about partials).

Here's what the contents of `_extension.yml` look like:

``` yaml
title: ACM Journal Format
author: Charles Teague
version: 0.1.0
quarto-required: ">=1.2.0"
contributes:
  format:
    common:
      csl: acm-sig-proceedings.csl
      number-sections: true
    pdf:
      shift-heading-level-by: -1
      template-partials:
        - partials/before-bib.tex
        - partials/doc-class.tex
        - partials/title.tex
      include-in-header:
        - include-in-header.tex
```

As you can see, many of the files located in the `_extensions/acm` folder are referenced here. Also note that while there are several options declared for the `pdf` format, there are also some options declared in `common`---these options will be applied to `pdf` and will also be applied to other format variants (e.g. HTML) when they are developed.

### Format Template

Now let's return to the files outside of the `_extensions` directory. The `LICENSE` and `README.md` files provide documentation that is good form to include in all extensions. The `.gitignore` files masks selected files out of version control. The remainder of the files provide a format template that make it easier for users to get started with your format.

For any custom format that includes a `template.qmd`, users can get started with the format with a command like this:

``` {.bash filename="Terminal"}
quarto use template quarto-journals/acm
```

The files included within the ACM template are:

-   `template.qmd` is a starter template for using the format. Here's what the YAML document options for the template look like:

    ``` yaml
    ---
    title: Short Paper
    author:
      - name: Alice Anonymous
        email: alice@example.com
        affiliation: Some Institute of Technology
      - name: Bob Security
        email: bob@example.com
        affiliation: Another University
    abstract: |
      This is the abstract.
      It consists of two paragraphs.
    format:
      acm-pdf: 
        keep-tex: true  
    bibliography: bibliography.bib
    ---
    ```

-   `bibliography.bib` is a sample bibliography referenced by `template.qmd`

Note that the schema for author information used here is relatively straightforward. See the article on [Authors & Affiliations](authors.qmd) to learn about more sophisticated schemas for author information.

You can also include other files alongside `template.qmd` and they will be copied as well. Note that by default, Quarto will exclude common Github repository files when copying an extension template. This includes any file name or directory starting with a `.` (e.g. `.gitignore`), `README.md`, `LICENSE`, etc.. If you'd like, you can place a `.quartoignore` file in the root of your repository with each line of the file being a glob describing file(s) to ignore (using syntax like a `.gitignore` file).

{{< include ../extensions/_formats-common.qmd >}}

## Learning More

Here are some additional learning resources you may find valuable:

-   The source code for the Journal article formats available from the [quarto-journals](https://github.com/quarto-journals/) GitHub organization.

-   The [GitHub template repository](https://github.com/quarto-journals/article-format-template) for creating new Journal formats. The code in the template repository is heavily annotated so creating a new repository using this template and experimenting with it is an excellent way to learn.

-   In depth treatment of creating [Article Templates](templates.qmd) for Journals (including how to use partials to compose templates)

-   Review of the schema and options for expressing and rendering [Authors & Affiliations](authors.qmd).


# quarto-web/docs/journals/authors.qmd

---
title: "Authors & Affiliations"
---

{{< include ../extensions/_extension-version.qmd >}}

## Overview

An important goal for Quarto is to make it possible to use the same source document to produce multiple output formats. One significant challenge to overcome is defining a consistent way to express author and affiliation metadata such that articles targeting multiple Journals do not require special tweaking of authors and affiliations for each publication.

Quarto's answer to this challenge is two-fold:

1.  Parse a variety of expressions of authors and affiliations into a standard schema.

2.  Provide de-normalized views of authors together with affiliations such that it is straightforward for template authors to create the LaTeX required by Journals.

Below we'll explore these facilities in more detail from the standpoint of template authors. To learn more about these facilities from the perspective of article writers, see [Authors & Affiliations](/docs/authoring/front-matter.qmd#authors-and-affiliations).

::: callout-note
Note that while there is a great deal of variety afforded in how authors and affiliations are specified, for a given Journal `template.qmd` you will likely have a preferred approach, and it's good form to seed the template with an example of this approach.
:::

## Author Metadata

Quarto will look in the `author` or `authors` field for data that can be parsed into a normalized representation of authors. This can be as simple as a name of list of names:

``` yaml
author:   
  - Norah Jones   
  - Bill Gates
```

Or alternatively can be a complex data structure expressing a variety of properties and attributes of authors along with their affiliations:

``` yaml
author:
  - name: Bill Gates
    orcid: 0000-0003-1689-0557
    email: bill@gates.com
    affiliations:
      - name: Bill & Melinda Gates Foundation
        address: 440 5th Ave N
        city: Seattle
        state: WA
        postal-code: 98109-4631
```

For both of the above expressions, Quarto processes and normalizes the author and affiliation data into the keys described below.

### author

The `author` metadata key receives a simple list of names that will render properly in most existing Pandoc templates not aware of the Quarto extended schema.

### authors

The `authors` metadata key contains the normalized author data structure. Affiliations are referenced (rather than placed inline), so this typically shouldn't be used by templates to output author data. The order the authors appear in the metadata will be preserved.

### affiliations

The `affiliations` metadata key contains the normalized affiliation data structure. Ids are automatically assigned if not defined. Affiliations contain no reference to their authors, so are typically not used by templates to output affiliation data. The order the affiliations appear in the metadata will be preserved. Duplicate affiliations are removed.

### by-author

The `by-author` metadata key contains a denormalized version of the author data organized in the original order of the authors. Rather than referencing affiliations, each author will have the full parsed contents of affiliations available in the affiliations subkey, making it easy for template authors to iterate through authors and then, within that, their affiliations. The order the authors appear in the metadata will be preserved.

### by-affiliation

The `by-affiliation` metadata key contains a denormalized version of affiliation data in the original order the affiliations appeared. Author data appears in order in the authors subkey, which contains the full parsed author data. This makes it easy for template authors to iterate over affiliations and the authors for each affiliation. The order the affiliations appear in the metadata will be preserved.

## Author Schema

The complete, normalized, author schema is as follows:

``` yaml
author:
  - id: string
    number: number
    name:
      given: string
      family: string
      literal: string
      dropping-particle: string
      non-dropping-particle: string
    url: string
    email: string
    phone: string
    fax: string
    orcid: string
    note: string
    acknowledgements: string
    attributes:
      corresponding: boolean
      equal-contributor: boolean
      deceased: boolean
    roles: 
      # see schema below
    metadata: object
    affiliations: 
      # see schema below
```

### Names

Most often, users will write a single string for name, like:

``` yaml
author: Norah Jones
```

or perhaps like:

``` yaml
author:
  - name: Norah Jones
```

Which will be parsed into:

``` yaml
author:
  - name:
      given: Norah
      family: Jones
      literal: Norah Jones
```

Quarto will parse names using BibTeX (a la [openjournals/inara](https://github.com/openjournals/inara/blob/main/data/filters/normalize-author-names.lua)), supporting BibTeX's parsing behavior for comma count, capitalization, and so on. When the name is unparseable by BibTeX, Quarto will attempt to parse names into given and family using spaces (everything after the last space is considered a family name), but to disambiguate, you may provide separate keys for the given name, family name and particle:

``` yaml
name:
  given: Norah
  family: Jones
  dropping-particle: von
```

### Attributes

Recognized attribute keys that appear at the top level (for example, `corresponding`) will automatically be normalized under attributes. For example:

``` yaml
author:
  name: Norah Jones
  corresponding: true
```

would be normalized into:

``` yaml
author:
  - name:
      given: Norah
      family: Jones
      literal: Norah Jones
    attributes:
      corresponding: true
```

### Roles

Author roles can be specified with either `role` or `roles` and can be any of:

-   A single string:

    ``` yaml
    author: 
      role: "Conceived and designed the study"
    ```
-   An array of strings:

    ``` yaml
    author: 
      role: 
        - conceptualization
        - methodology
    ```
    
-   An array of key-value pairs of the form `role: contribution`:

    ``` yaml
    author: 
      role: 
        - conceptualization: lead
        - methodology: supporting
    ```

If a role matches one of the [CRediT roles or their aliases](https://github.com/quarto-dev/quarto-cli/blob/f65180a75e1cf2996328cd51cb4fd5d02d391511/src/resources/filters/modules/authors.lua#L119-L144), the additional properties `vocab-identifier`, `vocab-term`, and `vocab-term-indentifier`, will be added to the role with the appropriate value from the CRediT specification.

### Arbitrary Metadata

The normalized authors schema at the top level is a closed schema. Unrecognized keys that are passed in the root of authors will be normalized under the `metadata` key. For example:

``` yaml
author:
  name: Norah Jones
  corresponding: true
  custom-info: "custom value"
```

would be normalized into:

``` yaml
author:
  - name:
      given: Norah
      family: Jones
      literal: Norah Jones
    attributes:
      corresponding: true
    metadata:
      custom-info: "custom value"
```

Keys that are normalized into `metadata` should be considered potentially template specific and may not be present or depended upon when implementing a template.

## Affiliations Schema

The complete, normalized affiliations schema is defined as:

``` yaml
affiliations:
  - id: string
    number: number
    name: string
    department: string
    address: string
    city: string
    region: string
    country: string
    postal-code: string
    url: string
```

### Parsing Notes

-   You may specify either state or region- either will be normalized into the region key.

-   If you specify only a string for an affiliation, it will be used as the name of affiliation.

-   You may omit an id and the id will be automatically generated (a simple counter based id will be used).

-   The url field may also be populated by an `affiliation-url` key in the author, which preserves compatibility with Distill metadata for authors and affiliations.

## Combinations

To combine the above schemas, users may specify author and affiliations in a number of different ways. Each will be normalized into the standard schema described above.

### Inline Affiliations

You may write affiliations as simple string or complex affiliations inline. For example:

``` yaml
author:
  - name: Norah Jones
    affiliations:
      - Carnegie Mellon University
      - University of Chicago
```

or

``` yaml
author:
  - name: Norah Jones
    affiliations:
      - name: Carnegie Mellon University
        city: Pittsburgh
        state: PA
      - name: University of Chicago
        city: Chicago
        state: IL
```

### Reference Affiliations

You may write out the affiliations into a separate key and only reference the affiliation in the author. For example:

``` yaml
author:
  - name: Norah Jones
    affiliations:
      - ref: cmu
      - ref: chicago
affiliations:
  - id: cmu
    name: Carnegie Mellon University
    city: Pittsburgh
    state: PA
  - id: chicago
    name: University of Chicago
    city: Chicago
    state: IL
```

### Inline References

You may also assign ids to affiliations created in the author key and use those ids as references in other authors. For example:

``` yaml
author:
  - name: Norah Jones
    affiliations:
      - id: cmu
        name: Carnegie Mellon University
        city: Pittsburgh
        state: PA
      - id: chicago
        name: University of Chicago
        city: Chicago
        state: IL
  - name: John Hamm
    affiliations:
      - ref: cmu
      - name: University of California, San Diego
        city: San Diego
        state: CA
```


# quarto-web/docs/journals/_draft/create-extensions.qmd

---
title: Creating an Extension
draft: true
---

For an overview of Quarto extensions, see [the overview](index.qmd) of Quarto Extensions.

## Extension Structure

Quarto extensions are conceptually very simple though powerful. An extension is a bundle of metadata and resources that is made available to Quarto during the rendering of a document. When the user of the extension refers to the extension (for example by using a shortcode, by placing the extension name in a list of filters, or by using the extension format name as a render target), the contributions of the extension are merged into the render pipeline as appropriate.

Extensions are structured on the file system as follows:

``` {.bash filename="Terminal"}
# Extension root folder
_extensions/<organization-name>/<extension-name>/

# Extension YAML file
_extensions/<organization-name>/<extension-name>/_extension.yml

# Other resources
_extensions/<organization-name>/<extension-name>/*
```

The `_extension.yml` file provides the metadata and configuration of the extension.

Extensions can be hosted and distributed as tarballs via URL, but the easiest way to distribute and host them is to use Github. When distributing extensions with Github, the `organization-name` above corresponds to the Github organization name and the `extension-name` corresponds to the repo name. For example, for the repo:

`https://github.com/quarto-ext/fontawesome`

The extension folder is

``` {.bash filename="Terminal"}
# The extension root folder
_extensions/quarto-ext/fontawesome/
```

and the command to add, update, or remove this extension is:

``` {.bash filename="Terminal"}
quarto add quarto-ext/fontawesome
quarto update quarto-ext/fontawesome
quarto remove quarto-ext/fontawesome
```

## Extension Metadata

Each extension is defined by its `_extension.yml` file which contains the metadata about the extension as well as the what items it contributes when used. At the root level, specify the following information in the `_extension.yml` file:

`title`

:   The extension's name

`author`

:   The author of the extension

`version`

:   A semantic version number this release. When installing, updating, or releasing an extension, this version number will be used to present a summary of actions to the user.

`quarto-required`

:   A semantic version number indicating the minimum version of quarto required to run this extension.

`contributes`

:   The items that this extension will contribute to the render. There are three allowed subkeys:

::: {style="margin-left: 1em;"}

`shortcodes`

:   A list of shortcode files that should be loaded when this extension is installed.

`filters`

:   A list of filters that should be loaded when this extension is included in the list of filters used to render a document or project. The order of the filters in this list will be preserved.

`formats`:

:   A record containing the key value pairs of output formats and the metadata associated with that output format.
:::

## Filter Extensions

For example, a simple filter extension looks like:

``` yaml
title: My Filter Extension
author: Norah Jones
version: 0.0.1
contributes:
  filters:
    - extension.lua
```

For more information about authoring filters, see [Pandoc Filters](https://quarto.org/docs/authoring/filters.html#pandoc-filters).

## Shortcode Extensions

A simple shortcode filter extension looks like:

``` yaml
title: My Filter Extension
author: Norah Jones
version: 0.0.1
contributes:
  shortcodes:
    - shortcode.lua
```

For more information about authoring shortcodes, see [Shortcodes](https://quarto.org/docs/authoring/shortcodes.html).

## Format Extensions

And a simple format extension looks like:

``` yaml
title: My Filter Extension
author: Norah Jones
version: 0.0.1
contributes:
  formats:
    pdf:
      keep-tex: true
      pdf-engine: lualatex
      cite-method: natbib
    html:
      css: my-style.css
    
```

Format extensions permit you to combine metadata and resources to provide specific behavior when rendering specific output formats. For example, if you'd like to create LaTeX and PDF output targeting a specific academic journal, you could create a format that provides the proper Quarto metadata as well as referenced LaTeX class files and bibliography styles. That metadata will be activated when the user renders a document targeting the extension format, by doing:

`quarto render my-article.qmd –to <extension>-pdf`

### Common Metadata

If you have metadata that is common to any output format when your format extension is targeted, you can place that metadata under the `common` key. For example:

``` yaml
contributes:
  format:
    common:
      filters:
        - filter.lua
      shortcodes:
        - quarto-ext/fancy-text
```

### Resources

You can easily include other files and resources within a format extension by placing those files within the extension directory and using relative paths to reference them. These relative paths will be properly handled.

If there are resources that you need to have copied to the input directory as a part of rendering the document (for example, a `bst` file for LaTeX bibliographies or a logo file), you can provide `format-resources`, which is a list of file paths. Each of these files will be copied into the directory containing the input that is being rendered when the document is rendered.

### Embedding Other Extensions in a Format Extension

It is often convenient to include the functionality from an extension in another extension, particularly for format extensions which might embed shortcodes or filters from another extension. This is allowed, but installing extensions into another extension must be done with a special syntax to embed them in the extension.

For example, running the following command from the the directory which contains your `_extensions` directory:

``` {.bash filename="Terminal"}
$ quarto add quarto-ext/fancy-text --embed quarto-journals/jss
```

Will add the `quarto-ext/fancy-text` extension into the `quarto-journals/jss` extension in the `_extensions` folder. Once you have added the embedded extension, you can simply refer to it using its name under the `filters` or `shortcodes` keys in the relevant formats.

### Complete Example YML

``` yml
title: Journal of Statistical Software Format
author: Charles Teague
version: 0.9.2
contributes:
  format:
    common:
      filters:
        - filter.lua
      shortcodes:
        - quarto-ext/fancy-text
      knitr:
        opts_chunk:
          R.options:
            prompt: "R> "
            continue: "+"
    pdf:
      shift-heading-level-by: -1
      tbl-cap-location: bottom
      highlight-style: none
      include-in-header:
        text: |
          \usepackage{orcidlink,thumbpdf,lmodern}

          \newcommand{\class}[1]{`\code{#1}'}
          \newcommand{\fct}[1]{\code{#1()}}
      fig-width: 4.9 # 6.125" * 0.8, as in template
      fig-height: 3.675 # 4.9 * 3:4
      template-partials:
        - "partials/doc-class.tex"
        - "partials/title.tex"
        - "partials/before-body.tex"
        - "partials/_print-address.tex"
        - "partials/_print-author.tex"
      cite-method: natbib
      biblio-config: false
      format-resources:
        - jss.bst
        - jss.cls
        - jsslogo.jpg
    html:
      number-sections: true
      toc: true
```

The above could be rendered using:

``` {.bash filename="Terminal"}
$ quarto render my-article.qmd --to jss-pdf
```

Note that the command

``` {.bash filename="Terminal"}
$ quarto render my-article.qmd --to pdf
```

Would render a simple pdf. Since the extension name prefix is omitted, none of the extensions `pdf` or `common` metadata is merged into the document metadata when rendering.


# quarto-web/docs/journals/_draft/extension-templates.qmd

---
title: Extension Templates
draft: true
---

For format extensions in particular, it is often very useful to have a sample document that can demonstrate the functionality of the format extension and serve as a starting point for a user who is authoring a document targeting that format. You can support this by adding a template to the repository that hosts your Quarto extension. Users can then choose whether they'd like to simply install your extension (for example, into an existing project) or install the extension and use a template to start a new project.

## Using a Template

When you'd like to install an an extension and use its template, you can do so with the following command:

`quarto use template <extension>`

For example, to install the format extension for author PLOS journal articles, you can use the command:

`quarto use template quarto-journals/plos`

When the `quarto use template` command is executed, the extension hosted at `quarto-journals/plos` will be installed, but in addition, other files in the repo will be placed in the directory, providing the user a scaffolding to get started.

If the command is run in an empty directory, you will be prompted whether you'd like to use the existing directory or whether you'd like to create a new directory. If the command is run in a directory which contains other files or directories, you will be prompted for the name of a directory to create.

## Template.qmd

Usually, an extension template will provide a `template.qmd` file in the root of the repository. This is the primary `qmd` file that demonstrates the functionality of the extension or serves as the starting point for the user. When the extension template is copied into the target directory, the `template.qmd` will automatically be renamed to match the name that the user provided for the directory.

## Choosing Which Files Exclude

By default, Quarto will exclude common Github repository files when copying an extension template. This includes any file name or directory starting with a `.` (e.g. `.gitignore`), `README.md`, `LICENSE`, and other such files. If you'd like, you can place `.quartoignore` file in the root of your repository with each line of the file being a glob describing file(s) to ignore (using syntax like a `.gitignore` file).

Unless excluded, any files or folders within the repository that aren't automatically ignored or listed in the `.quartoignore` file be copied into the target directory when using an extension template.

If you want to include a file that is automatically excluded, prepend a `!` to the glob (for example, `!README.md`).

## Creating a Template

To create a template, you can add any number of files to the root of your repository and they will be treated as template files when your extension is used in a directory. We recommend that you:

-   Provide a `template.qmd` file that will serve as the main document

-   Include other files that are used by your `template.qmd`, for example a bibliography file that is used, a CSL file that is used, or images, stylesheets or other files.

-   Provide a `_quarto.yml` file if appropriate

Your extension repository extension is structured in such a a way that you can test your extension and the template by simply rendering the `template.qmd` file right in the root of your repository. The `template.qmd` will be able to load your extension just as it would when installed, so testing and iterating should be as simple as working within your extension directory until you're satisfied (without the need to repeatedly install or update the extension in order to test it).


# quarto-web/docs/computations/execution-options.qmd

---
title: Execution Options
format: html
---

## Output Options

There are a wide variety of options available for customizing output from executed code. All of these options can be specified either globally (in the document front-matter) or per code-block. For example, here's a modification of the Python example to specify that we don't want to "echo" the code into the output document:

``` yaml
---
title: "My Document"
execute:
  echo: false
jupyter: python3
---
```

Note that we can override this option on a per code-block basis. For example:

```{{python}}
#| echo: true

import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.show()
```

Code block options are included in a special comment at the top of the block (lines at the top prefaced with `#|` are considered options).

Options available for customizing output include:

+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option    | Description                                                                                                                                                                                       |
+===========+===================================================================================================================================================================================================+
| `eval`    | Evaluate the code chunk (if `false`, just echos the code into the output).                                                                                                                        |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `echo`    | Include the source code in output                                                                                                                                                                 |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `output`  | Include the results of executing the code in the output (`true`, `false`, or `asis` to indicate that the output is raw markdown and should not have any of Quarto's standard enclosing markdown). |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `warning` | Include warnings in the output.                                                                                                                                                                   |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `error`   | Include errors in the output (note that this implies that errors executing code will not halt processing of the document).                                                                        |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `include` | Catch all for preventing any output (code or results) from being included (e.g. `include: false` suppresses all output from the code block).                                                      |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Here's a Knitr example with some of these additional options included:

````         
---
title: "Knitr Document"
execute:
  echo: false
---

```{{r}}
#| warning: false

library(ggplot2)
ggplot(airquality, aes(Temp, Ozone)) + 
  geom_point() + 
  geom_smooth(method = "loess", se = FALSE)
```

```{{r}}
summary(airquality)
```
````

::: callout-tip
When using the Knitr engine, you can also use any of the available native options (e.g. `collapse`, `tidy`, `comment`, etc.). See the [Knitr options documentation](https://yihui.org/knitr/options/) for additional details. You can include these native options in option comment blocks as shown above, or on the same line as the `{r}` as shown in the Knitr documentation.
:::

## Figure Options

There are a number of ways to control the default width and height of figures generated from code. First, it's important to know that Quarto sets a default width and height for figures appropriate to the target output format. Here are the defaults (expressed in inches):

| Format                  | Default   |
|-------------------------|-----------|
| Default                 | 7 x 5     |
| HTML Slides             | 9.5 x 6.5 |
| HTML Slides (reveal.js) | 9 x 5     |
| PDF                     | 5.5 x 3.5 |
| PDF Slides (Beamer)     | 10 x 7    |
| PowerPoint              | 7.5 x 5.5 |
| MS Word, ODT, RTF       | 5 x 4     |
| EPUB                    | 5 x 4     |
| Hugo                    | 8 x 5     |

These defaults were chosen to provide attractive well proportioned figures, but feel free to experiment to see whether you prefer another default size. You can change the default sizes using the `fig-width` and `fig-height` options. For example:

``` yaml
---
title: "My Document"
format: 
  html:
    fig-width: 8
    fig-height: 6
  pdf:
    fig-width: 7
    fig-height: 5
---
```

How do these sizes make their way into the engine-level defaults for generating figures? This differs by engine:

-   For the Knitr engine, these values become the default values for the `fig.width` and `fig.height` chunk options. You can override these default values via chunk level options.

-   For Python, these values are used to set the [Matplotlib](https://matplotlib.org/stable/tutorials/introductory/customizing.html) `figure.figsize` rcParam (you can of course manually override these defaults for any given plot).

-   For Julia, these values are used to initialize the default figure size for the [Plots.jl](https://docs.juliaplots.org/stable/) GR backend.

    If you are using another graphics library with Jupyter and want to utilize these values, you can read them from `QUARTO_FIG_WIDTH` and `QUARTO_FIG_HEIGHT` environment variables.

::: callout-caution
When using the Knitr engine, `fig-width` and `fig-height` are supported on a per-cell basis. But when using the Jupyter engine, these options only have an effect if specified at the document- or project-level metadata.
:::

### Caption and Alt Text

You can specify the caption and alt text for figures generated from code using the `fig-cap` and `fig-alt` options. For example, here we add these options to a Python code cell that creates a plot:

```{{python}}
#| fig-cap: "Polar axis plot"
#| fig-alt: "A line plot on a polar axis"

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

## Inline Code

Jupyter, Knitr and OJS all support executing inline code within markdown (e.g. to allow narrative to automatically use the most up to date computations). The syntax for this varies across the engines.

### Jupyter

To include executable expressions within markdown in a Python notebook, you use [`IPython.display.Markdown`](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html) to dynamically generate markdown from within an ordinary code cell. For example, if we have a variable `radius` we can use it within markdown as follows:

```{{python}}
#| echo: false
radius = 10
from IPython.display import Markdown
Markdown(f"The _radius_ of the circle is **{radius}**.")
```

You can do the same in a Julia notebook using the [`Markdown`](https://docs.julialang.org/en/v1/stdlib/Markdown/) package:

```{{julia}}
#| echo: false
radius = 10
using Markdown
Markdown.parse("""
The radius of the circle is $radius.
""")
```

Note that we also include the `echo: false` option to ensure that the code used to generate markdown isn't included in the final output.

### Knitr

To include executable expressions within markdown for Knitr, enclose the expression in `` `r ` ``. For example, if we have a variable `radius` we can use it within markdown as follows:

``` markdown
## Circle

The radius of the circle is `r radius`.
```

### OJS

To include reactive OJS expressions within markdown, use the syntax `${expr}`. For example, if we have a reactive called `radius` we can use it within markdown as follows:

``` markdown
## Circle

The radius of the circle is ${radius}
```

## Raw Output

The `output: asis` option enables you to generate raw markdown output. When `output: asis` is specified none of Quarto's standard enclosing divs will be included. For example, here we specify `output: asis` in order to generate a pair of headings:

::: panel-tabset
## Jupyter

```{{python}}
#| echo: false
#| output: asis

print("# Heading 1\n")
print("## Heading 2\n")
```

## Knitr

```{{r}}
#| echo: false
#| output: asis

cat("# Heading 1\n")
cat("## Heading 2\n")
```
:::

Which generates the following output:

``` default
# Heading 1

## Heading 2
```

Note that we also include the `echo: false` option to ensure that the code used to generate markdown isn't included in the final output.

If we had not specified `output: asis` then the output would have been this:

```` default
::: {.cell-output-stdout}
```
# Heading 1

## Heading 2

```
:::
````

For the Jupyter engine, you can also create raw markdown output using the functions in `IPython.display`. For example:

```{{python}}
#| echo: false
radius = 10
from IPython.display import Markdown
Markdown(f"The _radius_ of the circle is **{radius}**.")
```

{{< include _knitr-options.md >}}

## Intermediates

On the way from markdown input to final output, there are some intermediate files that are created and automatically deleted at the end of rendering. You can use the following options to keep these intermediate files:

+--------------+------------------------------------------------------------------------------------------------+
| Option       | Description                                                                                    |
+==============+================================================================================================+
| `keep-md`    | Keep the markdown file generated by executing code.                                            |
+--------------+------------------------------------------------------------------------------------------------+
| `keep-ipynb` | Keep the notebook file generated from executing code (applicable only to markdown input files) |
+--------------+------------------------------------------------------------------------------------------------+

For example, here we specify that we want to keep the jupyter intermediate file after rendering:

``` yaml
---
title: "My Document"
execute:
  keep-ipynb: true
jupyter: python3
---
```

## Fenced Echo

If you are writing a tutorial or documentation on using Quarto code blocks, you'll likely want to include the fenced code delimiter (e.g. ```` ```{python} ````) in your code output to emphasize that executable code requires that delimiter. You can do this using the `echo: fenced` option. For example, the following code block:

```{{python}}
#| echo: fenced
1 + 1
```

Will be rendered as:

```{python}
#| echo: fenced
1 + 1
```

This is especially useful when you want to demonstrate the use of cell options. For example, here we demonstrate the use of the `output` and `code-overflow` options:

```{{python}}
#| echo: fenced
#| output: false
#| code-overflow: wrap
1 + 1
```

This code block appears in the rendered document as:

```{python}
#| echo: fenced
#| output: false
#| code-overflow: wrap
1 + 1
```

Note that all YAML options will be included in the fenced code output *except for* `echo: fenced` (as that might be confusing to readers).

This behavior can also be specified at the document level if you want all of your executable code blocks to include the fenced delimiter and YAML options:

``` yaml
---
title: "My Document"
format: html
execute:
  echo: fenced
---
```

#### Unexecuted Blocks

{{< include _unexecuted-blocks.md >}}

## Engine Binding

Earlier we said that the engine used for computations was determined automatically. You may want to customize this---for example you may want to use the Jupyter [R kernel](https://github.com/IRkernel/IRkernel) rather than Knitr, or you may want to use Knitr with Python code (via [reticulate](https://rstudio.github.io/reticulate/)).

Here are the basic rules for automatic binding:

+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Extension | Engine Binding                                                                                                                                                                                                                         |
+===========+========================================================================================================================================================================================================================================+
| .qmd      | Use Knitr engine if an `{r}` code block is discovered within the file                                                                                                                                                                  |
|           |                                                                                                                                                                                                                                        |
|           | Use Jupyter engine if *any other* executable code block (e.g. `{python}`, `{julia}`, `{bash}`, etc.) is discovered within the file. The kernel used is determined based on the language of the first executable code block discovered. |
|           |                                                                                                                                                                                                                                        |
|           | Use no engine if no executable code blocks are discovered.                                                                                                                                                                             |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| .ipynb    | Jupyter engine                                                                                                                                                                                                                         |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| .Rmd      | Knitr engine                                                                                                                                                                                                                           |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| .md       | No engine (note that if an `md` document does contain executable code blocks then an error will occur)                                                                                                                                 |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

For `.qmd` files in particular, you can override the engine used via the `engine` option. For example:

``` markdown
engine: jupyter
```

``` markdown
engine: knitr
```

You can also specify that no execution engine should be used via `engine: markdown`.

The presence of the `knitr` or `jupyter` option will also override the default engine:

``` markdown
knitr: true
```

``` markdown
jupyter: python3
```

Variations with additional engine-specific options also work to override the default engine:

``` markdown
knitr:
  opts_knit:
    verbose: true
```

``` markdown
jupyter:
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
```

## Shell Commands

Using shell commands (from Bash, Zsh, etc.) within Quarto computational documents differs by engine. If you are using the Jupyter engine you can use [Jupyter shell magics](https://jakevdp.github.io/PythonDataScienceHandbook/01.05-ipython-and-shell-commands.html). For example:

```` markdown
---
title: "Using Bash"
engine: jupyter
---

```{{python}}
!echo "foo"
```
````

Note that `!` preceding `echo` is what enables a Python cell to be able to execute a shell command.

If you are using the Knitr engine you can use ```` ```{bash} ```` cells, for example:

```` markdown
---
title: "Using Bash"
engine: knitr
---

```{{bash}}
echo "foo" 
```
````

Note that the Knitr engine also supports ```` ```{python} ```` cells, enabling the combination of R, Python, and Bash in the same document


# quarto-web/docs/computations/ojs.qmd

---
title: "Using Observable"
execute:
  echo: false
search: false
---

## Overview

Quarto includes native support for [Observable JS](https://observablehq.com/@observablehq/observables-not-javascript), a set of enhancements to vanilla JavaScript created by [Mike Bostock](https://en.wikipedia.org/wiki/Mike_Bostock) (also the author of [D3](https://d3js.org/)). Observable JS is distinguished by its [reactive runtime](https://github.com/observablehq/runtime), which is especially well suited for interactive data exploration and analysis.

The creators of Observable JS (Observable, Inc.) run a hosted service at <https://observablehq.com/> where you can create and publish notebooks. Additionally, you can use Observable JS ("OJS") in standalone documents and websites via its [core libraries](https://github.com/observablehq). Quarto uses these libraries along with a [compiler](https://github.com/asg017/unofficial-observablehq-compiler/tree/beta) that is run at render time to enable the use of OJS within Quarto documents.

OJS works in any Quarto document (plain markdown as well as Jupyter and Knitr documents). Just include your code in an `{ojs}` executable code block. The rest of this article explains the basics of using OJS with Quarto.

## Example

We'll start with a simple example based on Allison Horst's [Palmer Penguins](https://allisonhorst.github.io/palmerpenguins/) dataset. Here we look at how penguin body mass varies across both sex and species (use the provided inputs to filter the dataset by bill length and island):

```{ojs}
filtered = transpose(data).filter(function(penguin) {
  return bill_length_min < penguin.bill_length_mm &&
         islands.includes(penguin.island);
})
```

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

Let's take a look at the source code for this example. First we create an `{ojs}` cell that reads in some data from a CSV file using a [FileAttachment](https://observablehq.com/@observablehq/file-attachments):

```{{ojs}}
data = FileAttachment("palmer-penguins.csv").csv({ typed: true })
```

The example above doesn't plot all of the data but rather a filtered subset. To create our filter we'll need some inputs, and we'll want to be able to use the values of these inputs in our filtering function. To do this, we use the `viewof` keyword and with some standard [Inputs](https://observablehq.com/@observablehq/inputs):

```{{ojs}}
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

Now we write the filtering function that will transform the `data` read from the CSV using the values of `bill_length_min` and `island`.

```{{ojs}}
filtered = data.filter(function(penguin) {
  return bill_length_min < penguin.bill_length_mm &&
         islands.includes(penguin.island);
})
```

Here we see reactivity in action: we don't need any special syntax to refer to the dynamic input values, they "just work", and the filtering code is automatically re-run when the inputs change. This works in much the same way a spreadsheet works when you update a cell and other cells that refer to it are recalculated.

Finally, we'll plot the filtered data using [Observable Plot](https://observablehq.com/@observablehq/plot) (an open-source JavaScript library for quick visualization of tabular data):

```{{ojs}}
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

Note that as with our inputs, we refer to the `filtered` variable with no special syntax---the plotting code will be automatically re-run whenever `filtered` changes (which in turn is updated whenever an input changes).

That covers a basic end-to-end use of OJS (see the [Penguins](/docs/interactive/ojs/examples/penguins.qmd) examples for the full source code).

::: {.callout-tip appearance="simple"}
If you take a look at the [Penguins](/docs/interactive/ojs/examples/penguins.qmd) code, you'll notice something curious: the inputs and plotting code are defined *before* the data processing code. This demonstrates a critical difference between OJS cell execution and traditional notebooks: cells do not need to be defined in any particular order.

Because execution is fully reactive, the runtime will automatically execute cells in the correct order based on how they reference each other. This is more akin to a spreadsheet than a traditional notebook with linear cell execution.
:::

## Libraries

Our example above made use of several standard libraries, including:

1.  [Observable stdlib](https://github.com/observablehq/stdlib) --- Core primitives for DOM manipulation, file handling, importing code, and much more.

2.  [Observable Inputs](https://github.com/observablehq/inputs) --- Standard inputs controls including sliders, drop-downs, tables, check-boxes, etc.

3.  [Observable Plot](https://github.com/observablehq/plot) --- High level plotting library for exploratory data visualization.

The libraries are somewhat special because they are automatically available within notebooks on <https://observablehq.com> as well as within `{ojs}` cells in Quarto documents.

Using other JavaScript libraries is also straightforward, they just need to be explicitly imported. For example, here we import a some libraries using the [require](https://github.com/observablehq/stdlib#require) function (which in turn loads NPM modules from [jsDelivr](https://www.jsdelivr.com/){.uri}):

```{{ojs}}
d3 = require("d3@7")
topojson = require("topojson")
```

See the article on [Libraries](/docs/interactive/ojs/libraries.qmd) to learn more about using standard and third-party libraries.

## Data Sources

In our initial example we used a [FileAttachment](https://github.com/observablehq/stdlib#file-attachments) as our data source. File attachments support many formats including CSV, TSV, JSON, Arrow (uncompressed), and SQLite so are a convenient way to read a dataset that has already been prepared for analysis.

Frequently though you'll need to do some pre-processing of your data in Python or R before it's ready for visualization. Within Quarto, you can do this pre-processing during document render then make the results available to OJS.

Use the `ojs_define()` function from Python or R to define variables that you want to use within JavaScript. For example, to reproduce the simple CSV read in Python you might do this:

```{python}
#| echo: fenced
import pandas as pd
penguins = pd.read_csv("palmer-penguins.csv")
ojs_define(data = penguins)
```

The call to `ojs_define(data = penguins)` says that we want to make a variable named `data` (with the value of the `penguins` data frame) available to OJS

Depending on the visualization library you use, one additional step may be required to consume the data from JavaScript. In this case, the `Plot` function expects data by row rather than by column, so we `transpose()` it before filtering:

```{{ojs}}
filtered = transpose(data).filter(function(penguin) {
  return bill_length_min < penguin.bill_length_mm &&
         islands.includes(penguin.island);
})
```

See the article on [Data Sources](/docs/interactive/ojs/data-sources.qmd) to learn more about the various ways to prepare and read data.

## OJS Cells

There are many options available to customize the behavior of `{ojs}` code cells, including showing, hiding, and collapsing code as well as controlling the visibility and layout of outputs.

The most important cell option to be aware of is the `echo` option, which controls whether source code is displayed. You'll have different preferences depending on whether you are embedding visualizations in an article or creating a notebook or full-on tutorial.

Code in `{ojs}` cells is displayed by default. To prevent display of code for an entire document, set the `echo: false` option in YAML metadata:

``` yaml
---
title: "My Document"
execute:
  echo: false
---
```

You can also specify this option on a per-cell basis. For example:

```{{ojs}}
//| echo: false
data = FileAttachment("palmer-penguins.csv").csv({ typed: true })
```

To learn about all of the options available, see the article on [OJS Cells](/docs/interactive/ojs/ojs-cells.qmd).

## Learning More

These articles go into more depth on using OJS in Quarto documents:

-   [Libraries](/docs/interactive/ojs/libraries.qmd) covers using standard libraries and external JavaScript libraries.

-   [Data Sources](/docs/interactive/ojs/data-sources.qmd) outlines the various ways to read and pre-process data.

-   [OJS Cells](/docs/interactive/ojs/ojs-cells.qmd) goes into more depth on cell execution, output, and layout.

-   [Shiny Reactives](/docs/interactive/ojs/shiny.qmd) describes how to integrate Shiny with OJS.

-   [Code Reuse](/docs/interactive/ojs/code-reuse.qmd) delves into ways to re-use OJS code across multiple documents.

If you want to learn more about the underlying mechanics of reactivity, check out these notebooks from [Mike Bostock](https://observablehq.com/@mbostock):

-   [Five Minute Introduction](https://observablehq.com/@observablehq/five-minute-introduction)

-   [Observable's not JavaScript](https://observablehq.com/@observablehq/observables-not-javascript)

-   [Introduction to Views](https://observablehq.com/@observablehq/introduction-to-views)


-   [How Observable Runs](https://observablehq.com/@observablehq/how-observable-runs)


# quarto-web/docs/computations/python.qmd

---
title: "Using Python"
jupyter-language: "Python"
jupyter-screenshot: "![](../get-started/hello/images/jupyter-basics.png){.border fig-alt='A Jupyter notebook titled Quarto Basics containing some text, a code cell, and the result of the code cell, which is a line plot on a polar axis.'}"
vscode-extension: "[Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)"
vscode-screenshot: "![](images/python-vscode){.border fig-alt='Screen shot of VS Code editor with three vertical sections. The leftmost includes the file explorer, and quarto help. The second pane is the source code for a quarto file with python code. The third is interactive with Python running and output of the code cells shown.'}"
---

## Overview

Quarto supports executable Python code blocks within markdown. This allows you to create fully reproducible documents and reports---the Python code required to produce your output is part of the document itself, and is automatically re-run whenever the document is rendered.

If you have Python and the `jupyter` package installed then you have all you need to render documents that contain embedded Python code (if you don't, we'll cover this in the [installation](#installation) section below). Next, we'll cover the basics of creating and rendering documents with Python code blocks.

### Code Blocks

Code blocks that use braces around the language name (e.g. ```` ```{python} ````) are executable, and will be run by Quarto during render. Here is a simple example:

```` markdown
---
title: "matplotlib demo"
format:
  html:
    code-fold: true
jupyter: python3
---

For a demonstration of a line plot on a polar axis, see @fig-polar.

```{{python}}
#| label: fig-polar
#| fig-cap: "A line plot on a polar axis"

import numpy as np
import matplotlib.pyplot as plt

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
fig, ax = plt.subplots(
  subplot_kw = {'projection': 'polar'} 
)
ax.plot(theta, r)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.grid(True)
plt.show()
```
````

You'll note that there are some special comments at the top of the code block. These are cell level options that make the figure [cross-referenceable](../authoring/cross-references.qmd).

This document would result in the following rendered output:

![](../../images/hello-jupyter.png){.border fig-alt="Example output where header reads: matplotlib demo, the body reads: For a demonstration of a line plot on a polar axis, see Figure 1. Below the body text is a toggleable field to reveal the code, and the Figure 1 image with a caption that reads: Figure 1: A line plot on a polar axis."}

You can produce a wide variety of output types from executable code blocks, including plots, tabular output from data frames, and plain text output (e.g. printing the results of statistical summaries).

There are many options which control the behavior of code execution and output, you can read more about them in the article on [Execution Options](execution-options.qmd).

{{< include _jupyter-rendering.md >}}

## Installation {#installation}

If you already have Python 3 and Jupyter installed in your environment, then you should have everything required to render Jupyter notebooks with Python kernels.

{{< include _jupyter-install.md >}}

{{< include _jupyter-authoring-tools.md >}}

{{< include _jupyter-cache.md >}}

{{< include _caching-more.md >}}


## Kernel Selection

The Jupyter kernel used by Quarto is determined using the `jupyter` metadata option. For example, to use the [Xeus Python](https://github.com/jupyter-xeus/xeus-python) kernel, do this:

``` yaml
---
title: "My Document"
jupyter: xpython
---
```

Note that you can also provide a full `kernelspec`, for example:

``` yaml
---
title: "My Document"
jupyter: 
  kernelspec:
    name: "xpython"
    language: "python"
    display_name: "Python 3.7 (XPython)"
---
```

If no Jupyter kernel is specified, then the kernel is determined by finding an available kernel that supports the language of the first executable code block found within the file (e.g. ```` ```{python} ````).

::: callout-important
## Kernels from Conda

If you are using a kernel that is contained within an external conda environment you need to take an extra step to make sure it is recognized by Quarto. Please follow the instructions here to make conda managed kernels available:

<https://github.com/Anaconda-Platform/nb_conda_kernels#use-with-nbconvert-voila-papermill>

Note that this step is not required if you are merely using conda with Quarto. It applies to using kernels other than the default Python kernel that happen to be installed within a conda environment separate from the one you are using.
:::

{{< include _jupyter-daemon.md >}}



# quarto-web/docs/computations/parameters.qmd

---
title: "Parameters"
document: "document"
---

{{< include _parameters.md >}}

# quarto-web/docs/computations/caching.qmd

---
title: "Caching"
---

## Overview

When rendering documents with embedded computations becomes time-consuming, you may want to consider adding an execution cache, which will store the results of cell executions so they aren't re-executed with every document render.

Quarto integrates with the [Jupyter Cache](https://jupyter-cache.readthedocs.io/en/latest/) and [Knitr Cache](https://bookdown.org/yihui/rmarkdown-cookbook/cache.html) to to cache time consuming code chunks. These two caching facilities distinct capabilities, and we'll cover each in detail below.

## Jupyter Cache

[Jupyter Cache](https://jupyter-cache.readthedocs.io/en/latest/) enables you to cache all of the cell outputs for a notebook. If any of the cells in the notebook change then all of the cells will be re-executed.

To use Jupyter Cache you'll want to first install the `jupyter-cache` package:

+-----------+---------------------------------------+
| Platform  | Command                               |
+===========+=======================================+
| Mac/Linux | ``` {.bash filename="Terminal"}       |
|           | python3 -m pip install jupyter-cache  |
|           | ```                                   |
+-----------+---------------------------------------+
| Windows   | ``` {.powershell filename="Terminal"} |
|           | py -m pip install jupyter-cache       |
|           | ```                                   |
+-----------+---------------------------------------+
| Conda     | ``` {.bash filename="Terminal"}       |
|           | conda install jupyter-cache           |
|           | ```                                   |
+-----------+---------------------------------------+

::: callout-note
## Julia Installation

Note that if you are using Julia along with the integrated Python environment provided by `IJulia` then you should alternatively follow the directions on [Installing Jupyter Cache for Julia](julia.qmd#jupyter-cache).
:::

To enable the cache for a document, add the `cache` option. For example:

``` yaml
---
title: "My Document"
format: html
execute: 
  cache: true
jupyter: python3
---
```

You can also specify caching at the project level. For example, within a project file:

``` yaml
project:
  type: website
  
format:
  html:
    theme: united
    
execute:
  cache: true
```

Note that changes within a document that aren't within code cells (e.g. markdown narrative) do not invalidate the document cache. This makes caching a very convenient option when you are working exclusively on the prose part of a document.

Jupyter Cache include a `jcache` command line utility that you can use to analyze and manage the notebook cache. See the [Jupyter Cache](https://jupyter-cache.readthedocs.io/en/latest/) documentation for additional details.

## Knitr Cache

The Knitr Cache operates at the level of individual cells rather than the entire document. While this can be very convenient, it also introduced some special requirements around managing the dependencies between cells.

You can enable the Knitr cache at the document or project level using standard YAML options:

``` yaml
---
title: "My Document"
format: html
execute: 
  cache: true
---
```

You can also enable caching on a per-cell basis (in this you would *not* set the document level option):

```{{r}}
#| cache: true

summary(cars)
```

There are a variety of other cell-level options that affect Knitr caching behavior. You can learn about them in the Knitr [cell options](https://quarto.org/docs/reference/cells/cells-knitr.html#cache) reference. Another excellent resource is Yihui Xie's article on [cache invalidation](https://yihui.org/en/2018/06/cache-invalidation/).

## Rendering

You can use \`quarto render\` command line options to control caching behavior without changing the document's code. Use options to force the use of caching on all chunks, disable the use of caching on all chunks (even if it's specified in options), or to force a refresh of the cache even if it has not been invalidated:

``` {.bash filename="Terminal"}
# use a cache (even if the document options don't enable it)
quarto render example.qmd --cache 

# don't use a cache (even if the documentation options enable it)
quarto render example.qmd --no-cache 

# use a cache and force a refresh (even if the cells haven't changed)
quarto render example.qmd --cache-refresh 
```

## Alternatives

If you are using caching to mitigate long render-times, there are some alternatives you should consider alongside caching.

### Disabling Execution

If you are working exclusively with prose / markdown, you may want to disable execution entirely. Do this by specifying the `enabled: false` execute option For example:

``` yaml
---
title: "My Document"
format: html
execute: 
  enabled: false
---
```

Note that if you are authoring using Jupyter `.ipynb` notebooks (as opposed to plain-text `.qmd` files) then this is already the default behavior: no execution occurs when you call `quarto render` (rather, execution occurs as you work within the notebook).

### Freezing Execution

If you are working within a project and your main concern is the cumulative impact of rendering many documents at once, consider using the `freeze` option.

{{< include ../projects/_freeze-basics.md >}} 


Learn more about using `freeze` with projects in the article on [managing project execution](https://quarto.org/docs/projects/code-execution.html#freeze).



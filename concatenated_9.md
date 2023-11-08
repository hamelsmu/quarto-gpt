# quarto-web/docs/reference/formats/textile.qmd

---
title: "Textile Options"
spec: https://www.promptworks.com/textile
---

Textile is a simple text markup language that makes it easy to structure content for blogs, wikis, and documentation. To learn more about Textile see <https://www.promptworks.com/textile>.


# quarto-web/docs/reference/formats/muse.qmd

---
title: "Emacs Muse Options"
spec: https://www.gnu.org/software/emacs-muse/manual/
---

Emacs Muse is an authoring and publishing environment for Emacs. It simplifies the process of writing documents and publishing them to various output formats. To learn more about Emacs Muse see <https://www.gnu.org/software/emacs-muse/manual/>.


# quarto-web/docs/reference/formats/jats.qmd

---
title: "JATS Options"
spec: https://jats.nlm.nih.gov/publishing/
---

JATS (Journal Article Tag Suite) is an XML format for marking up and exchanging journal content. You can learn more about JATS here <https://jats.nlm.nih.gov/publishing/>.

``` yaml
format: jats
format: jats_archiving
format: jats_articleauthoring
format: jats_publishing
```


# quarto-web/docs/reference/formats/texinfo.qmd

---
title: "Texinfo Options"
spec: https://www.gnu.org/software/texinfo/
---

Texinfo is the official documentation format of the [GNU project](http://www.gnu.org/). Texinfo uses a single source file to produce output in a number of formats, both online and printed (DVI, HTML, Info, PDF, XML, etc.). To learn more about Texinfo see <https://www.gnu.org/software/texinfo/>.


# quarto-web/docs/reference/formats/html.qmd

---
title: "HTML Options"
spec: https://en.wikipedia.org/wiki/HTML5
search: true
---

HTML is a markup language used for structuring and presenting content on the web. To learn more about HTML see <https://en.wikipedia.org/wiki/HTML5>.

See the HTML format [user guide](../../output-formats/html-basics.qmd) for more details on creating HTML output with Quarto.


# quarto-web/docs/reference/formats/markdown/markua.qmd

---
title: "Markua Options"
spec: https://leanpub.com/markua/read
---

Markua is a markdown variant used by Leanpub. You can learn more about Markua at <https://leanpub.com/markua/read>.


# quarto-web/docs/reference/formats/markdown/commonmark.qmd

---
title: "CommonMark Options"
spec: https://commonmark.org/
---

CommonMark is a strongly defined, highly compatible specification of Markdown. You can learn more about CommonMark at <https://commonmark.org/>.


# quarto-web/docs/reference/formats/markdown/gfm.qmd

---
title: "GFM Options"
spec: https://github.github.com/gfm/
---

GitHub Flavored Markdown, often shortened as GFM, is the dialect of Markdown that is currently supported for user content on GitHub.com and GitHub Enterprise. To learn about GFM see <https://github.github.com/gfm/>.

See the GFM format [user guide](../../../output-formats/gfm.qmd) for more details on creating GFM output with Quarto.


# quarto-web/docs/reference/formats/wiki/mediawiki.qmd

---
title: "MediaWiki Options"
spec: https://www.mediawiki.org/wiki/Help:Formatting
---

MediaWiki is the native document format of Wikipedia. To learn more about MediaWiki see <https://www.mediawiki.org>.


# quarto-web/docs/reference/formats/wiki/dokuwiki.qmd

---
title: "DocuWiki Options"
spec: https://www.dokuwiki.org/wiki:syntax
---

DokuWiki is a simple to use and highly versatile open source wiki software that doesn't require a database. To learn more about DokuWiki see <https://www.dokuwiki.org>.


# quarto-web/docs/reference/formats/wiki/jira.qmd

---
title: "Jira Wiki Options"
spec: https://jira.atlassian.com/secure/WikiRendererHelpAction.jspa?section=all
---

Jira Wiki is the native document format for the Jira issue tracking and project management system from Atlassian. To learn more about Jira Wikis see <https://jira.atlassian.com/secure/WikiRendererHelpAction.jspa?section=all>.


# quarto-web/docs/reference/formats/wiki/xwiki.qmd

---
title: "XWiki Options"
spec: https://www.xwiki.org/xwiki/bin/view/Documentation/
---

XWiki is an open-source enterprise wiki system. To learn more about XWiki see <https://www.xwiki.org/>.


# quarto-web/docs/reference/formats/wiki/zimwiki.qmd

---
title: "ZimWiki Options"
spec: https://zim-wiki.org/
---

Zim is a graphical text editor used to maintain a collection of wiki pages. To learn more about ZimWiki see <https://zim-wiki.org/>.


# quarto-web/docs/reference/formats/presentations/beamer.qmd

---
title: "Beamer Options"
spec: https://ctan.org/pkg/beamer
---

Beamer is a LaTeX class for producing presentations and slides. To learn more about Beamer see <https://ctan.org/pkg/beamer>.

See the Beamer format [user guide](../../../presentations/beamer.qmd) for more details on creating Beamer output with Quarto.


# quarto-web/docs/reference/formats/presentations/pptx.qmd

---
title: "PowerPoint Options"
spec: https://en.wikipedia.org/wiki/Microsoft_PowerPoint
---

PowerPoint is the presentation editing software included with Microsoft Office. You can learn more about PowerPoint at <https://en.wikipedia.org/wiki/Microsoft_PowerPoint>.

See the PowerPoint format [user guide](../../../presentations/powerpoint.qmd) for more details on creating PowerPoint output with Quarto.


# quarto-web/docs/reference/formats/presentations/revealjs.qmd

---
title: "Revealjs Options"
spec: https://revealjs.com/
---

Revealjs is an open source HTML presentation framework. To learn more about Revealjs see <https://revealjs.com/>.

See the Revealjs format [user guide](../../../presentations/revealjs/index.qmd) for more details on creating Revealjs output with Quarto.


# quarto-web/docs/reference/projects/books.qmd

---
title: "Book Options"
project-type: book
project-type-upper: Book
project-output-dir: _book
---

All available options for `book` projects are documented below. See [Creating a Book](../../books/) for an in-depth guide to creating books with Quarto.

{{< include _websites-pre.md >}}

::: {#table-book}
:::

{{< include _websites.md >}}



# quarto-web/docs/reference/projects/websites.qmd

---
title: "Website Options"
project-type: website
project-type-upper: Website
project-output-dir: _site
---

All available options for `website` projects are documented below. See [Creating a Website](../../websites/) for an in-depth guide to creating websites with Quarto.

{{< include _websites-pre.md >}}


::: {#table-website}
:::

{{< include _websites.md >}}



# quarto-web/docs/reference/projects/core.qmd

---
title: "Project Options"
---

This article documents options that define the type, render targets, and output of a project.

See the [Project Basics](../../projects/quarto-projects.qmd) article for additional documentation on using projects.

Project options are specified under the `project` key. For example:

``` yaml
---
project:
  type: website
  output-dir: _site
---
```

::: {#table-project}
:::

### Preview

Specify options that control the behavior of `quarto preview` within the `preview` key. For example:

``` yaml
---
project:
  type: website
  output-dir: _site
  preview:
    port: 4200
    browser: false
---
```

Available `preview` options include:

::: {#table-preview}
:::


# quarto-web/docs/reference/projects/options.qmd

---
title: "Project Options"
project-type: default
project-output-dir: _output
---

{{< include _options.md >}}


# quarto-web/docs/reference/metadata/citation.qmd

---
title: "Citation Metadata"
---

You can provide citation data for Quarto documents in the document front matter. The citation options are based upon the [Citation Style Language (CSL) specification for items](https://docs.citationstyles.org/en/stable/specification.html), but as YAML (rather than XML).

``` yaml
---
citation:
  type: article-journal
  container-title: ACM Transactions on Embedded Computing Systems
  volume: 21
  issue: 2
  issued: 2022-03
  issn: 1539-9087
  doi: 10.1145/3514174
---
```


# quarto-web/docs/get-started/index.qmd

---
title: "Get Started"
subtitle: "Install Quarto, then check out the tutorials to learn the basics."
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
page-layout: full
toc: false
anchor-sections: false
editor: source
aliases:
  - /docs/getting-started/installation.html
image: /images/hero_right.png
---

::: {.grid .step .column-page-right}
::: {.g-col-lg-3 .g-col-12}
## Step 1 

#### Install Quarto {.fw-light}
:::

::: {.g-col-lg-9 .g-col-12}


::: {.content-visible when-profile="rc"}

{{< include ../download/_download-pre.md >}}

:::

::: {.content-visible unless-profile="rc"}

{{< include ../download/_download.md >}}

:::


:::
:::

::: {.grid .step .column-page-right}
::: {.g-col-lg-3 .g-col-12}
## Step 2 

#### Choose your tool<br/>and get started{.fw-light}
:::

::: {.tool .g-col-lg-9 .g-col-12}


<a href="hello/vscode.html" role="button" class="btn btn-outline-light">
![](images/vscode-logo.png){width="77" fig-alt="VS Code logo."}VS Code
</a>

<a href="hello/jupyter.html" role="button" class="btn btn-outline-light">
![](images/jupyter-logo.png){width="77" fig-alt="Jupyter logo."}Jupyter
</a>

<a href="hello/rstudio.html" role="button" class="btn btn-outline-light">
![](images/rstudio-logo.png){width="77" fig-alt="RStudio logo."}RStudio
</a>


<a href="hello/neovim.html" role="button" class="btn btn-outline-light">
![](images/neovim-logo.svg){width="77" fig-alt="Neovim logo."}Neovim
</a>


<a href="hello/text-editor.html" role="button" class="btn btn-outline-light">
![](images/text-editor-logo.png){width="77" fig-alt="Text Editor logo: circle with white outline and black fill inside of which is a command-line prompt."}Text Editor
</a>

:::
:::


# quarto-web/docs/get-started/computations/jupyter.qmd

---
title: "Tutorial: Computations"
editor_options:
  markdown:
    wrap: sentence
---

{{< include ../_tool-chooser.md >}}

## Overview

Quarto has a wide variety of options available for controlling how code and computational output appear within rendered documents.
In this tutorial we'll take a simple notebook that has some numeric output and plots, and cover how to apply these options.

If you want to follow along step-by-step in your own environment, download the notebook below:

::: {.callout-note appearance="minimal"}
<i class="bi bi-journal-code"></i> [Download computations.ipynb](_computations.ipynb){download="computations.ipynb"}
:::

Then, create a new directory to work within and copy the notebook into this directory.

Once you've done that, switch to this directory in a Terminal, install notebook dependencies (if necessary), and open Jupyter Lab to get started working with the notebook.
The commands you can use for installation and opening Jupyter Lab are given in the table below.

+-----------+------------------------------------------------------+
| Platform  | Commands                                             |
+===========+======================================================+
|           | ```{.bash filename="Terminal"}                       |
| Mac/Linux | python3 -m pip install jupyter matplotlib plotly     |
|           | python3 -m jupyter lab computations.ipynb            |
|           | ```                                                  |
+-----------+------------------------------------------------------+
|           | ```{.powershell filename="Terminal"}                 |
| Windows   | py -m pip install jupyter matplotlib plotly          |
|           | py -m jupyter lab computations.ipynb                 |
|           | ```                                                  |
+-----------+------------------------------------------------------+

The notebook as we start out is shown below.
Note that none of the cells are executed yet.

```` {.markdown .visually-hidden}
---
title: Quarto Computations
jupyter: python3
---

## NumPy

```{{python}}
import numpy as np
a = np.arange(15).reshape(3, 5)
a
```

## Matplotlib

```{{python}}
import matplotlib.pyplot as plt

fig = plt.figure()
x = np.arange(10)
y = 2.5 * np.sin(x / 20 * np.pi)
yerr = np.linspace(0.05, 0.2, 10)

plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')
plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')
plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True,
             label='uplims=True, lolims=True')

upperlimits = [True, False] * 5
lowerlimits = [False, True] * 5
plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits,
             label='subsets of uplims and lolims')

plt.legend(loc='lower right')
plt.show(fig)
```

## Plotly

```{{python}}
import plotly.express as px
import plotly.io as pio
gapminder = px.data.gapminder()
gapminder2007 = gapminder.query("year == 2007")
fig = px.scatter(gapminder2007, 
                 x="gdpPercap", y="lifeExp", color="continent", 
                 size="pop", size_max=60,
                 hover_name="country")
fig.show()
```
````

![](images/jupyter-computations.png){.border fig-alt="Screen shot of computations.ipynb Jupyter notebook with NumPy, Matplotlib, and Plotly code cells shown."}

Next, create a new Terminal within Jupyter Lab to use for Quarto commands.

![](../hello/images/jupyter-terminal.png){.border fig-alt="Screenshot of menu items in Jupuyter Lab: File > New > Terminal."}

Finally, run `quarto preview` in the Terminal, and position Jupyter Lab side-by-side with the browser showing the preview.

``` {.bash filename="Terminal"}
quarto preview computations.ipynb
```

![](images/jupyter-computations-preview.png){.border fig-alt="Side-by-side preview of notebook on the left and live preview in the browser on the right."}

Go ahead and run all of the cells and then save the notebook.
You'll see that the preview updates immediately.

## Cell Output

All of the code in the notebook is displayed within the rendered document.
However, for some documents, you may want to hide all of the code and just show the output.
Let's go ahead and specify `echo: false` within the document `execute` options to prevent code from being printed.

``` {.yaml .visually-hidden}
---
title: Quarto Computations
execute:
  echo: false
jupyter: python3
---
```

![](images/jupyter-execute-echo-false.png){.border fig-alt="Screen shot of metadata section of Jupyter notebook with 'echo: false' included under the 'execute:' option."}

Save the notebook after making this change.
The preview will update to show the output with no code.

![](images/exec-echo-false-preview.png){.border fig-alt="Output of notebook with echo: false set, shows resulting array in NumPy section, line chart in Numpy section, and interactive bubble chart in Plotly section."}

You might want to selectively enable code `echo` for some cells.
To do this add the `echo: true` cell option.
Try this with the NumPy cell.

```` {.markdown .visually-hidden}
```{{python}}
#| echo: true

import numpy as np
a = np.arange(15).reshape(3, 5)
a
```
````

![](images/jupyter-exec-echo-true.png){.border fig-alt="Screen shot of NumPy section of Jupyter notebook with 'echo: true' set as a cell option for the code cell."}

Save the notebook and note that the code is now included for the NumPy cell.

![](images/exec-echo-true-preview.png){.border fig-alt="Screen shot of rendered NumPy section of Jupyter notebook which shows the code and the resulting array."}

There a large number of other options available for cell output, for example `warning` to show/hide warnings (which can be especially helpful for package loading messages), `include` as a catch all for preventing any output (code or results) from being included in output, and `error` to prevent errors in code execution from halting the rendering of the document (and print the error in the rendered document).

See the [Jupyter Cell Options](https://quarto.org/docs/reference/cells/cells-jupyter.html) documentation for additional details.

## Code Folding

Rather than hiding code entirely, you might want to fold it and allow readers to view it at their discretion.
You can do this via the `code-fold` option.
Remove the `echo` option we previously added and add the `code-fold` HTML format option.

``` {.yaml .visually-hidden}
---
title: Quarto Computations
execute:
   code-fold: true
jupyter: python3
---
```

![](images/jupyter-code-fold.png){.border fig-alt="Screen shot of metadata section of Jupyter notebook with 'code-fold: true' included under the 'html:' option, which is under the `format:` option."}

Save the notebook.
Now a "Code" widget is available above the output of each cell.

![](images/code-fold-preview.png){.border fig-alt="Screen shot of rendered NumPy section of Jupyter notebook which shows a toggleable section that is labelled 'Code' and the resulting array."}

You can also provide global control over code folding.
Try adding `code-tools: true` to the HTML format options.

``` {.yaml .visually-hidden}
---
title: Quarto Computations
execute:
   code-fold: true
   code-tools: true
jupyter: python3
---
```

![](images/jupyter-code-tools.png){.border fig-alt="Metadata section of Jupyter notebook with 'code-tools: true' added to the HTML format options."}

Save the notebook and you'll see that a code menu appears at the top right of the document that provides global control over showing and hiding code.

![](images/code-tools-preview.png){.border fig-alt="Output of notebook with 'code-tools: true' which includes a Code dropdown button next to the document header with two options: Show All Code, and Hide All Code."}

```` {.markdown .visually-hidden}
```{{python}}
#| label: fig-limits
#| fig-cap: "Errorbar limit selector"

import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_size_inches(12, 7)
```
````

Let's improve the appearance of our Matplotlib output.
It could certainly stand to be wider, and it would be nice to provide a caption and a label for cross-referencing.

Go ahead and modify the Matplotlib cell to include `label` and `fig-cap` options as well as a call to `fig.set_size_inches()` to set a larger figure size with a wider aspect ratio.

```` {.markdown .visually-hidden}
```{{python}}
#| label: fig-limits
#| fig-cap: "Errorbar limit selector"

import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_size_inches(12, 7)
```
````

![](images/jupyter-figure-options.png){.border fig-alt="Code cell with label and fig-cap options added, as well as a call to set the figure size explicitly."}

Execute the cell to see the updated plot.
Then, save the notebook so that the Quarto preview is updated.

![](images/figure-options-preview.png){.border fig-alt="Output of Matplotlib section of notebook which includes a caption under the figure that reads 'Figure 1: Errorbar limit selection.'"}

## Multiple Figures

The Plotly cell visualizes GDP and life expectancy data from a single year (2007).
Let's plot another year next to it for comparison and add a caption and subcaptions.
Since this will produce a wider visualization we'll also use the `column` option to lay it out across the entire page rather than being constrained to the body text column.

There are quite a few changes to this cell.
Copy and paste the code below into the notebook if you want to try them locally.

``` python
#| label: fig-gapminder
#| fig-cap: "Life Expectancy and GDP"
#| fig-subcap:
#|   - "Gapminder: 1957"
#|   - "Gapminder: 2007"
#| layout-ncol: 2
#| column: page

import plotly.express as px
import plotly.io as pio
gapminder = px.data.gapminder()
def gapminder_plot(year):
    gapminderYear = gapminder.query("year == " + 
                                    str(year))
    fig = px.scatter(gapminderYear, 
                     x="gdpPercap", y="lifeExp",
                     size="pop", size_max=60,
                     hover_name="country")
    fig.show()
    
gapminder_plot(1957)
gapminder_plot(2007)
```

Run the modified cell then save the notebook.
The preview will update as follows:

![](images/plotly-preview.png){.border fig-alt="Output of Plotly section which shows two charts side-by-side. The first has a caption below that reads '(a) Gapminder: 1957', the second's caption reads '(b) Gapminder 2007'. Below both figures, there's a caption that reads 'Figure 1: Life Expectancy and GDP (Data from World Bank via gapminder.org).'"}

Let's discuss some of the new options used here.
You've seen `fig-cap` before but we've now added a `fig-subcap` option.

``` python
#| fig-cap: "Life Expectancy and GDP"
#| fig-subcap:
#|   - "Gapminder: 1957"
#|   - "Gapminder: 2007"
```

For code cells with multiple outputs adding the `fig-subcap` option enables us to treat them as subfigures.

We also added an option to control how multiple figures are laid out---in this case we specified side-by-side in two columns.

``` python
#| layout-ncol: 2
```

If you have 3, 4, or more figures in a panel there are many options available for customizing their layout.
See the article on [Figures](/docs/authoring/figures.qmd) for details.

Finally, we added an option to control the span of the page that our figures occupy.

``` python
#| column: page
```

This allows our figure display to span out beyond the normal body text column.
See the documentation on [Article Layout](/docs/authoring/article-layout.qmd) to learn about all of the available layout options.

{{< include _footer.md >}}


# quarto-web/docs/get-started/computations/_computations.qmd

---
title: "Quarto Computations"
---

This dataset contains a subset of the fuel economy data from the EPA.
Specifically, we use the `mpg` dataset from the **ggplot2** package.

```{r}
#| label: load-packages
#| echo: false

library(ggplot2)
```

The visualization below shows a positive, strong, and linear relationship between the city and highway mileage of these cars.
Additionally, mileage is higher for cars with fewer cylinders.

```{r}
#| label: scatterplot

ggplot(mpg, aes(x = hwy, y = cty, color = cyl)) +
  geom_point(alpha = 0.5, size = 2) +
  scale_color_viridis_c() +
  theme_minimal()
```


# quarto-web/docs/get-started/computations/vscode.qmd

---
title: "Tutorial: Computations"
editor_options:
  markdown:
    wrap: sentence
    canonical: true
---

{{< include ../_tool-chooser.md >}}

## Overview

Quarto has a wide variety of options available for controlling how code and computational output appear within rendered documents.
In this tutorial we'll take a `.qmd` file that has some numeric output and plots, and cover how to apply these options.

This tutorial will make use of the `matplotlib` and `plotly` Python packages.
The commands you can use to install them are given in the table below.

+-----------+--------------------------------------------------+
| Platform  | Commands                                         |
+===========+==================================================+
| Mac/Linux | ```{.bash filename="Terminal"}                   |
|           | python3 -m pip install jupyter matplotlib plotly |
|           | ```                                              |
+-----------+--------------------------------------------------+
| Windows   | ```{.powershell filename="Terminal"}             |
|           | py -m pip install jupyter matplotlib plotly      |
|           | ```                                              |
+-----------+--------------------------------------------------+

If you want to follow along step-by-step in your own environment, create a `computations.qmd` file and copy the following content into it.

```` markdown
---
title: Quarto Computations
jupyter: python3
---

## NumPy

```{{python}}
import numpy as np
a = np.arange(15).reshape(3, 5)
a
```

## Matplotlib

```{{python}}
import matplotlib.pyplot as plt

fig = plt.figure()
x = np.arange(10)
y = 2.5 * np.sin(x / 20 * np.pi)
yerr = np.linspace(0.05, 0.2, 10)

plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')
plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')
plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True,
             label='uplims=True, lolims=True')

upperlimits = [True, False] * 5
lowerlimits = [False, True] * 5
plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits,
             label='subsets of uplims and lolims')

plt.legend(loc='lower right')
plt.show(fig)
```

## Plotly

```{{python}}
import plotly.express as px
import plotly.io as pio
gapminder = px.data.gapminder()
gapminder2007 = gapminder.query("year == 2007")
fig = px.scatter(gapminder2007, 
                 x="gdpPercap", y="lifeExp", color="continent", 
                 size="pop", size_max=60,
                 hover_name="country")
fig.show()
```
````

Then, execute the **Quarto: Preview** command.
You can alternatively use the <kbd>Ctrl+Shift+K</kbd> keyboard shortcut, or the **Preview** button at the top right of the editor:

![](/docs/tools/images/vscode-preview-button.png){.border fig-alt="The top of the Visual Studio code editor. The right side of the editor tab area includes a Preview button."}

::: {.callout-note appearance="simple"}
Note that on the Mac you should use `Cmd` rather than `Ctrl` as the prefix for all Quarto keyboard shortcuts.
:::

Here is what you should see within VS Code:

![](images/vscode-computations-preview.png){.border .column-page-outset-right fig-alt="Side-by-side preview of text editor on the left and live preview in the browser on the right."}

## Cell Execution

As you author a document you may want to execute one or more cells without re-rendering the entire document.
You can do this using the **Run Cell** button above the code cell.
Click that button to execute the cell (output is shown side by side in the Jupyter interactive console):

![](/docs/tools/images/vscode-execute-cell.png){.border fig-alt="VS Code with two panes open, vscode.qmd source code on the right, and the interactive output of that code shown in a second pane on the left."}

There are a variety of commands and keyboard shortcuts available for executing cells:

| Quarto Command       | Keyboard Shortcut   |
|----------------------|---------------------|
| Run Current Cell     | <kbd>⇧⌘ Enter</kbd> |
| Run Selected Line(s) | <kbd>⌘ Enter</kbd>  |
| Run Next Cell        | <kbd>⌥⌘ N</kbd>     |
| Run Previous Cell    | <kbd>⌥⌘ P</kbd>     |
| Run All Cells        | <kbd>⌥⌘ R</kbd>     |
| Run Cells Above      | <kbd>⇧⌥⌘ P</kbd>    |
| Run Cells Below      | <kbd>⇧⌥⌘ N</kbd>    |

## Cell Output

All of the code in the source file is displayed within the rendered document.
However, in some cases, you may want to hide all of the code and just show the output.
Let's go ahead and specify `echo: false` within the document `execute` options to prevent code from being printed.

``` yaml
---
title: Quarto Computations
execute:
  echo: false
jupyter: python3
---
```

Re-render the document and the preview will update to show the output with no code (remember that you do not need to save the file before rendering, as this happens automatically when you render).

![](images/exec-echo-false-preview.png){.border fig-alt="Output of computations.qmd with 'echo: false' set, shows Title, resulting array in NumPy section, line chart in Matplotlib section, and interactive bubble chart in Plotly section."}

You might want to selectively enable code `echo` for some cells.
To do this add the `echo: true` cell option.
Try this with the NumPy cell.

```` markdown
```{{python}}
#| echo: true

import numpy as np
a = np.arange(15).reshape(3, 5)
a
```
````

Re-render note that the code is now included for the NumPy cell.

![](images/exec-echo-true-preview.png){.border fig-alt="Rendered NumPy section of computations.qmd which shows the code and the resulting array."}

There a large number of other options available for cell output, for example `warning` to show/hide warnings (which can be especially helpful for package loading messages), `include` as a catch all for preventing any output (code or results) from being included in output, and `error` to prevent errors in code execution from halting the rendering of the document (and print the error in the rendered document).

See the [Jupyter Cell Options](https://quarto.org/docs/reference/cells/cells-jupyter.html) documentation for additional details.

## Code Folding

Rather than hiding code entirely, you might want to fold it and allow readers to view it at their discretion.
You can do this via the `code-fold` option.
Remove the `echo` option we previously added and add the `code-fold` HTML format option.

``` yaml
---
title: Quarto Computations
format:
  html:
    code-fold: true
jupyter: python3
---
```

Render the document.
Now a "Code" widget is available above the output of each cell.

![](images/code-fold-preview.png){.border fig-alt="Rendered NumPy section of computations.qmd which shows a toggleable section that is labelled 'Code' and the resulting array."}

You can also provide global control over code folding.
Try adding `code-tools: true` to the HTML format options.

``` yaml
---
title: Quarto Computations
format:
  html:
    code-fold: true
    code-tools: true
jupyter: python3
---
```

Render the document and you'll see that a code menu appears at the top right of the document that provides global control over showing and hiding code.

![](images/text-editor-code-tools-preview.png){.border fig-alt="Rendered version of the computations.qmd document. A new code widget appears on top right of the document. The screenshot shows that the widget is clicked on, which reveals a drop down menu with three choices: Show All Code, Hide All Code, and View Source. In the background is the rendered document. The title is followed by some text, which is followed by a Code widget that would expand if clicked on, which is followed by the output of the code. The Code widgets are folded, so the code is not visible in the rendered document."}

## Figures

Let's improve the appearance of our Matplotlib output.
It could certainly stand to be wider, and it would be nice to provide a caption and a label for cross-referencing.

Go ahead and modify the Matplotlib cell to include `label` and `fig-cap` options as well as a call to `fig.set_size_inches()` to set a larger figure size with a wider aspect ratio:

```` markdown
```{{python}}
#| label: fig-limits
#| fig-cap: "Errorbar limit selector"

import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_size_inches(12, 7)
```
````

After re-rendering the document you'll see the updated plot:

![](images/figure-options-preview.png){.border fig-alt="Rendered Matplotlib section of computations.qmd which includes a toggleable code-folding widget, the figure, and a caption under the figure that reads 'Figure 1: Errorbar limit selection.'"}

## Multiple Figures

The Plotly cell visualizes GDP and life expectancy data from a single year (2007).
Let's plot another year next to it for comparison and add a caption and subcaptions.
Since this will produce a wider visualization we'll also use the `column` option to lay it out across the entire page rather than being constrained to the body text column.

There are quite a few changes to this cell.
Copy and paste this code into `computations.qmd` if you want to try them locally:

``` python
#| label: fig-gapminder
#| fig-cap: "Life Expectancy and GDP"
#| fig-subcap:
#|   - "Gapminder: 1957"
#|   - "Gapminder: 2007"
#| layout-ncol: 2
#| column: page

import plotly.express as px
import plotly.io as pio
gapminder = px.data.gapminder()
def gapminder_plot(year):
    gapminderYear = gapminder.query("year == " + 
                                    str(year))
    fig = px.scatter(gapminderYear, 
                     x="gdpPercap", y="lifeExp",
                     size="pop", size_max=60,
                     hover_name="country")
    fig.show()
    
gapminder_plot(1957)
gapminder_plot(2007)
```

Render the document and the preview will update as follows:

![](images/plotly-preview.png){.border fig-alt="Output of Plotly section which shows two charts side-by-side. The first has a caption below that reads '(a) Gapminder: 1957', the second's caption reads '(b) Gapminder 2007'. Below both figures, there's a caption that reads 'Figure 1: Life Expectancy and GDP (Data from World Bank via gapminder.org).'"}

Let's discuss some of the new options used here.
You've seen `fig-cap` before but we've now added a `fig-subcap` option:

``` python
#| fig-cap: "Life Expectancy and GDP"
#| fig-subcap:
#|   - "Gapminder: 1957"
#|   - "Gapminder: 2007"
```

For code cells with multiple outputs adding the `fig-subcap` option enables us to treat them as subfigures.

We also added an option to control how multiple figures are laid out---in this case we specified side-by-side in two columns:

``` python
#| layout-ncol: 2
```

If you have 3, 4, or more figures in a panel there are many options available for customizing their layout.
See the article [Figures](/docs/authoring/figures.qmd) for details.

Finally, we added an option to control the span of the page that our figures occupy:

``` python
#| column: page
```

This allows our figure display to span out beyond the normal body text column.
See the documentation on [Article Layout](/docs/authoring/article-layout.qmd) to learn about all of the available layout options.

{{< include _footer.md >}}


# quarto-web/docs/get-started/computations/_computations-text-editor.qmd

---
title: Quarto Computations
jupyter: python3
---

## NumPy

```{python}
import numpy as np
a = np.arange(15).reshape(3, 5)
a
```

## Matplotlib

```{python}
import matplotlib.pyplot as plt

fig = plt.figure()
x = np.arange(10)
y = 2.5 * np.sin(x / 20 * np.pi)
yerr = np.linspace(0.05, 0.2, 10)

plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')
plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')
plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True,
             label='uplims=True, lolims=True')

upperlimits = [True, False] * 5
lowerlimits = [False, True] * 5
plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits,
             label='subsets of uplims and lolims')

plt.legend(loc='lower right')
plt.show()
```

## Plotly

```{python}
import plotly.express as px
import plotly.io as pio
gapminder = px.data.gapminder()
gapminder2007 = gapminder.query("year == 2007")
fig = px.scatter(gapminder2007, 
                 x="gdpPercap", y="lifeExp", color="continent", 
                 size="pop", size_max=60,
                 hover_name="country")
fig.show()
```



# quarto-web/docs/get-started/computations/index.qmd

---
title: "Tutorial: Computations"
include-in-header: ../_redirect.html
---


# quarto-web/docs/get-started/computations/_computations-complete.qmd

---
title: "Quarto Computations"
format:
  html:
    code-fold: true
---

```{r}
#| label: load-packages
#| echo: false

library(ggplot2)
```

There are `r nrow(mpg)` observations in our data.

```{r}
#| echo: false

mean_cty <- round(mean(mpg$cty), 2)
mean_hwy <- round(mean(mpg$hwy), 2)
```

The average city mileage of the cars in our data is `r mean_cty` and the average highway mileage is `r mean_hwy`.

The plots in @fig-mpg show the relationship between city and highway mileage for 38 popular models of cars.
In @fig-mpg-1 the points are colored by the number of cylinders while in @fig-mpg-2 the points are colored by engine displacement.

```{r}
#| label: fig-mpg
#| fig-cap: "City and highway mileage for 38 popular models of cars."
#| fig-subcap:
#|   - "Color by number of cylinders"
#|   - "Color by engine displacement, in liters"
#| layout-ncol: 2
#| column: page
#| cache: true

ggplot(mpg, aes(x = hwy, y = cty, color = cyl)) +
  geom_point(alpha = 0.5, size = 2) +
  scale_color_viridis_c() +
  theme_minimal()

ggplot(mpg, aes(x = hwy, y = cty, color = displ)) +
  geom_point(alpha = 0.5, size = 2) +
  scale_color_viridis_c(option = "E") +
  theme_minimal()
```


# quarto-web/docs/get-started/computations/neovim.qmd

{{< include text-editor.qmd >}}

# quarto-web/docs/get-started/computations/text-editor.qmd

---
title: "Tutorial: Computations"
editor_options:
  markdown:
    wrap: sentence
    canonical: true
---

{{< include ../_tool-chooser.md >}}

## Overview

Quarto has a wide variety of options available for controlling how code and computational output appear within rendered documents.
In this tutorial we'll take a `.qmd` file that has some numeric output and plots, and cover how to apply these options.

This tutorial will make use of the `matplotlib` and `plotly` Python packages.
The commands you can use to install them are given in the table below.

+-----------+---------------------------------------------------------+
| Platform  | Commands                                                |
+===========+=========================================================+
| Mac/Linux | ```{.bash filename="Terminal"}                          |
|           | python3 -m pip install jupyter matplotlib plotly pandas |
|           | ```                                                     |
+-----------+---------------------------------------------------------+
| Windows   | ```{.powershell filename="Terminal"}                    |
|           | py -m pip install jupyter matplotlib plotly pandas      |
|           | ```                                                     |
+-----------+---------------------------------------------------------+

If you want to follow along step-by-step in your own environment, create a `computations.qmd` file and copy the following content into it.

```` markdown
---
title: Quarto Computations
jupyter: python3
---

## NumPy

```{{python}}
import numpy as np
a = np.arange(15).reshape(3, 5)
a
```

## Matplotlib

```{{python}}
import matplotlib.pyplot as plt

fig = plt.figure()
x = np.arange(10)
y = 2.5 * np.sin(x / 20 * np.pi)
yerr = np.linspace(0.05, 0.2, 10)

plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')
plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')
plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True,
             label='uplims=True, lolims=True')

upperlimits = [True, False] * 5
lowerlimits = [False, True] * 5
plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits,
             label='subsets of uplims and lolims')

plt.legend(loc='lower right')
plt.show(fig)
```

## Plotly

```{{python}}
import plotly.express as px
import plotly.io as pio
gapminder = px.data.gapminder()
gapminder2007 = gapminder.query("year == 2007")
fig = px.scatter(gapminder2007, 
                 x="gdpPercap", y="lifeExp", color="continent", 
                 size="pop", size_max=60,
                 hover_name="country")
fig.show()
```
````

Now, open a Terminal and run `quarto preview`, then position your editor side-by-side with the browser showing the preview.

``` {.bash filename="Terminal"}
quarto preview computations.qmd
```

![](images/text-editor-computations-preview.png){.border .column-page-outset-right fig-alt="Side-by-side preview of text editor on the left and live preview in the browser on the right."}

## Cell Output

All of the code in the source file is displayed within the rendered document.
However, in some cases, you may want to hide all of the code and just show the output.
Let's go ahead and specify `echo: false` within the document `execute` options to prevent code from being printed.

``` yaml
---
title: Quarto Computations
execute:
  echo: false
jupyter: python3
---
```

Save the file after making this change.
The preview will update to show the output with no code.

![](images/exec-echo-false-preview.png){.border fig-alt="Output of computations.qmd with 'echo: false' set, shows Title, resulting array in NumPy section, line chart in Matplotlib section, and interactive bubble chart in Plotly section."}

You might want to selectively enable code `echo` for some cells.
To do this add the `echo: true` cell option.
Try this with the NumPy cell.

```` markdown
```{{python}}
#| echo: true

import numpy as np
a = np.arange(15).reshape(3, 5)
a
```
````

Save the file and note that the code is now included for the NumPy cell.

![](images/exec-echo-true-preview.png){.border fig-alt="Rendered NumPy section of computations.qmd which shows the code and the resulting array."}

There a large number of other options available for cell output, for example `warning` to show/hide warnings (which can be especially helpful for package loading messages), `include` as a catch all for preventing any output (code or results) from being included in output, and `error` to prevent errors in code execution from halting the rendering of the document (and print the error in the rendered document).

See the [Jupyter Cell Options](https://quarto.org/docs/reference/cells/cells-jupyter.html) documentation for additional details.

## Code Folding

Rather than hiding code entirely, you might want to fold it and allow readers to view it at their discretion.
You can do this via the `code-fold` option.
Remove the `echo` option we previously added and add the `code-fold` HTML format option.

``` yaml
---
title: Quarto Computations
format:
  html:
    code-fold: true
jupyter: python3
---
```

Save the file.
Now a "Code" widget is available above the output of each cell.

![](images/code-fold-preview.png){.border fig-alt="Rendered NumPy section of computations.qmd which shows a toggleable section that is labelled 'Code' and the resulting array."}

You can also provide global control over code folding.
Try adding `code-tools: true` to the HTML format options.

``` yaml
---
title: Quarto Computations
format:
  html:
   code-fold: true
   code-tools: true
jupyter: python3
---
```

Save the file and you'll see that a code menu appears at the top right of the document that provides global control over showing and hiding code.

![](images/text-editor-code-tools-preview.png){.border fig-alt="Rendered version of the computations.qmd document. A new code widget appears on top right of the document. The screenshot shows that the widget is clicked on, which reveals a drop down menu with three choices: Show All Code, Hide All Code, and View Source. In the background is the rendered document. The title is followed by some text, which is followed by a Code widget that would expand if clicked on, which is followed by the output of the code. The Code widgets are folded, so the code is not visible in the rendered document."}

## Figures

Let's improve the appearance of our Matplotlib output.
It could certainly stand to be wider, and it would be nice to provide a caption and a label for cross-referencing.

Go ahead and modify the Matplotlib cell to include `label` and `fig-cap` options as well as a call to `fig.set_size_inches()` to set a larger figure size with a wider aspect ratio:

```` markdown
```{{python}}
#| label: fig-limits
#| fig-cap: "Errorbar limit selector"

import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_size_inches(12, 7)
```
````

Save the file to re-render and see the updated plot:

![](images/figure-options-preview.png){.border fig-alt="Rendered Matplotlib section of computations.qmd which includes a toggleable code-folding widget, the figure, and a caption under the figure that reads 'Figure 1: Errorbar limit selection.'"}

## Multiple Figures

The Plotly cell visualizes GDP and life expectancy data from a single year (2007).
Let's plot another year next to it for comparison and add a caption and subcaptions.
Since this will produce a wider visualization we'll also use the `column` option to lay it out across the entire page rather than being constrained to the body text column.

There are quite a few changes to this cell.
Copy and paste this code into `computations.qmd` if you want to try them locally:

``` python
#| label: fig-gapminder
#| fig-cap: "Life Expectancy and GDP"
#| fig-subcap:
#|   - "Gapminder: 1957"
#|   - "Gapminder: 2007"
#| layout-ncol: 2
#| column: page

import plotly.express as px
import plotly.io as pio
gapminder = px.data.gapminder()
def gapminder_plot(year):
    gapminderYear = gapminder.query("year == " + 
                                    str(year))
    fig = px.scatter(gapminderYear, 
                     x="gdpPercap", y="lifeExp",
                     size="pop", size_max=60,
                     hover_name="country")
    fig.show()
    
gapminder_plot(1957)
gapminder_plot(2007)
```

Save the file, the preview will update as follows:

![](images/plotly-preview.png){.border fig-alt="Output of Plotly section which shows two charts side-by-side. The first has a caption below that reads '(a) Gapminder: 1957', the second's caption reads '(b) Gapminder 2007'. Below both figures, there's a caption that reads 'Figure 1: Life Expectancy and GDP (Data from World Bank via gapminder.org).'"}

Let's discuss some of the new options used here.
You've seen `fig-cap` before but we've now added a `fig-subcap` option:

``` python
#| fig-cap: "Life Expectancy and GDP"
#| fig-subcap:
#|   - "Gapminder: 1957"
#|   - "Gapminder: 2007"
```

For code cells with multiple outputs adding the `fig-subcap` option enables us to treat them as subfigures.

We also added an option to control how multiple figures are laid out---in this case we specified side-by-side in two columns:

``` python
#| layout-ncol: 2
```

If you have 3, 4, or more figures in a panel there are many options available for customizing their layout.
See the article [Figures](/docs/authoring/figures.qmd) for details.

Finally, we added an option to control the span of the page that our figures occupy:

``` python
#| column: page
```

This allows our figure display to span out beyond the normal body text column.
See the documentation on [Article Layout](/docs/authoring/article-layout.qmd) to learn about all of the available layout options.

{{< include _footer.md >}}


# quarto-web/docs/get-started/computations/rstudio.qmd

---
title: "Tutorial: Computations"
editor_options:
  markdown:
    wrap: sentence
    canonical: true
---

{{< include ../_tool-chooser.md >}}


## Overview

Quarto supports executable code blocks within markdown.
This allows you to create fully reproducible documents and reports---the code required to produce your output is part of the document itself, and is automatically re-run whenever the document is rendered.

In this tutorial we'll show you how to author fully reproducible computational documents with Quarto in RStudio.

If you would like to follow along step-by-step in your own environment, download the Quarto document (`.qmd`) below, open it in RStudio, and click on <kbd>![](images/rstudio-render-button.png){width="25" height="20"}</kbd> **Render** (or use the keyboard shortcut ⇧⌘K).
We recommend also checking the box for **Render on Save** for a live preview of your changes.

::: {.callout-note appearance="minimal"}
<i class="bi bi-download"></i> [Download computations.qmd](_computations.qmd){download="computations.qmd"}
:::

Note that you will need to open this document in RStudio {{< var rstudio.min_version >}} or later, which you can download [here](https://posit.co/download/rstudio-desktop/).

## Cell Output

By default, the code and its output are displayed within the rendered document.

![](images/rstudio-computations-preview.png){.border .column-page-right fig-alt="RStudio window with computations.qmd open in the visual editor (on the right) and the rendered document (on the left). The document is titled Quarto Computations and contains some text and code. The rendered version also shows a visualization."}

However, for some documents, you may want to hide all of the code and just show the output.
To do so, specify `echo: false` within the `execute` option in the YAML.

``` yaml
---
title: "Quarto Computations"
execute:
  echo: false
---
```

If you checked **Render on Save** earlier, just save the document after making this change for a live preview.
Otherwise render the document to see your updates reflected.
The result will look like the following.

![](images/rstudio-exec-echo-false.png){.border fig-alt="Rendered computations.qmd document with title Quarto Computations, some descriptive text, and a plot. Code is not shown."}

You might want to selectively enable code `echo` for some cells.
To do this add the `echo: true` cell option.
Try this with the chunk labelled `scatterplot`.

``` r
#| label: scatterplot
#| echo: true

ggplot(mpg, aes(x = hwy, y = cty, color = cyl)) +
  geom_point(alpha = 0.5, size = 2) +
  scale_color_viridis_c() +
  theme_minimal()
```

Save the document again and note that the code is now included for the `scatterplot` chunk.

![](images/rstudio-exec-echo-true-preview.png){.border fig-alt="Rendered computations.qmd document with title Quarto Computations, some descriptive text, and a plot. Code is shown for the plot, but not for package loading."}

The `echo` option can be set to `true`, `false`, or `fenced`.
The last one might be of special interest for writing documentation and teaching materials as it allows you to include the fenced code delimiter in your code output to emphasize that executable code requires that delimiter.
You can read more about this option in the [Fenced Echo](https://quarto.org/docs/computations/execution-options.html#fenced-echo) documentation.

There are a large number of other options available for cell output, for example `warning` for showing/hiding warnings (which can be especially helpful for package loading messages), `include` as a catch all for preventing any output (code or results) from being included in output, and `error` to prevent errors in code execution from halting the rendering of the document (and print the error in the rendered document).

See the [Knitr Cell Options](https://quarto.org/docs/reference/cells/cells-knitr.html) documentation for additional details.

## Code Folding

Rather than hiding code entirely, you might want to fold it and allow readers to view it at their discretion.
You can do this via the `code-fold` option.
Remove the `echo` option we previously added and add the `code-fold` HTML format option.

``` yaml
---
title: "Quarto Computations"
format:
  html:
    code-fold: true
---
```

Save the document again and note that new Code widgets are now included for each code chunk.

![](images/rstudio-code-fold-preview.png){.border .column-page-right fig-alt="RStudio with computations.qmd open. On the right is the visual editor. The YAML has title and format defined. Title is Quarto Computations. Format is html, and code-fold option is set to true. On the right is the rendered version of the document. The title is followed by some text, which is followed by a Code widget that would expand if clicked on, which is followed by some more text, another code widget, and finally the plot. The Code widgets are folded, so the code is not visible in the rendered document."}

You can also provide global control over code folding.
Try adding `code-tools: true` to the HTML format options.

``` yaml
---
title: "Quarto Computations"
format:
  html:
    code-fold: true
    code-tools: true
---
```

Save the document and you'll see that a code menu appears at the top right of the rendered document that provides global control over showing and hiding all code.

![](images/rstudio-code-tools-preview.png){.border fig-alt="Rendered version of the computations.qmd document. A new code widget appears on top right of the document. The screenshot shows that the widget is clicked on, which reveals a drop down menu with three choices: Show All Code, Hide All Code, and View Source. In the background is the rendered document. The title is followed by some text, which is followed by a Code widget that would expand if clicked on, which is followed by some more text, another code widget, and finally the plot. The Code widgets are folded, so the code is not visible in the rendered document."}

## Code Linking

The `code-link` option enables hyper-linking of functions within code blocks to their online documentation.
Try adding `code-link: true` to the HTML format options.

``` yaml
---
title: "Quarto Computations"
format:
  html:
    code-link: true
---
```

Save the document and observe that the functions are now clickable hyperlinks.

![](images/rstudio-code-link-preview.png){.column-page-right fig-alt="Rendered version of the computations.qmd document. The document contains a title (Quarto Computations), text, code chunks, and a plot. The screenshot shows that function names in code chunks are clickable, and clicking on one brings you to documentation on the package website (which is shown on the foreground of the image). The function shown is theme_minimal() from ggplot2."}

Note that code linking is currently implemented only for the knitr engine via the [downlit](https://downlit.r-lib.org/) package.
A limitation of downlit currently prevents code linking if `code-line-numbers` and/or `code-annotations` are also `true`.

## Figures

We can improve the appearance and accessibility of our plot.
We can change its aspect ratio by setting `fig-width` and `fig-height`, provide a `fig-cap`, modify its `label` for cross referencing, and add [alternative text](https://medium.com/nightingale/writing-alt-text-for-data-visualization-2a218ef43f81) with `fig-alt`.

We'll add the following chunk options.

``` r
#| label: fig-scatterplot
#| fig-cap: "City and highway mileage for 38 popular models of cars."
#| fig-alt: "Scatterplot of city vs. highway mileage for cars, where points are colored by the number of cylinders. The plot displays a positive, linear, and strong relationship between city and highway mileage, and mileage increases as the number of cylinders decreases."
#| fig-width: 6
#| fig-height: 3.5
```

Save the document to see the updated plot.
Note that we have also updated the narrative with a [cross reference](https://quarto.org/docs/authoring/cross-references.html#computations) to this figure using the following.

``` markdown
@fig-scatterplot shows a positive, strong, and linear relationship between the city and highway mileage of these cars.
```

![](images/rstudio-figure-options.png){.border .column-page-right fig-alt="RStudio with computations.qmd open. On the right is the visual editor. The YAML has title and format defined. Title is Quarto Computations. Format is html, and code-fold option is set to true. Compared to earlier images on the page, the code chunk shows the new chunk options added to the code chunk. On the right is the rendered version of the document. The title is followed by some text, which is followed by a Code widget that would expand if clicked on, which is followed by some more text, another code widget, and finally the plot. The Code widgets are folded, so the code is not visible in the rendered document."}

## Multiple Figures

Let's add another plot to our chunk---a scatterplot where the points are colored by engine displacement, using a different color scale.
Our goal is to display these plots side-by-side (i.e., in two columns), with a descriptive subcaption for each plot.
Since this will produce a wider visualization we'll also use the `column` option to lay it out across the entire page rather than being constrained to the body text column.

There are quite a few changes to this chunk.
To follow along, copy and paste the options outlined below into your Quarto document.

``` r
#| label: fig-mpg
#| fig-cap: "City and highway mileage for 38 popular models of cars."
#| fig-subcap:
#|   - "Color by number of cylinders"
#|   - "Color by engine displacement, in liters"
#| layout-ncol: 2
#| column: page

ggplot(mpg, aes(x = hwy, y = cty, color = cyl)) +
  geom_point(alpha = 0.5, size = 2) +
  scale_color_viridis_c() +
  theme_minimal()

ggplot(mpg, aes(x = hwy, y = cty, color = displ)) +
  geom_point(alpha = 0.5, size = 2) +
  scale_color_viridis_c(option = "E") +
  theme_minimal()
```

Additionally, replace the existing text that describes the visualization with the following.

``` markdown
The plots in @fig-mpg show the relationship between city and highway mileage for 38 popular models of cars.
In @fig-mpg-1 the points are colored by the number of cylinders while in @fig-mpg-2 the points are colored by engine displacement.
```

Then, save the document and inspect the rendered output, which should look like the following.

![](images/rstudio-multi-figure-preview.png){.border fig-alt="Rendered version of the computations.qmd document with a new plot. The document contains a title (Quarto Computations), text, code chunks, and figure include two side-by-side subfigures, each scatterplots. The text shows clickable cross reference links to Figure 1, Figure 1a, and Figure 1b."}

Let's discuss some of the new options used here.
You've seen `fig-cap` before but we've now added a `fig-subcap` option.

``` r
#| fig-cap: "City and highway mileage for 38 popular models of cars."
#| fig-subcap:
#|   - "Color by number of cylinders"
#|   - "Color by engine displacement, in liters"
```

For code cells with multiple outputs adding the `fig-subcap` option enables us to treat them as subfigures.

We also added an option to control how multiple figures are laid out---in this case we specified side-by-side in two columns.

``` r
#| layout-ncol: 2
```

If you have 3, 4, or more figures in a panel there are many options available for customizing their layout.
See the article [Figure Layout](../../authoring/figures.qmd#figure-panels) for details.

Finally, we added an option to control the span of the page that our figures occupy.

``` r
#| column: page
```

This allows our figure display to span out beyond the normal body text column.
See the documentation on [Article Layout](../../authoring/article-layout.qmd) to learn about all of the available layout options.

## Data Frames

{{< include ../../computations/_knitr-df-print.md >}}


## Inline Code

To include executable expressions within markdown, enclose the expression in `` `r ` ``.
For example, we can use inline code to state the number of observations in our data.
Try adding the following markdown text to your Quarto document.

```{=html}
<div class="sourceCode">
<pre class="sourceCode markdown">
<code class="sourceCode markdown">
There are &#96;r nrow(mpg)&#96; observations in our data. 
</code>
</pre>
</div>
```
Save your document and inspect the rendered output.
The expression inside the backticks has been executed and the sentence includes the actual number of observations.

::: border
There are 234 observations in our data.
:::

If the expression you want to inline is more complex, involving many functions or a pipeline, we recommend including it in a code chunk (with `echo: false`) and assigning the result to an object.
Then, you can call that object in your inline code.

For example, say you want to state the average city and highway mileage in your data.
First, compute these values in a code chunk.

``` r
#| echo: false

mean_cty <- round(mean(mpg$cty), 2)
mean_hwy <- round(mean(mpg$hwy), 2)
```

Then, add the following markdown text to your Quarto document.

```{=html}
<div class="sourceCode">
<pre class="sourceCode markdown">
<code class="sourceCode markdown">
The average city mileage of the cars in our data is &#96;r mean_cty&#96 and the average highway mileage is &#96;r mean_hwy&#96. 
</code>
</pre>
</div>
```
Save your document and inspect the rendered output.

::: border
The average city mileage of the cars in our data is 16.86 and the average highway mileage is 23.44.
:::

## Caching

If your document includes code chunks that take too long to compute, you might want to cache the results of those chunks.
You can use the `cache` option either at the document level using the YAML execute option.

``` yaml
execute:
  cache: true
```

However caching all code chunks in a document may not be preferable.
You can also indicate which chunks should be cached directly with using a chunk option.

``` r
#| cache: true
```

Try adding this chunk option to one of the code chunks in your document that produces a plot and save.
When the document is rendered, you'll see that a new folder has been created in your working directory with the same name as your document and the suffix `_cache`.
This folder contains the cached results.
You can find out more about caching in Quarto documents in the [Cache](https://quarto.org/docs/projects/code-execution.html#cache) documentation.

If you followed along step-by-step with this tutorial, you should now have a Quarto document that implements everything we covered.
Otherwise, you can download a completed version of `computations.qmd` below.

::: {.callout-note appearance="minimal"}
<i class="bi bi-download"></i> [Download computations-complete.qmd](_computations-complete.qmd){download="computations-complete.qmd"}
:::

{{< include _footer.md >}}


# quarto-web/docs/get-started/authoring/jupyter.qmd

---
title: "Tutorial: Authoring"
code-copy: hover
editor_options:
  markdown:
    wrap: sentence
    canonical: true
---

{{< include ../_tool-chooser.md >}}

## Overview

In this tutorial we'll show you how to author Quarto documents in Jupyter Lab.
In particular, we'll discuss the various document formats you can produce and show you how to add components like table of contents, equations, citations, cross-references, and more.

## Output Formats

Quarto supports rendering notebooks to dozens of different [output formats](/docs/output-formats/all-formats.qmd).
By default, the `html` format is used, but you can specify an alternate format (or formats) within document options.

### Format Options

Let's create a notebook and define various formats for it to be rendered to and add some options to each of the formats.
As a reminder, document options are specified in YAML within a "Raw" cell at the beginning of the notebook.
To create a Raw cell, add a cell at the top of the notebook and set its type to Raw using the notebook toolbar:

![](images/jupyter-raw-cell.png){.border fig-alt="Notebook formats.ipynb with a dropdown shown for a cell with three options: Code, Markdown, and Raw. Raw is highlighted."}

Now, let's add some basic document metadata and a default output format.

``` {.yaml .visually-hidden}
---
title: "Quarto Document"
author: "Norah Jones"
format: pdf
jupyter: python3
---
```

![](images/jupyter-format.png){.border fig-alt=""}

We specified `pdf` as the default output format (if we exclude the `format` option then it will default to `html`).

Let's add some options to control our PDF output.

``` {.yaml .visually-hidden}
---
title: "Quarto Document"
author: "Norah Jones"
format: 
  pdf: 
    toc: true
    number-sections: true
jupyter: python3
---
```

![](images/jupyter-format-options.png){.boder fig-alt=""}

### Multiple Formats

Some documents you create will have only a single output format, however in many cases it will be desirable to support multiple formats.
Let's add the `html` and `docx` formats to our document.

``` {.yaml .visually-hidden}
---
title: "Quarto Document"
author: "Norah Jones"
toc: true
number-sections: true
highlight-style: pygments
format: 
  html: 
    code-fold: true
    html-math-method: katex
  pdf: 
    geometry: 
      - top=30mm
      - left=20mm
  docx: default
jupyter: python3
---
```

![](images/jupyter-formats.png){.border fig-alt=""}

There's a lot to take in here!
Let's break it down a bit.
The first two lines are generic document metadata that aren't related to output formats at all.

``` yaml
title: "Quarto Document"
author: "Norah Jones"
```

The next three lines are document format options that *apply to all formats*.
which is why they are specified at the root level.

``` yaml
toc: true
number-sections: true
highlight-style: pygments
```

Next, we have the `format` option, where we provide format-specific options.

``` yaml
format:
  html: 
    code-fold: true
    html-math-method: katex
  pdf:
    geometry: 
      - top=30mm
      - left=30mm
  docx: default
```

The `html` and `pdf` formats each provide an option or two.
For example, for the HTML output we want the user to have control over whether to show or hide the code (`code-fold: true`) and use `katex` for math text.
For PDF we define some margins.
The `docx` format is a bit different---it specifies `docx: default`.
This means just use all of the default options for the format.

## Rendering

The formats specified within document options define what is rendered by default.
If we render the notebook with all the options given above using the following.

``` {.bash filename="Terminal"}
quarto render notebook.ipynb
```

Then, the following files would be created.

-   `notebook.html`
-   `notebook.pdf`
-   `notebook.docx`

We can select one or more formats using the `--to` option.

``` {.bash filename="Terminal"}
quarto render notebook.ipynb --to docx
quarto render notebook.ipynb --to docx,pdf
```

Note that the target file (in this case `notebook.ipynb`) should always be the very first command line argument.

If needed we can also render formats that aren't specified within document options.

``` {.bash filename="Terminal"}
quarto render notebook.ipynb --to odt
```

Since the `odt` format isn't included within document options, the default options for the format will be used.

::: {.callout-note appearance="simple"}
Note that when rendering an `.ipynb` Quarto **will not** execute the cells within the notebook by default (the presumption being that you already executed them while editing the notebook).
If you want to execute the cells you can pass the `--execute` flag to render.

``` {.bash filename="Terminal"}
quarto render notebook.ipynb --execute
```
:::

## Sections

You can use a table of contents and/or section numbering to make it easier for readers to navigate your document.
Do this by adding the `toc` and/or `number-sections` options to document options.
Note that these options are typically specified at the root level because they are shared across all formats.

``` {.yaml .visually-hidden}
---
title: Quarto Basics
author: Norah Jones
date: 'May 22, 2021'
toc: true
number-sections: true
jupyter: python3
---

## Colors

- Red
- Green 
- Blue

## Shapes

- Square
- Circle
- Triangle

## Textures

- Smooth
- Bumpy
- Fuzzy
```

![](images/jupyter-sections.png){.border fig-alt=""}

Here's what this document looks like when rendered to HTML.

![](images/sections-render.png){.border fig-alt="Document with title Quarto Basics, author, and date. Table of contents is on the left-hand side with numbered items for each of the three sections: 1. Colors, 2. Shapes, 3. Textures. Each section is shown in the document with the list contents from the source ipynb."}

There are lots of options available for controlling how the table of contents and section numbering behave.
See the output format documentation (e.g. [HTML](/docs/output-formats/html-basics.qmd), [PDF](/docs/output-formats/pdf-basics.qmd), [MS Word](/docs/output-formats/ms-word.qmd)) for additional details.

## Equations

You can add LaTeX equations to markdown cells within Jupyter Lab.

``` {.markdown .visually-hidden}
Einstein's theory of special relatively that expresses the equivalence of mass and energy:

$E = mc^{2}$
```

$E = mc^{2}$

![](/docs/get-started/authoring/images/jupyter-equation.png){.border fig-alt=""}

Equations are rendered when you run the cell.

![](/docs/get-started/authoring/images/jupyter-equation-render.png){.border fig-alt="Rendered notebook with LaTeX equation shown for E equals mc squared."}

Inline equations are delimited with `$…$`.
To create equations in a new line (display equation) use `$$…$$`.
See the documentation on [markdown equations](/docs/authoring/markdown-basics.html#equations) for additional details.

## Citations

To cite other works within a Quarto document.
First create a bibliography file in a supported format (BibTeX or CSL).
Then, link the bibliography to your document using the `bibliography` YAML metadata option.

Here's a notebook that includes a bibliography and single citation.
Note that markdown cells are un-executed so you can see all of the syntax.

```` {.markdown .visually-hidden}
---
title: Quarto Basics
format: html
bibliography: references.bib
jupyter: python3
---

## Overview

Knuth says always be literate [@knuth1984].

```{{python}}
1 + 1
```

## References
````

![](/docs/get-started/authoring/images/jupyter-citations.png){.border fig-alt=""}

Note that items within the bibliography are cited using the `@citeid` syntax.

``` markdown
 Knuth says always be literate [@knuth1984].
```

References will be included at the end of the document, so we include a `## References` heading at the bottom of the notebook.

Here is what this document looks like when rendered.

![](/docs/get-started/authoring/images/citations-render.png){.border width="600" fig-alt="Rendered notebook with references section at the bottom the content of which reads 'Knuth, Donald E. 1984. Literate Programming. The Computer Journal 27 (2): 97-111.'"}

\
The `@` citation syntax is very flexible and includes support for prefixes, suffixes, locators, and in-text citations.
See the documentation on [Citations and Footnotes](/docs/authoring/footnotes-and-citations.qmd) to learn more.

## Cross References

Cross-references make it easier for readers to navigate your document by providing numbered references and hyperlinks to figures, tables, equations, and sections.
Cross-reference-able entities generally require a label (unique identifier) and a caption.

The notebook below illustrates cross-referencing various types of entities.
Once again, the markdown cells are again un-executed so that the syntax is visible.

```` {.markdown .visually-hidden}
---
title: Quarto Crossrefs
format: html
jupyter: python3
---

## Overview

See @fig-simple in @sec-plot for a demonstration of a simple plot. 

See @eq-stddev to better understand standard deviation.

## Plot {#sec-plot}

```{{python}}
#| label: fig-simple
#| fig-cap: "Simple Plot"
import matplotlib.pyplot as plt
plt.plot([1,23,2,4])
plt.show()
```

## Equation {#sec-equation}

$$
s = \sqrt{\frac{1}{N-1} \sum_{i=1}^N (x_i - \overline{x})^2}
$$ {#eq-stddev}
````

$$
x + 1
$$

![](/docs/get-started/authoring/images/jupyter-crossref.png){.border fig-alt=""}

This example includes cross-referenced sections, figures, and equations.
The table below shows how we expressed each of these.

+----------+---------------+----------------------------------+
| Entity   | Reference     | Label / Caption                  |
+==========+===============+==================================+
| Section  | `@sec-plot`   | ID added to heading:             |
|          |               |                                  |
|          |               | ``` {.default code-copy="false"} |
|          |               | # Plot {#sec-plot}               |
|          |               | ```                              |
+----------+---------------+----------------------------------+
| Figure   | `@fig-simple` | YAML options in code cell:       |
|          |               |                                  |
|          |               | ``` {.default code-copy="false"} |
|          |               | #| label: fig-simple             |
|          |               | #| fig-cap: "Simple Plot"        |
|          |               | ```                              |
+----------+---------------+----------------------------------+
| Equation | `@eq-stddev`  | At end of display equation:      |
|          |               |                                  |
|          |               | ``` default                      |
|          |               | $$ {#eq-stddev}                  |
|          |               | ```                              |
+----------+---------------+----------------------------------+

: {tbl-colwidths=\[20,30,50\]}

And finally, here is what this notebook looks like when rendered.

![](/docs/get-started/authoring/images/crossref-render.png){.border width="600" fig-alt="Rendered page with linked cross references to figures and equations."}

See the article on [Cross References](/docs/authoring/cross-references.qmd) to learn more, including how to customize caption and reference text (e.g. use "Fig." rather than "Figure").

## Callouts

Callouts are an excellent way to draw extra attention to certain concepts, or to more clearly indicate that certain content is supplemental or applicable to only some scenarios.

Callouts are markdown divs that have special callout attributes.
Here's an example of creating a callout within a markdown cell.

``` {.markdown .visually-hidden}
::: {.callout-note}
Note that there are five types of callouts, including:
`note`, `tip`, `warning`, `caution`, and `important`.
:::
```

![](/docs/get-started/authoring/images/jupyter-callout.png){.border fig-alt=""}

When we ultimately render the document with Quarto the callout appears as intended.

::: callout-note
Note that there are five types of callouts, including `note`, `tip`, `warning`, `caution`, and `important`.
:::

You can learn more about the different types of callouts and options for their appearance in the [Callouts](/docs/authoring/callouts.qmd) documentation.

## Article Layout

The body of Quarto articles have a default width of approximately 700 pixels.
This width is chosen to [optimize readability](https://medium.com/ben-shoemate/optimum-web-readability-max-and-min-width-for-page-text-dee9987a27a0).
This normally leaves some available space in the document margins and there are a few ways you can take advantage of this space.

In this notebook, we use the `reference-location` option to indicate that we would like footnotes to be placed in the right margin.

We also use the `column: screen-inset` cell option to indicate we would like our figure to occupy the full width of the screen, with a small inset.

```` {.markdown .visually-hidden}
---
title: Quarto Layout
format: html
reference-location: margin
jupyter: python3
---

## Placing Colorbars

Colorbars indicate the quantitative extent of image data.
Placing in a figure is non-trivial because room needs to
be made for them. The simplest case is just attaching a 
colorbar to each axes:^[See the [Matplotlib Gallery](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/colorbar_placement.html) to explore colorbars further].

```{{python}}
#| code-fold: true
#| column: screen-inset
import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(2, 2)
fig.set_size_inches(20, 8)
cmaps = ['RdBu_r', 'viridis']
for col in range(2):
    for row in range(2):
        ax = axs[row, col]
        pcm = ax.pcolormesh(
          np.random.random((20, 20)) * (col + 1),
          cmap=cmaps[col]
        )
        fig.colorbar(pcm, ax=ax)
plt.show()
```
````

![](images/jupyter-layout.png){.border fig-alt=""}

Here is what this document looks like when rendered.

![](images/layout-render.png){.border fig-alt="Document with Quarto Layout title at the top followed by Placing Colorbars header with text below it. Next to the text is a footnote in the page margin. Below the text is a toggleable code widget to hide/reveal the code followed by four plots displayed in two rows and two columns."}

You can locate citations, footnotes, and [asides](https://quarto.org/docs/authoring/article-layout.html#asides,) in the margin.
You can also define custom column spans for figures, tables, or other content.
See the documentation on [Article Layout](/docs/authoring/article-layout.qmd) for additional details.

{{< include _footer.md >}}


# quarto-web/docs/get-started/authoring/vscode.qmd

---
title: "Tutorial: Authoring"
code-copy: hover
editor_options:
  markdown:
    wrap: sentence
    canonical: true
---

{{< include ../_tool-chooser.md >}}

{{< include _text-editor.md >}}


Additionally, if you are interested in seeing how to use Quarto from within `.ipynb` notebooks, check out the documentation on using the VS Code [Notebook Editor](/docs/tools/vscode.qmd#notebook-editor) with Quarto.


# quarto-web/docs/get-started/authoring/_authoring-complete.qmd

---
title: "Housing Prices"
author: "Mine Çetinkaya-Rundel"
toc: true
number-sections: true
highlight-style: pygments
format:
  html: 
    code-fold: true
    html-math-method: katex
  pdf:
    geometry: 
      - top=30mm
      - left=30mm
  docx: default
bibliography: references.bib
---

## Introduction

In this analysis, we build a model predicting sale prices of houses based on data on houses that were sold in the Duke Forest neighborhood of Durham, NC around November 2020. Let's start by loading the packages we'll use for the analysis.

```{r}
#| label: load-pkgs
#| code-summary: "Packages"
#| message: false

library(openintro)  # for data
library(tidyverse)  # for data wrangling and visualization
library(knitr)      # for tables
library(broom)      # for model summary
```

We present the results of exploratory data analysis in @sec-eda and the regression model in @sec-model.

We're going to do this analysis using literate programming [@knuth1984].

## Exploratory data analysis {#sec-eda}

The data contains `r nrow(duke_forest)` houses. As part of the exploratory analysis let's visualize and summarize the relationship between areas and prices of these houses.

### Data visualization

@fig-histogram shows two histograms displaying the distributions of `price` and `area` individually.

```{r}
#| label: fig-histogram
#| fig-cap: "Histograms of individual variables"
#| fig-subcap:
#|   - "Histogram of `price`s"
#|   - "Histogram of `area`s" 
#| layout-ncol: 2
#| column: page-right

ggplot(duke_forest, aes(x = price)) +
  geom_histogram(binwidth = 50000) +
  labs(title = "Histogram of prices")

ggplot(duke_forest, aes(x = area)) +
  geom_histogram(binwidth = 250) +
  labs(title = "Histogram of areas")
```

@fig-scatterplot displays the relationship between these two variables in a scatterplot.

```{r}
#| label: fig-scatterplot
#| fig-cap: "Scatterplot of price vs. area of houses in Duke Forest"

ggplot(duke_forest, aes(x = area, y = price)) +
  geom_point() +
  labs(title = "Price and area of houses in Duke Forest")
```

### Summary statistics

@tbl-stats displays basic summary statistics for these two variables.

```{r}
#| label: tbl-stats
#| tbl-cap: "Summary statistics for price and area of houses in Duke Forest"

duke_forest %>%
  summarise(
    `Median price` = median(price),
    `IQR price` = IQR(price),
    `Median area` = median(area),
    `IQR area` = IQR(area),
    `Correlation, r` = cor(price, area)
    ) %>%
  kable(digits = c(0, 0, 0, 0, 2))
```

## Modeling {#sec-model}

We can fit a simple linear regression model of the form shown in @eq-slr.

$$
price = \hat{\beta}_0 + \hat{\beta}_1 \times area + \epsilon
$$ {#eq-slr}

@tbl-lm shows the regression output for this model.

```{r}
#| label: tbl-lm
#| tbl-cap: "Linear regression model for predicting price from area"

price_fit <- lm(price ~ area, data = duke_forest)
  
price_fit %>%
  tidy() %>%
  kable(digits = c(0, 0, 2, 2, 2))
```

::: callout-note
This is a pretty incomplete analysis, but hopefully the document provides a good overview of some of the authoring features of Quarto!
:::

## References {.unnumbered}


# quarto-web/docs/get-started/authoring/_authoring.qmd

---
title: "Housing Prices"
author: "Mine Çetinkaya-Rundel"
format: pdf
---

## Introduction

In this analysis, we build a model predicting sale prices of houses based on data on houses that were sold in the Duke Forest neighborhood of Durham, NC around November 2020.
Let's start by loading the packages we'll use for the analysis.

```{r}
#| label: load-pkgs
#| code-summary: "Packages"
#| message: false

library(openintro)  # for data
library(tidyverse)  # for data wrangling and visualization
library(knitr)      # for tables
library(broom)      # for model summary
```

We present the results of exploratory data analysis in @sec-eda and the regression model in @sec-model.

<!--# ADD CITATION HERE -->

## Exploratory data analysis {#sec-eda}

The data contains `r nrow(duke_forest)` houses.
As part of the exploratory analysis let's visualize and summarize the relationship between areas and prices of these houses.

### Data visualization

@fig-histogram shows two histograms displaying the distributions of `price` and `area` individually.

```{r}
#| label: fig-histogram
#| fig-cap: "Histograms of individual variables"
#| fig-subcap:
#|   - "Histogram of `price`s"
#|   - "Histogram of `area`s" 
#| layout-ncol: 2

ggplot(duke_forest, aes(x = price)) +
  geom_histogram(binwidth = 50000) +
  labs(title = "Histogram of prices")

ggplot(duke_forest, aes(x = area)) +
  geom_histogram(binwidth = 250) +
  labs(title = "Histogram of areas")
```

@fig-scatterplot displays the relationship between these two variables in a scatterplot.

```{r}
#| label: fig-scatterplot
#| fig-cap: "Scatterplot of price vs. area of houses in Duke Forest"

ggplot(duke_forest, aes(x = area, y = price)) +
  geom_point() +
  labs(title = "Price and area of houses in Duke Forest")
```

### Summary statistics

@tbl-stats displays basic summary statistics for these two variables.

```{r}
#| label: tbl-stats
#| tbl-cap: "Summary statistics for price and area of houses in Duke Forest"

duke_forest %>%
  summarise(
    `Median price` = median(price),
    `IQR price` = IQR(price),
    `Median area` = median(area),
    `IQR area` = IQR(area),
    `Correlation, r` = cor(price, area)
    ) %>%
  kable(digits = c(0, 0, 0, 0, 2))
```

## Modeling {#sec-model}

We can fit a simple linear regression model of the form shown in @eq-slr.

\[ADD EQUATION HERE\]

@tbl-lm shows the regression output for this model.

```{r}
#| label: tbl-lm
#| tbl-cap: "Linear regression model for predicting price from area"

price_fit <- lm(price ~ area, data = duke_forest)
  
price_fit %>%
  tidy() %>%
  kable(digits = c(0, 0, 2, 2, 2))
```

<!--# ADD CALLOUT HERE -->

<!--# ADD SECTION HEADING FOR REFERENCES HERE -->


# quarto-web/docs/get-started/authoring/index.qmd

---
title: "Tutorial: Authoring"
include-in-header: ../_redirect.html
---


# quarto-web/docs/get-started/authoring/neovim.qmd

---
title: "Tutorial: Authoring"
code-copy: hover
---

{{< include ../_tool-chooser.md >}}

{{< include _text-editor.md >}}


See the article on [Using Neovim with Quarto](/docs/tools/neovim.qmd) to learn more about installing, using, and customizing Neovim for Quarto. 

# quarto-web/docs/get-started/authoring/text-editor.qmd

---
title: "Tutorial: Authoring"
code-copy: hover
editor_options:
  markdown:
    wrap: sentence
    canonical: true
---

{{< include ../_tool-chooser.md >}}

{{< include _text-editor.md >}}




# quarto-web/docs/get-started/authoring/rstudio.qmd

---
title: "Tutorial: Authoring"
editor_options:
  markdown:
    wrap: sentence
    canonical: true
---

{{< include ../_tool-chooser.md >}}

## Overview

In this tutorial we'll show you how to author Quarto documents in RStudio.
In particular, we'll discuss the various document formats you can produce with the same source code and show you how to add components like table of contents, equations, citations, etc.
The [visual markdown editor](/docs/visual-editor/) in RStudio makes many of these tasks easier so we'll highlight its use in this tutorial, but note that it's possible to accomplish these tasks in the source editor as well.

If you would like to follow along step-by-step in your own environment, make sure that you have the [latest release](https://posit.co/download/rstudio-desktop/) of RStudio ({{< var rstudio.current_release >}}), which you can download [here](https://posit.co/download/rstudio-desktop/), installed.

## Output Formats

Quarto supports rendering notebooks to dozens of different output formats.
By default, the `html` format is used, but you can specify an alternate format (or formats) within document options.

### Format Options

You can choose the format you want to render your Quarto document to at the time of creating your new document.
To create a new document, go to **File** \> **New File** \> **Quarto Document...** Alternatively, use the command palette (accessible via Ctrl+Shift+P), search for **Create a new Quarto document** and hit return.

In the **Title** field, give a title for your document (e.g. the screenshot below suggests "Housing Prices") and add your name to the **Author** field.
Next, you will select the output format for your document.
By default, RStudio suggests using HTML as the output, let's leave that default for now.

![](images/rstudio-new-document.png){.border fig-alt="Pop up menu for creating a new document. The title field shows that we entered \"Housing Prices\" and the author field shows the name \"Mine Çetinkaya-Rundel\". HTML format is selected via the radio button. All else is left as default choices (e.g., Engine is Knitr and the Use visual markdown editor checkbox is checked)." fig-align="center" width="600"}

A new document will be created with the following YAML.

``` yaml
---
title: "Housing Prices"
author: "Mine Çetinkaya-Rundel"
---
```

Note that our format choice (HTML) is not even reflected in the YAML as it is the default output format for Quarto documents.
However you can directly edit the YAML to change the output format, e.g. to PDF (`pdf`) or MS Word (`docx`).
Add `format: pdf` to your document's YAML as shown below.

``` yaml
---
title: "Housing Prices"
author: "Mine Çetinkaya-Rundel"
format: pdf
---
```

Unfortunately, this document has no content, so rendering it would not result in very interesting output.
To make it a bit easier to demonstrate all the features we want to highlight in this tutorial, let's close this empty document and start with one that has a little bit of content in it.
If you would like to follow along step-by-step in your own environment, download the Quarto document (`.qmd`) below and open it in RStudio.

::: {.callout-note appearance="minimal" icon="false"}
<i class="bi bi-download"></i> [Download authoring.qmd](_authoring.qmd){download="authoring.qmd"}
:::

In order to create PDFs you will need to install a recent distribution of [LaTeX](https://www.latex-project.org/).
We recommend the use of TinyTeX (which is based on TexLive), which you can install with the following command:

``` {.bash filename="Terminal"}
quarto install tinytex
```

See the article on [PDF Engines](../../output-formats/pdf-engine.qmd) for details on using other LaTeX distributions and PDF compilation engines.

Once you have LaTeX setup, click on <kbd>![](images/rstudio-render-button.png){width="25" height="20"}</kbd> **Render** (or use the keyboard shortcut ⇧⌘K).
We recommend also checking the box for **Render on Save** for a live preview of your changes.
As shown below, you should see the rendered PDF in the Viewer in RStudio.

![](images/rstudio-pdf-preview.png){.border .column-page-right fig-alt="RStudio with authoring.qmd open. On the left: Source code in the visual editor. On the left: Rendered document as a PDF in the Viewer."}

Next, let's add an option to the YAML, e.g. to add line numbers to the code chunks (`code-line-numbers: true`).
Add this option to your document's YAML as shown below, paying attention to the indentation scheme.
Under `format:` our format choice `pdf` is indented (with two spaces) and it's followed by `:` to indicate that further options for that format will be specified.
In the next line, further indented by two spaces, we add `code-line-numbers: true`.

``` yaml
---
title: "Housing Prices"
author: "Mine Çetinkaya-Rundel"
format:
  pdf:
    code-line-numbers: true
---
```

If you checked **Render on Save** earlier, just save the document after making this change for a live preview.
Otherwise render the document to see your updates reflected, including a table of contents that looks like the following.

![](images/rstudio-code-line-numbers.png){.border fig-alt="Rendered version of authoring.qmd as PDF, with line numbers next to each of the lines of code chunks." fig-align="center"}

An incredibly exciting format option that we won't go into too much detail in this tutorial is `revealjs`.
Yes, you can make presentations with Quarto as well!
In fact, Quarto supports a variety of formats for creating presentations, including `revealjs` for HTML slides, `pptx` for PowerPoint, and `beamer` for LaTeX/PDF.
The [Presentations](/docs/presentations/) article gives a thorough walk through of creating slide decks with Quarto.

### Multiple Formats

Some documents you create will have only a single output format, however in many cases it will be desirable to support multiple formats.
Let's add the `html` and `docx` formats to our document and modify some options specific to each format.

``` yaml
---
title: "Housing Prices"
author: "Mine Çetinkaya-Rundel"
highlight-style: pygments
format:
  html: 
    code-fold: true
    html-math-method: katex
  pdf:
    geometry: 
      - top=30mm
      - left=30mm
  docx: default
---
```

There's a lot to take in here!
Let's break it down a bit.
The first two lines are generic document metadata that aren't related to output formats at all.

``` yaml
---
title: "Housing Prices"
author: "Mine Çetinkaya-Rundel"
---
```

The next line is a document format option that *applies to all formats*, which is why it is specified at the root level.

``` yaml
---
highlight-style: pygments
---
```

Next, we have the `format` option, where we provide format-specific options.

``` yaml
---
format:
  html: 
    code-fold: true
    html-math-method: katex
  pdf:
    geometry: 
      - top=30mm
      - left=30mm
  docx: default
---
```

The `html` and `pdf` formats each provide an option or two.
For example, for the HTML output we want the user to have control over whether to show or hide the code (`code-fold: true`) and use `katex` for math text.
For PDF we define some margins.
The `docx` format is a bit different---it specifies `docx: default`.
This indicates that we just want to use all of the default options for the format.

## Rendering

Clicking the <kbd>![](images/rstudio-render-button.png){width="25" height="21"}</kbd> **Render** button (or using the keyboard shortcut <kbd>⇧⌘K</kbd>) in RStudio will render the document to the first format listed in the YAML.

![](images/rstudio-html-preview.png){.border fig-alt="Rendered version of authoring.qmd as HTML. There is no table of contents and the code chunks are folded, hiding the code."}

Note that the <kbd>![](images/rstudio-render-button.png){width="25" height="21"}</kbd> **Render** button also has a drop down menu that enables you to render to any of the formats listed in YAML front matter:

![](images/rstudio-render-formats.png){.border}

If you would like to render to all formats, you can do so with the [**quarto**](https://github.com/quarto-dev/quarto-r) package, which provides an R interface to the Quarto CLI. For example, to render the current document, use `quarto::quarto_render()`.
You can also specify the name of the document you want to render as well as the output format(s).

``` r
quarto::quarto_render(
  "authoring.qmd", 
  output_format = c("pdf", "html", "docx")
)
```

As a result, you will see three new files appear in your Files pane:

-   `authoring.docx`
-   `authoring.html`
-   `authoring.pdf`

![](images/rstudio-files-pane.png){.border fig-alt="RStudio Files pane, with four document, all titled authoring, but with different suffixes: docx, html, pdf, qmd." fig-align="center" width="600"}

## Sections

You can use a table of contents and/or section numbering to make it easier for readers to navigate your document.
Do this by adding the `toc` and/or `number-sections` options to document options.
Note that these options are typically specified at the root level because they are shared across all formats.

``` yaml
---
title: "Housing Prices"
author: "Mine Çetinkaya-Rundel"
toc: true
number-sections: true
highlight-style: pygments
format:
  html: 
    code-fold: true
    html-math-method: katex
  pdf:
    geometry: 
      - top=30mm
      - left=30mm
  docx: default
---
```

Here's what this document looks like when rendered to HTML.

![](images/rstudio-toc-secnum.png){.border fig-alt="Rendered version of authoring.qmd as HTML with numbered sections and a table of contens on the top right. The table of contents shows three sections: Introduction, Exploratory data analysis (with subsections Data visualization and Summary statistics), and Modeling."}

There are lots of options available for controlling how the table of contents and section numbering behave.
See the output format documentation (e.g. [HTML](/docs/output-formats/html-basics.qmd), [PDF](/docs/output-formats/pdf-basics.qmd), [MS Word](/docs/output-formats/ms-word.qmd)) for additional details.

## Equations

If you are using the visual editor mode, you can add LaTeX equations to Quarto documents in RStudio using the [Insert Anything](/docs/visual-editor/index.qmd#insert-anything) tool.
You can access it with <kbd>/</kbd> at the beginning of an empty block or <kbd>Cmd+/</kbd> anywhere else.

![](images/rstudio-insert-equation.png){.border fig-alt="Insert anything tool in the RStudio visual editor being used to insert a display math." fig-align="center" width="600"}

Display equations (in a new line) are delimited with `$$…$$` while inline equations are delimited with `$…$`.
Add the following as display math in the document.

``` markdown
price = \hat{\beta}_0 + \hat{\beta}_1 \times area + \epsilon
```

RStudio displays a rendered version of the tutorial as you type it in the editor.
See the documentation on [markdown equations](/docs/authoring/markdown-basics.html#equations) for additional details.

![](/docs/get-started/authoring/images/rstudio-equation-render.png){.border}

## Citations

The Insert Anything tool can also be used to insert citations to your document.

![](images/rstudio-insert-citation.png){fig-alt="Using the visual editor insert citation tool." width="700"}

In the next window you can insert a citation via from a variety of sources including your document bibliography, [Zotero](/docs/visual-editor/technical.qmd#citations-from-zotero) personal or group libraries, [DOI](/docs/visual-editor/technical.qmd#citations-from-dois) (Document Object Identifier) references, and searches of [Crossref](https://www.crossref.org/), [DataCite](https://datacite.org/), or [PubMed](https://pubmed.ncbi.nlm.nih.gov/).
You can find out more about citations with the visual editor [here](/docs/visual-editor/technical.qmd#citations).

Select **From DOI** on the left and copy-and-paste the DOI [`10.1093/comjnl/27.2.97`](https://doi.org/10.1093/comjnl/27.2.97) in the search bar and hit **Search**.
Then, select the found reference, and **Insert** it into your document.

![](images/rstudio-insert-citaton-menu.png){fig-alt="Insert citation to Knuth, D's Literate Programming article via DOI."}

If this is the first citation you are adding to your document, RStudio will automatically create a bibliography file for you.
This file is called `references.bib` by default and RStudio will also add `bibliography: references.bib` to your document's YAML metadata.

Note that items within the bibliography are cited using the `@citeid` syntax.
Add the following text to your document.

``` markdown
We're going to do this analysis using literate programming [@knuth1984].
```

References will be included at the end of the document, so we include a `## References` heading at the bottom of the notebook.
You might also add `.unnumbered` class to this section by clicking on the three dots (<kbd>...</kbd>) to edit its attributes.

![](images/rstudio-references-section.png){.border fig-alt="Edit Attributes window for the section title References. The image shows that this menu can be accessed by cliking on the three dots." width="700"}

Here is what this document looks like when rendered (with middle sections removed to highlight the relevant parts.

![](images/rstudio-references.png){.border fig-alt="Document with a single citation and a references section at the end."}

The `@` citation syntax is very flexible and includes support for prefixes, suffixes, locators, and in-text citations.
See the documentation on [Citations and Footnotes](/docs/authoring/footnotes-and-citations.qmd) to learn more.

## Cross References

Cross-references make it easier for readers to navigate your document by providing numbered references and hyperlinks to figures, tables, equations, and sections.
Cross-reference-able entities generally require a label (unique identifier) and a caption.

For example, to add a label to the equation inserted earlier, click on the three dots to edit its attributes and use the suggested format (starting with `#eq-`) to label the equation.

![](images/rstudio-crossref-equation.png){.border fig-alt="Add label to an equation using the visual editor. The label added is #eq-slr."}

Then, add a cross reference using the Insert Anything tool in the visual editor.
You might add a sentence like `"We can fit a simple linear regression model of the form shown in"` to contextualize the cross reference and then add the reference to the end of that sentence.

![](images/rstudio-crossref-equation-insert.png){.border fig-alt="Use the insert anything tool in the visual editor to insert a cross reference."}

In the Insert Cross Reference menu, navigate to the desired cross reference entity on the left, and select the equation labeled earlier.

![](images/rstudio-crossref-insert-menu.png){.border fig-alt="Use the insert cross reference menu, select Equations on the left side, and select an equation to cross reference."}

Alternatively, start typing the label of the equation to be referenced in the visual editor, and the autofill tool will bring up the cross references to choose from.

![](images/rstudio-crossref-eq-autofill.png){.border fig-alt="Cross reference an equation by starting to type out its label."}

Below we illustrate cross-referencing various types of entities using fragments from the document you've been working with.

``` markdown
We present the results of exploratory data analysis in @sec-eda and the regression model in @sec-model.


@fig-scatterplot displays the relationship between these two variables in a scatterplot.


@tbl-stats displays basic summary statistics for these two variables.


We can fit a simple linear regression model of the form shown in @eq-slr.
```

This examples include cross-referenced sections, figures, and equations.
The table below summarizes how we express each of these.

+----------+--------------------+------------------------------------------------------------------------------+
| Entity   | Reference          | Label / Caption                                                              |
+==========+====================+==============================================================================+
| Section  | `@sec-eda`         | ID added to heading:                                                         |
|          |                    |                                                                              |
|          |                    | ``` {.default code-copy="false"}                                             |
|          |                    | # Exploratory data analysis {#sec-eda}                                       |
|          |                    | ```                                                                          |
+----------+--------------------+------------------------------------------------------------------------------+
| Figure   | `@fig-scatterplot` | YAML options in code cell:                                                   |
|          |                    |                                                                              |
|          |                    | ``` {.default code-copy="false"}                                             |
|          |                    | #| label: fig-scatterplot                                                    |
|          |                    | #| fig-cap: "Scatterplot of price vs. area of houses in Duke Forest"         |
|          |                    | ```                                                                          |
+----------+--------------------+------------------------------------------------------------------------------+
| Table    | `@tbl-stats`       | YAML options in code cell:                                                   |
|          |                    |                                                                              |
|          |                    | ``` {.default code-copy="false"}                                             |
|          |                    | #| label: tbl-stats                                                          |
|          |                    | #| tbl-cap: "Summary statistics for price and area of houses in Duke Forest" |
|          |                    | ```                                                                          |
+----------+--------------------+------------------------------------------------------------------------------+
| Equation | `@eq-slr`          | At end of display equation:                                                  |
|          |                    |                                                                              |
|          |                    | ``` default                                                                  |
|          |                    | $$ {#eq-slr}                                                                 |
|          |                    | ```                                                                          |
+----------+--------------------+------------------------------------------------------------------------------+

: {tbl-colwidths=\[20,30,50\]}

See the article on [Cross References](/docs/authoring/cross-references.qmd) to learn more, including how to customize caption and reference text (e.g. use "Fig." rather than "Figure").

## Callouts

Callouts are an excellent way to draw extra attention to certain concepts, or to more clearly indicate that certain content is supplemental or applicable to only some scenarios.

Callouts are markdown divs that have special callout attributes.
We can insert a callout using the Insert Anything tool.

![](images/rstudio-insert-callout.png){.border fig-alt="Insert Anything tool to insert a callout."}

In the subsequent dialogue you can select one of five types of callout (note, tip, important, caution, or warning), customize its appearance (default, simple, or minimal), and decide whether you want to show the icon.

![](images/rstudio-callout-dialogue.png){.border fig-alt="Callout dialogue. Type note is selected with default appearance and show icon box is checked." fig-align="center" width="500"}

Then, try inserting the following text in the callout box.

``` markdown
This is a pretty incomplete analysis, but hopefully the document provides a good overview of some of the authoring features of Quarto!
```

Here is what a callout looks like in the visual editor.

![](images/rstudio-callout-note-source.png){.border fig-alt="Callout box in the visual editor. Callout text reads \"This is a pretty incomplete analysis, but hopefully the document provides a good overview of some of the authoring features of Quarto!\""}

And here is the rendered callout in the output document.

![](images/rstudio-callout-note-rendered.png){.border fig-alt="Callout box in the rendered HTML document. Callout text reads \"This is a pretty incomplete analysis, but hopefully the document provides a good overview of some of the authoring features of Quarto!\""}

You can learn more about the different types of callouts and options for their appearance in the [Callouts](/docs/authoring/callouts.qmd) documentation.

## Article Layout

The body of Quarto articles have a default width of approximately 700 pixels.
This width is chosen to [optimize readability](https://medium.com/ben-shoemate/optimum-web-readability-max-and-min-width-for-page-text-dee9987a27a0).
This normally leaves some available space in the document margins and there are a few ways you can take advantage of this space.

We can use the `column: page-right` cell option to indicate we would like our figure to occupy the full width of the screen, with some inset.
Go ahead and add this chunk option to the chunk labeled `fig-histogram`.

``` r
#| label: fig-histogram
#| fig-cap: "Histograms of individual variables"
#| fig-subcap:
#|   - "Histogram of `price`s"
#|   - "Histogram of `area`s" 
#| layout-ncol: 2
#| column: page-right
```

Here is what the relevant section of the document looks like when rendered.

![](images/rstudio-column-page-right-render.png){.border fig-alt="Rendered version of authoring.qmd as HTML. Exploratory data analysis section is shown, the side-by-side histograms span a width wider than the rest of the document."}

You can locate citations, footnotes, and asides in the margin.
You can also define custom column spans for figures, tables, or other content.
See the documentation on [Article Layout](/docs/authoring/article-layout.qmd) for additional details.

## Publishing

Once your document is rendered to HTML, you can publish to [RPubs](https://rpubs.com/) (a free service from RStudio for sharing documents on the web) simply by clicking the <kbd>![](images/rstudio-publish-button.png){width="25" height="23"}</kbd> Publish button on the editor toolbar or preview window.
Alternatively, you can use the `quarto::quarto_publish_doc()` function.

``` r
quarto::quarto_publish_doc(
  "authoring.qmd", 
  server = "rpubs.com"
  )
```

Other possible publishing options include RStudio Connect and ShinyApps as well as GitHub Pages, Netlify, etc.
The [Publishing HTML](/docs/output-formats/html-publishing.html) article gives a much more detailed overview of your publishing options.

If you followed along step-by-step with this tutorial, you should now have a Quarto document that implements everything we covered.
Otherwise, you can download a completed version of `computations.qmd` below.

::: {.callout-note appearance="minimal"}
<i class="bi bi-download"></i> [Download authoring-complete.qmd](_authoring-complete.qmd){download="authoring-complete.qmd"}
:::

{{< include _footer.md >}}



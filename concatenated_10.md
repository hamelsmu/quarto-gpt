# quarto-web/docs/get-started/hello/jupyter.qmd

---
title: "Tutorial: Hello, Quarto"
editor_options:
  markdown:
    wrap: sentence
    canonical: true
---

{{< include ../_tool-chooser.md >}}

## Overview

In this tutorial we'll show you how to use Jupyter Lab with Quarto.
You'll edit code and markdown in Jupyter Lab, just as you would with any notebook, and preview the rendered document in a web browser as you work.

Below is an overview of how this will look.

![](images/jupyter-quarto-preview.png){fig-alt="On the left: A Jupyter notebook titled Quarto Basics containing some text, a code cell, and the result of the code cell, which is a line plot on a polar axis. On the right: Rendered version of the same notebook."}

The notebook on the left is *rendered* into the HTML version you see on the right.
This is the basic model for Quarto publishing---take a source document (in this case a notebook) and render it to a variety of [output formats](https://quarto.org/docs/output-formats/all-formats.html), including HTML, PDF, MS Word, etc.

::: callout-note
Note that while this tutorial uses Python, using Julia (via the [IJulia](https://julialang.github.io/IJulia.jl/stable/) kernel) is also well supported.
See the article on [Using Julia](/docs/computations/julia.qmd) for additional details.
:::

## Rendering

We'll start out by opening a notebook (`hello.ipynb`) in Jupyter Lab and rendering it to a couple of formats.
If you want to follow along step-by-step in your own environment, download the notebook below.

::: {.callout-note appearance="minimal"}
<i class="bi bi-journal-code"></i> [Download hello.ipynb](_hello.ipynb){download="hello.ipynb"}
:::

Then, create a new directory to work within, copy the notebook into this directory, and switch to this directory in a Terminal.

Next, execute these commands to install JupyterLab along with the packages used in the tutorial (`matplotlib` and `plotly),` and to open the tutorial notebook:

+---------------+------------------------------------------------+
| Platform      | Commands                                       |
+===============+================================================+
| Mac/Linux     | ```{.bash filename="Terminal"}                 |
|               | python3 -m pip install jupyter jupyterlab      |
|               | python3 -m pip install matplotlib plotly       |
|               | python3 -m jupyter lab hello.ipynb             |
|               | ```                                            |
+---------------+------------------------------------------------+
| Windows       | ```{.bash filename="Terminal"}                 |
|               | py -m pip install jupyter jupyterlab           |
|               | py -m pip install matplotlib plotly            |
|               | py -m jupyter lab hello.ipynb                  |
|               | ```                                            |
+---------------+------------------------------------------------+

Here is our notebook in Jupyter Lab.

```` {.markdown .visually-hidden}
---
title: "Quarto Basics"
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

![](images/jupyter-basics.png){.border fig-alt="A Jupyter notebook titled Quarto Basics containing some text, a code cell, and the result of the code cell, which is a line plot on a polar axis."}

Next, create a new Terminal within Jupyter Lab to use for Quarto commands.

![](images/jupyter-terminal.png){.border fig-alt="Screenshot of menu items in Jupuyter Lab: File > New > Terminal."}

And finally, render the notebook to a couple of formats.

``` {.bash filename="Terminal"}
quarto render hello.ipynb --to html
quarto render hello.ipynb --to docx
```

Note that the target file (in this case `hello.ipynb`) should always be the very first command line argument.

When you render a Jupyter notebook with Quarto, the contents of the notebook (code, markdown, and outputs) are converted to plain markdown and then processed by [Pandoc](http://pandoc.org/), which creates the finished format.

![](images/ipynb-how-it-works.png){style="margin-left: 15px;" fig-align="left" width="516" fig-alt="Workflow diagram starting with a Jupyter notebook, then md, then pandoc, then PDF, MS Word, or HTML."}

## Authoring

The `quarto render` command is used to create the final version of your document for distribution.
However, during authoring you'll use the `quarto preview` command.
Try it now from the Terminal with `hello.ipynb`.

``` {.bash filename="Terminal"}
quarto preview hello.ipynb
```

This will render your document and then display it in a web browser.

![](images/quarto-preview.png){.border fig-alt="Rendered version of the earlier notebook in a web browser." width="500"}

You might want to position Jupyter Lab and the browser preview side-by-side so you can see changes as you work.

![](images/jupyter-quarto-preview.png){fig-alt="Side-by-side preview of notebook on the left and live preview in the browser on the right."}

To see live preview in action:

1.  Change the the line of code that defines `theta` as follows:

    ``` python
    theta = 4 * np.pi * r
    ```

2.  Re-run the code cell to generate a new version of the plot.

3.  Save the notebook (the preview will update automatically).

This is the basic workflow for authoring with Quarto. Once you are comfortable with this, we also recommend installing the [Quarto JupyterLab Extension](/docs/tools/jupyter-lab-extension.qmd) which provides additional tools for working with Quarto in JupyterLab.

There are few different types of cells in our notebook, let's work a bit with each type.

## YAML Options

You are likely already familiar with markdown and code cells, but there is a new type of cell ("Raw") that is used for document-level YAML options.

``` {.yaml .visually-hidden}
---
title: "Quarto Basics"
format:
  html:
    code-fold: true
jupyter: python3
---
```

![](images/jupyter-yaml.png){.border fig-alt="YAML of the notebook with the fields title, format, and jupyter. Title is set to Quarto Basics with title: \"Quarto Basics\". Format is defined as html in the next line, and within the html format, code-fold is set to true. Jupyter is set to python3 with jupyter: python3."}

Try changing the `code-fold` option to `false`.

``` yaml
format: 
  html:
    code-fold: false
```

Then save the notebook.
You'll notice that the code is now shown above the plot, where previously it was hidden with a **Code** button that could be used to show it.

## Markdown Cells

Markdown cells contain raw markdown that will be passed through to Quarto during rendering.
You can use any valid Quarto [markdown syntax](/docs/authoring/markdown-basics.qmd) in these cells.
Here we specify a header and a cross-reference to the figure created in the code cell below.

``` {.markdown .visually-hidden}
## Polar Axis

For a demonstration of a line plot on a polar axis, see @fig-polar.
```

![](images/jupyter-markdown.png){.border fig-alt="A Markdown cell with the title Polar Axis as a second level header and text that reads 'For a demonstration of a line plot on a polar axis, see @fig-polar.'"}

Try changing the header and saving the notebook---the preview will update with the new header text.

## Code Cells

You are likely already familiar with code cells, like the one shown below.

```` {.markdown .visually-hidden}
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

![](images/jupyter-cell.png){.border fig-alt="A code cell with cell options for label and fig-cap and the code required to create the line plot on a polar axis."}

But there are some new components at the top of the code cell: `label` and `fig-cap`options.
Cell options are written in YAML using a specially prefixed comment (`#|`).

In this example, the cell options are used to make the figure cross-reference-able.
Try changing the `fig-cap` and/or the code, running the cell, and then saving the notebook to see the updated preview.

There are a wide variety of [cell options](/docs/reference/cells/cells-jupyter.qmd) that you can apply to tailor your output.
We'll delve into these options in the next tutorial.

::: callout-note
One particularly useful cell option for figures is `fig-alt`, which enables you to add alternative text to images for users with visual impairments.
See Amy Cesal's article on [Writing Alt Text for Data Visualization](https://medium.com/nightingale/writing-alt-text-for-data-visualization-2a218ef43f81) to learn more.
:::


{{< include _footer.md >}}

Additionally, you may want to install the [Quarto JupyterLab Extension](/docs/tools/jupyter-lab-extension.qmd) which provides additional tools for working with Quarto in JupyterLab.


# quarto-web/docs/get-started/hello/_hello.qmd

---
title: "Quarto Basics"
format:
  html:
    code-fold: true
jupyter: python3
---

## Polar Axis

For a demonstration of a line plot on a polar axis, see @fig-polar.

```{python}
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


# quarto-web/docs/get-started/hello/vscode.qmd

---
title: "Tutorial: Hello, Quarto"
editor_options:
  markdown:
    wrap: sentence
    canonical: true
---

{{< include ../_tool-chooser.md >}}


## Overview

In this tutorial we'll show you how to use Quarto with VS Code.
Before getting started, you should install the [Quarto VS Code Extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto), which includes many tools that enhance working with Quarto, including:

-   Integrated render and preview for Quarto documents.
-   Syntax highlighting for markdown and embedded languages
-   Completion and diagnostics for YAML options
-   Completion for embedded languages (e.g. Python, R, Julia, etc.)
-   Commands and key-bindings for running cells and selected lines.

You can install the Quarto extension from within the **Extensions** tab in VS Code, from the [Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=quarto.quarto), the [Open VSX Registry](https://open-vsx.org/extension/quarto/quarto) or directly from a [VISX extension file](https://github.com/quarto-dev/quarto-vscode#visx-install).

::: callout-note
This tutorial focuses on editing plain text Quarto `.qmd` files in VS Code. Depending on your preferences and the task at hand there are two other editing modes available for Quarto documents: the [Visual Editor](/docs/visual-editor/vscode/index.qmd) and the [Notebook Editor](/docs/tools/vscode-notebook.qmd). For the purposes of learning we recommend you work through this tutorial using the VS Code text editor, then after you've mastered the basics explore using the other editing modes.
:::

### Basic Workflow

Quarto `.qmd` files contain a combination of markdown and executable code cells.
Here's what it might look like in VS Code to edit and preview a `.qmd` file:

![](/docs/tools/images/vscode-render.png){.border fig-alt="Two windows arranged side by side. The window on the left is a qmd file opened in VSCode. The contents of this document are the same as the first part of the Getting Started: Welcome section of this website. The contents of this document are rendered by Quarto in the window on the right."}

The document on the left is *rendered* into the HTML version you see on the right.
This is the basic model for Quarto publishing---take a source document and render it to a variety of [output formats](https://quarto.org/docs/output-formats/all-formats.html), including HTML, PDF, MS Word, etc.

The tutorials will make use of the `matplotlib` and `plotly` Python packages---the commands you can use to install them are given in the table below.

+-----------+---------------------------------------------------+
| Platform  | Commands                                          |
+===========+===================================================+
|           | ```{.bash filename="Terminal"}                    |
| Mac/Linux | python3 -m pip install jupyter matplotlib plotly  |
|           | ```                                               |
+-----------+---------------------------------------------------+
|           | ```{.powershell filename="Terminal"}              |
| Windows   | py -m pip install jupyter matplotlib plotly       |
|           | ```                                               |
+-----------+---------------------------------------------------+

::: callout-note
Note that while this tutorial uses Python, using Julia (via the [IJulia](https://julialang.github.io/IJulia.jl/stable/) kernel) is also well supported.
See the article on [Using Julia](/docs/computations/julia.qmd) for additional details.
:::

## Render and Preview

We'll start out by rendering a simple example (`hello.qmd`) to a couple of formats.
If you want to follow along step-by-step in your own environment, create a new file named `hello.qmd` and copy the following content into it.

```` markdown
---
title: "Quarto Basics"
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

Note that if you are following along be sure to install the required dependencies if you haven't already:

+-----------+----------------------------------------------------+
| Platform  | Commands                                           |
+===========+====================================================+
|           | ```{.bash filename="Terminal"}                     |
| Mac/Linux | python3 -m pip install jupyter matplotlib plotly   |
|           | ```                                                |
+-----------+----------------------------------------------------+
|           | ```{.powershell filename="Terminal"}               |
| Windows   | py -m pip install jupyter matplotlib plotly        |
|           | ```                                                |
+-----------+----------------------------------------------------+

To render and preview, execute the **Quarto: Preview** command.
You can alternatively use the <kbd>Ctrl+Shift+K</kbd> keyboard shortcut, or the **Preview** button at the top right of the editor:

![](/docs/tools/images/vscode-preview-button.png){.border fig-alt="The top of the Visual Studio code editor. The right side of the editor tab area includes a Preview button."}

::: {.callout-note appearance="simple"}
Note that on the Mac you should use `Cmd` rather than `Ctrl` as the prefix for all Quarto keyboard shortcuts.
:::


### How it Works

When you render a `.qmd` file with Quarto, the executable code blocks are processed by Jupyter, and the resulting combination of code, markdown, and output is converted to plain markdown.
Then, this markdown is processed by [Pandoc](http://pandoc.org/), which creates the finished format.

![](images/qmd-how-it-works.png){alt="" fig-alt="Workflow diagram starting with a qmd file, then Jupyter, then md, then pandoc, then PDF, MS Word, or HTML." fig-align="left"}

### Authoring

Let's try making a small change and then re-rendering:

1.  Change the line of code that defines `theta` as follows:

    ``` python
    theta = 4 * np.pi * r
    ```

2.  Re-render the file (using **Quarto: Preview** or the <kbd>Ctrl+Shift+K</kbd> shortcut) The document is rendered, and the browser preview is updated.

This is the basic workflow for authoring with Quarto.

You do not need to save the file before rendering (as this happens automatically when you render).
If you prefer, you can configure the Quarto extension to render whenever you save a document.
See the documentation on [Render on Save](/docs/tools/vscode.qmd#render-on-save) for additional details.

### Running Cells

You don't need to fully render documents in order to iterate on code cells.
You'll notice that there is a **Run Cell** button above the code cell.
Click that button to execute the cell (output is shown side by side in the Jupyter interactive console):

![](/docs/tools/images/vscode-execute-cell.png){.border fig-alt="VS Code with two panes open, vscode.qmd source code on the right, and the interactive output of that code shown in a second pane on the left."}

Execute the current cell with <kbd>Ctrl+Shift+Enter</kbd>, the current line(s) with <kbd>Ctrl+Enter</kbd>, or previous cells with <kbd>Ctrl+Alt+P</kbd> (note that on the Mac you should use `Cmd` rather than `Ctrl` as the prefix for all Quarto keyboard shortcuts).

There are few different types of content in `hello.qmd`, let's work a bit with each type.

## YAML Options

At the top of the file there is a YAML block with document level options.

``` yaml
---
title: "Quarto Basics"
format:
  html:
    code-fold: true
jupyter: python3
---
```

Try changing the `code-fold` option to `false`:

``` yaml
format: 
  html:
    code-fold: false
```

Then re-render the document (again, no need to save before rendering).
You'll notice that the code is now shown above the plot, where previously it was hidden with a **Code** button that could be used to show it.

## Markdown

Narrative content is written using markdown.
Here we specify a header and a cross-reference to the figure created in the code cell below.

``` markdown
## Polar Axis

For a demonstration of a line plot on a polar axis, see @fig-polar.
```

Try changing the header and re-rendering---the preview will update with the new header text.

## Code Cells

Code cells contain executable code to be run during render, with the output (and optionally the code) included in the rendered document.

```` markdown
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

You are likely familiar with the Matplotlib code given here.
However, there are some less familiar components at the top of the code cell: `label` and `fig-cap` options.
Cell options are written in YAML using a specially prefixed comment (`#|`).

In this example, the cell options are used to make the figure cross-reference-able.
Try changing the `fig-cap` and/or the code then re-rendering to see the updated preview.

There are a wide variety of [cell options](/docs/reference/cells/cells-jupyter.qmd) that you can apply to tailor your output.
We'll delve into these options in the next tutorial.

::: callout-note
One particularly useful cell option for figures is `fig-alt`, which enables you to add alternative text to images for users with visual impairments.
See Amy Cesal's article on [Writing Alt Text for Data Visualization](https://medium.com/nightingale/writing-alt-text-for-data-visualization-2a218ef43f81) to learn more.
:::

## External Preview

In this tutorial we've demonstrated previewing rendered output in a pane within VS Code.
If you prefer to use an external browser for preview (or have no preview triggered at all by rendering) you can use the **Preview Type** option to specify an alternate behavior:

![](/docs/tools/images/vscode-preview-settings.png){.border fig-alt="VS Code settings interface with 'quarto preview type' entered into the search bar. User settings reveals Quarto > Render: Preview Type, with a dropdown to select location for document preview after render. The default, internal, is selected, which previews using a side-by-side panel in VS Code. The other two options in the dropdown are external and none."}

{{< include _footer.md >}}

Additionally, may wish to learn about the other editing modes for Quarto documents available within VS Code:

-  The [Visual Editor](/docs/visual-editor/vscode/index.qmd) for WYSIWYG editing of `.qmd` documents.

-  The [Notebook Editor](/docs/tools/vscode-notebook.qmd) for editing `.ipynb` notebooks.


# quarto-web/docs/get-started/hello/index.qmd

---
title: "Tutorial: Hello, Quarto"
include-in-header: ../_redirect.html
---



# quarto-web/docs/get-started/hello/neovim.qmd

---
title: "Tutorial: Hello, Quarto"
editor_options:
  markdown:
    wrap: sentence
    canonical: true
---

{{< include ../_tool-chooser.md >}}

## Overview

In this tutorial we'll show you how to use Quarto with Neovim. While we cover the basics here, you will also want to review the article on [Using Neovim with Quarto](/docs/tools/neovim.qmd) to learn more about installing, using, and customizing Neovim for Quarto. 

If you already have Neovim configured to your liking, you may only want to add the [quarto-nvim](https://github.com/quarto-dev/quarto-nvim) plugin and only refer to this guide for inspiration and seeing the possibilities.
But if you are entirely new to Neovim or want to simply try out a configuration already set up for data science with Quarto, you should head over to this [kickstarter configuration](https://github.com/jmbuhr/quarto-nvim-kickstarter).
This is also what we will be using for this tutorial.

::: callout-note
Neovim is a highly customizable editor.
So much so that Neovim core member TJ Devries has recently coined the term Personal Development Environments (PDE)^[In [this video](https://www.youtube.com/watch?v=QMVIJhC9Veg)] to separate the concept from Integrated Development Environments (IDEs) such as VS Code and RStudio.

Out of the box neovim is fairly minimal.
To work efficiently and get all the nice features, you have to configure it.
You have to make it your own.
If this approach sounds enticing to you, read on.
Welcome to the rabbit hole. 🐰
:::


You can also watch [this video](https://youtu.be/3sj7clNowlA) for a quick guide to getting started with the kickstarter configuration alongside this write-up.

{{< video https://youtu.be/3sj7clNowlA >}}

The Quarto Neovim plugin aims to not reinvent the wheel.
Existing plugins in the Neovim ecosystem are leveraged to provide the full experience.
Some of the features provided by `quarto-nvim` and enhanced by plugins found in the kickstarter configuration are:

-   Preview for Quarto documents.
-   Syntax highlighting for markdown and embedded languages
-   Completion for embedded languages (e.g. Python, R, Julia, etc.)
-   Commands and key-bindings for running cells and selected lines.
-   Completion for bibliography references, file paths, LaTeX math symbols, emoji.
-   Optional spellchecking and completion.
-   Code snippets.
-   Export of code chunks into standalone scripts.

See the article on [Using Neovim with Quarto](/docs/tools/neovim.qmd) for all of the details.

### Basic Workflow

Quarto `.qmd` files contain a combination of markdown and executable code cells.
Here's what it might look like in Neovim to edit and preview a `.qmd` file:

![](./images/neovim-overview.png){.border fig-alt="Three windows arranged side by side. The window on the left is a qmd file opened in Neovim. The upper window on the right is a web browser. The contents of the qmd document are rendered by Quarto in the browser window. The third window is a rendered graph showing the output of executing a code chunk in the qmd file."}

The document on the right is *rendered* into the HTML version you see on the left.
This is the basic model for Quarto publishing---take a source document and render it to a variety of [output formats](https://quarto.org/docs/output-formats/all-formats.html), including HTML, PDF, MS Word, etc.

The tutorials will make use of the `matplotlib` and `plotly` Python packages---the commands you can use to install them are given in the table below.

+-----------+-----------------------------------------------------+
| Platform  | Commands                                            |
+===========+=====================================================+
|           | ```{.bash filename="Terminal"}                      |
| Mac/Linux | python3 -m pip install jupyter matplotlib plotly    |
|           | ```                                                 |
+-----------+-----------------------------------------------------+
|           | ```{.powershell filename="Terminal"}                |
| Windows   | py -m pip install jupyter matplotlib plotly         |
|           | ```                                                 |
+-----------+-----------------------------------------------------+

::: callout-note
Note that while this tutorial uses Python, using Julia (via the [IJulia](https://julialang.github.io/IJulia.jl/stable/) kernel) or using R (via the [knitr package](https://github.com/yihui/knitr)), are also well supported.
See the articles on [Using Julia](/docs/computations/julia.qmd) and [Using R](/docs/computations/r.qmd) for additional details.
:::

## Render and Preview

We'll start out by rendering a simple example (`hello.qmd`) to a couple of formats.
If you want to follow along step-by-step in your own environment, create a new file named `hello.qmd` and copy the following content into it.

```` markdown
---
title: "Quarto Basics"
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
ax.plot(theta, r);
ax.set_rticks([0.5, 1, 1.5, 2]);
ax.grid(True);
plt.show()
```
````

To render and preview, execute the **QuartoPreview** command by pressing `:` to enter command mode and typing the command (there is autocompletion if you press the <kbd>tab</kbd> key).
In the kickstarter configuration, there are more shortcuts starting with <kbd>space q</kbd> (spacebar followed by q, in normal mode).

### How it Works

When you render a `.qmd` file with Quarto, the executable code blocks are processed by Jupyter, and the resulting combination of code, markdown, and output is converted to plain markdown.
Then, this markdown is processed by [Pandoc](http://pandoc.org/), which creates the finished format.

![](images/qmd-how-it-works.png){alt="" fig-alt="Workflow diagram starting with a qmd file, then Jupyter, then md, then pandoc, then PDF, MS Word, or HTML." fig-align="left"}

### Authoring

Let's try making a small change and then re-rendering:

1.  Change the line of code that defines `theta` as follows:

    ``` python
    theta = 4 * np.pi * r
    ```

2.  Save the file using either `:w` in normal mode or `ctrl-s` ^[if you are using the kickstarter configuration -- otherwise `ctrl-s` puts your terminal in a waiting mode until you press `ctrl+q`, which can be confusing]

The document is rendered, and the browser preview is updated.
This is the basic workflow for authoring with Quarto.

### Running Cells

{{< include _neovim-running-cells.md >}}

There are few different types of content in `hello.qmd`, let's work a bit with each type.

## YAML Options

At the top of the file there is a YAML block with document level options.

``` yaml
---
title: "Quarto Basics"
format:
  html:
    code-fold: true
jupyter: python3
---
```

Try changing the `code-fold` option to `false`:

``` yaml
format: 
  html:
    code-fold: false
```

Then re-render the document by saving it.
You'll notice that the code is now shown above the plot, where previously it was hidden with a **Code** button that could be used to show it.

Narrative content is written using markdown.
Here we specify a header and a cross-reference to the figure created in the code cell below.

``` markdown
## Polar Axis

For a demonstration of a line plot on a polar axis, see @fig-polar.
```

Try changing the header and re-rendering---the preview will update with the new header text.

## Code Cells

Code cells contain executable code to be run during render, with the output (and optionally the code) included in the rendered document.

```` markdown
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

You are likely familiar with the Matplotlib code given here.
However, there are some less familiar components at the top of the code cell: `label` and `fig-cap` options.
Cell options are written in YAML using a specially prefixed comment (`#|`).

In this example, the cell options are used to make the figure cross-reference-able.
Try changing the `fig-cap` and/or the code then re-rendering to see the updated preview.

There are a wide variety of [cell options](/docs/reference/cells/cells-jupyter.qmd) that you can apply to tailor your output.
We'll delve into these options in the next tutorial.

::: callout-note
One particularly useful cell option for figures is `fig-alt`, which enables you to add alternative text to images for users with visual impairments.
See Amy Cesal's article on [Writing Alt Text for Data Visualization](https://medium.com/nightingale/writing-alt-text-for-data-visualization-2a218ef43f81) to learn more.
:::


## Next Up

You now know the basics of creating and authoring Quarto documents. The following tutorials explore Quarto in more depth:

-   [Tutorial: Computations](../computations/) --- Learn how to tailor the behavior and output of executable code blocks.

-   [Tutorial: Authoring](../authoring/) --- Learn more about output formats and technical writing features like citations, crossrefs, and advanced layout.

See the article on [Using Neovim with Quarto](/docs/tools/neovim.qmd) to learn more about installing, using, and customizing Neovim for Quarto. 


# quarto-web/docs/get-started/hello/text-editor.qmd

---
title: "Tutorial: Hello, Quarto"
editor_options:
  markdown:
    wrap: sentence
    canonical: true
---

{{< include ../_tool-chooser.md >}}


## Overview

In this tutorial we'll show you how to use your favorite text editor with Quarto.
You'll edit plain text `.qmd` files and preview the rendered document in a web browser as you work.

Below is an overview of how this will look.

![](images/text-editor-quarto-preview.png){.border .column-body-outset-right fig-alt="On the left: A VS Code notebook titled Quarto Basics containing some text, a code cell, and the result of the code cell, which is a line plot on a polar axis. On the right: Rendered version of the same notebook."}

The notebook on the left is *rendered* into the HTML version you see on the right.
This is the basic model for Quarto publishing---take a source document (in this case a notebook) and render it to a variety of [output formats](https://quarto.org/docs/output-formats/all-formats.html), including HTML, PDF, MS Word, etc.

The tutorials will make use of the `matplotlib` and `plotly` Python packages---the commands you can use to install them are given in the table below.

+-----------+---------------------------------------------------+
| Platform  | Commands                                          |
+===========+===================================================+
|           | ```{.bash filename="Terminal"}                    |
| Mac/Linux | python3 -m pip install jupyter matplotlib plotly  |
|           | ```                                               |
+-----------+---------------------------------------------------+
|           | ```{.powershell filename="Terminal"}              |
| Windows   | py -m pip install jupyter matplotlib plotly       |
|           | ```                                               |
+-----------+---------------------------------------------------+

::: callout-note
Note that while this tutorial uses Python, using Julia (via the [IJulia](https://julialang.github.io/IJulia.jl/stable/) kernel) is also well supported.
See the article on [Using Julia](/docs/computations/julia.qmd) for additional details.
:::

## Editor Modes

If you are using VS Code, you should install the [Quarto Extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto) for VS Code before proceeding.
The extension provides syntax highlighting for markdown and embedded languages, completion for embedded languages (e.g. Python, R, Julia, LaTeX, etc.), commands and key-bindings for running cells and selected line(s), and much more.

There are also Quarto syntax highlighting modes available for several other editors:

| Editor       | Extension                                      |
|--------------|------------------------------------------------|
| Emacs        | <https://github.com/quarto-dev/quarto-emacs>   |
| Vim / Neovim | <https://github.com/quarto-dev/quarto-vim>     |
| Neovim       | <https://github.com/quarto-dev/quarto-nvim>    |
| Sublime Text | <https://github.com/quarto-dev/quarto-sublime> |

: {tbl-colwidths="\[30,70\]"}

## Rendering

We'll start out by rendering a simple example (`hello.qmd`) to a couple of formats.
If you want to follow along step-by-step in your own environment, create a new file named `hello.qmd` and copy the following content into it.

```` markdown
---
title: "Quarto Basics"
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

Next, open a Terminal and switch to the directory containing `hello.qmd`.

Let's start by rendering the document to a couple of formats.

``` {.bash filename="Terminal"}
quarto render hello.qmd --to html
quarto render hello.qmd --to docx
```

Note that the target file (in this case `hello.qmd`) should always be the very first command line argument.

When you render a `.qmd` file with Quarto, the executable code blocks are processed by Jupyter, and the resulting combination of code, markdown, and output is converted to plain markdown.
Then, this markdown is processed by [Pandoc](http://pandoc.org/), which creates the finished format.

![](images/qmd-how-it-works.png){alt="" fig-alt="Workflow diagram starting with a qmd file, then Jupyter, then md, then pandoc, then PDF, MS Word, or HTML." fig-align="left"}

## Authoring

The `quarto render` command is used to create the final version of your document for distribution.
However, during authoring you'll use the `quarto preview` command.
Try it now from the Terminal with `hello.qmd`.

``` {.bash filename="Terminal"}
quarto preview hello.qmd
```

This will render your document and then display it in a web browser.

![](images/quarto-preview.png){.border fig-alt="Rendered version of the earlier notebook in a web browser." width="500"}

You might want to position your editor and the browser preview side-by-side so you can see changes as you work.

![](images/text-editor-quarto-preview.png){.border .column-body-outset-right fig-alt="Side-by-side preview of notebook on the left and live preview in the browser on the right."}

To see live preview in action:

1.  Change the the line of code that defines `theta` as follows:

    ``` python
    theta = 4 * np.pi * r
    ```

2.  Save the file.
    The document is re-rendered, and the browser preview is updated.

This is the basic workflow for authoring with Quarto.

There are few different types of content in `hello.qmd`, let's work a bit with each type.

## YAML Options

At the top of the file there is a YAML block with document level options.

``` yaml
---
title: "Quarto Basics"
format:
  html:
    code-fold: true
jupyter: python3
---
```

Try changing the `code-fold` option to `false`:

``` yaml
format: 
  html:
    code-fold: false
```

Then save the file.
You'll notice that the code is now shown above the plot, where previously it was hidden with a **Code** button that could be used to show it.

## Markdown

Narrative content is written using markdown.
Here we specify a header and a cross-reference to the figure created in the code cell below.

``` markdown
## Polar Axis

For a demonstration of a line plot on a polar axis, see @fig-polar.
```

Try changing the header and saving the notebook---the preview will update with the new header text.

## Code Cells

Code cells contain executable code to be run during render, with the output (and optionally the code) included in the rendered document.

```` markdown
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

You are likely familiar with the Matplotlib code given here.
However, there are some less familiar components at the top of the code cell: `label` and `fig-cap` options.
Cell options are written in YAML using a specially prefixed comment (`#|`).

In this example, the cell options are used to make the figure cross-reference-able.
Try changing the `fig-cap` and/or the code, running the cell, and then saving the file to see the updated preview.

There are a wide variety of [cell options](/docs/reference/cells/cells-jupyter.qmd) that you can apply to tailor your output.
We'll delve into these options in the next tutorial.

::: callout-note
One particularly useful cell option for figures is `fig-alt`, which enables you to add alternative text to images for users with visual impairments.
See Amy Cesal's article on [Writing Alt Text for Data Visualization](https://medium.com/nightingale/writing-alt-text-for-data-visualization-2a218ef43f81) to learn more.
:::

{{< include _footer.md >}}


# quarto-web/docs/get-started/hello/rstudio.qmd

---
title: "Tutorial: Hello, Quarto"
editor_options:
  markdown:
    wrap: sentence
    canonical: true
---

{{< include ../_tool-chooser.md >}}

## Overview

Quarto is a multi-language, [next-generation](/docs/faq/rmarkdown.qmd) version of R Markdown from Posit and includes dozens of new features and capabilities while at the same being able to render most existing Rmd files without modification.

In this tutorial, we'll show you how to use RStudio with Quarto.
You'll edit code and markdown in RStudio just as you would with any computational document (e.g., R Markdown) and preview the rendered document in the Viewer tab as you work.

The following is a Quarto document with the extension `.qmd` (on the left), along with its rendered version as HTML (on the right).
You could also choose to render it into other formats like PDF, MS Word, etc.

![](images/rstudio-hello.png){.column-page-right .border fig-alt="RStudio with a Quarto document titled \"Penguins, meet Quarto!\" open on the left side and the rendered version of the document on the right side." fig-align="center"}

This is the basic model for Quarto publishing---take a source document and render it to a variety of output formats.

If you would like a video introduction to Quarto before you dive into the tutorial, watch the [Get Started with Quarto](https://youtu.be/_f3latmOhew) where you can see a preview of authoring a Quarto document with executable code chunks, rendering to multiple formats, including revealjs presentations, creating a website, and publishing on QuartoPub.

{{< video "https://www.youtube.com/embed/_f3latmOhew" >}}

If you would like to follow along with this tutorial in your own environment, follow the steps outlined below.

1.  Download and install the latest release of RStudio ({{< var rstudio.current_release >}}):

    ::: {.callout appearance="minimal"}
    <i class="bi bi-download"></i> [Download RStudio {{< var rstudio.current_release >}}](https://posit.co/download/rstudio-desktop/)
    :::

2.  Be sure that you have installed the `tidyverse` and `palmerpenguins` packages:

    ``` r
    install.packages("tidyverse")
    install.packages("palmerpenguins")
    ```

3.  Download the Quarto document (`.qmd`) below, open it in RStudio, and click on <kbd>![](images/rstudio-render-button.png){width="25" height="20"}</kbd> Render.

    ::: {.callout appearance="minimal"}
    <i class="bi bi-download"></i> [Download hello.qmd](rstudio/_hello.qmd){download="hello.qmd"}
    :::

## Rendering

Use the <kbd>![](images/rstudio-render-button.png){width="25" height="20"}</kbd> **Render** button in the RStudio IDE to render the file and preview the output with a single click or keyboard shortcut (⇧⌘K).

![](images/rstudio-render.png){.border fig-alt="Top of the text editor in RStudio with the Render button highlighted with a purple box." fig-align="center"}

If you prefer to automatically render whenever you save, you can check the Render on Save option on the editor toolbar.
The preview will update whenever you re-render the document.
Side-by-side preview works for both HTML and PDF outputs.

![](images/rstudio-render-on-save.png){.border fig-alt="Top of the text editor in RStudio with the Render on Save checkbox checked and highlighted with a purple box." fig-align="center"}

Note that documents can also be rendered from the R console via the **quarto** package:

``` r
install.packages("quarto")
quarto::quarto_render("hello.qmd")
```

When rendering, Quarto generates a new file that contains selected text, code, and results from the .qmd file.
The new file can be an [HTML](https://quarto.org/docs/output-formats/all-formats.html), [PDF](https://quarto.org/docs/output-formats/pdf-basics.html), [MS Word](https://quarto.org/docs/output-formats/ms-word.html) document, [presentation](https://quarto.org/docs/presentations/), [website](https://quarto.org/docs/websites/), [book](https://quarto.org/docs/books/), [interactive document](https://quarto.org/docs/interactive/), or [other format](https://quarto.org/docs/output-formats/all-formats.html).

## Authoring

In the image below, we can see the same document in the two modes of the RStudio editor: visual (on the left) and source (on the right).
RStudio's [visual editor](/docs/visual-editor/) offers an [WYSIWYM](https://en.wikipedia.org/wiki/WYSIWYM) authoring experience for markdown.
For formatting (e.g., bolding text), you can use the toolbar, a keyboard shortcut (⌘B), or the markdown construct (`**bold**`).
The plain text source code underlying the document is written for you, and you can view/edit it at any point by switching to source mode for editing.
You can toggle back and forth between these two modes by clicking on **Source** and **Visual** in the editor toolbar (or using the keyboard shortcut ⌘⇧ F4).

![](images/rstudio-source-visual.png){.column-page-right fig-alt="On the left: Document in the visual editor. On the right: Same document in the source editor. The visual/source editor toggle is highlighted in both documents marking their current state. The document shown is the \"Hello Quarto\" document from a previous image on the page." fig-align="center"}

Next, let's turn our attention to the contents of our Quarto document.
The file contains three types of content: a YAML header, code chunks, and markdown text.

### YAML header

An (optional) YAML header demarcated by three dashes (`---`) on either end.

``` yaml
---
title: "Hello, Quarto"
format: html
editor: visual
---
```

When rendered, the `title`, `"Hello, Quarto"`, will appear at the top of the rendered document with a larger font size than the rest of the document.
The other two YAML fields denote that the output should be in `html` `format` and the document should open in the `visual` `editor` by default.

The basic syntax of YAML uses key-value pairs in the format `key: value`.
Other YAML fields commonly found in headers of documents include metadata like `author`, `subtitle`, `date` as well as customization options like `theme`, `fontcolor`, `fig-width`, etc.
You can find out about all available YAML fields for HTML documents [here](/docs/reference/formats/html.html).
The available YAML fields vary based on document format, e.g., see [here](/docs/reference/formats/pdf.html) for YAML fields for PDF documents and [here](/docs/reference/formats/docx.html) for MS Word.

### Code chunks

R code chunks identified with `{r}` with (optional) chunk options, in YAML style, identified by `#|` at the beginning of the line.

```` markdown
```{{r}}
#| label: load-packages
#| include: false

library(tidyverse)
library(palmerpenguins)
```
````

In this case, the `label` of the code chunk is `load-packages`, and we set `include` to `false` to indicate that we don't want the chunk itself or any of its outputs in the rendered documents.

In addition to rendering the complete document to view the results of code chunks, you can also run each code chunk interactively in the RStudio editor by clicking the ![](https://d33wubrfki0l68.cloudfront.net/18153fb9953057ee5cff086122bd26f9cee8fe93/3aba9/images/notebook-run-chunk.png) icon or keyboard shortcut (⇧⌘⏎).
RStudio executes the code and displays the results either inline within your file or in the Console, depending on your preference.

![](images/rstudio-inline-output.png){fig-alt="In the background, the code chunk labeled plot-penguins from hello.qmd. The chunk is partially covered by its output, a scatterplot showing the relationship between bill length and flipper length of penguins, colors by species. The button for running the code chunk is highlighted, and an arrow extends to the plot, showing that clicking the button results in the plot being generated." fig-align="center"}

### Markdown text

Text with formatting, including section headers, hyperlinks, an embedded image, and an inline code chunk.

![](images/rstudio-text.png){.border fig-alt="Text portion of the of the linked example document titled \"Penguins, meet Quarto!\", with an annotation that reads \"Text\"." fig-align="center"}

Quarto uses markdown syntax for text.
If using the visual editor, you won't need to learn much markdown syntax for authoring your document, as you can use the menus and shortcuts to add a header, bold text, insert a table, etc.
If using the source editor, you can achieve these with markdown expressions like `##`, `**bold**`, etc.

## How it works

When you render a Quarto document, first [knitr](http://yihui.name/knitr/) executes all of the code chunks and creates a new markdown (.md) document, which includes the code and its output.
The markdown file generated is then processed by [pandoc](http://pandoc.org/), which creates the finished format.
The Render button encapsulates these actions and executes them in the right order for you.

![](images/rstudio-qmd-how-it-works.png){.border fig-alt="Workflow diagram starting with a qmd file, then knitr, then md, then pandoc, then PDF, MS Word, or HTML." fig-align="center"}

{{< include _footer.md >}}


# quarto-web/docs/get-started/hello/rstudio/_hello.qmd

---
title: "Hello, Quarto"
format: html
editor: visual
---

```{r}
#| label: load-packages
#| include: false

library(tidyverse)
library(palmerpenguins)
```

## Meet Quarto

Quarto enables you to weave together content and executable code into a finished document. To learn more about Quarto see <https://quarto.org>.

## Meet the penguins

![](https://raw.githubusercontent.com/quarto-dev/quarto-web/main/docs/get-started/hello/rstudio/lter_penguins.png){style="float:right;" fig-alt="Illustration of three species of Palmer Archipelago penguins: Chinstrap, Gentoo, and Adelie. Artwork by @allison_horst." width="401"}

The `penguins` data from the [**palmerpenguins**](https://allisonhorst.github.io/palmerpenguins "palmerpenguins R package") package contains size measurements for `r nrow(penguins)` penguins from three species observed on three islands in the Palmer Archipelago, Antarctica.

The plot below shows the relationship between flipper and bill lengths of these penguins.

```{r}
#| label: plot-penguins
#| warning: false
#| echo: false

ggplot(penguins, 
       aes(x = flipper_length_mm, y = bill_length_mm)) +
  geom_point(aes(color = species, shape = species)) +
  scale_color_manual(values = c("darkorange","purple","cyan4")) +
  labs(
    title = "Flipper and bill length",
    subtitle = "Dimensions for penguins at Palmer Station LTER",
    x = "Flipper length (mm)", y = "Bill length (mm)",
    color = "Penguin species", shape = "Penguin species"
  ) +
  theme_minimal()
```


# quarto-web/docs/websites/website-about.qmd

---
title: About Pages
---

## Overview

Quarto makes it easy to create a simple about page for an individual or organization. When the `about` option is provided for a document, a special template will be used to layout the content of the current page with a custom layout designed to present a person or organization.

For example:

``` markdown
---
title: "Finley Malloc"
about:
  template: jolla
  image: profile.jpg
  links:
    - icon: twitter
      text: twitter
      href: https://twitter.com
    - icon: github
      text: Github
      href: https://github.com
---

Finley Malloc is the Chief Data Scientist at Wengo Analytics. When not innovating on data platforms, Finley enjoys spending time unicycling and playing with her pet iguana.

## Education

University of California, San Diego | San Diego, CA
PhD in Mathematics | Sept 2011 - June 2015

Macalester College | St. Paul MA
B.A in Economics | Sept 2007 - June 2011

## Experience

Wengo Analytics | Head Data Scientist | April 2018 - present

GeoScynce | Chief Analyst | Spet 2012 - April 2018
```

The contents of this page will be laid out using the `jolla` template with the `profile.jpg` image, and generate a set of links for the items specified in `links`.

You can write and format the content of the page however you'd like - when the page is rendered, Quarto will use the content and options provided in the `about` option to create the about page, arranging the content of the `about` option with the content in the page itself.

## Templates

Quarto includes 5 built in templates, drawing inspiration from the [Postcards R Package](https://cran.r-project.org/web/packages/postcards/readme/README.html). Built-in templates include:

-   `jolla`
-   `trestles`
-   `solana`
-   `marquee`
-   `broadside`

Each template will position the about elements with the content in a different layout. Select the template using the `template` option:

``` yaml
about:
  template: trestles
```

Here is a preview of each of the templates:

::: panel-tabset
### jolla

![](images/about-jolla.png){.border fig-alt="Screenshot of About page with jolla template. Photo is a centered circle above a heading with the author's name. There is a centered paragraph below the header, a separator line, and then buttons for twitter and github centered at the bottom."}

### trestles

![](images/about-trestles.png){.border fig-alt="Screenshot of About page with trestles template. On the left-hand side there is a rectangular photo above the author's name, and two buttons (one for twitter, and one for github below). On the right hand side there is a paragraph of body text followed by headered sections for Education and Experience."}

### solana

![](images/about-solana.png){.border fig-alt="Screenshot of About page with solana template. The left-hand side has the name as a main header with buttons for twitter and github below it. Below the buttons there is a paragraph of body text, followed by headered sections for Education and Experience. In the upper right-hand column there is a rectangular image."}

### marquee

![](images/about-marquee.png){.border fig-alt="Screenshot of About page with marquee template. A large square image is at the top. Beneath that the author's name is a header, and there is a paragraph of body text, followed by headered sections for Education and Experience. Centered at the bottom of the page are links to Twitter and GitHub with their respective icons next to them."}

### broadside

![](images/about-broadside.png){.border fig-alt="Screenshot of About page with broadside template. The left side is a rectangular image. On the right-hand side the author's name is a header, and there is a paragraph of body text, followed by headered sections for Education and Experience. Centered at the bottom of the page are links to Twitter and GitHub with their respective icons next to them."}
:::

### Image

The image for the about page will be read from the document-level `image` option:

``` yaml
title: Finley Malloc
image: profile.jpg
about:
  template: jolla
```

In addition, you can customize how the image is displayed in the page to better meet your needs by setting the following options.

| option        | description                                                                           | templates                     |
|------------------|----------------------------------|--------------------|
| `image-width` | A valid CSS width for your image.                                                     | all                           |
| `image-shape` | The shape of the image on the about page. Choose from:`rectangle`, `round`, `rounded` | `jolla`, `solana`, `trestles` |
| `image-alt`   | Alternative text for image                                                            | all                           |
| `image-title` | Title for image                                                                       | all                           |

For example:

``` yaml
title: Finley Malloc
image: profile.png
about:
  template: trestles
  image-width: 10em
  image-shape: round
```

### Links

Your about page also may contain a set of links to other resources about you or your organization. Each template will render these links in a slightly different way. Here are the options that you can specify for each link:

| Option       | Description                                                                                                                        |
|-------------------|-----------------------------------------------------|
| `href`       | Link to file contained with the project or an external URL.                                                                        |
| `text`       | Text to display for navigation item (defaults to the document `title` if not provided).                                            |
| `icon`       | Name of one of the standard [Bootstrap 5 icons](https://icons.getbootstrap.com/) (e.g. "github", "twitter", "share", etc.).        |
| `aria-label` | [Accessible label](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-label) for the navigation item. |

## Partial Page Content

By default, the about page will be generated using the entire contents of the page. If you'd like, however, you may also choose to use only a portion of the page's content to populate the about template. In this case, you can specify an `id` for the about page in the document front matter. When rendering the page, Quarto will find any `div` with that `id` and use the contents of that `div` to populate the about template. The `div` that provided the contents will be replaced with the formatted 'about' content. For example, you could write:

``` markdown
---
title: "Finley Malloc"
about:
  id: hero-heading
  template: jolla
  image: profile.jpg
  links:
    - icon: twitter
      text: twitter
      href: https://twitter.com
    - icon: github
      text: Github
      href: https://github.com
---

### This content appears above the formatted about page content.

:::{#hero-heading}

Finley Malloc is the Chief Data Scientist at Wengo Analytics. When not innovating on data platforms, Finley enjoys spending time unicycling and playing with her pet iguana.

## Education

University of California, San Diego | San Diego, CA
PhD in Mathematics | Sept 2011 - June 2015

Macalester College | St. Paul MA
B.A in Economics | Sept 2007 - June 2011

## Experience

Wengo Analytics | Head Data Scientist | April 2018 - present

GeoScynce | Chief Analyst | Sept 2012 - April 2018

:::

### This content appears below the formatted about page content.
```


# quarto-web/docs/websites/website-search.qmd

---
title: "Website Search"
---

## Overview

Quarto includes support for full text search of websites and books. By default, Quarto will automatically index the contents of your site and make it searchable using a locally built index. You can also configure Quarto search to use a hosted [Algolia](https://www.algolia.com/products/search-and-discovery/hosted-search-api/) index.

## Search Appearance

Search is enabled by default for websites and books. If the site has a navbar the search UI will appear on the navbar, otherwise it will appear on the sidebar. You can control the location of search with the following options:

| Option     | Description                                                                                                 |
|------------|-------------------------------------------------------------------------------------------------------------|
| `location` | `navbar` or `sidebar` (defaults to `navbar` if one is present on the page).                                 |
| `type`     | `overlay` or `textbox` (`overlay` provides a button that pops up a search UI, `textbox` does search inline).|

For example:

``` yaml
website:
  search: 
    location: navbar
    type: overlay
```

Note that the above example reflects the default behavior so need not be explicitly specified. Note also that search is enabled by default for websites (you can disable it with `search: false`).

The `overlay` option displays the search UI as follows:

![](images/navbar-overlay.png){.border .column-page-outset-right fig-alt="Quarto page with algolia search overlay in 'detached' mode. The webpage behind the search dialog is darkened, and the search dialog itself has a field for entering input tect, and displays a list of matching documents and preview of their tect below."}

The `textbox` option displays search like this:

![](images/navbar-textbox.png){.border .column-page-outset-right fig-alt="Algolia search with textbox in navbar. The search dialog opens as a dropdown in the right-hand side of the screen as an expansion of the textbox."}

## Customizing Results

You can use the following `search` options to customize how search results are displayed:

+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option           | Description                                                                                                                                                                                                                       |
+==================+===================================================================================================================================================================================================================================+
| `limit`          | The number of results to display in the search results. Defaults to 20.                                                                                                                                                           |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `collapse-after` | The number of sections matching a document to show before hiding additional sections behind a 'more matches' link. Defaults to 2.                                                                                                 |
|                  |                                                                                                                                                                                                                                   |
|                  | ![](images/collapse-after.png){.border fig-alt="Part of a search result that shows a matching result for the search term, and at the bottom reads '3 more matches in this document'"}                                             |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `copy-button`    | If true, the search textbox will include a small icon that when clicked will copy a url to the search results to the clipboard (this is useful if users would like to share a particular search with results). Defaults to false. |
|                  |                                                                                                                                                                                                                                   |
|                  | ![](images/copy-button.png){.border fig-alt="search box with clickable clipboard icon on the right hand side that, if clicked, will copy the resulting url."}                                                                     |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## Using Algolia

In addition to the built-in search capability, Quarto websites can also be configured to use an external Algolia search index. When rendering a website, Quarto will produce a JSON file (`search.json` in the site output directory) which can be used to update an Algolia index. For more on creating indexes with Algolia, see [Send and Update Your Data](https://www.algolia.com/doc/guides/sending-and-managing-data/send-and-update-your-data/) using Algolia.

### Basic Configuration

In order for Quarto to connect to your Algolia index, you need to provide basic connection information in your Quarto project file. You can find this connection information for your Algolia index in the Dashboard in the [API Keys](https://www.algolia.com/api-keys) section. The following basic connection information is required:

+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option                | Description                                                                                                                                                                                      |
+=======================+==================================================================================================================================================================================================+
| `index-name`          | The name of the index to use when performing a search.                                                                                                                                           |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `application-id`      | The unique ID used by Algolia to identify your application.                                                                                                                                      |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `search-only-api-key` | The Search-Only API key to use to connect to Algolia.                                                                                                                                            |
|                       |                                                                                                                                                                                                  |
|                       | ::: callout-important                                                                                                                                                                            |
|                       | Be sure to use the **Search Only** API key, which provides read only access to your index and is safe to include in project files. Never use your Admin API key in a Quarto document or project. |
|                       | :::                                                                                                                                                                                              |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `show-logo`           | Displays a 'search by Algolia' logo in the footer of search results.                                                                                                                             |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

For example:

``` yaml
website:
  search:
    algolia:
      index-name: <my-index-name>
      application-id: <my-application-id>
      search-only-api-key: <my-search-only-api-key>
```

### Custom Index Schema

If you are simply using the `search.json` file generated by Quarto as your Algolia index, the above configuration information is all that is required to set up search using Algolia.

However, if you are generating an index in some other fashion, you may need to provide additional information to specify which fields Quarto should use when searching. You do this by including an `index-fields` key under `algolia` which specifies the names of specific fields in your index.

+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option    | Description                                                                                                                                                                                                                |
+===========+============================================================================================================================================================================================================================+
| `href`    | The field to use to read the URL to this index entry. The user will be navigated to this URL when they select the matching search result. Note that Quarto groups results by URL (not including the anchor when grouping). |
|           |                                                                                                                                                                                                                            |
|           | This field is required (either as an existing field in your index or with a mapped field name).                                                                                                                            |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `title`   | The field to use to read the title of the index entry.                                                                                                                                                                     |
|           |                                                                                                                                                                                                                            |
|           | This field is required (either as an existing field in your index or with a mapped field name).                                                                                                                            |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `text`    | The field to use to read the text of the index entry.                                                                                                                                                                      |
|           |                                                                                                                                                                                                                            |
|           | This field is required (either as an existing field in your index or with a mapped field name).                                                                                                                            |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `section` | The field to use to read the section of the index entry. Quarto groups results by URL and uses the section information (if present) to show matching subsections of the same document.                                     |
|           |                                                                                                                                                                                                                            |
|           | This field is optional.                                                                                                                                                                                                    |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Any or all of the above may be specified in your Quarto project file. For example:

``` yaml
website:
  search:
    algolia:
      index-name: <my-index-name>
      application-id: <my-application-id>
      search-only-api-key: <my-search-only-api-key>
      index-fields:
        href: url
        section: sec
        text: body
```

### Algolia Insights

By default, Algolia provides a number of insights based upon the performance of your Algolia search. In addition, it may be helpful to understand more detailed tracking of the results that are viewed and clicked. You can enable click and conversion tracking using Algolia by setting the `analytics-events` to true:

``` yaml
website:
  search:
    algolia:
      index-name: <my-index-name>
      application-id: <my-application-id>
      search-only-api-key: <my-search-only-api-key>
      analytics-events: true
```

You can confirm that events are being properly sent to Algolia using the [Event Debugger](https://www.algolia.com/events/debugger). Note that the click and conversion events use cookies to maintain an anonymous user identifier---if [cookie consent](website-tools.qmd#cookie-consent) is enabled, search events will only be enabled if cookie consent has been granted.

### Advanced Configuration

In addition to the above configuration, you may also pass Algolia specific parameters when executing a search. For example, you may want to limit results to a particular facet or set of tags. To specify parameters, add the `params` key to your `algolia` yaml and provide params. For information about about available parameters, see Algolia's [Search API Parameters](https://www.algolia.com/doc/api-reference/search-api-parameters/).

For example:

``` yaml
website:
  search:
    algolia:
      index-name: <my-index-name>
      application-id: <my-application-id>
      search-only-api-key: <my-search-only-api-key>
    index-fields:
      href: url
      section: sec
      text: body
    params:
      tagFilters: ['tag1','tag2']
```

## Disabling Search

You can disable search for an individual document by adding `search: false` to the document metadata. For example:

``` yaml
---
title: "My Document"
search: false
---
```

If you'd like to disable search support for an entire website, you can do so by including the following in your `_quarto.yml` file:

``` yaml
website:
  search: false
```


# quarto-web/docs/websites/website-listings.qmd

---
title: "Document Listings"
---

## Overview

Listings enable you to automatically generate the contents of a page (or region of a page) from a list of Quarto documents or other custom data.

Listings are useful for creating blogs, providing navigation for large numbers of documents, or any other scenario where you'd like the contents of a page to be automatically updated as documents are added, updated, and removed.

You can enable listings on a page using the `listing` option in the document front matter. This will instruct Quarto to generate additional content (the 'listings') when the page is rendered. For example, the following YAML in the front matter of a document:

``` yaml
---
title: "Listing Example"
listing: default
---
```

will result in a listing of all documents in the directory (with the exception of the current document). It might look something like this:

![](images/listing-example.png){.border fig-alt="Screenshot of Listing Example page. There is a navbar at the top with the site name on the left, and a collapsed menu icon on the right. The header (Listing example). Below on the left there is a sortable dropdown for the order in which the items are displayed. On the right, across, is a search input box. The items are listed full-width rows that display the item’s metadata (author and date), title, description, and image."}

## Listing Contents

You can control what documents are included in the listing by using the `contents` option, which allows you to provide a set of input files (or globs of input files) that should be included in the listing. For each of the inputs that matches the `contents` of a listing, an item will be included using the metadata in the front matter of the document. 

::: {.callout-note}
To have an item in the list, it must contains at least the "title" metadata.
:::

For example to include all the Quarto documents in the `posts` directory, you would write:

``` yaml
---
title: "Listing Example"
listing:
  contents: posts
---
```

You can write much more complex rules for including content by using globs and using a list of targets in the contents, such as:

``` yaml
---
title: "Listing Example"
listing:
  contents:
    - "reports/*.qmd"
    - "lab-notes/*reports.qmd"
```

Review the [Quarto Glob Reference](/docs/reference/globs.qmd) for more information about supported glob syntax.

::: callout-note
If you provide a path to a directory, it will be treated as `<directory>/**` - the directory will be searched recursively for project inputs.
:::

It is important to note that when providing a list of targets, these will be identified _relative_ to the location of the listings page, not the root of the project file.  For example, if your listings page is located at `/pages/listings.qmd` specifying `contents: "reports/*.qmd"` will search in `/pages/reports/` not `/reports/` for the targeted files.

In addition to specifying lists of files or globs, contents can contain lists of metadata as well. For more about this, see [Custom Listings](website-listings-custom.qmd).

## Listing Types

There are three built-in types of listings that you can choose from. Use the `type` option to choose the appearance of the listing:

``` yaml
---
listing:
  contents: posts
  type: default
---
```

The type field accepts the following values:

+----------------+----------------------------------+
| Type           | Description                      |
+================+==================================+
| `default`      | A blog style list of items.      |
+----------------+----------------------------------+
| `table`        | A table of listings.             |
+----------------+----------------------------------+
| `grid`         | A grid of listing cards.         |
+----------------+----------------------------------+

::: panel-tabset
#### Default

By default, listings will appear in full width rows that display the item's metadata (author and date), title, description, and image.

![](images/listing-default.png){.border alt="A default style listing." fig-alt="The default layout for listings page. The top is a header (Listing Example). Below on the left there is a sortable dropdown for the order in which the items are displayed. On the right, across, is a search input box. The items are listed full-width rows that display the item’s metadata (author and date), title, description, and image."}

#### Grid

Grid style listings display a card for each item.

![](images/listing-grid.png){.border alt="A grid style listing." fig-alt="Listing Example page with grid-style layout cards for each item."}

#### Table

The table listing style provides a traditional tabular layout.

![](images/listing-table.png){.border alt="A table type listing." fig-alt="Listing Example with a text table displaying (from left to right): Date, Title, and Author."}
:::

## Sorting Items

By default, listings created from documents will be ordered by their title. Use the `sort` option to control the order of the listing. For example:

``` yaml
listing:
  contents: posts
  sort: "date"
```

Each `sort` key can include a field name and optionally either `asc` or `desc` to control whether to sort in ascending or descending order. When only the name is specified, sorting by that field will be in ascending order.

The sort key can also contain one or more fields to sort by. For example:

``` yaml
listing:
  contents: posts
  sort:
    - "date"
    - "title desc"
```

This will sort the documents in the `posts` directory first by their date in ascending order, then by their title in descending order.

If you'd like to disable sorting entirely and display the items in the order in which they are specified, you can pass `sort: false` (which will disable sorting and preserve the item's original order).

## Listing Options

It is possible to customize the appearance of listings using the following options for each type of listing display.

### Default

+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option              | Description                                                                                                                                             |
+=====================+=========================================================================================================================================================+
| `max-items`         | The maximum number of items to include in this listing.                                                                                                 |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| `image-align`       | Whether to place the image on the right or left side of the post content. Defaults to `right`.                                                          |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| `image-height`      | The height of the image being displayed. The width is automatically determined and the image will fill the rectangle without scaling (i.e. cropped to fill). |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| `image-placeholder` | The default image for items if they have no image.                                                                                                      |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+

### Grids

+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option              | Description                                                                                                                                             |
+=====================+=========================================================================================================================================================+
| `max-items`         | The maximum number of items to include in this listing.                                                                                                 |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| `image-height`      | The height of the image being displayed. The width is automatically determined and the image will fill the rectangle without scaling (i.e. cropped to fill). |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| `image-placeholder` | The default image for items if they have no image.                                                                                                      |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| `grid-columns`      | The number of columns in the grid display. Defaults to 3.                                                                                               |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| `grid-item-border`  | Whether to display a border around the item card. Defaults to `true`.                                                                                   |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| `grid-item-align`   | Aligns the content within the card (`left`, `right`, or `center`). Defaults to `left`.                                                                  |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+

### Tables

+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| Options             | Description                                                                                                                                         |
+=====================+=====================================================================================================================================================+
| `max-items`         | The maximum number of items to include in this listing.                                                                                             |
+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| `image-height`      | The height of the image being displayed. The width is automatically select and the image will fill the rectangle without scaling (i.e. cropped to fill). |
+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| `image-placeholder` | The default image for items if they have no image.                                                                                                  |
+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| `table-striped`     | Display the table rows with alternating background colors (`true` or `false`). Defaults to `false`                                                  |
+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| `table-hover`       | Highlight rows of the table when the user hovers the mouse over them (`true` or `false`). Defaults to `false`.                                      |
+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| `field-links`       | A list of fields that should link to the document in the table (defaults to `title`).                                                               |
+---------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

### Advanced Options

+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option                   | Description                                                                                                                                                                                                                      |
+==========================+==================================================================================================================================================================================================================================+
| `field-display-names`    | A mapping that provides display name for specific fields. For example, to display the title column as 'Report' in a table listing you would write:                                                                               |
|                          |                                                                                                                                                                                                                                  |
|                          | ``` yaml                                                                                                                                                                                                                         |
|                          | listing:                                                                                                                                                                                                                         |
|                          |   field-display-names:                                                                                                                                                                                                           |
|                          |     title: "Report"                                                                                                                                                                                                              |
|                          | ```                                                                                                                                                                                                                              |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `max-description-length` | The maximum length of the description displayed in the listing (in characters). Defaults to 175.                                                                                                                                 |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `date-format`            | The date format to use when displaying dates (e.g. `d-M-yyyy`).                                                                                                                                                                  |
|                          |                                                                                                                                                                                                                                  |
|                          | You may either provide a date style (`full`, `long`, `medium`, `short` or `iso`) or a format string for formatting the date. The behavior of date styles varies depending upon locale, but examples in the `en` locale are as follows: |
|                          |                                                                                                                                                                                                                                  |
|                          | full                                                                                                                                                                                                                             |
|                          |                                                                                                                                                                                                                                  |
|                          | :   Saturday, February 5, 2022                                                                                                                                                                                                   |
|                          |                                                                                                                                                                                                                                  |
|                          | long                                                                                                                                                                                                                             |
|                          |                                                                                                                                                                                                                                  |
|                          | :   February 5, 2022                                                                                                                                                                                                             |
|                          |                                                                                                                                                                                                                                  |
|                          | medium                                                                                                                                                                                                                           |
|                          |                                                                                                                                                                                                                                  |
|                          | :   Feb 5, 2022                                                                                                                                                                                                                  |
|                          |                                                                                                                                                                                                                                  |
|                          | short                                                                                                                                                                                                                            |
|                          |                                                                                                                                                                                                                                  |
|                          | :   2/5/22                                                                                                                                                                                                                       |
|                          |                                                                                                                                                                                                                                  |
|                          | iso                                                                                                                                                                                                                              |
|                          |                                                                                                                                                                                                                                  |
|                          | :   2022-05-22                                                                                                                                                                                                                   |
|                          |                                                                                                                                                                                                                                  |
|                          | Learn more about supported date formatting values [here](/docs/reference/dates.qmd).                                                                                                                                             |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

In addition to the above listing-wide options, each listing type has a variety of options to customize its appearance.

## Categories

In addition to displaying the listing contents, listings can also automatically add a list of categories to the page that they appear on. To enable categories you can set the `categories` option like:

``` yaml
listing:
  categories: true
```

which results in categories appearing in the right sidebar:

![](images/listing-categories.png){.border .column-page-right fig-alt="Default layout listings page with a sidebar on the right showing categories and the counts of items for each category."}

When users click a category, the page will be updated to show only the listing items that match the selected category.

#### Category Appearance

You can choose between a few different display styles for categories:

+--------------+------------------------------------------------------------------------------------------------------------------------------------+
| Option       | Description                                                                                                                        |
+==============+====================================================================================================================================+
| `numbered`   | Displays a list of categories in alphabetical order with the number of items in that category displayed next to the category name. |
+--------------+------------------------------------------------------------------------------------------------------------------------------------+
| `unnumbered` | Display a list of categories in alphabetical order.                                                                                |
+--------------+------------------------------------------------------------------------------------------------------------------------------------+
| `cloud`      | Displays a 'word cloud' of categories.                                                                                             |
+--------------+------------------------------------------------------------------------------------------------------------------------------------+

When multiple listings appear on the page, categories will be enabled based upon the option set in the first listing. If categories are enabled for the first listing, all listings on the page will contribute their item categories to the list of categories and all will be filtered when the user clicks a category.

## Feeds

You can also have an RSS feed generated based upon the contents of a listing. This is great to allow your content to be syndicated or to be accessible via RSS Readers. Include a feed for your listing by including the `feed` option:

``` yaml
listing:
  contents: posts
  feed: true
```

When a feed is enabled for a listing on a page, an RSS file will be automatically generated using the name of the the file. For example, `index.qmd` will produce a feed at `index.xml`. A link to the feed will be included in the `head` of the page as well.

Generating feeds requires that the `site-url` be set for the site in your `_quarto.yml` file. For example:

``` yaml
website:
  site-url: "https://www.quarto.org"
```

You can further customize your feed using the following options:

+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option        | Description                                                                                                                                                                                                   |
+===============+===============================================================================================================================================================================================================+
| `items`       | The number of items to include in your feed. Defaults to 20.                                                                                                                                                  |
+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `type`        | `full` or `partial`. `full`, the default, includes the full contents of each document in the feed. `partial` includes only the first paragraph contents in the feed.                                          |
+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `title`       | The title for this feed. Defaults to the site title provided in your `_quarto.yml` file.                                                                                                                      |
+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `image`       | The image for this feed. If not specified, the image for the page the listing appears on will be used, otherwise an image will be used if specified for the site in your `_quarto.yml` file.                  |
+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `description` | The description of this feed. If not specified, the description for the page the listing appears on will be used, otherwise the description of the site will be used if specified in your `_quarto.yml` file. |
+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `language`    | The language of the feed. Omitted if not specified. See <https://www.rssboard.org/rss-language-codes> for a list of valid language codes.                                                                     |
+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `categories`  | Generates a separate feed for each of the categories included in this list of category names.                                                                                                                 |
+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## Listing Fields

When reading the contents of a listing, Quarto uses the metadata read from the front matter of the document or the contents of the document itself to populate the following fields for each item:

+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field Name      | Description                                                                                                                                                                                                                                                                               |
+=================+===========================================================================================================================================================================================================================================================================================+
| `title`         | The title of the item, read from the `title` field of the front matter (or the first H1 of the document).                                                                                                                                                                                 |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `subtitle`      | The subtitle of the item, read from the `subtitle` field of the front matter.                                                                                                                                                                                                             |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `author`        | The author of the item, read from the `author` field of the front matter.                                                                                                                                                                                                                 |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `description`   | The description of the item, read from the `description` or `abstract` field of the front matter or from the first paragraph of the document.                                                                                                                                             |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `date`          | The date of the item, read from the `date` field of the front matter.                                                                                                                                                                                                                     |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `image`         | The image for this item, read from the `image` field of the front matter, or automatically discovered by taking the first of an image of class `preview-image`, an image with a file name starting with `feature`, `cover`, or `thumbnail`, or the first image to appear in the document. |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `image-alt`     | The alt text for the image for this item.                                                                                                                                                                                                                                                  |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `reading-time`  | An estimate of the reading time for this item, computed by counting the words in the item and assuming a reading speed of 200 words per minute.                                                                                                                                           |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `categories`    | Categories for the item, read from the `categories` field of the front matter.                                                                                                                                                                                                            |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `filename`      | The name of the input file.                                                                                                                                                                                                                                                               |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `file-modified` | The last modified date of this input file.                                                                                                                                                                                                                                                |
+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Depending upon the type of listing that you are using, different fields are displayed automatically:

+---------------+---------------+--------------+--------------+
| Field         | Type: Default | Type: Table  | Type: Grid   |
+===============+:=============:+:============:+:============:+
| `title`       | x             | x            | x            |
+---------------+---------------+--------------+--------------+
| `subtitle`    | x             |              |              |
+---------------+---------------+--------------+--------------+
| `author`      | x             | x            | x            |
+---------------+---------------+--------------+--------------+
| `description` | x             |              | x            |
+---------------+---------------+--------------+--------------+
| `date`        | x             | x            | x            |
+---------------+---------------+--------------+--------------+
| `image`       | x             |              | x            |
+---------------+---------------+--------------+--------------+

### Customizing Fields

Though specific columns are displayed by default, each of the types will allow you to display any of the above columns by using the `fields` options. For example, to display more fields in a table (as columns), you write:

``` yaml
listing:
  type: table
  contents: posts
  fields: [image, date, title, author, reading-time]
```

which produces:

![](images/list-fields-list.png){fig-alt="Table with small image thumbnail for each item and custom list of fields: Date, Title, Author, and Reading Time."}

Each type of listing will handle the fields in different ways.

Default

:   For default type listings, the various fields will be placed logically, with the `image` in the right column, the `title`, `subtitle`, and `description` in the center column, and any other fields in the left column.

    ![](images/default-fields.png){.border .column-page-right fig-alt="Default listings layout with the image in the right column, the title, subtitle, and description in the center column, and author, date, reading time, file, and file modified fields in the left column."}

Tables

:   For table type listings, the list of fields will be displayed as columns in the order that the fields appear in the list.

Grid

:   For grid listings, the `image`, `title`, `subtitle`, `reading-time`, `categories`, `description`, `author`, and `date` fields will be arranged on the body of the card. The `filename` and `file-modified` fields will appear in the card footer. Any other fields will appear in a table at the bottom of the card body.

    ![](images/grid-fields.png){.border fig-alt="Grid listing layout item with image thumbnail at the top of the card, followed below by the title, then subtitle, reading time, category tags, and description. Below the description there is a line with author and date, and another line with file and file modified."}

## Including or Excluding Items

You can control what documents are included or excluding based upon the metadata of the items by using the `include` and `exclude` options. These options allow you to specify one or more field names and values that must be present or absent in order for the item to be included or excluded. For example, to include only items authored by `Harlow` or `Tristan`, you write:

``` yaml
listing:
  contents: posts
  type: grid
  include:
    author: "{Harlow,Tristan}*"
```

To exclude any items authored by `Charles`, you write:

``` yaml
listing:
  contents: posts
  type: grid
  exclude:
    author: "Charles*"
```

When including or excluding items based upon a string field value, Quarto will use glob syntax when comparing values. Any other type of comparison will be done by testing for equality.

## User Tools

Listings support interactive tools to allow the viewer of the listing to sort, filter, or page through listings.

### Sorting

Users can use the select box to choose how to sort the items in the listing (or in the case of tables, by clicking on the column headings). By default, the sorting control will allow the user to sort by `title`, `date`, or `author`. You can stop this UI from being displayed to the user with the option:

``` yml
listing:
  sort-ui: false
```

You can control which fields are included in the sort list by providing a list of field names in the `sort-ui` key:

``` yaml
listing:
  sort-ui: [title, date]
```

### Filtering

Listings include a filter box positioned on the top right of the listing content. The filter box allows readers to perform a 'typeahead' search of the listing contents. You can disable the filtering control using the option:

``` yaml
listing:
  filter-ui: false
```

By default, if the filtering control is enabling, all fields that are being displayed in the listing will be searchable. If you'd like to limit searching / filtering to specific fields, you can do so by providing a field list in the `filter-ui` key:

``` yaml
listing:
  filter-ui: [title, date]
```

### Pagination

Listings also natively support pagination of the items. The default number of items displayed on a page depends up the listing type:

| Listing Type | Items Per Page |
|--------------|:--------------:|
| `default`    |       25       |
| `table`      |       30       |
| `grid`       |       18       |

You can control the number of items displayed per page using the option `page-size`:

``` yaml
listing:
  page-size: 36
```

## Listing Location

By default, listings will simply be appended to the main content region of the page. If you'd like to control where a listing appears, set an `id` for that listing and use that `id` on a corresponding div in the page. For example, updating the page used in the previous example to this:

``` yaml
---
title: "Listing Example"
listing:
  id: sample-listings
  contents: posts
  sort: "date desc"
  type: table
---

You can review the following documents for additional information:

::: {#sample-listings}
:::

Learn more about Quarto [here](https://www.quarto.com).
```

Results in a listing page like:

![](images/listing-example-id.png){fig-alt="Default layout listings page with a footer that reads 'Learn more about Quarto here'."}

## Multiple Listings

You can place any number of listings on a single page. The following would populate two listings on a single page:

``` yaml
---
title: Team Documents
listing: 
  - id: lab-reports
    contents: "lab-reports/*.qmd"
    type: table
  - id: meeting-notes
    contents: "meeting-notes/*.qmd"
    type: table
---

## Lab Reports

:::{#lab-reports}
:::

## Meeting Notes

:::{#meeting-notes}
:::
```

## YAML Listing Content

In addition to populating a listing with inputs that match one or more globs, you can also provide items explicitly via a YAML file. For example, the following listing:

``` yaml
---
title: "Listing Example"
listing:
  id: sample-listings
  contents: 
    - posts
    - archived-items.yaml
  sort: "date desc"
  type: table
---
```

will include all the documents in the `posts` directory, but will also merge in the contents of the `archived-items.yaml` file. The contents of the `archived-items.yaml` file should be a list of items, each of which is a map of field names to values. For example:

``` yaml
- title: "Archived Item 1"
  author: Norah Jones
  date: 2020-01-01
  path: "archived/archived-item-.html"
  categories: [archived, technology]
```

This is useful for cases such as migrating existing content to Quarto - you can begin creating new content as Quarto documents, but still include existing content in your listings by providing their metadata via a yaml file.


# quarto-web/docs/websites/website-navigation.qmd

---
title: "Website Navigation"
format: html
project-type: website
---

## Overview

There are a variety of options available for providing website navigation, including:

-   Using top navigation (a navbar) with optional sub-menus.

-   Using side navigation with a hierarchy of pages.

-   Combining top and side navigation (where top navigation links to different sections of the site with their own side navigation).

In addition, you can add full text search to either the top or side navigation interface.

## Top Navigation

To add top-navigation to a website, add a `navbar` entry to the `website` config in `_quarto.yml`. For example, the following YAML:

``` yaml
website:
  navbar:
    background: primary
    search: true
    left:
      - text: "Home"
        file: index.qmd
      - talks.qmd
      - about.qmd 
```

Results in a navigation bar that looks something like this:

![](images/nav-bar.png){fig-alt="A navigation bar. The title 'My Site' is on the left. To the right of the title are the words 'Home', 'Talks', and 'About'. 'Home' is slightly lighter than the other two words. On the far right side of the navigation bar is a search box."}

Above we use the `left` option to specify items for the left side of the navigation bar. You can also use the `right` option to specify items for the right side.

The text for navigation bar items will be taken from the underlying target document's title. Note that in the above example we provide a custom `text: "Home"` value for `index.qmd`.

You can also create a navigation bar menu by including a `menu` (which is a list of items much like `left` and `right)`. For example:

``` yaml
left:
  - text: "More"
    menu:
      - talks.qmd
      - about.qmd 
```

Here are all of the options available for top navigation:

| Option           | Description                                                                                                                                                                                                                 |
|------------------|------------------------------------------------------|
| `title`          | Navbar title (uses the `site: title` if none is specified). Use `title: false` to suppress the display of the title on the navbar.                                                                                          |
| `logo`           | Logo image to be displayed left of the title.                                                                                                                                                                               |
| `logo-alt`       | Alternate text for the logo image.                                                                                                                                                                                          |
| `logo-href`      | Target href from navbar logo / title. By default, the logo and title link to the root page of the site (`/index.html`).                                                                                                     |
| `background`     | Background color ("primary", "secondary", "success", "danger", "warning", "info", "light", "dark", or hex color).                                                                                                           |
| `foreground`     | Foreground color ("primary", "secondary", "success", "danger", "warning", "info", "light", "dark", or hex color). The foreground color will be used to color navigation elements, text and links that appear in the navbar. |
| `search`         | Include a search box (true or false).                                                                                                                                                                                       |
| `tools`          | List of navbar tools (e.g. link to github or twitter, etc.). See [Navbar Tools](#navbar-tools) for details.                                                 |
| `left` / `right` | Lists of navigation items for left and right side of navbar.                                                                                                                                                                |
| `pinned`         | Always show the navbar (true or false). Defaults to false, and uses [headroom.js](https://wicky.nillia.ms/headroom.js/) to automatically show the navbar when the user scrolls up on the page.                         |
| `collapse`       | Collapse the navbar items into a hamburger menu when the display gets narrow (defaults to true).                                                                                                                            |
| `collapse-below` | Responsive breakpoint at which to collapse navbar items to a hamburger menu ("sm", "md", "lg", "xl", or "xxl", defaults to "lg").                                                                                           |

Here are the options available for individual navigation items:

| Option       | Description                                                                                                                                  |
|------------------|------------------------------------------------------|
| `href`       | Link to file contained with the project or external URL.                                                                                     |
| `text`       | Text to display for navigation item (defaults to the document `title` if not provided).                                                      |
| `icon`       | Name of one of the standard [Bootstrap 5 icons](https://icons.getbootstrap.com/) (e.g. "github", "twitter", "share", etc.).                  |
| `aria-label` | [Accessible label](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-label) for the navigation item.           |
| `rel`        | Value for [rel](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel) attribute. Multiple space-separated values are permitted.  |
| `menu`       | List of navigation items to populate a drop-down menu.                                                                                       |

: {tbl-colwidths="30,70"}

For more information on controlling the appearance of the navigation bar using HTML themes, see [HTML Themes - Navigation](/docs/output-formats/html-themes.qmd#navigation).

### Navbar Tools {#navbar-tools}

{{< include ../_require-1.3.qmd >}}

In addition to traditional navigation, the navbar can also display a set of tools (e.g. social actions, GitHub view or edit actions, etc.) A tool definition consists of an icon name and an href to follow when clicked. For icon, use the icon name of any of the 1,300+ Bootstrap Icons.

For example:

::: {layout="[60,40]"}
``` yaml
website:
  navbar:
    tools:
      - icon: twitter
        href: https://twitter.com
      - icon: github
        menu:
          - text: Source Code
            url:  https://code.com
          - text: Report a Bug
            url:  https://bugs.com
```

![](images/navbar-tools.png){.border alt="The right section of a Quarto navbar containing a Twitter and Github logo. The Github logo is selected and a menu is underneath it with two items: 'Source Code' and 'Report a Bug"}
:::

Tools specified for a navigation bar will appear on the right side of the Navbar. If you specify a dark theme or reader mode for your website, the controls for those options will appear with any specified tools.

When the navbar is collapsed into a menu on smaller screens, the tools will be placed at the bottom of the menu.

## Side Navigation {#side-navigation}

If your site consists of more than a handful of documents, you might prefer to use side navigation, which enables you to display an arbitrarily deep hierarchy of articles.

If you are reading this page on a desktop device then you will see the default side navigation display on the left (otherwise you'll see a title bar at the top which you can click or touch to reveal the navigation).

To add side navigation to a website, add a `sidebar` entry to the `website` section of `_quarto.yml`. For example:

``` yaml
website:
  sidebar:
    style: "docked"
    search: true
    contents:
      - section: "Basics"
        contents:
          - index.qmd
          - basics-knitr.qmd
          - basics-jupyter.qmd
      - section: "Layout"
        contents:
          - layout.qmd
          - layout-knitr.qmd
          - layout-jupyter.qmd
```

There are two styles of side navigation available: "docked" which shows the navigation in a sidebar with a distinct background color, and "floating" which places it closer to the main body text. Here's what the "docked" and "floating" styles look like (respectively):

::: column-screen-inset-shaded
|                                                                                                                                  |                                                                                                                                                         |
|:-------------------------------:|:-------------------------------------:|
| ![](images/nav-side-anchored.png){.preview-image fig-alt="A screenshot of a Quarto document where the sidebar is colored gray."} | ![](images/nav-side-floating.png){fit-alt="A screenshot of a Quarto document where the sidebar has a white background and is closer to the body text."} |
:::

Here are all of the options available for side navigation:

| Option           | Description                                                                                                                                                                                                                                                        |
|------------------|------------------------------------------------------|
| `id`             | Optional identifier (used only for hybrid navigation, described below).                                                                                                                                                                                            |
| `title`          | Sidebar title (uses the project title if none is specified).                                                                                                                                                                                                       |
| `subtitle`       | Optional subtitle.                                                                                                                                                                                                                                                 |
| `logo`           | Optional logo image.                                                                                                                                                                                                                                               |
| `search`         | Include a search box (true or false). Note that if there is already a search box on the top navigation bar it won't be displayed on the sidebar.                                                                                                                   |
| `tools`          | List of sidebar tools (e.g. link to github or twitter, etc.). See the next section for details.                                                                                                                                                                    |
| `items`          | List of navigation items to display (typically top level items will in turn have a list of sub-items).                                                                                                                                                             |
| `style`          | "docked" or "floating".                                                                                                                                                                                                                                            |
| `type`           | "dark" or "light" (hint to make sure the text color is the inverse of the background).                                                                                                                                                                             |
| `background`     | Background color ("none", "primary", "secondary", "success", "danger", "warning", "info", "light", "dark", or "white"). Defaults to "light".                                                                                                                       |
| `foreground`     | Foreground color ("primary", "secondary", "success", "danger", "warning", "info", "light", "dark", or hex color). The foreground color will be used to color navigation elements, text and links that appear in the sidebar.                                    |
| `border`         | Whether to show a border on the sidebar. "true" or "false".                                                                                                                                                                                                        |
| `alignment`      | Alignment ("left", "right", or "center").                                                                                                                                                                                                                          |
| `collapse-level` | Whether to show sidebar navigation collapsed by default. The default is 2, which shows the top and next level fully expanded (but leaves the 3rd and subsequent levels collapsed).                                                                                 |
| `pinned`         | Always show a title bar that expands to show the sidebar at narrower screen widths (true or false). Defaults to false, and uses [headroom.js](https://wicky.nillia.ms/headroom.js/) to automatically show the navigation bar when the user scrolls up on the page. |

For more information on controlling the appearance of the side navigation using HTML themes, see [HTML Themes - Navigation](/docs/output-formats/html-themes.qmd#navigation). If you need to control the width of the sidebar, see [Page Layout - Grid Customization](/docs/output-formats/page-layout.qmd#grid-customization).

### Auto Generation

Above we describe how to explicitly populate the `contents` of your sidebar with navigation items. You can also automatically generate sidebar navigation from the filesystem. The most straightforward way to do this is to specify the `contents` option as follows:

``` yaml
sidebar:
  contents: auto
```

Using `contents: auto` at the root level will result in all documents in your website being included within the navigation (save for the home page which can be navigated to via the title link). Navigation is constructed using the following rules:

1.  Navigation item titles will be read from the `title` field of documents.

2.  Sub-directories will create sections and will be automatically titled based on the directory name (including adding capitalization and substituting spaces for dashes and underscores). Use an `index.qmd` in the directory to provide an explicit `title` if you don't like the automatic one.

3.  Order is alphabetical (by filename) unless a numeric `order` field is provided in document metadata.

Automatic navigation automatically includes items in sub-directories. If you prefer not to do this, use an explicit `/*` to indicate only the documents in the root directory:

``` yaml
sidebar:
  contents: /*
```

Rather than specifying that all documents should be included, you can also specify a directory name or a glob pattern. For example, the following values for `contents` are all valid (note that the second form for `reports` is non-recursive):

``` yaml
sidebar:
  contents: reports
  
sidebar:
  contents: reports/*
  
sidebar:
  contents: "*.ipynb"
```

Note that in YAML we need to quote any strings that begin with `*` (as we do above for `*.ipynb`).

You can automatically build sidebar `contents` anywhere within a sidebar hierarchy. For example, here we add a section that is automatically generated from a directory:

``` yaml
sidebar:
  contents:
    - about.qmd
    - contributing.qmd
    - section: Reports
      contents: reports
```

You can also include automatically generated items in the middle of a list of normal items by including an item with an `auto` property. Here we add an `auto` entry in the middle of a list of items:

``` yaml
sidebar:
  contents:
    - about.qmd
    - contributing.qmd
    - auto: "*-report.qmd"
```

Note again that we quote the `auto` entry with a `*` in it so that it is correctly parsed.

### Sidebar Tools

In addition to traditional navigation, the sidebar can also display a set of tools (e.g. social actions, GitHub view or edit actions, etc.) A tool definition consists of an icon name and an href to follow when clicked. For `icon`, use the icon name of any of the 1,300+ [Bootstrap Icons](https://icons.getbootstrap.com).

For example:

::: {layout="[60,40]"}
``` yaml
website:
  sidebar:
    tools:
      - icon: twitter
        href: https://twitter.com
      - icon: github
        menu:
          - text: Source Code
            url:  https://code.com
          - text: Report a Bug
            url:  https://bugs.com
```

![](images/tools.png){fit-alt="The top section of a Quarto sidebar containing a Twitter and Github logo. The Github logo is selected and a menu is underneath it with two items: 'Source Code' and 'Report a Bug'"}
:::

## Hybrid Navigation

If you have a website with dozens or even hundreds of pages, you will likely want to use top and side navigation together, where the top navigation links to various sections, each with their own side navigation.

To do this, provide a group of `sidebar` entries and link each group of `sidebar` entries with a `navbar` entry by matching their `title`s and listing the page linked from the `navbar` as the first content in the `sidebar` group. For example, if you are using the [Diátaxis Framework](https://diataxis.fr/) for documentation, you might have separate sections for tutorials, how-to guides, explanations, and reference documents, your page might look like the following.

![](images/nav-bar-hybrid.png){fig-alt="A navigation bar titled 'ProjectX' on the left. To the right of the title are the menu items 'Home', 'Tutorials', 'How-To', 'Fundamentals', and 'Reference'. There is a search bar on the far right side of the navigation bar."}

With hybrid navigation, if then you click on, say, Tutorials, you might land in a page like the following.

![](images/nav-bar-hybrid-sidebar.png){fig-alt="A navigation bar titled 'ProjectX' on the left. To the right of the title are the menu items 'Home', 'Tutorials', 'How-To', 'Fundamentals', and 'Reference'. There is a search bar on the far right side of the navigation bar. The contents of the 'Tutorials' page is shown, with the sidebar showing the items 'Tutorials', 'Tutorial 1', and 'Tutorial 2'."}

To achieve this layout, your site configuration needs to look something like this:

``` yaml
website:
  title: ProjectX
  navbar:
    background: primary
    search: true
    left:
      - text: "Home"
        file: index.qmd
      - text: "Tutorials"
        file: tutorials.qmd
      - text: "How-To"
        file: howto.qmd
      - text: "Fundamentals"
        file: fundamentals.qmd
      - text: "Reference"
        file: reference.qmd

  sidebar:
    - title: "Tutorials"
      style: "docked"
      background: light
      contents:
        - tutorials.qmd
        - tutorial-1.qmd
        - tutorial-2.qmd

    - title: "How-To"
      contents:
        - howto.qmd
        # navigation items

    - title: "Fundamentals"
      contents:
        - fundamentals.qmd
        # navigation items

    - title: "Reference"
      contents:
        - reference.qmd
        # navigation items
    
```

Note that the first sidebar definition contains a few options (e.g. `style` and `background`). These options are automatically inherited by the other sidebars.

An alternative approach is to make the `sidebar` entries available from a drop down menu from the `navbar` items they're grouped with. To do this, provide a list of `sidebar` entries and give them each an `id`, which you then use to reference them from the `navbar`.

::: callout-note
A page that doesn't appear in any sidebar will inherit and display the first sidebar- you can prevent the sidebar from showing on a page by setting `sidebar: false` in it's front matter.
:::

![](images/nav-bar-hybrid-dropdown.png){fig-alt="A navigation bar titled 'ProjectX' on the left. To the right of the title are the menu items 'Home', 'Tutorials', 'How-To', 'Fundamentals', and 'Reference'. 'Home' is in a lighter color than the other menu options. The other menu options have a triangle pointing down next to each one, indicating the existence of a drop-down menu. There is a search bar on the far right side of the navigation bar."}

To achieve this, your site configuration needs to look something like this:

``` yaml
website:
  title: ProjectX
  navbar:
    background: primary
    search: true
    left:
      - text: "Home"
        file: index.qmd
      - sidebar:tutorials
      - sidebar:howto
      - sidebar:fundamentals
      - sidebar:reference

  sidebar:
    - id: tutorials
      title: "Tutorials"
      style: "docked"
      background: light
      collapse-level: 2
      contents: 
        # navigation items
        
    - id: howto
      title: "How-To"
      contents:
        # navigation items
        
    - id: fundamentals
      title: "Fundamentals"
      contents: :
        # navigation items
        
    - id: reference
      title: "Reference"
      contents: 
        # navigation items
    
```

{{< include _page-navigation.md >}}

### Separators

If you include a page separator in the sidebar (either between sections or items), page navigation controls will not appear to continue pagination across the separator. For example, in the following sidebar:

``` yaml
{{< meta project-type >}}:
  sidebar:
    contents:
      - section: "First Section"
        contents:
          - href: document1.qmd
          - href: document2.qmd
          - href: document3.qmd
      - text: "---"
      - section: "Second Section"
        contents:
          - href: document4.qmd
          - href: document5.qmd
          - href: document6.qmd
```

When the user reaches the bottom of document3.qmd, they will see previous navigation to go back to document2.qmd, but they will not see next navigation to continue onto document 4. This behavior is useful when you have sections of contents that don't naturally flow together in sequential order. Use the separator to denote this in the sidebar with a horizontal line and to break up pagination.

## Back to Top

You can include a "Back to top" link at the bottom of documents in a website using the `back-to-top-navigation` option. For example:

``` yaml
{{< meta project-type >}}:
  back-to-top-navigation: true
```

Note that you can disable back to top navigation on a page by page basis by specifying `back-to-top-navigation: false`.

{{< include _footer.md >}}

## Hiding Navigation

For some pages (especially those with a completely custom layout) you can hide navigation altogether (`navbar`, `sidebar`, or both). In these case, add the following to the page front matter:

``` yaml
# Hides the sidebar on this page
sidebar: false

# Hides the navbar on this page
navbar: false
```

## Reader Mode

If you'd like users to be able to hide the side navigation and table of contents and have a more focused reading experience, you can enabled `reader-mode`. When enabled, a `reader-mode` toggle will appear on the navbar, if present, or on the sidebar. When pressed, the toggle will 'roll up' the sidebar and table of contents.

![](images/reader-mode.png){fig-alt="Reader mode toggle appearing the top navigation."}

To enable `reader-mode`, use the following in your project:

``` yaml
website:
  reader-mode: true
```

## Site Search

You can add site search by including `search: true` in either your `site-navbar` or `site-sidebar` configuration. For example:

``` yaml
website:
  sidebar:
    style: "docked"
    search: true
    items:
      - text: "Basics"
        contents:
          - index.qmd
          - basics-jupyter.md
        # etc
```

## GitHub Links

You can add various links (e.g. to edit pages, report issues, etc.) to the GitHub repository where your site source code is hosted. To do this, add a `repo-url` along with one or more actions in `repo-actions`. For example:

``` yaml
website:
  repo-url: https://github.com/quarto-dev/quarto-demo
  repo-actions: [edit, issue]
```

The links will be displayed immediately below the page's table of contents:

![](images/repo-actions.png){.border fig-alt="A screen shot of a Quarto document. Underneath the page table of contents on the right side are two options: 'Edit this page' and 'Report an issue'. There is a Github icon to the left of 'Edit this Page.'"}

There are a couple of additional options that enable you to customize the behavior of repository links:

| Option        | Description                                                                      |
|------------------|------------------------------------------------------|
| `repo-subdir` | Subdirectory of repository containing source files (defaults to root directory). |
| `repo-branch` | Repository branch containing the source files (defaults to `main`)               |
| `issue-url`   | Provide an explicit URL for the 'Report an Issue' action.                        |

: {tbl-colwidths="\[40,60\]"}

## Redirects

If you rename or move a page on your site, you may want to create redirects from the old URLs so that existing links don't break. You can do this by adding `aliases` from old pages to renamed pages.

For example, let's say you renamed `page.qmd` to `renamed-page.qmd`. You would add the following `aliases` entry to `renamed-page.qmd` to create the redirect:

``` yaml
---
title: "Renamed Page"
aliases:
  - page.html
---
```

This can also be useful for situations where you re-organize content on your site into a different directory hierarchy or break one large article into smaller ones. For this case, you may want to add the URL hash of the section that you have broken into a new page. For example:

``` yaml
---
title: "Learning More"
aliases:
  - overview.html#learning-more
---
```

::: callout-tip
Depending on where you are deploying your site there may be more powerful tools available for defining redirects based on patterns. For example, Netlify [`_redirects`](https://docs.netlify.com/routing/redirects/) files or [`.htaccess`](https://www.danielmorell.com/guides/htaccess-seo/redirects/introduction-to-redirects) files. Search your web host's documentation for "redirects" to see if any of these tools are available.
:::

## 404 Pages {#pages-404}

When a browser can't find a requested web page, it displays a [404 error](https://en.wikipedia.org/wiki/HTTP_404) indicating that the file can't be found. Browser default 404 pages can be pretty stark, so you may want to create a custom page with a more friendly message and perhaps pointers on how users might find what they are looking for.

Most web serving platforms (e.g. Netlify, GitHub Pages, etc.) will use a file named `404.html` in the root of your website as a custom error page if you provide it. You can include a custom 404 page in a Quarto website by creating a markdown file named `404.qmd` in the root of your project. For example:

``` markdown
---
title: Page Not Found
---

The page you requested cannot be found (perhaps it was moved or renamed).

You may want to try searching to find the page's new location.
```

Note that you can use HTML alongside markdown within your `404.qmd` file in order to get exactly the appearance and layout you want.

Your 404 page will appear within the chrome of your site (e.g. fonts, css, layout, navigation, etc.). This is so that users don't feel that they've irrecoverably "left" your site when they get a 404 error. If you don't want this behavior, then provide a `404.html` rather than `404.qmd`.

Here are some examples of how various popular websites handle custom 404 pages: <https://blog.fluidui.com/top-404-error-page-examples/>.

#### Non-Root Site Paths

If your website is served from the root of a domain (e.g. <https://example.com/>) then simply providing a `404.qmd` file as described above is all that's required to create a custom 404 page.

However, if your website is **not** served from the root of a domain then you need to provide one additional bit of configuration to make sure that resources (e.g. your site's CSS) are resolved correctly within 404 pages.

For example, if your site is served from <https://example.com/mysite/> then you'd add the following to your project `website` configuration within `_quarto.yml`:

``` yaml
website:
  title: "My Site"
  site-path: "/mysite/"
```

Note that if you are already providing a `site-url` (which is required for generation of sitemaps and [social metadata](website-tools.qmd#social-metadata) preview images) then it's enough to simply include the path within the `site-url`:

``` yaml
website:
  title: "My Site"
  site-url: "https://example.com/mysite/"
```


# quarto-web/docs/websites/website-blog.qmd

---
title: Creating a Blog
---

## Overview

Quarto websites include integrated support for blogging. Blogs consist of a collection of posts along with a navigational page that lists them in reverse chronological order. Blogs can include a custom about page, publish an RSS feed, and use a wide variety of themes.

You can create websites that consist entirely of a single blog, websites that have multiple blogs, or you can add a blog to a website that contains other content.

## Quick Start

Follow the Quick Start for your tool of choice to get a simple blog up and running. After covering the basics, read on to learn about more advanced blog features.

::: {.panel-tabset group="tools-tabset"}
### VS Code

To create a new blog project within VS Code, execute the **Quarto: Create Project** command from the command-palette:

![](images/vscode-create-project-command.png)

Then, select **Blog Project**:

![](images/vscode-create-project-blog.png){.border}

You'll be prompted to select a parent directory to create the project within. Then, you'll be asked to name the directory for your blog project:

![](images/vscode-create-project-directory.png){.border}

The new blog project will be created and opened within VS Code. Click the **Render** button to preview the blog:

![](images/vscode-create-project-render-blog.png)

The preview will show to the right of the source file. As you re-render `index.qmd` or render other files like `about.qmd`, the preview is automatically updated.

### RStudio

To create a new blog project within RStudio, use the **New Project** command and select **Quarto Blog**:

::: {layout-ncol="2"}
![](images/rstudio-project-new-directory.png){.border}

![](images/rstudio-project-blog.png){.border}
:::

Then, provide a directory name and other relevant options for the blog:

![](images/rstudio-project-blog-options.png){.border}

Click the **Render** button to preview the blog:

![](images/rstudio-project-blog-preview.png)

The preview will show to the right of the source file. As you re-render `index.qmd` or render other files like `about.qmd`, the preview is automatically updated.

### Terminal

To create a new blog project from the Terminal, use the `quarto create project` command with `blog`, specifying the directory that will hold the new project as first argument:

``` {.bash filename="Terminal"}
quarto create project blog myblog
```

This will create the scaffolding for a simple blog in the `myblog` sub-directory. Use the `quarto preview` command to render and preview the blog:

``` {.bash filename="Terminal"}
quarto preview myblog
```

The blog preview will open in a new web browser. As you edit and save `index.qmd` (or other files like `about.qmd`) the preview is automatically updated.
:::

Here's a summary of the key files created within the starter blog project:

| File                  | Description                |
|:----------------------|:---------------------------|
| `_quarto.yml`         | Quarto project file.       |
| `index.qmd`           | Blog home page.            |
| `about.qmd`           | Blog about page.           |
| `posts/`              | Directory containing posts |
| `posts/_metadata.yml` | Shared options for `posts` |
| `styles.css`          | Custom CSS for website     |

In the following sections we'll take a closer look at the various components of the project.

## Home Page

The home page is a [listing page](website-listings.qmd) for all of the documents in the `posts` directory:

![](images/myblog.png){.border fig-alt="Screenshot of a blog page. There is a navigation bar at the top with the blog title ('myblog') on the left, and on the right: 'About', a GitHub icon, a Twitter icon, and a Search icon. The body has two posts listed with titles, tags, description and preview ordered by date. On the right of the body are categories with counts of posts next to them."}

Here's the source code for the home page:

``` yaml
---
title: "myblog"
listing:
  contents: posts
  sort: "date desc"
  type: default
  categories: true
---
```

When you render a new post, the listing page will automatically updated, adding the most recent post to the top of the list.

::: callout-warning
It is not recommended that you use dynamic dates (for example `today` or `last-modified`) in your blog posts. This will cause the order of your blog and feed to be changed each time the document is rendered or modified.
:::

See the article on [Listing Pages](website-listings.qmd) to learn more about customizing listings, including use a grid layout rather than the default shown above.

### Categories

The listing page is configured to enable categories, which display in the right margin of the page:

``` yaml
---
title: "myblog"
listing:
  # (additional metadata excluded for brevity)
  categories: true
---
```

The categories are read from the front matter of documents included in the listing. For example, here is sample post metadata that includes categories:

``` yaml
---
title: "Post With Code"
description: "Post description"
author: "Fizz McPhee"
date: "5/22/2021"
categories:
  - news
  - code
  - analysis
---
```

See the article on [Categories](website-listings.qmd#categories) to learn more.

## About Page

The `about.qmd` document includes additional information on the blog and its author. For example:

![](images/about-jolla.png){.border fig-alt="Screenshot of an about page. It has a large round circle in the top center with an image shown. Below that is a name in large type, with smaller placeholder body text beneath it. There are two buttons at the bottom, one for twitter, and one for GitHub."}

Here's what the source code of an `about.qmd` might look like:

``` markdown
---
title: "About"
image: profile.jpg
about:
  template: jolla
  links:
    - icon: twitter
      text: Twitter
      href: https://twitter.com
    # (additional links excluded for brevity)
---

## About this blog

This is the contents of the about page for my blog.
```

See the article on [About Pages](/docs/websites/website-about.qmd) to learn about the various options available for customizing page output.

## Posts Directory

The posts that make up the contents of the blog are located in the `posts` directory.

Add a new post to your blog by creating a sub-directory within `posts`, and adding an `index.qmd` file to the directory. That `qmd` file is the new blog post and when you render that, the blog home page will automatically update to include the newest post at the top of the listing.

### Drafts

Add `draft: true` to the document options if you'd like a post to not be included in the listing, site map, or site search. For example:

``` yaml
---
title: "My Post"
description: "Post description"
author: "Fizz McPhee"
date: "5/22/2021"
draft: true
---
```

To publish the post when it is complete, simply remove `draft: true` from the document options and then render it.

### Last Updated
To indicate the date of the last modification, but preserve the original publication date, you can add the `date-modified` field to the document options. For example:

``` yaml
---
title: "My Post"
description: "Post description"
author: "Fizz McPhee"
date: "5/22/2021"
date-modified: "5/23/2021"
---
```

### Freezing Posts

Blogs posts that contain executable code often have the problem that posts created last year can't be rendered this year (for example, because the packages used by the post have changed). A similar problem can also arise when a blog has multiple contributors and not everyone has the right software (or the right versions) to render all of the posts. Finally, posts that include computations can often take a while to render, and you don't want the cumulative time required to render the site to grow too large.

The solution to these problems is to *freeze* the output of computational blog posts. When a post is rendered with `freeze: true`, the markdown output from the the underlying engine (e.g. Jupyter or Knitr) is saved. When the entire site is rendered these computations are not re-run, but rather read from the previously frozen results.

The only time an article with `freeze: true` is rendered is when you explicitly re-render it. By specifying this option for blog posts you can ensure that posts rendered now will always re-render well with the rest of the site, even if the software required to originally render them isn't available.

In the default blog we include a file (`_metadata.yml`) that establishes [shared metadata](/docs/projects/quarto-projects.qmd#shared-metadata) for all documents within the `posts` directory. In this file, we specify that we want `freeze: true` set by default for all posts:

``` yaml
# options apply to all posts in this folder

# freeze computational output
freeze: true
```

See the article on the [`freeze`](/docs/projects/code-execution.qmd#freeze) option to learn more about freezing computational output within websites.

## Themes

Blogs can use any of the 25 [Bootswatch](https://bootswatch.com/) themes included with Quarto. You can also [create your own](/docs/output-formats/html-themes.qmd#theme-options) themes. The default blog generated by `quarto create project` uses the [cosmo](https://bootswatch.com/cosmo/) theme. Here are links to the available themes along with thumbnails of what the simple default blog looks like under a few of them:

::: {layout="[40,60]"}
::: theme-list
-   [default](https://bootswatch.com/default/)
-   [cerulean](https://bootswatch.com/cerulean/)
-   [cosmo](https://bootswatch.com/cosmo/)
-   [cyborg](https://bootswatch.com/cyborg/)
-   [darkly](https://bootswatch.com/darkly/)
-   [flatly](https://bootswatch.com/flatly/)
-   [journal](https://bootswatch.com/journal/)
-   [litera](https://bootswatch.com/litera/)
-   [lumen](https://bootswatch.com/lumen/)
-   [lux](https://bootswatch.com/lux/)
-   [materia](https://bootswatch.com/materia/)
-   [minty](https://bootswatch.com/minty/)
-   [morph](https://bootswatch.com/morph/)
-   [pulse](https://bootswatch.com/pulse/)
-   [quartz](https://bootswatch.com/quartz/)
-   [sandstone](https://bootswatch.com/sandstone/)
-   [simplex](https://bootswatch.com/simplex/)
-   [sketchy](https://bootswatch.com/sketchy/)
-   [slate](https://bootswatch.com/slate/)
-   [solar](https://bootswatch.com/solar/)
-   [spacelab](https://bootswatch.com/spacelab/)
-   [superhero](https://bootswatch.com/superhero/)
-   [united](https://bootswatch.com/united/)
-   [vapor](https://bootswatch.com/vapor/)
-   [yeti](https://bootswatch.com/yeti/)
-   [zephyr](https://bootswatch.com/zephyr/)
:::

::: theme-thumbnails
**litera**

[![](images/theme-litera.png){style="border: solid silver 1px;" fig-alt="Screenshot of blog with litera theme."}](https://bootswatch.com/litera/)

**solar**

[![](images/theme-solar.png){style="border: solid silver 1px;" fig-alt="Screenshot of blog with solar theme."}](https://bootswatch.com/solar/)

**morph**

[![](images/theme-morph.png){style="border: solid silver 1px;" fig-alt="Screenshot of blog with morph theme."}](https://bootswatch.com/morph/)
:::
:::

## RSS Feed

Blogs typically include an RSS feed that allows their content to be easily syndicated to feed readers and other websites. You can enable RSS for a blog by doing the following:

1.  In the `quarto.yml` file, add a `site-url` and `description` to the `website` key (without these options being set in the project file, Quarto cannot generate a feed). For example:

    ``` yaml
    website:
      title: "myblog"
      site-url: https://www.myblogexample.io
      description: "A great sample blog"
    ```

2.  In your blog home page `index.qmd` add the `feed: true` option to the listing. For example:

    ``` yaml
    ---
    title: "myblog"
    listing:
      contents: posts
      sort: "date desc"
      type: default
      categories: true
      feed: true
    ---
    ```

Now, when your site is rendered, an RSS feed will also be generated. To learn more, see the article on [RSS Feeds](/docs/websites/website-listings.qmd#feeds).

::: callout-tip
## Including an RSS Link on the Navbar

You can add an RSS link to your navbar by including the following in your `_quarto.yml` project file. For example:

``` yaml
website:
  title: "myblog"
  site-url: https://www.myblogexample.io
  description: "A great sample blog"
  navbar:
    right:
      - icon: rss
        href: index.xml
```
:::

### Category Feeds

You can also generate RSS feeds for specific categories in your blog. For example, to create feeds for the categories `news` and `posts` in a blog, you could write the following:

``` yaml
---
title: "myblog"
listing:
  contents: posts
  sort: "date desc"
  type: default
  categories: true
  feed:
    categories: [news, posts]
---
```

This will create an `index.xml` file with the RSS feed for the listing, but also create an `index-news.xml` and `index-posts.xml` file with RSS feeds for the respective categories.

## Publishing

There are a wide variety of ways to publish Quarto blogs. Blog content is by default written to the `_site` sub-directory. Publishing is simply a matter of copying this directory to a web server or web hosting service.

The article on [Publishing Websites](../publishing/index.qmd) describes in more detail how to publish to the following services:

-   [Quarto Pub](../publishing/quarto-pub.qmd)
-   [GitHub Pages](../publishing/github-pages.qmd)
-   [Netlify](../publishing/netlify.qmd)
-   [Posit Connect](../publishing/rstudio-connect.qmd)
-   [Firebase](../publishing/other.qmd#google-firebase)
-   [Site44](../publishing/other.qmd#site44)
-   [Amazon S3](../publishing/other.qmd#amazon-s3)

## Subscriptions

You may want to allow readers of your blog to subscribe to updates via email. You can use a third party email service to manage and send these emails.

Third party email services will typically take your RSS Feed as input (e.g. `https://www.myblogexample.io/index.xml`) and provide HTML for a subscription widget that you can place on your blog. A good place to locate that widget is often right margin of your blog.

Here are the steps required to add a subscription widget:

1.  Use your email service features to generate the HTML for your subscription widget. MailChimp, for example, provides HTML like this for a minimal subscription widget.

    ``` html
    <span style="font-weight: 600;">Subscribe</span>

    <!-- Begin Mailchimp Signup Form -->
    <link href="http://cdn-images.mailchimp.com/embedcode/slim-10_7_dtp.css" rel="stylesheet" type="text/css">
    <style type="text/css">
        #mc_embed_signup{background:#fff; clear:left; font:14px Helvetica,Arial,sans-serif;  width:170px;}
        /* Add your own Mailchimp form style overrides in your site stylesheet or in this style block.
           We recommend moving this block and the preceding CSS link to the HEAD of your HTML file. */
        #mc-embedded-subscribe-form{margin-left:-5px;}
    </style>
    <div id="mc_embed_signup">
    <form action="<site_url>" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>
        <div id="mc_embed_signup_scroll">

        <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
        <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
        <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_f718424fc5df77c22533bdaa6_a3c37fb57b" tabindex="-1" value=""></div>
            <div class="optionalParent">
                <div class="clear foot" style="margin-top: 10px;">
                    <input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button">
                    <p class="brandingLogo"></p>
                </div>
            </div>
        </div>
    </form>
    </div>

    <!--End mc_embed_signup-->
    ```

    ::: callout-warning
    The above widget HTML will not work in your blog as the subscription HTML needs to contain value specific to your blog. See your email service provider's instructions for generating a subscription widget.
    :::

2.  Create the file `subscribe.html` in the root of your project.

3.  Paste the HTML for your subscription widget into `subscribe.html` and save the file.

4.  Add `subscribe.html` to the `margin-header` in your `_quarto.yml` file:

    ``` yaml
    website:
      # (additional metadata excluded for brevity)
      margin-header: subscribe.html
    ```

The result looks like this:

![](images/myblog-subscribe.png){.border fig-alt="Screenshot of blog with a Subscribe section in the top of the right-hand section of the bofy. There is an input field marked 'email address' and a button below it labelled 'Subscribe'."}


# quarto-web/docs/websites/website-tools.qmd

---
title: "Website Tools"
---

## Headers & Footers

You can provide standard headers and footers for pages on your site. These can apply to the main document body or to the sidebar. Available options include:

+-----------------+---------------------------------------------------------------------------------------------+
| Value           | Description                                                                                 |
+=================+=============================================================================================+
| `body-header`   | Markdown to insert at the beginning of each page's body (below the title and author block). |
+-----------------+---------------------------------------------------------------------------------------------+
| `body-footer`   | Markdown to insert below each page's body.                                                  |
+-----------------+---------------------------------------------------------------------------------------------+
| `margin-header` | Markdown to insert above right margin content (i.e. table of contents).                     |
+-----------------+---------------------------------------------------------------------------------------------+
| `margin-footer` | Markdown to insert below right margin content.                                              |
+-----------------+---------------------------------------------------------------------------------------------+

For example (included in \_quarto.yml) :

``` yaml
body-header: | 
  This page brought to you by <https://example.com>
margin-header: |
  ![Logo image](/img/logo.png)
```

Note that links to figures should start with a `/` to work on each level of the website.

## Social Metadata

You can enhance your website and the content that you publish to it by including additional types of metadata, including:

-   Favicon
-   Twitter Cards
-   Open Graph

{{< include ../books/_book-vs-website-key.qmd >}}

As you read the documentation below, keep in mind to substitute `book` for `website` if you are authoring a book.

### Favicon

The favicon for your site provides an icon for browser tabs and other sites that link to yours. Use the `favicon` option to provide the path to a favicon image. For example:

``` yaml
website:
  favicon: logo.png
```

### Twitter Cards

[Twitter Cards](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards) provide an enhanced appearance when someone links to your site on Twitter. When a link to your site is included in a Tweet, Twitter automatically crawls your site and fetches any Twitter Card metadata. To enable the automatic generation of Twitter Card metadata for your site, you can add the following to your `_quarto.yml` configuration file:

``` yaml
website:
  twitter-card: true
```

In this case, Quarto will automatically generate a title, description, and preview image for the content. For more information about how Quarto finds preview images, see [Preview Images].

You may also provide additional metadata to be used when generating the Twitter Card, including:

+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Key           | Description                                                                                                                                                                                                                                                                            |
+===============+========================================================================================================================================================================================================================================================================================+
| `title`       | The title of the page. Quarto will automatically use the `title` metadata from the page metadata. If you'd like you can override this just for the Twitter Card by including a `title` in the `twitter-card` metadata.                                                                 |
+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `description` | A short description of the content. Quarto will automatically use the `description` metadata from the page metadata. If you'd like you can override this just for the Twitter Card by including a `description` in the `twitter-card` metadata.                                        |
+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `image`       | The path to a preview image for this content. By default, Quarto will use the `image` value from the document metadata. If you provide an image, you may also optionally provide an `image-width` and `image-height` to improve the appearance of your Twitter Card.                   |
|               |                                                                                                                                                                                                                                                                                        |
|               | If `image` is not provided, Quarto will automatically attempt to locate a preview image. For more information, see [Preview Images].                                                                                                                                                   |
+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `card-style`  | Either `summary` or `summary_large_image`. If this is not provided, the best style will automatically selected based upon other metadata. You can learn more about Twitter Card styles [here](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards). |
+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `creator`     | `@username` of the content creator. Note that strings with special characters such as `@` must be quoted in yaml.                                                                                                                                                                      |
+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `site`        | `@username` of website. Note that strings with special characters such as `@` must be quoted in yaml.                                                                                                                                                                                  |
+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Here is a more comprehensive example of specifying Twitter Card metadata in a `quarto.yml` file:

``` yaml
website:
  twitter-card:
    creator: "@dragonstyle"
    site: "@rstudio"
```

Quarto will automatically merge global metadata found in the `website: twitter-card` key with any metadata provided in the document itself in the `twitter-card` key. This is useful when you need to specify a mix of global options (for example, `site`) with per document options such as `title` or `image`.

### Open Graph

The [Open Graph protocol](http://ogp.me/) is a specification that enables richer sharing of links to articles on the web. It will improve the previews of your content when a link to it is pasted into applications like Slack, Discord, Facebook, Linkedin, and more. To enable the automatic generation of Open Graph metadata for your content, include the following in your `_quarto.yml` configuration file:

``` yaml
website:
  open-graph: true
```

In this case, Quarto will automatically generate a title, description, and preview image for the content. For more information about how Quarto finds preview images, see [Preview Images].

You may also provide additional metadata to be used when generating the Open Graph metadata, including:

+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Key           | Description                                                                                                                                                                                                                                          |
+===============+======================================================================================================================================================================================================================================================+
| `title`       | The title of the page. Quarto will automatically use the `title` metadata from the page metadata. If you'd like you can override this just for the Open Graph metadata by including a `title` in the `open-graph` metadata.                          |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `description` | A short description of the content. Quarto will automatically use the `description` metadata from the page metadata. If you'd like you can override this just for the Open Graph metadata by including a `description` in the `open-graph` metadata. |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `image`       | The path to a preview image for this content. By default, Quarto will use the `image` value from the `site:` metadata. If you provide an image, you may also optionally provide an `image-width` and `image-height`.                                 |
|               |                                                                                                                                                                                                                                                      |
|               | If `image` is not provided, Quarto will automatically attempt to locate a preview image. For more information, see [Preview Images].                                                                                                                 |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `locale`      | The locale that the Open Graph metadata is marked up in.                                                                                                                                                                                             |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `site-name`   | The name which should be displayed for the overall site. If not explicitly provided in the `open-graph` metadata, Quarto will use the `site:title` value.                                                                                            |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Here is a more comprehensive example of specifying Open Graph metadata in a `quarto.yml` file:

``` yaml
website:
  open-graph:
    locale: es_ES
    site-name: Quarto
```

Quarto will automatically merge global metadata found in the `website: open-graph` key with any metadata provided in the document itself in the `open-graph` key. This is useful when you need to specify a mix of global options (for example, `site`) with per document options such as `title` or `image`.

### Preview Images

You can specify a preview image for your article in several different ways:

1.  You can explicitly provide a full url to the preview image using the `image` field in the appropriate metadata. For example:

    ``` yaml
    title: "My Document"
    twitter-card:
      image: "https://quarto.org/docs/websites/images/tools.png"
    ```

2.  You may provide a document relative path to an image (such as `images/preview-code.png`) or a project relative path to an image (such as `/images/preview-code.png`). If you provide a relative path such as this, you must also provide a `site-url` in your site's metadata. For example in your `_quarto.yml` configuration file:

    ``` yaml
    website:
      site-url: "https://www.quarto.org"
    ```

    and in your document front matter:

    ``` yaml
    title: "My Document"
    twitter-card:
      image: "/docs/websites/images/tools.png"
    ```

3.  Any image that is being rendered in the page may also be used as a preview image by giving it the class name `preview-image`. Quarto will select the first image it finds with this class. For example, the following image will be used as the preview image when included on a page:

    ``` markdown
    ![](images/tools.png){.preview-image}
    ```

    If you label an image with this class, you must also provide a `site-url` in your site's metadata.

4.  If none of the above ways of specifying a preview image have been used, Quarto will attempt to find a preview image by looking for an image included in the rendered document with one of the following names: `preview.png`, `feature.png`, `cover.png`, or `thumbnail.png`.

## Google Analytics

You can add [Google Analytics](https://analytics.google.com/) to your website by adding adding a `google-analytics` key to your `_quarto.yml` file. In its simplest form, you can just pass your Google Analytics tracking Id (e.g. `UA-xxxxxxx`) or Google Tag measurement Id (e.g. `G-xxxxxxx`) like:

``` yaml
website:
  google-analytics: "UA-XXXXXXXX"
```

Quarto will use the key itself to determine whether to embed Google Analytics (analytics.js) or Google Tags (gtag) as appropriate.

In addition to this basic configuration, you can exercise more fine grained control of your site analytics using the following keys.

+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Key            | Description                                                                                                                                                                                         |
+================+=====================================================================================================================================================================================================+
| `tracking-id`  | The Google tracking Id or measurement Id of this website.                                                                                                                                           |
+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `storage`      | **cookies -** Use cookies to store unique user and session identification (default).                                                                                                                |
|                |                                                                                                                                                                                                     |
|                | **none -** Do not use cookies to store unique user and session identification.                                                                                                                      |
|                |                                                                                                                                                                                                     |
|                | For more about choosing storage options see [Storage].                                                                                                                                              |
+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `anonymize-ip` | Anonymize the user ip address. For more about this feature, see [IP Anonymization (or IP masking) in Google Analytics](https://support.google.com/analytics/answer/2763052?hl=en).                  |
+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `version`      | The version number of Google Analytics to use. Currently supports either 3 (for analytics.js) or 4 (for gtag). This is automatically detected based upon the `tracking-id`, but you may specify it. |
+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: {tbl-colwidths="[20,80]"}

### Storage

Google Analytics uses cookies to distinguish unique users and sessions. If you choose to use cookies to store this user data, you should consider whether you need to enable [Cookie Consent] in order to permit the viewer to control any tracking that you enable.

If you choose `none` for storage, this will have the following effects:

-   For Google Analytics v3 (analytics.js)\
    No tracking cookies will be used. Individual page hits will be properly tracked, enabling you to see which pages are viewed and how often they are viewed. Unique user and session tracking will not report data correctly since the tracking cookies they rely upon are not set.

-   For Google Tags (gtag)\
    User consent for ad and analytics tracking cookies will be withheld. In this mode, Google Analytics will still collect user data without the user identification, but that data is currently not displayed in the Google Analytics reports.

## Cookie Consent

Quarto includes the ability to request cookie consent before enabling scripts that set cookies, using [Cookie Consent](https://www.cookieconsent.com).

The user's cookie preferences will automatically control [Google Analytics] (if enabled) and can be used to control custom scripts you add as well (see [Custom Scripts and Cookie Consent]. You can enable the default request for cookie consent using the following:

``` yaml
website:
  cookie-consent: true
```

You can further customize the appearance and behavior of the consent using the following:

+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Key          | Description                                                                                                                                                                          |
+==============+======================================================================================================================================================================================+
| `type`       | The type of consent that should be requested, using one of these two values:                                                                                                         |
|              |                                                                                                                                                                                      |
|              | **implied -** (default) This will notify the user that the site uses cookies and permit them to change preferences, but not block cookies unless the user changes their preferences. |
|              |                                                                                                                                                                                      |
|              | **express -** This will block cookies until the user expressly agrees to allow them (or continue blocking them if the user doesn't agree).                                           |
+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `style`      | The style of the consent banner that is displayed:                                                                                                                                   |
|              |                                                                                                                                                                                      |
|              | **simple -** (default) A simple dialog in the lower right corner of the website.                                                                                                     |
|              |                                                                                                                                                                                      |
|              | **headline -** A full width banner across the top of the website.                                                                                                                    |
|              |                                                                                                                                                                                      |
|              | **interstitial -** An semi-transparent overlay of the entire website.                                                                                                                |
|              |                                                                                                                                                                                      |
|              | **standalone -** An opaque overlay of the entire website.                                                                                                                            |
+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `palette`    | Whether to use a dark or light appearance for the consent banner:                                                                                                                    |
|              |                                                                                                                                                                                      |
|              | **light -** A light colored banner.                                                                                                                                                  |
|              |                                                                                                                                                                                      |
|              | **dark -** A dark colored banner.                                                                                                                                                    |
+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `policy-url` | The url to the website's cookie or privacy policy.                                                                                                                                   |
+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `prefs-text` | The text to display for the cookie preferences link in the website footer.                                                                                                           |
+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: {tbl-colwidths="[20,80]"}

A custom example might look more like:

``` yaml
website:
  cookie-consent:
    type: express
    style: headline
    palette: dark
  google-analytics:
    tracking-id: "G-XXXXXXX"
    anonymize-ip: true
```

### Cookie Preferences

In addition to requesting consent when a new user visits your website, Cookie Consent will also add a cookie preferences link to the footer of the website. You can control the text of this link using `prefs-text`. If you would rather position this link yourself, just add a link with the id `#open_preferences_center` to the website and Cookie Consent will not add the preferences link to the footer. For example:

``` markdown
Change [cookie preferences]{#open_preferences_center}
```

### Custom Scripts and Cookie Consent

Cookie Consent works by preventing the execution of scripts unless the user has expressed their consent. To control your custom scripts using Cookie Consent:

1.  Insert script tags as `type='text/plain'` (when the user consents, the type will be switched to `text/javascript` and the script will be executed).

<!-- -->

2.  Add a `cookie-consent` attribute to your script tag, setting it one of the following 4 levels:

    +----------------------+------------------------------------------------------------------------------------------------------------------------+
    | Level                | Description                                                                                                            |
    +======================+========================================================================================================================+
    | `strictly-necessary` | Strictly scripts are loaded automatically and cannot be disabled by the user.                                          |
    +----------------------+------------------------------------------------------------------------------------------------------------------------+
    | `functionality`      | Scripts that are required for basic functionality of the website, for example, remembering a user language preference. |
    +----------------------+------------------------------------------------------------------------------------------------------------------------+
    | `tracking`           | Scripts that are used to track users, for example [Google Analytics].                                                  |
    +----------------------+------------------------------------------------------------------------------------------------------------------------+
    | `targeting`          | Scripts that are used for the purpose of advertising to ad targeting, for example Google AdSense remarketing.          |
    +----------------------+------------------------------------------------------------------------------------------------------------------------+

An example script that is used for user tracking would look like:

``` javascript
<script type="text/plain" cookie-consent="tracking">

// My tracking JS code here

</script>
```

## Site Resources

Besides input and configuration files, your site likely also includes a variety of resources (e.g. images) that you will want to publish along with your site. Quarto will automatically detect any files that you reference within your site and copy them to the output directory (e.g. `_site`).

If this auto-detection fails for any reason, or if you want to publish a file not explicitly linked to from within your site, you can add a `resources` entry to your configuration. For example, here we specify that we want to include all Excel spreadsheets within the project directory as part of the website:

``` {.yaml .yml}
project:
  type: website
  resources: 
    - "*.xlsx"
```

Note that the `*.xslx` value is quoted: this is because YAML requires that strings that begin with non-alphanumeric characters be quoted.

You can also add a `resources` metadata value to individual files. For example:

``` yaml
title: "My Page"
resources:
  - "sheet.xlsx"
```

Images are the most commonly used type of resource file. If you have global images (e.g. a logo) that you want to reference from various pages within your site, you can use a site-absolute path to refer to the images, and it will be automatically converted to a relative path during publishing. For example:

``` markdown
![](/images/logo.png)
```

## Dark Mode

Quarto websites can support both a light and dark mode. For example, you may use the `flatly` and `darkly` themes (which are designed to be used in tandem as dark and light appearances) as:

``` yaml
theme:
  light: flatly
  dark: darkly
```

For more about selecting the dark and light themes for your website, see [Dark Mode](../output-formats/html-themes.html#dark-mode).

::: column-page-outset
+--------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Light                                                                                                        | Dark                                                                                                      |
+==============================================================================================================+===========================================================================================================+
| ![](images/site-light.png){fig-alt="A Quarto sidebar showing a light theme. The 'Dark mode' toggle is off."} | ![](images/site-dark.png){fig-alt="A Quarto sidebar showing a dark theme. The 'Dark mode' toggle is on."} |
+--------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
:::

When enabled, a toggle that allows your reader to control the appearance of the website will appear. The toggle will automatically be added to the website navigation as follows:

1.  If a navbar has been specified, the toggle will appear in the top right corner of the nav bar.
2.  If there is no navbar present, but a sidebar has been specified, the toggle will appear in the same location that the sidebar tools appears (adjacent to the title or logo in the sidebar).
3.  If there is no navbar or sidebar present, the toggle will appear in the top right corner of the page.


# quarto-web/docs/websites/website-basics.qmd

---
title: "Creating a Website"
format: 
  html:
    output-file: index.html
---

## Overview

Quarto Websites are a convenient way to publish groups of documents. Documents published as part of a website share navigational elements, rendering options, and visual style.

Website navigation can be provided through a global navbar, a sidebar with links, or a combination of both for sites that have multiple levels of content. You can also enable full text search for websites.

Quarto websites can be published to a wide variety of destinations including GitHub Pages, Netlify, Posit Connect, or any other static hosting service or intranet web server. See the documentation on [Publishing Websites](../publishing/index.qmd) for additional details.

## Quick Start

Follow the Quick Start for your tool of choice to get a simple website up and running. After covering the basics, read on to learn about website navigation and other more advanced website features.

::: {.panel-tabset group="tools-tabset"}

### VS Code

To create a new website project within VS Code, execute the **Quarto: Create Project** command from the command-palette:

![](images/vscode-create-project-command.png)

Then, select **Website Project**:

![](images/vscode-create-project-website.png){.border}

You'll be prompted to select a parent directory to create the project within. Then, you'll be asked to name the directory for your website project:

![](images/vscode-create-project-directory.png){.border}

The new website project will be created and opened within VS Code. Click the **Render** button to preview the website:

![](images/vscode-create-project-render.png)

The preview will show to the right of the source file. As you re-render `index.qmd` or render other files like `about.qmd`, the preview is automatically updated.


### RStudio

To create a new website project within RStudio, use the **New Project** command and select **Quarto Website**:

:::{layout-ncol="2"}

![](images/rstudio-project-new-directory.png){.border}

![](images/rstudio-project-website.png){.border}
:::

Then, provide a directory name and other relevant options for the website:

![](images/rstudio-project-website-options.png){.border fig-alt="A section of the 'New Project Wizard' menu from Rstudio. This section is titled 'Create Quarto Website'. The Quarto logo is displayed on the left. On the right are fields for 'Directory name', and 'Create project as subdirectory of:'. Underneath that are options for 'Engine'. The option for 'Engine' is set to 'None'. Underneath are options for 'Create a git repository', and 'Use visual markdown editor'.There are buttons for 'Create Project' and 'Cancel' arranged side-by-side in the bottom right of the window. There is an option to 'Open in new session' in the button left corner."}

Click the **Render** button to preview the website:

![](images/rstudio-project-website-preview.png)

The preview will show to the right of the source file. As you re-render `index.qmd` or render other files like `about.qmd`, the preview is automatically updated.


### Terminal

To create a new website project from the Terminal, use the `quarto create project` command, following the prompt to select the type and to provide a name for the project (will be used as the directory name):

```{.bash filename="Terminal"}
quarto create project website mysite
```

This will create the scaffolding for a simple website in the `mysite` sub-directory. Use the `quarto preview` command to render and preview the website:

```{.bash filename="Terminal"}
quarto preview mysite
```

The website preview will open in a new web browser. As you edit and save `index.qmd` (or other files like `about.qmd`) the preview is automatically updated.

:::


## Workflow

Above we have demonstrated how to create and edit a simple website. In this section we go into more depth on website workflow.

### Config File

Every website has a `_quarto.yml` config file that provides website options as well as defaults for HTML documents created within the site. For example, here is the default config file for the simple site created above:

```{.yaml filename="_quarto.yml"}
project:
  type: website

website:
  title: "today"
  navbar:
    left:
      - href: index.qmd
        text: Home
      - about.qmd

format:
  html:
    theme: cosmo
    css: styles.css
    toc: true
```

See the documentation on [Website Navigation](website-navigation.qmd) and [Website Tools](website-tools.qmd) for additional details on website configuration. See [HTML Documents](/docs/output-formats/html-basics.qmd) for details on customizing HTML format options.

### Website Preview

If you are using VS Code or RStudio, the **Render** button automatically renders and runs `quarto preview` in an embedded window. You can also do the same thing from the Terminal if need be:

``` {.bash filename="Terminal"}
# preview the website in the current directory
quarto preview
```

Note that when you preview a site (either using VS Code / RStudio integrated tools or from the terminal)  changes to configuration files (e.g. `_quarto.yml`) as well as site resources (e.g. theme or CSS files) will cause an automatic refresh of the preview.

You can customize the behavior of the preview server (port, whether it opens a browser, etc.) using command line options or the `_quarto.yml` config file. See `quarto preview help` or the [project file reference](/docs/reference/projects/options.qmd#preview) for additional details.


::: callout-important
As you preview your site, pages will be rendered and updated. However, if you make changes to global options (e.g. `_quarto.yml` or included files) you need to fully re-render your site to have all of the changes reflected. Consequently, you should always fully `quarto render` your site before deploying it, even if you have already previewed changes to some pages with the preview server.
:::


### Website Render

To render (but not preview) a website, use the `quarto render` command, which will render the website into the `_site` directory by default:

``` {.bash filename="Terminal"}
# render the website in the current directory
quarto render 
```

See the [Project Basics](../projects/quarto-projects.qmd) article to learn more about working with projects, including specifying an explicit list of files to render, as well as adding custom pre and post render scripts to your project.

{{< include ../projects/_render-targets.md >}}


## Linking

When creating links between pages in your site, you can provide the source file as the link target (rather than the `.html` file). You can also add hash identifiers (`#)` to the source file if you want to link to a particular section in the document. For example:

``` markdown
[about](about.qmd)
[about](about.qmd#section)
```

One benefit of using this style of link as opposed to targeting `.html` files directly is that if you at some point convert your site to a [book](../books/book-basics.qmd) the file-based links will automatically resolve to section links for formats that produce a single file (e.g. PDF or MS Word).

## Learning More

Once you've got a basic website up and running check out these articles for various ways to enhance your site:

- [Website Navigation](website-navigation.qmd) describes various ways to add navigation to a website, including top-level navigation bars, sidebars, or hybrid designs that uses both. This article also covers adding full-text search as well as a site-wide footer.

- [Website Tools](website-tools.qmd) covers adding social metadata (e.g. for Twitter Cards) and Google Analytics to your site, as well as enabling users to toggle between dark and light color schemes.

- [Website Options](../reference/projects/websites.qmd) provides a comprehensive reference to all of the available website options.

- [Code Execution](../projects/code-execution.qmd) provides tips for optimizing the rendering of sites with large numbers of documents or expensive computations.

- [Publishing Websites](../publishing/index.qmd) enumerates the various options for publishing websites including GitHub Pages, Netlify, and Posit Connect.


# quarto-web/docs/websites/website-listings-custom.qmd

---
title: Custom Listings
---

## Overview

In addition to the 3 built in types of listings, you can also build a completely custom display of the items. This custom display can generate any HTML and can optionally still take advantage of the sorting, filtering, and pagination provided by listings.

## Listing Templates

To build a custom listing display, you create an [EJS template](https://ejs.co) that will be used to generate the HTML for a set of items that are passed to the template. EJS templates allow to generate HTML using plain javascript, making it easy to loop through items and output their values in your custom HTML.

To use a custom template, pass it in the `template` option for a listing:

``` yaml
listing:
  template: gallery.ejs
```

When a listing with a custom template is rendered, the listing contents will be read and processed into a set of items that are passed to the template for rendering. For example, in this case, all the documents in the posts directory will be read into items and passed to the `gallery.ejs` template.

``` yaml
listing:
  contents: posts
  template: gallery.ejs
```

A simple template for outputing a list of documents might look like:

``` html
<ul>
<% for (const item of items) { %>
  <li><a href="<%- item.path %>"><%= item.title %></a></li>
<% } %>
</ul>
```

which produces simple HTML output like:

![](images/listing-custom-output.png){.border}

When rendered, the above template will receive an array of listing items called `items`. When the contents of a listing are loaded from a list of documents, each of those items will be populated with the fields described in [Listing Item Fields](website-listings.qmd#listing-item-fields). In addition, any other fields included in a documents metadata will be passed as a property of the item, making it possible to use custom metadata in your documents and the listing display.

## Metadata Listings

The `contents` option for a listing most commonly contains a list of paths or globs, but it can also contain metadata. When contents are metadata, the metadata will be read into items and passed to the template. For example:

``` yaml
listing:
  template: custom.ejs
  contents:
    - name: First Item
      href: https://www.quarto.org
      custom-field: A custom value
    - name: Second Item
      href: https://www.rstudio.org
      custom-field: A second custom value
```

could be rendered using:

```` html
```{=html}
<ul>
<% for (const item of items) { %>
  <li>
    <a href="<%- item.href %>"><%= item.name %></a><br/>
    <%= item['custom-field'] %>
  </li>
<% } %>
</ul>
```
````

which produces a simple HTML display like:

![](images/listing-custom-metadata.png){.border}

## Metadata File Listings

The `contents` option for a listing can also point to one or more `yaml` files (which contain metadata). In that case, the metadata will be read from the files into items and passed to the template. For example:

``` yaml
listing:
  template: custom.ejs
  contents:
    - items.yml
```

where the contents of `items.yml` is:

``` yaml
- name: First Item
  href: https://www.quarto.org
  custom-field: A custom value
- name: Second Item
  href: https://www.rstudio.org
  custom-field: A second custom value
```

### Template Examples

Portions of this website are built using custom listings. The best place to start is with [our gallery](/docs/gallery/), which is a listing built using a custom template and a metadata file. You can view the source code used to create the gallery page in our [Github repository](https://github.com/quarto-dev/quarto-web).

| File                                                                                       | Description                                                                          |
|-------------------------------------|-----------------------------------|
| [gallery.yml](https://github.com/quarto-dev/quarto-web/blob/main/docs/gallery/gallery.yml) | The metadata that controls what items are displayed in the gallery listing.          |
| [gallery.ejs](https://github.com/quarto-dev/quarto-web/blob/main/docs/gallery/gallery.ejs) | The template used to display the items on the page.                                  |
| [index.qmd](https://github.com/quarto-dev/quarto-web/blob/main/docs/gallery/index.qmd)     | The Quarto document that configures and positions the listing in the `#gallery` div. |

: {tbl-colwidths="\[30,70\]"}

## Sorting, Filtering, and Pagination

By default, sorting, filtering, and pagination are disabled for custom listings templates, but with some simple changes to your template and listing options, you can add this capability to your custom listing. To do this, you need to include the following three things in your custom template:

1.  Include a `list` class on the HTML tag that contains the list of items.

2.  For each item, include `<%= metadataAttrs(item) %>` in the HTML tag that contains the item. This will allow Quarto write custom attributes that are used for sorting and filtering.

3.  Within each item, include a class that identifies the tag whose text represents the contents of an item's field. The class must be the name of the field prefixed with `listing-`, for example the tag whose inner text is the `item.name` should include a class `listing-name`.

For example, we can modify the above `custom.ejs` template as follows:

``` html
<ul class="list">
<% for (const item of items) { %>
  <li <%= metadataAttrs(item) %>>
    <a href="<%- item.href %>" class="listing-name"><%= item.name %></a><br/>
    <span class="listing-custom-field"><%= item['custom-field'] %><span>
  </li>
<% } %>
</ul>
```

Once you have included these items in your template, you can then enable the options in your listing:

``` yaml
listing:
  sort-ui: true
  filter-ui: true
  page-size: 10
```

The UI elements will now appear on the page and should interact properly with your custom listing.

### Field Display Names

You may want to provide a custom display name for your field to provide a better name than the field name. For example, the field name would appear in the sort UI. You can use `field-display-names` to create mapping from a field to a display name. For example:

``` yaml
listing:
  template: custom.ejs
  contents:
    - items.yml
  sort-ui: true
  filter-ui: true
  page-size: 10
  field-display-names:
    name: "Name"
    custom-field: "Custom"
```

### Date Sorting and Formatting

To properly format and sort date values, you can specify type information for fields in your items. If you specify a field is a date, it will automatically be formatted using the specified date formatting (either default or specified using `date-format`) and will support date sorting in ascending or descending order. If you specify a field as a number, it will support ascending and descending numeric sorting.

You can specify field types as follows:

``` yaml
listing:
  template: custom.ejs
  contents:
    - items.yml
  field-types:
    custom-date: date
    custom-number: number
```

### Required Fields

Since listings are generated using fields that are specified in other documents or via metadata, it can be helpful to ensure that required fields are present. You can note required fields as following:

``` yaml
listing:
  template: custom.ejs
  contents:
    - items.yml
  field-required: [name, custom-field]
```

If the listing page is rendered and any of contents is missing a value for either of the required fields, an error will be thrown noting the field that is required and the file or metadata that has omitted it.

## Template Parameters

You may also make your custom template more dynamic by using parameters to control its behavior. You can provide parameters for custom templates using the `template-params` option like:

```yaml
listing:
  template: custom.ejs
  contents:
    - items.yml
  template-params:
    param1: "param-value"
```

Template parameters can then be accessed in your template using `<%= params.param1 %>`. For example, we can modify the above `custom.ejs` template as follows:

``` html
<h3><%= templateParams.param1 %></h3>
<ul class="pub-list list">
  <% for (const item of items) { %>
      <li <%= metadataAttrs(item) %>>
        <span class="listing-title"><%= item.title %>.</span>
      </li>
  <% } %>
</ul>
```


# quarto-web/docs/prerelease/_highlights.qmd

### Highlights

{{< include /docs/prerelease/1.4/_highlights.qmd >}}

# quarto-web/docs/prerelease/1.4/typst.qmd

---
title: "Typst Format"
tbl-colwidths: [35,65]
---

{{< include _pre-release-feature.qmd >}}

Quarto v1.4 includes support for the `typst` output format. [Typst](https://github.com/typst/typst) is a new open-source markup-based typesetting system that is designed to be as powerful as LaTeX while being much easier to learn and use. Typst creates beautiful PDF output with blazing fast render times.

## Getting Started

To try out the `typst` format:

1.  Download and install the [latest pre-release](https://quarto.org/docs/download/prerelease) of Quarto 1.4 (ensure you have installed Quarto v1.4.145 or  higher).

2.  Create a document that uses `format: typst`. For example:

    ``` yaml
    ---
    title: "My document"
    format: typst
    ---

    Hello, typst!
    ```

Rendering or previewing this document will invoke the Typst CLI to create a PDF from your markdown source file. Note that Quarto includes version 0.8 of the Typst CLI so no separate installation of Typst is required.

## Typst Format

When authoring a Typst document you'll be using a Quarto format that is in turn based on a Typst template, which defines its structure, layout, and available options. The default Typst format and template that ships with Quarto (`format: typst`) includes options for specifying title, author, and abstract information along with basic layout and appearance (numbering, margins, fonts, columns, etc.).

The following options are available for customizing Typst output:

| Option                | Description                                                                                                                                                                        |
|---------------------------|---------------------------------------------|
| `title`               | Main document title                                                                                                                                                                |
| `author`              | One or more document authors.                                                                                                                                                      |
| `date`                | Date of publication                                                                                                                                                                |
| `abstract`            | Article abstract                                                                                                                                                                   |
| `toc`                 | Include a table of contents.                                                                                                                                                       |
| `number-sections`     | Apply numbering to sections and sub-sections                                                                                                                                       |
| `section-numbering`   | Schema to use for numbering sections, e.g. `1.1.a`.                                                                                                                                |
| `margin`              | Margins: `x`, `y`, `top`, `bottom`, `left`, `right`. Specified with units (e.g. `y: 1.25in` or `x: 2cm`).                                                                          |
| `papersize`           | Paper size: `a4`, `us-letter`, etc. See the docs on [paper sizes](https://typst.app/docs/reference/layout/page/#parameters–paper) for all available sizes.                         |
| `fontsize`            | Font size (e.g., `12pt`)                                                                                                                                                           |
| `columns`             | Number of columns for body text.                                                                                                                                                   |
| `include-in-header`   | `.typ` file to include in header                                                                                                                                                   |
| `include-before-body` | `.typ` file to include before body                                                                                                                                                 |
| `include-after-body`  | `.typ` file to include after the body                                                                                                                                              |
| `keep-typ`            | Keep the intermediate `.typ` file after render.                                                                                                                                    |
| `bibliography`        | `.bib` file to use for citations processing                                                                                                                                        |
| `bibliographystyle`   | Style to use with Typst's bibliography processing - See the doc about [bibliography](https://typst.app/docs/reference/meta/bibliography/#parameters–style) to see supported style. |
| `citeproc`            | If `true`, Pandoc's citeproc will be used for citation processing instead of Typst's own system (which is the default).                                                            |
| `csl`                 | `.csl` file to use when Pandoc's citeproc is used.                                                                                                                                 |

For example:

``` yaml
---
title: "My Document"
format:
  typst:
    toc: true
    section-numbering: 1.1.a
    columns: 2
bibliography: refs.bib
bibliographystyle: chicago-author-date
---
```

See the section below on [Custom Formats](#custom-formats) for details on creating your own specialized formats for use with Typst.


## Bibliography

Typst comes with its [own citation processing system for Bibliography](https://typst.app/docs/reference/meta/bibliography/) and using `format: typst` defaults to it. If you prefer to use Pandoc's citation processing with a `.csl` file (e.g to use same `.csl` for a HTML and PDF document), set `citeproc: true` explicitly in YAML header.

``` yaml
---
title: Typst doc using citeproc
format: typst
citeproc: true
bibliography: refs.bib
csl: https://www.zotero.org/styles/apa-with-abstract
---
```

## Typst Blocks

If you want to change the appearance of blocks using native Typst `#block()` calls, you can add the `.block` class to a Div and provide whatever arguments are appropriate. For example:

```` markdown
::: {.block fill="luma(230)" inset="8pt" radius="4pt"}

This is a block with gray background and slightly rounded corners.

:::
````

This gets compiled to

```` default
#block(fill:luma(230), inset=8pt, radius=4pt, 
[This is a block with gray background and slightly rounded corners])
````

## Raw Blocks

If you want to use raw `typst` markup, use a raw `typst` block. For example:

```` default
```{=typst} 
#set par(justify: true)

== Background 
In the case of glaciers, fluid dynamics principles can be used to understand how the movement and behavior of the ice is influenced by factors such as temperature, pressure, and the presence of other fluids (such as water).
```
````

To learn more about `typst` markup, see the tutorial here: <https://typst.app/docs/tutorial/>.


## Typst File (`.typ`)

The rendering process produces a native Typst file (`.typ)` which is then compiled to PDF using the Typst CLI. This intermediate file is then automatically removed. If you want to preserve the `.typ` file, use the `keep-typ` option. For example:

``` yaml
---
title: "My Document"
format:
  typst:
    keep-typ: true
---
```

You can compile a `.typ` file to PDF directly using the `quarto typst compile` command in a terminal. For example:

``` {.bash filename="Terminal"}
$ quarto typst compile article.typ
```

The `quarto typst` command uses the version of Typst built in to Quarto and support all Typst CLI actions and flags. For example, to determine the version of Typst embedeed in Quarto:

``` {.bash filename="Terminal"}
$ quarto typst --version
```

## Known Limitations

-   Callouts are not yet supported (they become block quotes with a bold heading)
-   Advanced page layout (panel layout, margin layout, etc.) does not work
-   Various other small things might not yet be implemented, please let us know if you see things that could use improvement!

## Custom Formats {#custom-formats}

You can create highly customized output with Typst by defining a new format based on a custom Typst template. The Typst team has created several useful [templates](https://github.com/typst/templates), a few which which have been adapted for use with Quarto as custom formats. These formats include:

| Format                                                                         | Usage                                                      |
|--------------------------|----------------------------------------------|
| [Poster](https://github.com/quarto-ext/typst-templates/tree/main/poster)       | `quarto use template quarto-ext/typst-templates/poster`    |
| [IEEE](https://github.com/quarto-ext/typst-templates/tree/main/ieee)           | `quarto use template quarto-ext/typst-templates/ieee`      |
| [AMS](https://github.com/quarto-ext/typst-templates/tree/main/ams)             | `quarto use template quarto-ext/typst-templates/ams`       |
| [Letter](https://github.com/quarto-ext/typst-templates/tree/main/letter)       | `quarto use template quarto-ext/typst-templates/letter`    |
| [Fiction](https://github.com/quarto-ext/typst-templates/tree/main/fiction)     | `quarto use template quarto-ext/typst-templates/fiction`   |
| [Dept News](https://github.com/quarto-ext/typst-templates/tree/main/dept-news) | `quarto use template quarto-ext/typst-templates/dept-news` |

: {tbl-colwidths=\[20,80\]}

The source code for these formats is available at <https://github.com/quarto-ext/typst-templates>.

To create a new custom Typst format (or package an existing Typst template for use with Quarto) use the `quarto create` command to get started:

``` {.bash filename="Terminal"}
$ quarto create extension format
```

Then, choose `typst` as the base format and provide a name for the extension (e.g. `letter`). A sample Typst format extension will be created based on the code used in the default template that ships with Quarto. It will include the following files which you can edit to implement your custom format:

To implement the custom format, edit the following files:

| File                 | Description                                                                                                                                           |
|-------------------------|-----------------------------------------------|
| `_extension.yml`     | Basic extension metadata (name, author, description, etc.) and format definition.                                                                     |
| `README.md`          | Documentation on how to install and use the format.                                                                                                   |
| `template.qmd`       | A starter document that demonstrates the basics of the format.                                                                                        |
| `typst-template.typ` | The core Typst template function (documentation on creating Typst templates can be found here: <https://typst.app/docs/tutorial/making-a-template/>). |
| `typst-show.typ`     | File that calls the template's function (mapping Pandoc metadata to function arguments).                                                              |

Additional resources you might find useful when creating custom formats include:

-   The official Typst tutorial on [Making a Template](https://typst.app/docs/tutorial/making-a-template/)

-   List of third party templates from the [Awesome Quarto](https://github.com/qjcg/awesome-typst#templates--libraries) repo.

### Template Partials

::: callout-note
This section covers advanced customization of Typst format output and can be safely ignored unless you have found the method of defining custom Typst formats described above too limited.
:::

Above we describe a method of creating a Typst format based on specifying two [template partials](https://quarto.org/docs/journals/templates.html#template-partials) (`typst-template.typ` and `typst-show.typ`). These partials customize components of the default Typst Pandoc template, but leave some of the core scaffolding including definitions required by Pandoc for its Typst output as well as handling of bibliographies and footnotes (this means that your own custom Typst formats do not need to explicitly handle them).

If you would like to fully override the Pandoc template used for rendering Typst, use the `template` option in your custom format (rather than `template-partials`) and provide an alternate implementation of the default template. For example, your `_extensions.yml` might look like this:

``` {.yaml filename="_extensions.yml"}
---
title: Typst Custom Format
author: Jane Smith
version: "0.2.0"
quarto-required: ">=1.4.11"
contributes:
  formats:
    typst:
      template: template.typ
      template-partials:
        - typst-template.typ
        - typst-show.typ
---
```

Use the [source code](https://github.com/quarto-dev/quarto-cli/blob/main/src/resources/formats/typst/pandoc/quarto/template.typ) of the default template as a starting point for your `template.typ`. Note that you can call all of the template partials provided by Quarto (e.g. `biblio.typ()` or `notes.typ()` from within your custom template implementation.

The [AMS](https://github.com/quarto-ext/typst-templates/tree/main/ams) format provides an example of redefining the main template (in that case, it is to prevent automatic bibliography processing by Quarto in deference to the built-in handling of the Typst AMS template).


# quarto-web/docs/prerelease/1.4/index.qmd

---
title: Quarto 1.4 Pre-Release
date: last-modified
search: false
---

{{< include _highlights.qmd >}}


See the [Pre-Release Download Page](/docs/download/prerelease) for a complete list of all the changes and bug fixes.


# quarto-web/docs/prerelease/1.4/lua_changes.qmd

---
title: "Lua filter changes"
---

{{< include _pre-release-feature.qmd >}}

Quarto v1.4 includes the following new features for Lua filters:

## Support for crossreferenceable elements in filters

Quarto v1.4 brings significant changes to the handling of figures, tables, listings, etc.
These changes simplify the writing of Lua filters that targets those elements, but will 
generally require changes in existing.

### The `FloatRefTarget` AST node

In v1.4, crossreferenceable elements all have a single generic type, `FloatRefTarget`. 
This element can be constructed explicitly in a Lua filter.
It can also be used as the element to be processed in a Lua filter directly.

```{.lua}
-- A filter targeting FloatRefTarget nodes
return {
  FloatRefTarget = function(float)
    if float.caption_long then
      float.caption_long.content:insert(pandoc.Str("[This will appear at the beginning of every caption]"))
      return float
    end
  end
}
```

`FloatRefTarget` nodes have the following fields:

- `type`: The type of element: `Figure`, `Table`, `Listing`, etc. Quarto v1.4 supports
  custom node types that can be declared at the document or project level.
- `content`: The content of the Figure, Table, etc. Quarto v1.4
  accepts any content in any `FloatRefTarget` type (so if your tables are better displayed
  as an image, you can use that.).
- `caption_long`: The caption that appears in the main body of the document
- `caption_short`: The caption that appears in the element collations (such as a list of tables, 
  list of figures, etc.)
- `identifier`, `attributes`, `classes`: these are analogous to `Attr` fields in Pandoc AST elements like spans and divs. 
  `identifier`, in addition, needs to be the string that is used in a crossref (`fig-cars`, `tbl-votes`, `lst-query`, and so on).
- `parent_id`: if a `FloatRefTarget` is a subfloat of a parent multiple-element float, then `parent_id` will hold the identifier
  of the parent float.

## Custom formats and Custom renderers

Quarto v1.4 adds support for extensible renderers of quarto AST nodes such as `FloatRefTarget`, `Callout`.
In order to declare a custom renderer, add the following to a Lua filter:

```lua
local predicate = function(float)
  -- return true if this renderer should be used;
  -- typically, this will return true if the custom format is active.
end
local renderer = function(float)
  -- returns a plain Pandoc representation of the rendered figure.
end
quarto._quarto.ast.add_renderer(
  "FloatRefTarget", 
  predicate, 
  renderer)
```

## Relative paths in `require()` calls

In larger, more complex filters, it becomes useful to structure your Lua code in modules.
Quarto v1.4 supports the use of relative paths in `require()` calls so that small modules
can be easily created and reused.

For example:

```{.lua filename="filter.lua"}
local utility = require('./utils')
function Pandoc(doc)
  -- process 
end
```

Using relative paths this way in quarto makes it harder for multiple filters to accidentally
create conflicting module names (as would eventually happen when using the standard Lua
`require('utils')` syntax). It's possible to refer to subdirectories and parent directories as well:

```{.lua filename="filter2.lua"}
local parsing = require('./utils/parsing')
function Pandoc(doc)
  -- process 
end
```

```{.lua filename="utils/parsing.lua"}
local utils = require("../utils")
-- ...
```



# quarto-web/docs/prerelease/1.4/lightbox.qmd

---
title: "Lightbox Support"
---

{{< include _pre-release-feature.qmd >}}

## Overview

The new lightbox feature in Quarto uses the [GLightbox javascript library](https://biati-digital.github.io/glightbox/) to add lightbox styling and behavior to images in your HTML documents. For example, the following document enables lightbox treatment for images in the document:

``` markdown
---
title: Simple Lightbox Example
lightbox: true
---

![A Lovely Image](mv-1.jpg)
```

The viewer of the rendered HTML page for this document will be able to click the image to zoom and see a larger version of the image (including any caption).

## Enabling Lightbox

You can enable lightbox either for all images within a document, or for only selected images within a document. To enable lightbox for all images within a document, use the following yaml:

``` yaml
---
lightbox: true
---
```

When lightbox is set to automatically select images, it will match any image used as a figure or which appears as a block (by itself within a paragraph). By default, images that appear inline with other content will not receive lightbox treatment.

### Applying Lightbox to Specific Images

You can select specific images to receive the lightbox treatment by applying the `lightbox` class on the images you'd like to receive the treatment. In this case, there is no need to include `lightbox` in the front matter, the use of the `lightbox` class will automatically enable lightbox. For example:

``` markdown
---
title: Simple Lightbox Example
---

![A Lovely Image](mv-1.jpg){.lightbox}

![Another Lovely Image](mv-2.jpg)
```

will result in the first image receiving a lightbox treatment, while the second image will not.

## Disabling Lightbox Treatment

You can disable lightbox for the whole document using the following yaml:

``` yaml
---
lightbox: false
---
```

When lightbox is explicitly disabled, no images will receive the lightbox treatment, even if the image is marked with a `lightbox` class (as described above).

### Disabling Lightbox for Specific Images

If automatic lightboxing of images is enabled, you can select specific images to not receive the treatment by marking them with a `no-lightbox` class. For example:

``` markdown
---
title: Simple Lightbox Example
lightbox: auto
---

![A Lovely Image](mv-1.jpg)

![Another Lovely Image](mv-2.jpg){.no-lightbox}
```

In this example, the first image will receive the lightbox treatment, while the second image will not.

## Galleries

In addition to simply providing a lightbox treatment for individual images, you can also group images into a 'gallery'. When the user activates the lightbox, they will be able to page through the images in the gallery without returning to the main document. To create galleries of images, apply a `group` attribute (with a name) to the images that you'd like to gather into a gallery. Images with the same group name will be placed together in a gallery when given a lightbox treatment.

For example, the following three images will be treated as a gallery:

``` markdown
![A Lovely Image](mv-1.jpg){group="my-gallery"}

![Another Lovely Image](mv-2.jpg){group="my-gallery"}

![The Last Lovely Image](mv-3.jpg){group="my-gallery"}
```

## Options

Quarto supports a number of options to customize the ligthbox behavior for a document. Options include:

| Option          | Description                                                                                                                                                              |
|---------------------|---------------------------------------------------|
| `match`         | Set this to `auto` if you'd like any image to be given lightbox treatment. If you omit this, only images with the class `lightbox` will be given the lightbox treatment. |
| `effect`        | The effect that should be used when opening and closing the lightbox. One of `fade`, `zoom`, `none`. Defaults to `zoom`.                                                 |
| `desc-position` | The position of the title and description when displaying a lightbox. One of `top`, `bottom`, `left`, `right`. Defaults to `bottom`.                                     |
| `loop`          | Whether galleries should 'loop' to first image in the gallery if the user continues past the last image of the gallery. Boolean that defaults to `true`.                 |
| `css-class`     | A class name to apply to the lightbox to allow css targeting. This will replace the lightbox class with your custom class name.                                          |

A complete example:

``` yaml
---
title: Complete Lightbox Example
filters:
  - lightbox
lightbox:
  match: auto
  effect: fade
  desc-position: right
  loop: false
  css-class: "my-css-class"
---
```

## Per Image Attributes

The following options may be specified as attributes on individual images to control the lightbox behavior:

| Option          | Description                                                                                                                         |
|--------------------|----------------------------------------------------|
| `desc-position` | The position of the title and description when displaying a lightbox. One of `top`, `bottom`, `left`, `right`. Defaults to `bottom` |

## Using Lightbox with Computational Cells

The Quarto lightbox treatment will use figure information for computational outputs. For example, the following plot will receive a lightbox treatment and will include a properly prefixed caption when the user zooms into the plot.

```` markdown
---
lightbox: auto
---

```{{r}}
#| label: fig-basic
#| fig-cap: Simple demo R plot 
plot(1:10, rnorm(10))
```
````

If your computational cell produces multiple subfigures, each of the subfigures will receive the lightbox treatment and when zoom, the user may page back and forth through the subfigures. For example, the following will produce a 'gallery' lightbox view which includes both of the subfigures, allowing the viewer to easily navigate between sub figures:

```` markdown
```{{r}}
#| label: fig-plots
#| fig-cap: |
#|   The below demonstrates placing more than one image in a gallery. Note
#|   the usage of the `layout-ncol` which arranges the images on the page
#|   side by date. Adding the `group` attribute to the markdown images places
#|   the images in a gallery grouped together based upon the group name
#|   provided.
#| fig-subcap:
#|   - "This is a caption for the first sub figure"
#|   - "This is a caption for the second sub figure"
#| layout-ncol: 2
plot(ToothGrowth)
plot(PlantGrowth)
```
````

### Advanced Customization In Computations

Options for lightbox can be passed using the code cell option `lightbox` like the following:

```` markdown
```{{r}}
#| fig-cap: Simple demo R plot 
#| lightbox:
#|   group: r-graph
#|   description: This is 1 to 10 plot
plot(1:10, rnorm(10))
```
````

It is possible to create several plots, and group them in a lightbox gallery. Use list in YAML for options when you have several plots, on per plot.

```` markdown
```{{r}}
#| fig-cap: 
#|   - Caption for first plot
#|   - Caption for second plot
#| lightbox: 
#|   group: cars
#|   description: 
#|     - This is the decription for first graph
#|     - This is the decription for second graph
plot(mtcars)
plot(cars)
```
````

# quarto-web/docs/prerelease/1.4/_highlights.qmd

Quarto 1.4 includes the following new features:

-   [Quarto Manuscripts](/docs/manuscripts/index.qmd)---A new project type for scholarly articles, where notebooks are both the source of the article, and part of the published record.

-   [Quarto Dashboards](/docs/dashboards/index.qmd)--A new format for creating interactive dashboards.

-   [Typst Format](/docs/prerelease/1.4/typst.qmd)---Support for the `typst` output format. [Typst](https://github.com/typst/typst) is a new open-source markup-based typesetting system that is designed to be as powerful as LaTeX while being much easier to learn and use.

-   [Shiny for Python](/docs/dashboards/interactivity/shiny-python/index.qmd)---Support for using Shiny for Python within Quarto documents. 

-   [Inline Execution for Jupyter](/docs/prerelease/1.4/inline.qmd)---Support for executing inline expressions when using Jupyter kernels. 

-   [Script Rendering for Jupyter](/docs/prerelease/1.4/script.qmd)---Support for rendering script files (e.g. `.py`, `.jl`, or `.r`) that are [specially formatted](https://jupytext.readthedocs.io/en/latest/formats-scripts.html) as notebooks.

-   [Easy Binder Configuration for Quarto Projects](/docs/prerelease/1.4/binder.qmd)---Support for generating files required to deploy a Quarto project using Binder.

-   [Lightbox Treatment for Images and Figures](/docs/prerelease//1.4/lightbox.qmd)---Support for zooming into images and figures using a `lightbox`. Includes support for grouping multiple images into a gallery.

-   [Lua changes](/docs/prerelease/1.4/lua_changes.qmd)---Quarto v1.4 adds new features to writers of Lua filters.

-   [Crossref changes](/docs/prerelease/1.4/crossref.qmd)---Quarto v1.4 makes crossreferenceable elements more powerful and general.

-   [AST processing changes](/docs/prerelease/1.4/ast.qmd)---Quarto v1.4 improves on the HTML table processing added in v1.3 and adds a way for LaTeX raw blocks to include Quarto-compatible markdown for processing.

# quarto-web/docs/prerelease/1.4/_pre-release-feature.qmd

::: {.callout-note}
## Pre-release Feature

This feature is new in the upcoming Quarto 1.4 release. To use the feature now, you'll need to [download](https://quarto.org/docs/download/prerelease) and install the Quarto pre-release.
:::

# quarto-web/docs/prerelease/1.4/binder.qmd

---
title: "Using Binder With Quarto"
---

{{< include _pre-release-feature.qmd >}}

## Overview

The Binder project provides a stack of tools designed to make it easy to share computing environments. When projects use best practices and are hosted online, Binder makes it straightforward to provide users with a link which restores the computing environment.

Quarto can now automatically create supporting files required to permit deployment of Quarto projects using Binder. Use the command `quarto use binder` from within a project directory to initialize your directory with required files.

## Creating Binder Files

Use the command `quarto use binder` from within your Quarto project directory to generate files required to make your project available via Binder. The command will scan the project and based upon the specific configuration (Quarto version and tools, computational engines, data about dependencies and the computational environment), determine the configuration restore the environment.

::: callout-tip
Files generated by the `quarto use binder` command should be committed into your repo so they are available when the repo is used by Binder to restore the computational environment.
:::

## Dependencies

When your project is restored to a new computational environment using Binder, any dependencies that the project has must also be restored. There are a few different ways of documenting these dependencies so they may be restored. The most common for the each environment are as follows:

| Language | Environment                                                         | File               |
|---------------|-------------------------------------------|---------------|
| R        | [renv](https://rstudio.github.io/renv/index.html)                   | `renv.lock`        |
| Python   | [Conda](https://docs.conda.io/projects/conda/en/stable/)            | `environment.yml`  |
| Python   | [Pip](https://pip.pypa.io/en/stable/user_guide/#requirements-files) | `requirements.txt` |
| Julia    | [Pkg](https://pkgdocs.julialang.org/v1/toml-files/)                 | `project.toml`     |

### Configuration Files

The following files may be generated by the command. Note that the command will prompt before overwriting any user files that it didn't generate or any files that have been modified since they were generated.

`postBuild`

:   The post build script runs code after restoring the environment. This script is generated with commands required to ensure the proper version of Quarto is present in the environment, install any required tools like TinyTex or Chromium are installed, and to configure VSCode and the Quarto extension for VSCode when applicable.

`runtime.txt`

:   For R projects, this file will be generated with the appropriate R version, which is used to ensure that the same R version is present in the computational environment. This also will result in RStudio being configured and available when the computational evironment is restored by a user.

`install.R`

:   For R projects, an `install.R` file will be generated to activate any `renv` environment that is present.

`apt.txt`

:   Provides a list of Debian packages to install with `apt-get`. This file is generated with all Quarto package dependencies.

`.jupyter`

:   For projects using QMD files with the Jupyter engine, a `.jupyter` directory will be generated which will configure support for VSCode from within the JupyterLab environment.


# quarto-web/docs/prerelease/1.4/ast.qmd

---
title: "AST processing changes in v1.4"
---

In Quarto v1.3, we added support for parsing HTML tables as native Pandoc elements, so that sophisticated table layouts are available in more formats. Quarto v1.4 extends this in a few ways.

## Finer control over table processing

In v1.3, this HTML processing could be disabled only by specifying an option in the HTML table itself, using `quarto-disable-processing="true"`.

In v1.4, this behavior can be controlled by document- and project-level metadata, using the `html-table-processing: none` YAML option:

````qmd
---
html-table-processing: none
---

No HTML tables in this document will be processed.

```{{r}}
library(huxtable)
# your huxtable tables won't be processed by quarto
```

````

In addition, you can disable the processing selectively in parts of the document, by surrounding the elements with a fenced div having the attribute `{html-table-processing="none"}`:

````qmd
---
html-table-processing: none
---

No HTML tables in this document will be processed.

::: {html-table-processing="none"}

```{{r}}
library(huxtable)
# your huxtable tables won't be processed by quarto because of
# the surrounding div
```

:::

```{{r}}
library(gt)
# your gt tables will be processed as in 1.3
```
````

## Include Quarto markdown in LaTeX Raw Blocks

In Quarto v1.3, HTML rawblocks can contain the syntax `<span data-qmd="<<markdown-content>>"/>` of `<span data-qmd-base64="<<base64-encoded-markdown-content>>"` to allow libraries that emit raw blocks to benefit
from Quarto features such as crossref resolution and shortcodes.

In Quarto v1.4, this feature is also available in LaTeX formats. If the syntax `\QuartoMarkdownBase64{<<base64-encoded-markdown-content>>}` is detected by Quarto, the contents will be decoded,
processed in Quarto (including user filters), and then inserted back into the LaTeX raw block.

This is useful for third-party libraries that seek to emit LaTeX content that nevertheless 
can have "quarto content". Note that, unlike the HTML feature, Quarto currently only 
supports base-64 encoded content in LaTeX blocks.

Note that, unlike the HTML table parsing feature, this LaTeX feature cannot currently be disabled.
We expect this to not be necessary because `QuartoMarkdownBase64` is unlikely to conflict with
existing LaTeX environments.

# quarto-web/docs/prerelease/1.4/script.qmd

---
title: "Script Rendering for Jupyter"
---

{{< include _pre-release-feature.qmd >}}

## Overview

Quarto v1.4 includes support for rendering script files (e.g. `.py`, `.jl`, or `.r`) that are specially formatted as notebooks. Script rendering makes use of the [percent format](https://jupytext.readthedocs.io/en/latest/formats-scripts.html) that is supported by several other other tools including Spyder, VS Code, PyCharm, and Jupytext.

For example, here is a Python script that includes both markdown and code cells:

``` {.python filename="script.py"}
# %% [markdown] 
# ---
# title: Palmer Penguins
# author: Norah Jones
# date: 3/12/23
# ---

# %% 
#| echo: false
import pandas as pd
df = pd.read_csv("palmer-penguins.csv")

# %% [markdown]
"""
## Exploring the data

See @fig-bill-sizes for an exploration of bill sizes by species.
"""

# %% 
#| label: fig-bill-sizes
#| fig-cap: Bill Sizes by Species

import matplotlib.pyplot as plt
import seaborn as sns

g = sns.FacetGrid(df, hue="species", height=3, aspect=3.5/1.5)
g.map(plt.scatter, "bill_length_mm", "bill_depth_mm").add_legend()
```

Code cells are delimited by `# %%` and markdown cells are delimited by `# %% [markdown]`. Markdown content can either be included in single line comments (`#`) or multi-line strings (`"""`), both of which are illustrated above.

Note that cell options are included as normal using `#|` prefixed comments (e.g. `#| echo: false`). Also note that you can include blank lines within cells (cells continue until another cell is encountered).

## Render and Preview

Rendering and previewing notebook scripts works exactly like `.qmd` and `.ipynb` files. For example, the following commands are all valid:

```bash
$ quarto render script.py
$ quarto render script.jl

$ quarto preview script.py
$ quarto preview script.jl
```

Jupyter scripts rendered with Quarto must begin with a `# %% [markdown]` cell (which normally includes the `title` and other YAML options). This convention is how Quarto knows that it should parse code cells using the percent format (as opposed to other notebook as script formats that may be supported in the future).

Jupyter script rendering is supported for Python, Julia, and R. Note that for R scripts, the [IRkernel](https://irkernel.github.io) will be used to execute code cells rather than Knitr (support for the Knitr [spin](https://bookdown.org/yihui/rmarkdown-cookbook/spin.html) script format is planned but not yet implemented).

The latest version (v1.97.0) of the [Quarto VS Code Extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto) also implements support for render and preview of Jupyter scripts.


## Generating Markdown

Jupyter scripts are especially convenient when most of your document consists of code that dynamically generates markdown. You can write markdown from Python using functions in the `IPython.display` module. For example:

```python
# %%
#| echo: false
radius = 10
from IPython.display import Markdown
Markdown(f"The _radius_ of the circle is **{radius}**.")
```

Note that dynamically generated markdown will still be enclosed in the standard Quarto output divs. If you want to remove all of Quarto's default output enclosures use the `output: asis` option. For example:

```python
# %%
#| echo: false
#| output: asis
radius = 10
from IPython.display import Markdown
Markdown(f"The _radius_ of the circle is **{radius}**.")
```


## Raw Cells

You can include raw cells (e.g. HTML or LaTeX) within scripts using the `# %% [raw]` cell delimiter along with a `format` attribute, for example:

```python
# %% [raw] format="html"
"""
<iframe width="560" height="315" src="https://www.youtube.com/embed/lJIrF4YjHfQ?si=aP7PxA1Pz8IIoQUX"></iframe>
"""
```

## Scripts in Projects

Jupyter scripts can also be included within [projects](/docs/projects/quarto-projects.qmd) (e.g. websites, blogs, etc.). Scripts within projects are only rendered by Quarto when they have a markdown cell at the top (e.g. `# %% [markdown]`). 

If for some reason you need to ignore a script that begins with a markdown cell, you can create an explict render list in `_quarto.yml` that excludes individual scripts as required, for example:

```yaml
project:
  type: website
  render:
    - "*.{qmd,ipynb,py}"
    - "!utils.py"
```

Note that this technique is documented for the sake of completeness---in practice you should almost never need to do this since Python scripts rarely begin with `# %% [markdown]` unless you are authoring them specifically as notebooks. 








# quarto-web/docs/prerelease/1.4/crossref.qmd

---
title: "Crossreferenceable elements"
---

## Crossreferenceable elements take arbitrary content

Crossreferenceable elements now support any kind of content.
In previous versions, Quarto figures needed (for the most part) to be images; Quarto tables needed to be `Table` elements, and so on.
In v1.4, you can declare a Figure like this:

````
::: {#fig-1}

::: {.figure-content}
This is the figure content.
:::

This is a caption.

:::
````

Here, the identifier of the figure is still `fig-1`, but the content of the "Figure" is a fenced Div with any kind of content. The figure
itself is still referenced by `@fig-1`. The prefix `fig` identifies the type of crossreferenceable element. By default, Quarto v1.4 has support
for Figures (`fig-`), Tables (`tbl-`) and Listings (`lst-`).

## Custom crossreferenceable types

In addition, Quarto v1.4 supports custom crossreferenceable types. If your document has a large number of, say diagrams or videos, you might
want to refer to them directly as such. To use them, add the following to your document or project metadata:

```yaml
crossref:
  custom: 
    - # crossreferenceable elements with captions are `float`
      kind: float

      # the prefix for reference in output ("In Figure 1, ..")
      prefix: Diagram 

      # the prefix for captions ("Figure 1: ..")
      name: Diagram

      # the prefix for the reference identifier ("In @fig-1, ...")
      ref-type: dia

      # the name of the custom environment in latex output
      latex-env: diagram 

      # used as the file extension for the auxiliary file
      # generated by latex during the collation process
      # if omitted, `lo${ref-type}` is used.
      latex-list-of-file-extension: lod

    - kind: float
      ref-type: supptbl
      latex-env: supptbl
      prefix: Table S
      name: Table S

      # when `false`, don't insert a number between `prefix`, `name` 
      # and the crossref numbering. In this case, crossrefs will be
      # `Table S1`, `Table S2`, etc.
      space-before-numbering: false
      
      # used to create the title, here "List of Supplementary Tables" in LaTeX
      latex-list-of-description: Supplementary Table
```

### Example: supplemental figures and tables

Using custom crossreferenceable types, you can define "Supplemental Figures", by creating a new prefix (eg, `supptbl` above) and giving it the
same appearance as regular figures. Then, if you only use this prefix for figures in the supplements, you will get a fresh crossref counter.

## Changes in HTML output

Keep in mind the following changes in the HTML output of figures, etc:

- The DOM structure for HTML figures used to be such that the following CSS selector would work:
  
  ```
  div#fig-elephant > figure > figcaption.figure-caption
  ```
  
  In Quarto v1.4, this is now
  
  ```
  div#fig-elephant > figure.quarto-float.quarto-float-fig > figcaption.quarto-float-caption.quarto-float-fig
  ```

  Here's a minimal, full HTML output for a figure:

  ```html
  <div id="fig-1" class="quarto-figure quarto-figure-center anchored">
    <figure class="quarto-float quarto-float-fig figure">
    <div aria-describedby="fig-1-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
      <img src="./img/content.jpg">
    </div>
    <figcaption id="fig-1-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca" class="figure quarto-float-caption quarto-float-fig">
    Figure&nbsp;1: This is a caption.
    </figcaption>
    </figure>
  </div>
  ```

  Concretely: 

  - All crossreferenceable elements use the `figure` HTML element with class `quarto-float`.
  - Different float types are differentiated by the CSS class `quarto-float-fig` (or `-tbl`, `-lst`, or the `ref_type` of custom crossref types) as well as the additional CSS class `figure`, `table`, etc. 
    If the element is a subfloat, this will be `quarto-subfloat-fig`.
  - Similarly, float captions use the `figcaption` element with class `quarto-float-caption` (or `quarto-subfloat-caption` if they're a subfloat), and are differentiated by the same additional CSS classes.
  
  This setup lets all "floats" be uniformly targeted by a single CSS rule, as well as allowing specific float types and their captions be targeted by a single additional CSS selector.

- Images by themselves used to have a surrounding paragraph; they no longer do.

- Floats include an extra div for ARIA referencing, so that captions are referenced appropriately and uniformly. 
  As a result, a table appears inside a float, its caption will be hoisted to the figure node itself 

## Cross-referenceable listings of executable code blocks:

To create crossreferenceable code listings from executable code blocks, use `lst-label` and `lst-cap`.

````
```{{r}}
#| label: fig-1
#| fig-cap: A figure caption
#| lst-label: lst-1
#| lst-cap: A listing caption
plot(1:10)
```

See @fig-1 and @lst-1.
````


# quarto-web/docs/prerelease/1.4/inline.qmd

---
title: "Inline Execution for Jupyter"
---

{{< include _pre-release-feature.qmd >}}

## Overview

Quarto v1.4 includes support for executing inline expressions when using Jupyter kernels. Inline expressions are similar to code blocks, except that they use a single tick (`` ` ``) rather than triple tick (```` ``` ````) and can appear anywhere. For example, the following code:

```` markdown
```{{python}}
x = 5
```

The answer is `{python} x`
````

Will create this markdown output:

```         
The answer is 5.
```

This syntax works for any Jupyter kernel---so for Julia you would write an inline expression as `` `{julia} x` ``).

::: callout-caution
One important consideration with inline expressions is that they should be confined to simple values that you have pre-computed within normal code cells (rather than function calls that do non-trivial work). This is because the protocol used for inline expressions is not compatible with some Python libraries (especially those that use multi-threading or multi-processing).
:::

## Usage in Notebooks

Inline expressions are always evaulated when rendering and previewing `.qmd` files. However, for notebooks you need to execute the notebook with Quarto in order to evaluate inline expressions (i.e. they won't be evaluated within the JupyterLab, VS Code, or PyCharm notebook editor).

You can work in your favorite notebook front-end without Quarto execution, then once you are ready to publish execute the notebook during rendering as follows:

``` {.bash filename="Terminal"}
$ quarto render notebook.ipynb --execute
```

You can also turn on execution within the YAML options of a notebook. For example:

``` yaml
---
title: "My Notebooks"
execute:
  enabled: true
---
```

## Markdown Output

Note that by default, the output of inline expressions is treated as ordinary text (i.e. markdown within it is not rendered). Any markdown like syntax within the output of inline expressions will be automatically escaped. For example, the following inline expression:

`` `{{python}} '**not bold**'` ``

Will produce the following markdown:

`\*\*not bold\*\*`

If you want to explicitly create markdown output, use the `Markdown()` function from `IPython.display`. For example, the following inline expression will result in bolded text:

```` markdown
```{{python}}
from IPython.display import Markdown
```

`{python} Markdown('**bold**')`
````

Note that for the Knitr engine, you use the `I()` function to designate that inline output has markdown to render. For example:

``` markdown
`{r} I('**bold**')`
```

## Escaping

If you are writing documentation about inline expressions (as we are in this article!) then you may need to escape the syntax so that it doesn't execute. You can do that in one of two ways:

1)  Use a double-brace around the expression. For example: `` `{{{python}}} x` ``

2)  Enclose the expression in an extra backtick. For example: ``` ``{python} x`` ```

Each of the expressions above will render (unexpected) as `` `{{python}} x` `` within the output document.

## Engine Binding

If you use inline expressions in a document that does not have any other executable code blocks then you should explicitly set the `engine` document option to ensure that your expressions are evaluated (automatic engine binding works for blocks but not inlines). For example:

``` markdown
---
title: "My Document"
engine: jupyter
---

`{python} "hello"`
```

## Syntax Compatibility

The Knitr and Observable engines each have their own syntax for inline expressions. To make it easier to learn and use expressions across engines, there is also a mapping from the Jupyter-compatible syntax to the native synaxes of Knitr and Observable. For example:

| Engine     | Example           | Converted   |
|------------|-------------------|-------------|
| Knitr      | `` `{{r}} x` ``   | `` `r x` `` |
| Observable | `` `{{ojs}} x` `` | `${x}`      |

So you can use either the standard Quarto inline expression syntax or the native syntax with these engines.

Note that native Knitr inline syntax has a different default behavior for handling of markdown content. Specificially, it treats all inline output as *containing markdown* (whereas Quarto assumes that it doesn't). So a strict equivalency between the Knitr and Quarto syntax would be:

| Knitr                | Quarto                    |
|----------------------|---------------------------|
| `` `r "**bold**"` `` | `` `{r} I("**bold**")` `` |

# quarto-web/docs/prerelease/1.3/index.qmd

---
title: Quarto 1.3 Pre-Release
date: last-modified
search: false
---

{{< include _highlights.qmd >}}


See the [Pre-Release Download Page](/docs/download/prerelease) for a complete list of all the changes and bug fixes.


<!--
- Large: Jupyter [Cell Embedding]
    - Notebook preview responsive size
-->


# quarto-web/docs/prerelease/1.3/_highlights.qmd

Quarto 1.3 includes the following new features:

-   [Confluence Publishing](/docs/publishing/confluence.qmd)---Publish quarto documents and projects to Confluence spaces.

-   [Multi-Format Publishing](/docs/output-formats/html-multi-format.qmd)---Simple discovery of other formats for HTML documents.

-   [Jupyter Cell Embedding](/docs/authoring/notebook-embed.qmd)---Embed code and outputs from Jupyter Notebooks in Quarto documents.

-   [Article Grid Customization](/docs/output-formats/page-layout.qmd#grid-customization)---Customize the widths within the article grid in HTML documents.

-   [Code Block Annotation](/docs/authoring/code-annotation.qmd)---Use annotation to provide contextual comments to help readers understand code.

-   [Quarto Book AsciiDoc Support](/docs/books/book-output.qmd#asciidoc-books)---Output Quarto books to AsciiDoc files

-   [Website Navigation Improvements](/docs/prerelease/1.3/website-nav.qmd)---Improved navigation for Quarto websites.

-   [Mermaid Diagram Theming](/docs/authoring/diagrams.qmd#mermaid-theming)---Mermaid diagram's appearance automatically matches your document's theme (or customize it)

-   [PDF: SVG and Remote Images](/docs/prerelease/1.3/pdf.qmd)---Improved handling for SVG images and remote images in PDF documents.

-   [`kbd` Shortcode](/docs/authoring/markdown-basics.qmd#keyboard-shortcuts)---Show well formatted keyboard shortcuts in Quarto documents.

-   [Extensions: Quarto AST](/docs/prerelease/1.3/ast.qmd)---Use custom AST nodes for Quarto types like Callout when writing extensions.

-   [Extensions: HTML Tables](/docs/prerelease/1.3/tables.qmd)---HTML tables are now processed and accessible to Lua filters in all formats (not just HTML).


# quarto-web/docs/prerelease/1.3/_pre-release-feature.qmd

::: {.callout-note}
## Pre-release Feature

This feature is new in the upcoming Quarto 1.3 release. To use the feature now, you'll need to [download](https://quarto.org/docs/download/prerelease) and install the Quarto pre-release.
:::

# quarto-web/docs/prerelease/1.3/pdf.qmd

---
title: PDF Format Improvements
---

{{< include _pre-release-feature.qmd >}}

## SVG Images

Starting in Quarto 1.3, we support rendering of PDF documents that include SVG files, automatically converting them to PDF images if `rsvg-convert` is available on the system path during rendering.

You can learn more about installing `librsvg`{spellcheck="false"} (which provides `rsvg-convert`{spellcheck="false"}), see <https://wiki.gnome.org/Projects/LibRsvg>. To install on specific platforms, follow the below instructions:

-   On MacOS, you an use Homebrew (<https://formulae.brew.sh/formula/librsvg>) `brew install librsvg`{spellcheck="false"}

-   Tarballs for Linux are available here: <https://download.gnome.org/sources/librsvg/>

-   On Windows, you can [install using chocolatey](https://community.chocolatey.org/packages/rsvg-convert): `choco install rsvg-convert`{spellcheck="false"}

## Remote Images

Starting in Quarto 1.3, when rendering PDFs, Quarto will automatically fetch remote image references and properly embed them within the PDF.

## Filenames with Modifiers

In quarto 1.3, the default filename for PDF files includes variants and modifiers, and so the following YAML front matter will work:

```yml
# example.qmd
format:
  pdf+simple: default # generates example+simple.pdf
  pdf: default # generates example.pdf
```


# quarto-web/docs/prerelease/1.3/ast.qmd

---
title: Custom AST Nodes
---

{{< include _pre-release-feature.qmd >}}

## Overview

Quarto now supports custom AST nodes in Pandoc filters. This allows more flexibility in defining and using Lua filters.

We will slowly roll out more extensive changes of the AST, but currently, the following objects are custom AST nodes:

-   [Callouts](custom-ast-nodes/callout.qmd)
-   [Tabsets](custom-ast-nodes/tabset.qmd)
-   [Conditional Blocks](custom-ast-nodes/conditional-block.qmd)

## Example: Callouts

In previous versions of Quarto, callouts would be represented directly as a div with a class starting with `callout`, and the contents laid out in a [particular way](/docs/authoring/callouts.qmd).

While *authoring* documents, this syntax remains unchanged. But when processing the document, the callout divs are now represented as a custom AST node, which can be processed directly in Lua filters. In Quarto 1.3, callouts can be captured in Lua filters more directly. For example, here is a filter that forces every callout to be of type "caution":

``` lua
function Callout(callout)
  -- do something with the callout
  callout.type = "caution"

  -- note that custom AST nodes are passed by reference. You can
  -- return the value if you choose, but you do not need to.
end
```

Finally, custom AST node constructors are available in the `quarto` object: `quarto.Callout`, `quarto.Tabset`, etc. See the pages above for details.


# quarto-web/docs/prerelease/1.3/tables.qmd

---
title: HTML Table Processing
---

{{< include _pre-release-feature.qmd >}}

## Overview

In Quarto 1.3, we have made some changes to how tables are processed. Recent Pandoc versions have added support for parsing HTML tables into Pandoc's native data structures (including features such as rowspans and colspans), and Quarto now leverages this to make it easier to produce properly formatted tables in more formats.

### HTML tables are now processed in every format

Specifically, Quarto will now attempt to parse HTML tables in `RawBlock` nodes in `html` format and convert them to Markdown tables, regardless of output format (intentionally including non-HTML formats). As a result, you can now use HTML table syntax in your documents and they will be properly converted to Markdown tables for all formats, and libraries which emit computational tables in HTML format can work in other output formats. In addition, this will allow Lua filters to manipulate the content of tables specified in HTML format.

::: callout-note

If you're a library author, we hope that you will consider emitting HTML tables in your output. This will allow your users to use the full power of Quarto's table processing in all formats.

With that said, it's possible that our processing of HTML tables interferes with your library's processing. If this is the case, you can disable Quarto's processing of HTML tables by adding the following data attribute to your table:

```
<table data-quarto-disable-processing="true">
  ...
</table>
```

:::

### Bootstrap classes can be added to tables

Bootstrap table classes given as attributes next to a table caption are now inserted into the `<table>` element. The classes permitted are those that apply expressly to the entire table, and these are: `"primary"`, `"secondary"`, `"success"`, `"danger"`, `"warning"`, `"info"`, `"light"`, `"dark"`, `"striped"`, `"hover"`, `"active"`, `"bordered"`, `"borderless"`, `"sm"`, `"responsive"`, `"responsive-sm"`, `"responsive-md"`, `"responsive-lg"`, `"responsive-xl"`, `"responsive-xxl"`. For example, the following Markdown table will be rendered with row stripes and the rows will also be highlighted on hover:

```
| fruit  | price  |
|--------|--------|
| apple  | 2.05   |
| pear   | 1.37   |
| orange | 3.09   |

: Fruit prices {.striped .hover}
```

### Embedded Markdown content can be specified

In addition, Quarto now supports the specification of embedded Markdown content in tables. This is done by providing a data attribute `qmd` or `qmd-base64` in an embedded `span` or `div` node. These nodes can appear anywhere that such content is allowed: table headers, footers, cells, captions, etc. For example, consider the following table:

```
<table>
  <caption><span data-qmd="As described in @Lovelace1864, computers are great."></span></caption>
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

The `span` nodes with the `data-qmd` attribute will be processed as embedded Markdown content. This allows you to embed arbitrary Markdown content in your tables, including citations, videos, etc. One thing to keep in mind is that the content of `data-qmd` needs to be escaped properly. Authors of libraries which generate table outputs should consider using the `data-qmd-base64` attribute, which will be decoded and then processed by Quarto.

## Limitations

Quarto **doesn't** support processing of:

- nested `<table>` elements.
- invalid HTML tables. Make sure your emitted HTML [passes validation](https://validator.w3.org/).


# quarto-web/docs/prerelease/1.3/website-nav.qmd

---
title: Responsive Website Navigation Improvements
---

## Navbar Tools

The navbar can now display a set of tools (e.g. social actions, GitHub view or edit actions, etc.), see [Navbar Tools](/docs/websites/website-navigation.qmd#navbar-tools).

## Responsive Navbar

We've updated the responsive behavior of the navbar to improve the usability of Quarto websites on mobile devices. Changes include:

-   When the items in a navbar collapse into a menu, we've moved the 'hamburger' button which controls the menu to the right side of the navbar. This makes it easier to access the menu on mobile devices.

-   When the items in a navbar collapse into a menu, we place the search icon on right side of the navbar (rather than placing in the collapsed menu). This makes search always available, even when on small screens.

![](images/top-nav.png){.border fig-alt="The top section of a mobile sized Quarto navbar." fig-align="center"}

## Responsive Sidebar

We've updated the responsive behavior of the sidebar to improve the usability of Quarto websites on mobile devices. Changes include:

-   The collapsed sidebar now appears as a vertically smaller band which includes a 'sidebar' icon on the left side. Clicking this icon will expand the sidebar to full width. In addition, this collapsed view includes 'breadcrumbs' for the current page which allow simple navigation up the hierarchy.

-   When revealed, the sidebar will now animate from the side of the screen.

![](images/top-nav-open.png){.border fig-alt="The top section of a mobile sized Quarto navbar with the sidebar fully opened, revealing a sidebar menu." fig-align="center"}


# quarto-web/docs/prerelease/1.3/custom-ast-nodes/callout.qmd

---
title: Quarto Callouts Custom Node API
date: last-modified
search: false
---

In Quarto 1.3, callouts are represented as a custom AST node. You can create callout AST nodes in Lua filters with the `quarto.Callout` constructor. The constructor takes a single parameter, a table with entries `type`, `title`, and `content`, as described below. In Lua filters, callouts are represented as a table with the following fields:

- `type`: the type of callout: `note`, `caution`, `warning`, etc (optional in the constructor).
- `title`: The callout title (if any) (optional in the constructor),
- `icon`: the callout icon (or `false` if none) (optional in the constructor)
- `appearance`: `"minimal"`, `"simple"`, or `"default"` (optional in the constructor)
- `collapse`: whether to render the callout as collapsible (optional in the constructor, default `false`)
- `content`: the content of the callout (a `pandoc.Blocks` object, or a plain list in the constructor)



# quarto-web/docs/prerelease/1.3/custom-ast-nodes/conditional-block.qmd

---
title: Quarto Conditional Blocks Custom Node API
date: last-modified
search: false
---

In Quarto 1.3, conditional blocks are represented as a custom AST node. You can create conditional block AST nodes in Lua filters with the `quarto.ConditionalBlock` constructor. The constructor takes a single parameter, a table with entries `node`, `behavior`, and `condition`, as described below.
In Lua filters, conditional blocks are represented as a table with the following fields:

- `node`: the div containing the content
- `behavior`: either `content-visible` or `content-hidden`
- `condition`: a list of 2-element lists, such as `{ { "unless-format", "html" } }` (optional in the constructor, default value `{}`). The first element of each sublist must be one of `when-format`, `unless-format`, `when-profile`, and `unless-profile`. The second element is the relevant format or profile.



# quarto-web/docs/prerelease/1.3/custom-ast-nodes/tabset.qmd

---
title: Quarto Tabsets Custom Node API
date: last-modified
search: false
---

In Quarto 1.3, tabsets are represented as a custom AST node. You can create conditional blocks in Lua filters with the `quarto.Tabset` constructor, with parameters `tabs`, `level` and `attr` as described above. In
addition, you can use `quarto.Tab` to create the tab objects for the `tabs` field. `quarto.Tab` is more lenient with parameter types, converting strings to `Blocks` and `Inlines` as needed. In Lua filters, tabsets are represented as a table with the following fields:

- `tabs`: a table containing the content for each tab. Each entry is a table with two entries: `title` (a `pandoc.Inlines`) and `content` (a `pandoc.Blocks`) (optional in the contructor, default value `{}`)
- `level`: the level of the tab headings to be used in rendering the tabset (optional in the constructor, default value `2`)
- `attr`: the `Attr` object for the resulting tabset div (optional in the constructor)




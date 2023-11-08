# quarto-web/bug-reports.qmd

---
title: "Bug Reports"
subtitle: "How to make an actionable bug report for Quarto"
---

We want to hear about Quarto bugs and, we want to fix those bugs! The following guidance will help us be as efficient as we can.

### Rule 0: Please submit your bug report anyway!

We have a better chance to fix your code quickly if you follow the instructions below. Still, we know that this takes work and isn't always possible.

**We would rather have a record of the problem than not know about it**.

We appreciate bug reports even if you are unable to take any or all of the following steps:

### Small is beautiful: Aim for a single document with \~10 lines

The most helpful thing you can do to help us is to provide a minimal, self-contained, and reproducible example.

-   **minimal**: This will often mean turning your large website project into a project with a single small document, and a single large `.qmd` file into a small (ideally, about 10-20 total lines of code) example. By doing this, you might also be able to learn more specifically what the problem is.
-   **self-contained**: The more software dependencies we need to understand and install, the harder it is to track the bug down. As you reduce the code, remove as many dependencies as possible.
-   **reproducible**: If we cannot run your example, we cannot track the bug down. Please make sure the file you submitted is enough to trigger the bug on its own.

## Formatting: Make GitHub's markdown work for us

The easiest way to include a `.qmd` file in a comment is to wrap it in a code block. To make sure that GitHub doesn't format your own `.qmd`, start and end your block with more backticks than you use in your `.qmd` file. In order to show `.qmd` files with three backticks (the most common case), use *four* backticks in your GitHub Issue:

    ```
    This is a code block
    ```

Sometimes you might need more backticks:

    ````
    This is a four backticks block.

    ```
    This is a code block
    ```
    ````

### Don't hold back: Tell us anything you think might make a difference

Although we want the `.qmd` file to be small, we still can use as much information from you as you're willing to share. Tell us all!, including:

-   The version of quarto you're running
-   The operating system you're running
-   The IDE you're using, and its version

If you are seeing an error from Quarto, you can also provide additional diagnostic information by defining the `QUARTO_PRINT_STACK` environment variable. 

For example on Unix: 

```bash
export QUARTO_PRINT_STACK=true
quarto render document.qmd
```

or on Windows in a Powershell Terminal

```powershell
$ENV:QUARTO_PRINT_STACK="true"
quarto render document.qmd
```


# quarto-web/trademark.qmd

---
title: "Trademark Policy"
---

::: {.callout-note appearance="simple"}
This policy is adapted directly from the WordPress Foundation's [trademark policy](https://wordpressfoundation.org/trademark-policy/) for the WordPress and WordCamp names and logos. We admire the job that WordPress has done building a thriving open source community while at the same time making possible a wide variety of WordPress related businesses. We hope that this policy will help us do the same for Quarto.
:::

## Goals

[Posit, PBC](https://www.posit.co/about/) owns and oversees the trademark for the Quarto name and logo. We have developed this trademark usage policy with the following goals in mind:

1.  We'd like to make it easy for anyone to use the Quarto name or logo for community-oriented efforts that help spread and improve Quarto.

2.  We'd like to make it clear how Quarto-related businesses and projects can (and cannot) use the Quarto name and logo.

3.  We'd like to make it hard for anyone to use the Quarto name and logo to unfairly profit from, trick or confuse people who are looking for official Quarto resources.

Please note that it is not the goal of this policy to limit open source or commercial activity around Quarto. We actively encourage Quarto-based open source projects and businesses---our goal with this policy is to prevent confusion about the source of Quarto related software and services.

## Permission

Permission from Posit is required to use the Quarto name or logo as part of any project, product, service, domain name, or company name.

We will grant permission to use the Quarto name and logo for projects that meet the following criteria:

-   The primary purpose of your project is to promote the spread and improvement of the Quarto software.

-   Your project is non-commercial in nature (it can make money to cover its costs or contribute to non-profit entities, but it cannot be run as a for-profit project or business).

-   Your project neither promotes nor is associated with entities that currently fail to comply with the GPL license under which Quarto is distributed.

If your project meets these criteria, you will be permitted to use the Quarto name and logo to promote your project in any way you see fit with these exceptions: (1) Please do not use Quarto as part of a domain name; and (2) We do not allow the use of the trademark in advertising, including AdSense/AdWords.

All other Quarto-related businesses or projects can use the Quarto name and logo to refer to and explain their services, but they cannot use them as part of a product, project, service, domain name, or company name and they cannot use them in any way that suggests an affiliation with or endorsement by the Quarto open source project.

The abbreviation "QMD" is not covered by the Quarto trademark and you are free to use it in any way you see fit.

## Examples

A consulting company can describe its business as "123 Publishing Services, offering Quarto consulting for publishers," but cannot call its business "The Quarto Consulting Company." Similarly, a business related to Quarto extensions can describe itself as "XYZ Extensions, the world's best Quarto extensions," but cannot call itself "The Quarto Extension Portal."

Similarly, it's OK to use the Quarto logo as part of a page that describes your products or services, but it is not OK to use it as part of your company or product logo or branding itself. Under no circumstances is it permitted to use Quarto as part of a domain name or top-level domain name.

When in doubt about your use of the Quarto name or logo, please contact Posit at [permissions\@rstudio.com](mailto:permissions@rstudio.com) for clarification.


# quarto-web/index.qmd

---
pagetitle: "Quarto"
page-layout: custom
section-divs: false
toc: false
css: index.css
editor: source
description: | 
  An open source technical publishing system for creating beautiful articles, websites, blogs, books, slides, and more. Supports Python, R, Julia, and JavaScript.
hide-description: true
image: quarto-dark-bg.jpeg
resources: 
  - images/hero_animation.mp4
---

::: {.hero-banner}


::: {.content-block}

::: {.hero-text}
# Welcome to Quarto^[®]{.trademark}^ {.mt-1}

### An open-source scientific and technical publishing system

- Author using [Jupyter](https://jupyter.org) notebooks or with plain text markdown in your favorite editor.
- Create dynamic content with [Python](docs/computations/python.qmd), [R](docs/computations/r.qmd), [Julia](docs/computations/julia.qmd), and [Observable](docs/computations/ojs.qmd).
- Publish reproducible, production quality articles, presentations, dashboards, websites, blogs, and books in HTML, PDF, MS Word, ePub, and more.
- Share knowledge and insights organization-wide by publishing to [Posit Connect](https://quarto.org/docs/publishing/rstudio-connect.html), [Confluence](docs/publishing/confluence.qmd), or other publishing systems. 
- Write using [Pandoc](https://pandoc.org) markdown, including equations, citations, crossrefs, figure panels, callouts, advanced layout, and more.

### Analyze. Share. Reproduce. You have a story to tell with data---tell it with Quarto.

::: {.hero-buttons}
[Get Started](docs/get-started/){.btn-action-primary .btn-action .btn .btn-success .btn-lg role="button"}
[Guide](docs/guide/){#btn-guide .btn-action .btn .btn-info .btn-lg role="button"}
::: 
:::

::: {.hero-animation}

<video autoplay muted playsinline loop>
<source src="images/hero_animation.mp4" type="video/mp4"/>
</video>
:::

:::


:::


::: {.hello-quarto .alt-background}
::: {.content-block}

::: {.hello-quarto-banner}
# Hello, Quarto 
<ul class="nav nav-pills" id="hello-quarto-tab" role="tablist">
  <li class="nav-item" role="presentation">
    <button class="nav-link active" id="python-tab" data-bs-toggle="tab" data-bs-target="#python" type="button" role="tab" aria-controls="python" aria-selected="true">Python</button>
  </li>
  <li class="nav-item" role="presentation">
    <button class="nav-link" id="knitr-tab" data-bs-toggle="tab" data-bs-target="#knitr" type="button" role="tab" aria-controls="knitr" aria-selected="false">R</button>
  </li>
  <li class="nav-item" role="presentation">
    <button class="nav-link" id="julia-tab" data-bs-toggle="tab" data-bs-target="#julia" type="button" role="tab" aria-controls="julia" aria-selected="false">Julia</button>
  </li>
  <li class="nav-item" role="presentation">
    <button class="nav-link" id="observable-tab" data-bs-toggle="tab" data-bs-target="#observable" type="button" role="tab" aria-controls="observable" aria-selected="false">Observable</button>
  </li>
</ul>
:::

<div class="tab-content" id="hello-quarto-tabcontent">

<div class="tab-pane fade  show active" id="python" role="tabpanel" aria-labelledby="python-tab">

Combine Jupyter notebooks with flexible options to produce production quality output in a wide variety of formats. Author using traditional notebook UIs or with a plain text markdown representation of notebooks.

::: {.grid}
::: {.g-col-lg-6 .g-col-12}
![](images/demo-jupyter-plain.png){.hello-output fig-alt="Example Jupyter notebook entitled Palmer Penguins with code cells, text, and a scatterplot." height="605"}
:::

::: {.g-col-lg-6 .g-col-12 style="background-color: white; border: 1px solid #dee2e6; height: 605px;"}
![](images/demo-jupyter-output.png){fig-alt="Output of example Jupyter notebook, Palmer Penguins, in HTML showing title, metadata, text, code, and scatterplot. At the top there is a dropdown option to show or hide the code."}
:::
:::

</div>

<div class="tab-pane fade" id="knitr" role="tabpanel" aria-labelledby="knitr-tab">

Quarto is a multi-language, next generation version of R Markdown from Posit, with many new new features and capabilities. Like R Markdown, Quarto uses [knitr](https://yihui.org/knitr/) to execute R code, and is therefore able to render most existing Rmd files without modification.

::: {.grid}
::: {.g-col-lg-6 .g-col-12}
````markdown
---
title: "ggplot2 demo"
author: "Norah Jones"
date: "5/22/2021"
format: 
  html:
    fig-width: 8
    fig-height: 4
    code-fold: true
---

## Air Quality

@fig-airquality further explores the impact of temperature on ozone level.

```{{r}}
#| label: fig-airquality
#| fig-cap: "Temperature and ozone level."
#| warning: false

library(ggplot2)
ggplot(airquality, aes(Temp, Ozone)) + 
  geom_point() + 
  geom_smooth(method = "loess")
```


````
:::

::: {.g-col-lg-6 .g-col-12}
![](images/hello-knitr.png){.hello-output fig-alt="Example output with title (ggplot2 demo), author (Norah Jones), and date (5/22/2021). Below is a header reading Air Quality followed by body text (Figure 1 further explores the impact of temperature on ozone level.) with a toggleable code field, and figure with caption Figure 1 Temperature and ozone level."}
:::
:::

</div>

<div class="tab-pane fade" id="julia" role="tabpanel" aria-labelledby="julia-tab">

Combine markdown and Julia code to create dynamic documents that are fully reproducible. Quarto executes Julia code via the [IJulia](https://github.com/JuliaLang/IJulia.jl) Jupyter kernel, enabling you to author in plain text (as shown below) or render existing Jupyter notebooks.

::: {.grid}
::: {.g-col-lg-6 .g-col-12}
````markdown
---
title: "Plots Demo"
author: "Norah Jones"
date: "5/22/2021"
format:
  html:
    code-fold: true
jupyter: julia-1.8
---

## Parametric Plots

Plot function pair (x(u), y(u)). 
See @fig-parametric for an example.

```{{julia}}
#| label: fig-parametric
#| fig-cap: "Parametric Plots"

using Plots

plot(sin, 
     x->sin(2x), 
     0, 
     2π, 
     leg=false, 
     fill=(0,:lavender))
```


````
:::

::: {.g-col-lg-6 .g-col-12}
![](images/hello-julia.png){.hello-output fig-alt="Example Plots Demo output with title, author, date published and main section on Parametric plots which contains text, a toggleable code field, and the output of the plot, with the caption Figure 1 Parametric Plots."}
:::
:::

</div>

<div class="tab-pane fade" id="observable" role="tabpanel" aria-labelledby="observable-tab">

Quarto includes native support for Observable JS, a set of JavaScript enhancements created by Mike Bostock (the author of D3). Observable JS uses a reactive execution model, and is especially well suited for interactive data exploration and analysis.



::: {.grid}
::: {.g-col-lg-6 .g-col-12}
````markdown
---
title: "observable plot"
author: "Norah Jones"
format: 
  html: 
    code-fold: true
---

## Seattle Precipitation by Day (2012 to 2016)

```{{ojs}}
data = FileAttachment("seattle-weather.csv")
  .csv({typed: true})
  
Plot.plot({
  width: 800, height: 500, padding: 0,
  color: { scheme: "blues", type: "sqrt"},
  y: { tickFormat: i => "JFMAMJJASOND"[i] },
  marks: [
    Plot.cell(data, Plot.group({fill: "mean"}, {
      x: d => new Date(d.date).getDate(),
      y: d => new Date(d.date).getMonth(),
      fill: "precipitation", 
      inset: 0.5
    }))
  ]
})
```
````
:::


::: {.g-col-lg-6 .g-col-12}
![](images/hello-observable.png){style="background-color: white; border: 1px solid #dee2e6; height: 625px;" fig-alt="Example output with title, author, and date. Below, the main section reads Seattle Precipitation by Day (2012 to 2016) with a toggleable section to show code and a heatmap of the precipitation by day."}
:::


:::

</div>

</div>



::: {.grid}


:::
:::
:::


::: {.content-block}
::: {.features}

::: {.feature}
### Dynamic Documents
Generate dynamic output using Python, R, Julia, and Observable. Create reproducible documents that can be regenerated when underlying assumptions or data change.

::: {.learn-more}
[Learn more »](docs/computations/python.qmd)
:::
:::

::: {.feature}
### Beautiful Publications
Publish high-quality articles, reports, presentations, websites, and books in HTML, PDF, MS Word, ePub, and more. Use a single source document to target multiple formats.

::: {.learn-more}
[Learn more »](docs/output-formats/all-formats.qmd)
:::
:::

::: {.feature}
### Scientific Markdown
Pandoc markdown has excellent support for LaTeX equations and citations. Quarto adds extensions for cross-references, figure panels, callouts, advanced page layout, and more.

::: {.learn-more}
[Learn more »](docs/authoring/markdown-basics.qmd)
:::
:::

::: {.feature}
### Authoring Tools
Use your favorite tools including VS Code, RStudio, Jupyter Lab, or any text editor. Use the Quarto visual markdown editor for long-form documents.

::: {.learn-more}
[Learn more »](docs/tools/jupyter-lab.qmd)
:::
:::

::: {.feature}
### Interactivity
Engage readers by adding interactive data exploration to your documents using Jupyter Widgets, htmlwidgets for R, Observable JS, and Shiny.

::: {.learn-more}
[Learn more »](docs/interactive/)
:::
:::

::: {.feature}
### Websites and Books
Publish collections of documents as a blog or full website. Create books and manuscripts in both print formats (PDF and MS Word) and online formats (HTML and ePub).

::: {.learn-more}
[Learn more »](docs/websites/)
:::
:::

:::
:::


::: {.get-started .alt-background}
::: {.content-block}

[Get Started](docs/get-started/index.html){.btn-action-primary  .btn-action .btn .btn-success .btn-lg role="button" style="margin-top: 1em;"}

:::
:::



# quarto-web/about.qmd

---
title: "About Quarto"
subtitle: "Open source tools for scientific and technical publishing"
---

## Goals

The overarching goal of Quarto is to make the process of creating and collaborating on scientific and technical documents dramatically better. We hope to do this in several dimensions:

-   Create a writing and publishing environment with great integrated tools for technical content. We want to make authoring with embedded code, equations, figures, complex diagrams, interactive widgets, citations, cross references, and the myriad other special requirements of scientific discourse straightforward and productive for everyone.

-   Help authors take full advantage of the web as a connected, interactive platform for communications, while still providing the ability to create excellent printed output from the same document source. Researchers shouldn't need to choose between LaTeX, MS Word, and HTML but rather be able to author documents that target all of them at the same time.

-   Make reproducible research and publications the norm rather than the exception. Reproducibility requires that the code and data required to create a manuscript are an integrated part of it. However, this isn't often straightforward in practice---Quarto aims to make it easier to adopt a reproducible workflow than not.

Quarto is open source software licensed under the [GNU GPL v2](license.qmd). We believe that it's better for everyone if the tools used for research and science are free and open. Reproducibility, widespread sharing of knowledge and techniques, and the leveling of the playing field by eliminating cost barriers are but a few of the shared benefits of free software in science.

## Project

At the core of Quarto is [Pandoc](https://pandoc.org), a powerful and flexible document processing tool. Quarto adds a number of facilities to Pandoc aimed at scientific and technical publishing, including:

1.  Embedding code and output from Python, R, and JavaScript via integration with [Jupyter](https://jupyter.org/), [Knitr](https://yihui.org/knitr/), and [Observable](https://github.com/observablehq/).

2.  A variety of extensions to Pandoc markdown useful for technical writing including cross-references, sub-figures, layout panels, hoverable citations and footnotes, callouts, and more.

3.  A project system for rendering groups of documents at once, sharing options across documents, and producing aggregate output like [websites](docs/websites/website-basics.qmd) and [books](docs/books/book-basics.qmd).

Development of Quarto is sponsored by [Posit, PBC](https://www.posit.co), where we previously created a similar system ([R Markdown](https://rmarkdown.rstudio.com/)) that shared the same goals, but was targeted principally at users of the R language. The same core team works on both Quarto and R Markdown:

-   J.J. Allaire ([\@jjallaire](https://github.com/jjallaire/))
-   Christophe Dervieux ([\@cderv](https://github.com/cderv))
-   Carlos Scheidegger ([\@cscheid](https://github.com/cscheid))
-   Charles Teague ([\@dragonstyle](https://github.com/dragonstyle))
-   Yihui Xie ([\@yihui](https://github.com/yihui))

With Quarto, we are hoping to bring these tools to a much wider audience.

Quarto is a registered trademark of Posit. Please see our [trademark policy](trademark.qmd) for guidelines on usage of the Quarto trademark.

## Contribute

You can contribute to Quarto in many ways:

-   By opening issues to provide feedback and share ideas.
-   By submitting Pull Request (PR) to fix opened issues
-   By submitting Pull Request (PR) to suggest new features (it is considered good practice to open an issue for discussion before working on a pull request for a new feature).

Please be mindful of our [code of conduct](https://github.com/quarto-dev/quarto-cli/blob/main/.github/CODE_OF_CONDUCT.md) as you interact with other community members.

### Pull Requests {.unlisted}

Pull requests are very welcome! Here's how to contribute via PR:

1.  [Fork](https://github.com/quarto-dev/quarto-cli/fork) the repository, clone it locally, and make your changes in a new branch specific to the PR. For example:

    ``` {.bash filename="Terminal"}
    # clone your fork
    $ git clone https://github.com/<username>/quarto-cli

    # configure for your platform (./configure.sh or ./configure.cmd for windows)
    $ cd quarto-cli
    $ ./configure.sh

    # checkout a new branch
    $ git checkout -b feature/newthing
    ```

2.  For significant changes (e.g more than small bug fixes), ensure that you have signed the [individual](https://posit.co/wp-content/uploads/2023/04/2023-03-13_TC_Indiv_contrib_agreement.pdf) or [corporate](https://posit.co/wp-content/uploads/2023/04/2023-03-13_TC_Corp_contrib_agreement.pdf) contributor agreement as appropriate. You can send the signed copy to [jj\@rstudio.com](mailto:jj@rstudio.com){.email}.

3.  Submit the [pull request](https://help.github.com/articles/using-pull-requests). It is ok to submit as draft in your are still working on it but would like some feedback from us. It always good to share in the open that you are working on it.

We'll try to be as responsive as possible in reviewing and accepting pull requests.


# quarto-web/license.qmd

---
title: "Open Source License"
---

Quarto is open source software licensed under the [GNU GPL v2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html). We believe that it's better for everyone if the tools used for research and science are free and open. Reproducibility, widespread sharing of knowledge and techniques, and the leveling of the playing field by eliminating cost barriers are but a few of the shared benefits of free software in science.

The Quarto source code is available at <https://github.com/quarto-dev/>

Quarto is a registered trademark of Posit. Please see our [trademark policy](trademark.qmd) for guidelines on usage of the Quarto trademark.

Quarto also makes use of several other open-source projects, the distribution of which is subject to their respective licenses. Major components and their licenses include:

| Project                                                       | License                                                            |
|---------------------------------------------------------------|--------------------------------------------------------------------|
| [Pandoc](https://pandoc.org/)                                 | [GNU GPL v2](https://github.com/jgm/pandoc/blob/master/COPYING.md) |
| [Bootstrap 5.1](https://getbootstrap.com/docs/5.1/)           | [MIT](https://github.com/twbs/bootstrap/blob/v5.1.3/LICENSE)       |
| [Bootswatch 5.1](https://bootswatch.com/)                     | [MIT](https://github.com/thomaspark/bootswatch/blob/v5/LICENSE)    |
| [Deno](https://deno.land/)                                    | [MIT](https://github.com/denoland/deno/blob/main/LICENSE.md)       |
| [esbuild](https://esbuild.github.io/)                         | [MIT](https://github.com/evanw/esbuild/blob/master/LICENSE.md)     |
| [Dart Sass](https://sass-lang.com/dart-sass)                  | [MIT](https://github.com/sass/dart-sass/blob/main/LICENSE)         |
| [Observable Runtime](https://github.com/observablehq/runtime) | [ISC](https://github.com/observablehq/runtime/blob/main/LICENSE)   |


# quarto-web/docs/_require-1.3.qmd

::: {.callout-note}
## Quarto 1.3 Feature

This feature is new in Quarto 1.3, which you can download at <https://quarto.org/docs/download/>
:::

# quarto-web/docs/guide/index.qmd

---
title: "Guide"
subtitle: Comprehensive guide to using Quarto. If you are just starting out, you may want to  explore the [tutorials](../get-started/index.qmd) to learn the basics.
page-layout: article
anchor-sections: false
search: false
listing:
  id: guide-links
  template: ../../ejs/links.ejs
  contents: guide.yml
image: /images/hero_right.png
---

::: {#guide-links .column-screen-inset-right style="max-width: 850px;"}
:::


# quarto-web/docs/publishing/netlify.qmd

---
title: "Netlify"
provider: netlify
provider-name: Netlify
provider-token: NETLIFY_AUTH_TOKEN
provider-publish-url: "https://tubular-unicorn-97bb3c.netlify.app"
---

## Overview

[Netlify](https://www.netlify.com/) is a professional web publishing platform with support for many advanced features including custom domains, authentication, branch previews, and instant rollbacks. Netlify also has a free plan that is ideal for personal projects, hobby sites, or experiments.

There are several ways to publish Quarto content to Netlify:

1.  Use the `quarto publish` command to publish content rendered on your local machine.

2.  If you are using GitHub, GitLab, Bitbucket, or Azure DevOps, you can point Netlify at your site's source code and have it deployed whenever your code changes.

3.  If you are using GitHub, you can use a [GitHub Action] to automatically render your project and publish the resulting content whenever your code changes.

4.  If you are using another Continuous Integration (CI) service, you can script the `quarto publish` command to render and publish content to Netlify.

We'll cover each of these methods below, starting with the most straightforward and then proceeding to more sophisticated scenarios.

{{< include _publish-command.md >}}

### Domain Name

The domain name for your published site will by default use a random identifier (e.g. `mystifying-jepsen-fa4396.netlify.app`). You can pick a more descriptive sub-domain (still using `netlify.app` as the main domain) or if you own another domain, assign that one to the site. These options are available (respectively) from the **Site settings** and **Domain settings** panels:

![](images/netlify-control-panel.png)

Within **Site settings**, click the **Change site name** button to specify a different sub-domain:

![](images/netlify-site-settings.png)

If you own another domain that you want to use for your site, follow the directions in **Domain settings**.

## Publish from Git Provider

Netlify has the ability to automatically deploy sites when changes are committed to Git repositories hosted on GitHub, GitLab, Bitbucket, and Azure DevOps. The most straightforward approach to this is to check your rendered site (i.e. the `_site` or `_book` directory) into version control and have Netlify deploy that. We'll cover that scenario first and then explore using a Netlify Build Plugin to render the site on Netlify servers.

### Importing a Project

Start by going to the main Netlify page for your team, choosing **Add new site,** and then **Import an existing project**:

![](images/netlify-import-project.png)

You'll be prompted to authenticate with your version control provider, select a repository, and then finally specify the configuration for publishing the site.

### Publishing Configuration

The build settings for our project will have no **Build command** and will specify `_site` or `_book` (as appropriate) for the **Publish directory**:

![](images/netlify-build-settings.png){.border}

If you have your `_site` or `_book` directory checked into version control then everything is now configured and your site will be deployed to Netlify automatically whenever you commit to your repository.

### Rendering on Netlify

If you prefer not to check your rendered site into version control, you can also use the Quarto [Netlify Build Plugin](https://github.com/quarto-dev/netlify-plugin-quarto) to render on a Netlify build server (note that Netlify servers can only render markdown and cannot execute R, Python, or Julia code).

#### Freezing Computations

{{< include _freeze-basics.md >}}

#### Ignoring Output

{{< include _ignoring-output.md >}}

#### Plugin Configuration

To use the Quarto Netlify Build Plugin, add the following two files to your project:

``` {.toml filename="netlify.toml"}
[[plugins]]
package = "@quarto/netlify-plugin-quarto"
```

``` {.json filename="package.json"}
{
  "dependencies": {
    "@quarto/netlify-plugin-quarto": "^0.0.5"
  }
}
```

Now, commit and push your modified project (including `_freeze`, `netlify.toml`, and `package.json`). Assuming that you configured the project correctly in the previous step (i.e. **Publish directory** set to the `_site` or `_book` directory) then Netlify will begin rendering and publishing your site each time you push a new commit.

## GitHub Action

{{< include _github-action-basics.md >}}

``` {.yaml filename=".github/workflows/publish.yml"}
on:
  workflow_dispatch:
  push:
    branches: main

name: Quarto Publish

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4 

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2

      - name: Render and Publish 
        uses: quarto-dev/quarto-actions/publish@v2
        with:
          target: {{< meta provider >}}
          NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
```

### Netlify Credentials

The final step is to configure your GitHub Action with the credentials required for publishing to Netlify. To to this you need to create a Netlify personal access token and then configure your GitHub action to be able to read it:

1.  If you don't already have an access token, go to the Netlify [applications page](https://app.netlify.com/user/applications), and click on **New Access Token** to create a new personal access token. Give this token a memorable name, and copy the token to the clipboard.

2.  Add the Netlify personal access token to your repository's action **Secrets** (accessible within repository **Settings**). You will see a **New repository secret** button at the top right:

    ![](images/gh-new-repository-secret.png){.border}

    Click the button and add the personal access token from step 1 as a secret named `NETLIFY_AUTH_TOKEN`:

    ![](images/netlify-gh-action-secret.png){.border}

### Ignoring Output

{{< include _ignoring-output.md >}}

### Commit to Publish

Once you've specified your publishing action and Netlify credentials, and pushed your updated repository (including the `_freeze` directory) to GitHub, your action will run with this and subsequent commits, automatically rendering and publishing to Netlify.

{{< include _github-action-executing-code.md >}}

#### Example: Jupyter with venv

Here is a complete example of a GitHub Action that installs Python, Jupyter, and package dependencies from `requirements.txt`, then executes code and renders output to Netlify:

``` {.yaml filename=".github/workflows/publish.yml"}
on:
  workflow_dispatch:
  push:
    branches: main

name: Quarto Publish

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4 

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2
        
      - name: Install Python and Dependencies
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
          cache: 'pip'
      - run: pip install jupyter
      - run: pip install -r requirements.txt
      
      - name: Render and Publish 
        uses: quarto-dev/quarto-actions/publish@v2
        with:
          target: {{< meta provider >}}
          NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
```

#### Example: Knitr with renv

Here is a complete example of a GitHub Action that installs R and package dependencies from `renv.lock`, then executes code and renders output to Netlify:

``` {.yaml filename=".github/workflows/publish.yml"}
on:
  workflow_dispatch:
  push:
    branches: main

name: Quarto Publish

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4 

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2
        
      - name: Install R
        uses: r-lib/actions/setup-r@v2
        with:
          r-version: '4.2.0'
      
      - name: Install R Dependencies 
        uses: r-lib/actions/setup-renv@v2
        with:
          cache-version: 1
      
      - name: Render and Publish
        uses: quarto-dev/quarto-actions/publish@v2
        with:
          target: {{< meta provider >}}
          NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
```

### Additional Options

It's possible to have a Quarto project in a larger GitHub repository, where the Quarto project does not reside at the top-level directory. In this case, add a `path` input to the invocation of the `publish` action. For example:

``` yaml
- name: Render and Publish
  uses: quarto-dev/quarto-actions/publish@v2
  with:
    target: {{< meta provider >}}
    path: subdirectory-to-use
    NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
```

By default, `quarto publish` will re-render your project before publishing it. However, if you store the rendered output in version control, you don't need the GitHub action to re-render the project. In that case, add the option `render: false` to the `publish` action:

``` yaml
- name: Render and Publish
  uses: quarto-dev/quarto-actions/publish@v2
  with:
    target: {{< meta provider >}}
    render: false
    NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
```

## Continuous Integration

You can publish Quarto content to Netlify using any CI service by scripting the `quarto publish` command.

{{< include _netlify-ci-example.md >}}

See the article on [Publishing with CI](ci.qmd) for additional details on the various approaches to rendering and publishing with Continuous Integration.


# quarto-web/docs/publishing/github-pages.qmd

---
title: "GitHub Pages"
editor: visual
provider: gh-pages
provider-token: GITHUB_TOKEN
---

## Overview

[GitHub Pages](https://pages.github.com/) is a website hosting service that enables you to publish content based on source code managed within a GitHub repository.

There are three ways to publish Quarto websites and documents to GitHub Pages:

1.  Render sites on your local machine to the `docs` directory, check the rendered site into GitHub, and then configure your GitHub repo to publish from the `docs` directory.

2.  Use the `quarto publish` command to publish content rendered on your local machine.

3.  Use a [GitHub Action] to automatically render your files (a single Quarto document or a Quarto project) and publish the resulting content whenever you push a source code change to your repository.

We'll cover each of these methods below, but first an important pre-requisite: you need to have a Git repository on your local machine that is synced to GitHub. The URL of the published website will be derived from the combination of your username and the repository name (e.g. `https://username.github.io/reponame/`).

You can optionally configure a [custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages) for a GitHub Pages site, but before exploring that ground you should get your site up and running with the default domain.

## Render to `docs` {#render-to-docs}

The simplest way to publish using GitHub Pages is to render to the `docs` directory and then check that directory into your repository. If you prefer not to check rendered output into version control see the discussion of using [Publish Command](#publish-command) below.

To get started, change your project configuration to use `docs` as the `output-dir`. For example:

``` {.yaml filename="_quarto.yml"}
project:
  type: website
  output-dir: docs
```

Then, add a `.nojekyll` file to the root of your repository that tells GitHub Pages not to do additional processing of your published site using Jekyll (the GitHub default site generation tool):

+---------------+---------------------------------+
| Mac/Linux     | ``` {.bash filename="Terminal"} |
|               | touch .nojekyll                 |
|               | ```                             |
+---------------+---------------------------------+
| Windows       | ``` {.bash filename="Terminal"} |
|               | copy NUL .nojekyll              |
|               | ```                             |
+---------------+---------------------------------+

Now, render your site and push it to GitHub:

``` {.bash filename="Terminal"}
quarto render
git push
```

Finally, configure your GitHub repository to publish from the `docs` directory of your `main` branch:

![](images/gh-pages-docs-dir.png){.border}

Once you've made this configuration change GitHub will trigger a deployment of your website. Your site will also be updated whenever you commit and push to `main`.

## Publish Command {#publish-command}

The `quarto publish` command is an easy way to publish locally rendered documents and websites. Before attempting to use `quarto publish` (either locally or from a GitHub Action) you should be sure to configure the [Source Branch](#source-branch) and [Ignore Output](#ignoring-output) as described below.

### Source Branch {#source-branch}

Before attempting to publish you should ensure that the **Source** branch for your repository is `gh-pages` and that the site directory is set to the repository root (`/`). You can modify these options in **Settings** : **Pages** for your repository. For example, if you already have a `gh-pages` branch:

![](images/gh-pages-user-site.png){.border}

If you do not already have a `gh-pages` branch, you can create one as follows. First, make sure you have committed all changes to your current working branch with `git status`. Then:

``` {.bash filename="Terminal"}
git checkout --orphan gh-pages
git reset --hard # make sure all changes are committed before running this!
git commit --allow-empty -m "Initialising gh-pages branch"
git push origin gh-pages
```

Double-check that the last `git push` action has indeed set the **Settings** : **Pages** for your repository as expected in the previous figure. Get back to your original repository branch with, for example, `git checkout main`.

### Ignoring Output {#ignoring-output}

{{< include _ignoring-output.md >}}

### Publishing

Once you have configured the source branch and updated your `.gitignore`, navigate to the directory where your project / git repository is located, make sure you are not on the `gh-pages` branch, and execute the `quarto publish` command for GitHub Pages:

``` {.bash filename="Terminal"}
quarto publish gh-pages
```

The publish command will confirm that you want to publish, render your content, copy the output to a special `gh-pages` branch, push that branch to GitHub, and then open a browser to view your site once it is deployed.

#### Private Sites

If you are publishing to a private (i.e. password protected) website then the logic within `quarto publish`that waits for your site to be available before opening a browser won't work correctly. In this case you should pass the `--no-browser` option to bypass this:

``` {.bash filename="Terminal"}
quarto publish gh-pages --no-browser
```

#### Documents

To publish a document rather than a website or book, provide the path to the document (note that you can publish only one document from a given GitHub repository):

``` {.bash filename="Terminal"}
quarto publish gh-pages document.qmd
```

#### Options

Here are all of the available command line options for `quarto publish gh-pages`:

{{< include _cli-options.md >}}

### GitHub Action

Using the `quarto publish {{< meta provider >}}` command to publish locally rendered content is the most simple and straightforward way to publish. Another option is to use [GitHub Actions](https://docs.github.com/en/actions) to render and publish your site (you might prefer this if you want execution and/or rendering to be automatically triggered from commits).

There are a few different ways to approach rendering and publishing content. Below, we'll provide a how-to guide for publishing with GitHub Actions. For more conceptual background on the various approaches, see the discussion on [Rendering for CI](ci.qmd#rendering-for-ci).

#### Freezing Computations

{{< include _freeze-basics.md >}}

Note that an alternative approach is to execute the code as part of the GitHub Action. For now we'll keep things simpler by executing code locally and storing the computations by using freeze. Then, further below, we'll cover [Executing Code](#executing-code) within a GitHub Action.

#### Publish Action

Before configuring the publishing action, it's important that you run `quarto publish gh-pages` locally, once. This will create the `_publish.yml` configuration required by the subsequent invocations of the GitHub Action. To do this, run the following from within your project:

``` bash
quarto publish gh-pages
```

Once you've completed a local publish, add a `publish.yml` GitHub Action to your project by creating this YAML file and saving it to `.github/workflows/publish.yml`:

``` {.yaml filename=".github/workflows/publish.yml"}
on:
  workflow_dispatch:
  push:
    branches: main

name: Quarto Publish

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2

      - name: Render and Publish
        uses: quarto-dev/quarto-actions/publish@v2
        with:
          target: {{< meta provider >}}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

This action will run whenever you push to the `main` branch of your repository. It will also run when you manually trigger the action from the **Actions** tab of your repository. The action will render your content and publish it to GitHub Pages, thus you need to ensure that GitHub Actions has permission to write to your repository. This is done by checking the **Read and write permissions** box under **Workflow permissions** in the **Actions** section of your repository **Settings**.

Once you've done this, check all of the newly created files (including the `_freeze` directory) into your repository and then push to GitHub. A GitHub Pages site will be created for your repository, and every time you push a new change to the repository it will be automatically rebuilt to reflect the change. Consult the **Pages** section of your repository **Settings** to see what the URL and publish status for your site is.

{{< include _github-action-executing-code.md >}}

#### Example: Jupyter with venv

Here is a complete example of a GitHub Action that installs Python, Jupyter, and package dependencies from `requirements.txt`, then executes code and renders output to GitHub Pages:

``` {.yaml filename=".github/workflows/publish.yml"}
on:
  workflow_dispatch:
  push:
    branches: main

name: Quarto Publish

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2

      - name: Install Python and Dependencies
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
          cache: 'pip'
      - run: pip install jupyter
      - run: pip install -r requirements.txt

      - name: Render and Publish
        uses: quarto-dev/quarto-actions/publish@v2
        with:
          target: gh-pages
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

#### Example: Knitr with renv

Here is a complete example of a GitHub Action that installs R and package dependencies from `renv.lock`, then executes code and renders output to GitHub Pages:

``` {.yaml filename=".github/workflows/publish.yml"}
on:
  workflow_dispatch:
  push:
    branches: main

name: Quarto Publish

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2

      - name: Install R
        uses: r-lib/actions/setup-r@v2
        with:
          r-version: '4.2.0'

      - name: Install R Dependencies
        uses: r-lib/actions/setup-renv@v2
        with:
          cache-version: 1

      - name: Render and Publish
        uses: quarto-dev/quarto-actions/publish@v2
        with:
          target: gh-pages
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

#### Additional Options

It's possible to have a Quarto project in a larger GitHub repository, where the Quarto project does not reside at the top-level directory. In this case, add a `path` input to the invocation of the `publish` action. For example:

``` yaml
- name: Render and Publish
  uses: quarto-dev/quarto-actions/publish@v2
  with:
    target: {{< meta provider >}}
    path: subdirectory-to-use
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

By default, `quarto publish` will re-render your project before publishing it. However, if you store the rendered output in version control, you don't need the GitHub action to re-render the project. In that case, add the option `render: false` to the `publish` action:

``` yaml
- name: Render and Publish
  uses: quarto-dev/quarto-actions/publish@v2
  with:
    target: {{< meta provider >}}
    render: false
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

See the full definition of the Quarto [publish action](https://github.com/quarto-dev/quarto-actions/blob/main/publish/action.yml) to learn about other more advanced options.

## User Site

In addition to creating sites tied to various repositories, you can also create a user site that is served from your root user domain (e.g. `https://username.github.io`). This is an ideal place to publish a blog or personal home page. To create a user site:

1.  Create a Git repo with the name `username.github.io` (where "username" is your GitHub username) and sync it to your local machine.

2.  Set the **Source** branch for your user site to `gh-pages` as described in [Source Branch](#source-branch).


# quarto-web/docs/publishing/rstudio-connect.qmd

---
title: "Posit Connect"
editor: visual
heading-pad: '#'
---

## Overview

[Posit Connect](https://www.rstudio.com/products/connect/) is a publishing platform for secure sharing of data products within an organization. Use Posit Connect when you want to publish content within an organization rather than on the public internet.

There are several ways to publish Quarto content to Posit Connect:

1.  Use the `quarto publish` command to publish static content rendered on your local machine.

2.  Use the [rsconnect-python](https://docs.rstudio.com/rsconnect-python/) Python package or [quarto](https://quarto-dev.github.io/quarto-r/) R package to publish code for rendering on an Posit Connect server (e.g. for a scheduled report).

3.  Use Connect's support for [Git backed content](https://docs.rstudio.com/connect/user/git-backed/) to automatically re-publish content when code is checked in to a Git repository.

4.  Use a Continuous Integration (CI) service like [Jenkins](https://www.jenkins.io/), [Airflow](https://airflow.apache.org/), or [GitHub Actions](https://docs.github.com/en/actions), to render and publish to Connect.

Each of these options is covered in detail below. If you are just getting started, we strongly recommend using the first approach (`quarto publish`). Then, as your needs evolve, you can consider other more sophisticated options.

## Publish Command

The `quarto publish` command is the easiest way to publish locally rendered content. From the directory where your project is located, execute the `quarto publish` command for Connect:

```{.bash filename="Terminal"}
quarto publish connect
```

If you haven't previously published to Connect you'll be prompted to enter your server's URL:

```{.bash filename="Terminal"}
$ quarto publish connect
 ? Server URL: › 
```

You'll then need to provide a [Connect API Key](https://docs.rstudio.com/connect/user/api-keys/):

```{.bash filename="Terminal"}
$ quarto publish connect
 ? Server URL: › https://connect.example.com/
 ? API Key: › 
```

After authenticating, your content will be rendered and published, and then a browser will open to view its admin page on Connect.

A record of your previous publishes will be stored in a `_publish.yml` file within the project or document directory. This file stores the service, id, and URL of the published content. For example:

``` yaml
- source: project
  connect:
    - id: "3bb5f59f-524a-45a5-9508-77e29a1e8bf0"
      url: "https://connect.example.com/content/3bb5f59f-524a-45a5-9508-77e29a1e8bf0/"
```

Account information is not stored in this file, so it is suitable for checking in to version control and being shared by multiple publishers.

You can customize this behavior of `quarto publish` by providing the following command line options:

{{< include _cli-options.md >}}

To publish a document rather than a website or book, provide the path to the document:

```{.bash filename="Terminal"}
quarto publish connect document.qmd
```

## Publishing with Code

In the preceding example, we rendered content locally and then published it to Connect. In some cases, however, you may want to publish your source code to Connect and then have it rendered on the server (for example, to create a scheduled report that is updated with new data automatically).

The tools for publishing code differ depending on whether you are using the Knitr (R) or Jupyter (Python) engine, so we'll cover them separately below. Note that Quarto must be installed on the Connect server before you attempt to publish with code (this is typically done by an administrator, see the [Quarto Installation](https://docs.rstudio.com/resources/install-quarto/) documentation for additional details).

### Knitr (R)

The [quarto](https://quarto-dev.github.io/quarto-r/) R package includes a set of publishing functions that you can use for publishing Quarto projects with R code to Posit Connect. For example, here we publish a document and a website:

``` r
library(quarto)

quarto_publish_doc(
  "document.qmd", 
  server = "rsc.example.com", 
  account = "njones",
  render = "server"
)

quarto_publish_site(
  server = "rsc.example.com", 
  account = "njones",
  render = "server"
)
```

The `render = "server"` argument is what specifies that you want code rather than just content published.

Note that once you've published for the first time you can update without providing the explicit arguments:

``` r
quarto_publish_site()
```

See the article on [Quarto Publishing from R](https://quarto-dev.github.io/quarto-r/articles/publishing.html) for additional details on using these functions.

#### RStudio IDE

If you are using the RStudio IDE, there is also support for push-button publishing to Posit Connect. Use the publish button <kbd>![](images/publish-button.png){width="23" height="20"}</kbd> from the source editor or viewer pane to publish a document or a website:

![](images/rstudio-publish.png){.border}

See the Connect documentation on [Publishing from the RStudio IDE](https://docs.rstudio.com/connect/user/publishing/) for additional details.

### Jupyter (Python)

The [rsconnect-python](https://docs.rstudio.com/rsconnect-python/) Python package provides a command line interface (CLI) that you can use to publish Quarto documents and websites that use Jupyter to Posit Connect. To use the CLI:

1.  First, install the rsconnect-python package and configure an Posit Connect server for publishing: <https://docs.rstudio.com/connect/user/connecting-cli/>

2.  Then, use the `rsconnect deploy quarto` command from your project directory:

    ```{.bash filename="Terminal"}
    rsconnect deploy quarto
    ```

See the complete documentation on [Publishing Quarto Content](https://docs.rstudio.com/connect/user/publishing-cli-quarto/) for additional details on using the CLI for publishing to Connect.

#### Notebook Plugin

If you are using the classic Jupyter Notebook you can install the [rsconnect-jupyter](https://docs.rstudio.com/rsconnect-jupyter/) notebook plugin to enable push button publishing of Jupyter notebooks:

1.  First, follow the directions in the rsconnect-jupyter [User Guide](https://docs.rstudio.com/rsconnect-jupyter/) to install the plugin.

2.  Then, click the publish button <kbd>![](images/publish-button.png){width="23" height="20"}</kbd>from a notebook you wish to publish. You'll be prompted to configure a Connect server and then be presented with a publishing dialog:

    ![](images/rsconnect-jupyter-usage.png){.border}

See the article on [Publishing Jupyter Notebooks](https://docs.rstudio.com/connect/user/publishing-notebook/) for complete documentation on using the plugin.

## Publishing from Git

Content may be deployed to Posit Connect directly from a remote Git repository. Content will automatically fetch from the associated remote Git repository and re-deploy. This allows for integration with Git-centric workflows and continuous deployment automation.

In order to deploy Git-backed content to Posit Connect you'll follow a two step process:

1.  Create and commit a manifest file (this includes information on the R or Python dependencies required to render your content)

2.  Link Posit Connect to the Git repository

Note that Quarto must be installed on the Connect server before you attempt to publish from Git (this is typically done by an administrator, see the [Quarto Installation](https://docs.rstudio.com/resources/install-quarto/) documentation for additional details).

### Creating a Manifest

Consult the Connect documentation on [Git Backed Content](https://docs.rstudio.com/connect/user/git-backed/) for complete details on creating manifests and checking them in to your repository. To give you a general idea of how this works, here is some sample code that creates a manifest for Knitr and Jupyter projects:

``` r
# write a manifest for a Knitr project
install.packages("rsconnect") # if required
rsconnect::writeManifest()
```

```{.bash filename="Terminal"}
# write a manifest for a Jupyter notebook
pip install rsconnect-python # if required
rsconnect write-manifest notebook MyNotebook.ipynb
```

See the documentation on [Git Backed Content](https://docs.rstudio.com/connect/user/git-backed/) for complete details on creating manifests.

### Connecting a Repository

Connect users must have *at least* the `publisher` role in order to create new content from a Git repository.

On the **Content** page, there is a button near the top labeled **Publish**. Clicking on this button will expand a menu which contains an item called "Import from Git", which may be clicked to launch a new content wizard.

![](images/import-from-git.png)

You'll be prompted to provide your repository URL, branch to publish from, and target directory to publish from (e.g., the one containing your `manifest.json`).

See the documentation on [Git Backed Content](https://docs.rstudio.com/connect/user/git-backed/) for complete details on connecting Git repositories to Connect.

## Continuous Integration

You can also deploy Quarto content using a Continuous Integration (CI) service like [Jenkins](https://www.jenkins.io/), [Airflow](https://airflow.apache.org/), or [GitHub Actions](https://docs.github.com/en/actions). In most cases, this will entail scripting the `quarto publish` command, however in the case of GitHub Actions, you can take advantage of the standard Quarto [publish action](https://github.com/quarto-dev/quarto-actions/tree/main/publish).

When publishing to Connect from a CI service you'll need to consider whether you want to execute your Python or R code directly on the CI server or whether you want to take advantage of previously [frozen](.../projects/code-execution.html#freeze) execution results. We'll explore this possibility first and then proceed to the specifics of how to publish from CI.

### Freezing Computations

Depending on how complicated your run-time requirements (packages, database credentials, etc.) are, you might find it more convenient to restrict execution of Python and R code to local contexts that have the required software and credentials.

{{< include _freeze-basics.md >}}

If you'd rather have CI publishing execute all Python and R code contained in your project, you'll need to ensure that the requisite version of these tools (and any required packages) are installed on the CI server. How to do this is outside the scope of this article---to learn more about saving and restoring dependencies, see the article on [Virtual Environments](../projects/virtual-environments.qmd).

### Publish Command

You can publish Quarto content to Connect using any CI service by scripting the `quarto publish` command. To do this, you'll need to make sure that your Connect server address and credentials are available as environment variables on the CI server.

| Variable          | Description                                                                |
|------------------|------------------------------------------------------|
| `CONNECT_SERVER`  | Address of Posit Connect server (e.g., `https://connect.example.com`).    |
| `CONNECT_API_KEY` | Posit Connect [API Key](https://docs.rstudio.com/connect/user/api-keys/) |

You will furthermore need to specify the ID of the target content to update. This will most frequently be drawn from the `_publish.yml` file that is saved into your project directory during publishing. For example:

```{.yaml filename="_publish.yml"}
- source: project
  connect:
    - id: 4f2ffc46-24b0-4cc7-a854-c5eb671e0dd7
      url: 'https://connect.example.com/content/4f2ffc46-24b0-4cc7-a854-c5eb671e0dd7/'
```

Assuming that you have a `_publish.yml` like the above, you can publish to Connect from CI with the following commands:

```{.bash filename="Terminal"}
export CONNECT_SERVER=https://connect.example.com/
export CONNECT_API_KEY=7C0947A852D8
quarto publish connect
```

Alternatively, if you don't have a `_publish.yml` file, you can specify the ID on the command line as follows:

```{.bash filename="Terminal"}
quarto publish connect --id 4f2ffc46-24b0-4cc7-a854-c5eb671e0dd7
```

### GitHub Actions

If your CI service is [GitHub Actions](https://docs.github.com/en/actions) then you can take advantage of Quarto's standard [publish action](https://github.com/quarto-dev/quarto-actions/tree/main/publish) to automate deploying to Connect.

#### Server Credentials

Before creating the publish action, you need to ensure that your repository has the credentials required for publishing to Connect. You can do this as follows:

1.  If you don't already have one, create an Posit Connect [API Key](https://docs.rstudio.com/connect/user/api-keys/) from the requisite Connect server and then copy it to the clipboard.

2.  Add the Connect API Key to your repository's action **Secrets** (accessible within repository **Settings**). You will see a **New repository secret** button at the top right:

    ![](images/gh-new-repository-secret.png){.border}

    Click the button and add the API Key from step 1 as a secret named `CONNECT_API_KEY`:

    ![](images/gh-action-connect-secret.png){.border}

#### Publish Action

To setup your publish action, create a `.github/workflows/publish.yml` file in your repository. If you are [Freezing Computations] (i.e. not running Python or R code within your action), then the file would look something like this:

```{.yaml filename=".github/workflows/publish.yml"}
on:
  workflow_dispatch:
  push:
    branches: main

name: Quarto Publish

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4 

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2

      - name: Render and Publish 
        uses: quarto-dev/quarto-actions/publish@v2
        with:
          target: connect
          CONNECT_SERVER: https://connect.example.com
          CONNECT_API_KEY: ${{ secrets.CONNECT_API_KEY }}
```

Once you've pushed your updated repository (including the publish action and `_freeze` directory) to GitHub, your action will run with this and subsequent commits, automatically rendering and publishing to Connect.

#### Executing Code

If you prefer, you can also configure GitHub Actions to execute Python or R code as part of rendering. While this might reflexively seem like the best approach, consider the following requirements imposed when you execute code within a CI service like GitHub Actions:

{{< include _ci-execute-requirements.md >}}

##### Prerequisites

The best way to ensure that your code can be executed within a GitHub Action is to use a virtual environment like [venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment) or [renv](https://rstudio.github.io/renv/articles/renv.html) with your project (below we'll provide example actions for each). If you aren't familiar with using these tools check out the article on using [Virtual Environments](../projects/virtual-environments.qmd) with Quarto to learn more.

Once you've decided to execute code within your GitHub Action you can remove the `freeze: auto` described above from your `_quarto.yml` configuration. Note that if you want to use `freeze` selectively for some documents or directories that is still possible (for a directory, create a `_metadata.yml` file in the directory and specify your freeze configuration there---this is what Quarto does by default for the `posts` folder of blog projects).

##### Example: Jupyter with venv

Here is a complete example of a GitHub Action that installs Python, Jupyter, and package dependencies from `requirements.txt`, then executes code and renders output to Connect:

```{.yaml filename=".github/workflows/publish.yml"}
on:
  workflow_dispatch:
  push:
    branches: main

name: Quarto Publish

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4 

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2
        
      - name: Install Python and Dependencies
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
          cache: 'pip'
      - run: pip install jupyter
      - run: pip install -r requirements.txt
      
      - name: Render and Publish 
        uses: quarto-dev/quarto-actions/publish@v2
        with:
          target: connect
          CONNECT_SERVER: https://connect.example.com
          CONNECT_API_KEY: ${{ secrets.CONNECT_API_KEY }}
```

##### Example: Knitr with renv

Here is a complete example of a GitHub Action that installs R and package dependencies from `renv.lock`, then executes code and renders output to Connect:

```{.yaml filename=".github/workflows/publish.yml"}
on:
  workflow_dispatch:
  push:
    branches: main

name: Quarto Publish

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4 

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2
        
      - name: Install R
        uses: r-lib/actions/setup-r@v2
        with:
          r-version: '4.2.0'
      
      - name: Install R Dependencies 
        uses: r-lib/actions/setup-renv@v2
        with:
          cache-version: 1
      
      - name: Render and Publish
        uses: quarto-dev/quarto-actions/publish@v2
        with:
          target: connect
          CONNECT_SERVER: https://connect.example.com
          CONNECT_API_KEY: ${{ secrets.CONNECT_API_KEY }}
```

#### Additional Options

It's possible to have a Quarto project in a larger GitHub repository, where the Quarto project does not reside at the top-level directory. In this case, add a `path` input to the invocation of the `publish` action. For example:

``` yaml
- name: Render and Publish
  uses: quarto-dev/quarto-actions/publish@v2
  with:
    target: connect
    path: subdirectory-to-use
    CONNECT_SERVER: https://connect.example.com
    CONNECT_API_KEY: ${{ secrets.CONNECT_API_KEY }}
```

By default, `quarto publish` will re-render your project before publishing it. However, if you store the rendered output in version control, you don't need the GitHub action to re-render the project. In that case, add the option `render: false` to the `publish` action:

``` yaml
- name: Render and Publish
  uses: quarto-dev/quarto-actions/publish@v2
  with:
    target: connect
    render: false
    CONNECT_SERVER: https://connect.example.com
    CONNECT_API_KEY: ${{ secrets.CONNECT_API_KEY }}
```


# quarto-web/docs/publishing/confluence.qmd

---
title: "Confluence"
provider: confluence
provider-name: Confluence
aliases:
  - /docs/prerelease/1.3/confluence.html
---

{{< include ../_require-1.3.qmd >}}

## Overview

[Atlassian Confluence](https://www.atlassian.com/software/confluence) is a publishing platform for supporting team collaboration. Confluence has a variety of hosting options which include both free and paid subscription plans.

::: callout-important

## Confluence Cloud Only

Publishing is currently limited to Confluence Cloud. 
We do not yet support publishing to Confluence Server or Confluence Data Center.

:::

Quarto provides support for publishing individual documents, as well as projects composed of multiple documents, into [Confluence Spaces](https://support.atlassian.com/confluence-cloud/docs/use-spaces-to-organize-your-work/).

::: {layout-ncol="2"}
![A Quarto Document](images/confluence-qmd.png){fig-alt="A screenshot of a Quarto document with the title Using R - Doc in the RStudio Editor."}

![Published to Confluence](images/confluence-page.png){fig-alt="A screenshot of a document with the title Using R - Doc in a Confluence Space."}
:::

::: {layout="[800,969]"}
![A Quarto Project](images/confluence-project.png){fig-alt="A screenshot of a Quarto project in VS Code. On the left in the Explorer, the project folder is called 'Guide-site', and contains folders 'authoring', and 'computation', along with some other files. A document from the folder 'python' inside the folder 'computations' with the title 'Using Python - site' is open in the Source Pane. "}

![Published to Confluence](images/confluence-site.png){fig-alt="A screenshot of Space in Confluence. On the left in the Sdiebar under Pages is a page called 'Guide-site'. Nested under this page are pages called 'authoring', and 'computation', along with some other pages. The 'computation' page item is expanded and shows a page called 'Using Python - site', nested under a page called 'python'. A page is displayed on the right with the title 'Using Python - site'"}
:::

Managing Confluence content with Quarto allows you to author content in Markdown, manage that content with your usual version control tools like Git and GitHub, and leverage Quarto's tools for including computational output.

The next section, [Confluence Publishing Basics](#publishing-basics), walks through the process of publishing a single page to Confluence, including how to [set up your Confluence account](#setting-up-account) in Quarto, and how to [specify a destination](#selecting-destination) for your document in your Confluence Space.

Before you use Confluence Publishing for your own project you'll want to read the remaining sections on this page:

-   [Publishing Projects](#collection-of-documents) describes how to publish a collection of documents, including how your [project structure](#project-structure) translates to the structure of pages in your Confluence Space.

-   [Publishing Workflow](#publishing-workflow) describes the model for making updates to Confluence pages published from Quarto, including the page permissions that are set when you publish from Quarto.

-   [Authoring for Confluence](#authoring) describes some of the differences between authoring for Confluence and authoring for a Quarto website.

-   [Publishing Settings](#publishing-settings) covers how to manage your publishing settings.

::: callout-important
## Be Careful with Sensitive or Confidential Content

Publishing Quarto documents to a public Confluence space will make the content of those documents public. It is your responsibility to understand the permissions of your Confluence Space and verify your publishing destination to protect against any sensitive or confidential content from being made publicly available.
:::

## Confluence Publishing Basics {#publishing-basics}

To demonstrate the process of publishing to Confluence, we'll take a single document, [`confluence-demo.qmd`](_confluence_examples/confluence-demo.qmd), and publish it as a page to a Confluence space. Here's the contents of `confluence-demo.qmd`:

``` markdown
---
title: Confluence Demo
format: confluence-html
---

## Overview

Write your content in Quarto documents and publish to Confluence.
```

Notice that the format is set to `confluence-html` in the document YAML. This allows the local preview of the document to mimic the eventual appearance on Confluence. You can preview your document locally as you would any other Quarto document, by using the **Render** command in VS Code and RStudio, or by using `quarto preview` from the command line:

``` {.bash filename="Terminal"}
quarto preview confluence-demo.qmd
```

The result of previewing `confluence-demo.qmd` locally is shown below:

![](images/confluence-demo-preview.png){fig-alt="Screenshot of the result of previewing the file confluence-demo.qmd."}

The preview attempts to provide an accurate idea of how your content will look. However, some items in the preview are merely placeholders, like the publishing date, author, and read time in the header. When the document is published to Confluence, these items will be generated by Confluence.

To publish a document to Confluence use `quarto publish confluence` followed by the file name:

``` {.bash filename="Terminal"}
quarto publish confluence confluence-demo.qmd
```

Unless you've published to Confluence before, you'll be prompted to set up an account and select a destination for your page.

### Setting Up Your Account {#setting-up-account}

When you publish to Confluence for the first time, you'll be prompted to set up a Confluence account in Quarto. To prepare, log in to Confluence, and navigate to the space, or page within a space, which you wish to publish to.

You'll first be prompted for your Confluence Domain. This is the first part of the URL to the Confluence page you wish to publish to. For example:

``` {.bash filename="Terminal"}
? Confluence Domain: ›
❯ e.g. https://mydomain.atlassian.net/
```

Next, you'll be asked to enter the Email Address for the account used in this Confluence Domain (if you are unsure, look at your account profile on Confluence):

``` {.bash filename="Terminal"}
? Confluence Account Email: › 
```

Finally, you'll be asked for an API Token:

``` {.bash filename="Terminal"}
? Confluence API Token: ›
❯ Create an API token at https://id.atlassian.com/manage/api-tokens
```

Confluence API Tokens are specific to your account. You'll need to [create a token](https://id.atlassian.com/manage/api-tokens), copy, and then paste it into this prompt. For more information on Access Tokens please see the [Confluence Documentation on API Tokens](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/).

Quarto saves this account information (domain, email and token) so it can be used for future calls to `quarto publish confluence`. The final prompt will ask you to select a destination for your page.

### Selecting a Destination {#selecting-destination}

Pages in Confluence are arranged in a hierarchy: every page has a parent. When you publish from Quarto to Confluence you'll be asked to specify the parent for your page by providing its URL:

``` {.bash filename="Terminal"}
? Space or Parent Page URL: ›
❯ Browse in Confluence to the space or parent, then copy the URL
```

If you want your page to be at the top level of your space, specify the space itself, e.g.:

```         
https://domain.atlassian.net/wiki/spaces/ABBR
```

Otherwise, specify the URL for the parent page, e.g.:

```         
https://domain.atlassian.net/wiki/spaces/ABBR/pages/123456
```

Once the destination is specified, Quarto will render the page for publishing, publish it to Confluence, and open a browser to view the published page.

An example of the published version of `confluence-demo.qmd` is shown below:

![](images/confluence-demo-published.png){fig-alt="Screenshot of the published confluence-demo.qmd file on Confluence. In the sidebar, the page Confluence Demo is listed under Pages at the top level."}

In the sidebar navigation this page is listed at the top level under Pages because the destination was set to the space URL.

## Publishing Projects {#collection-of-documents}

To publish a collection of documents, organize your documents in a [Quarto project](/docs/projects/quarto-projects.html), and use the `confluence` project type. Here's a minimal `_quarto.yml` file for a Confluence project:

``` {.yaml filename="_quarto.yml"}
project:
  type: confluence
```

Include this file in a project directory, then arrange your `.qmd` or `.ipynb` documents into whatever hierarchy you want to use for publishing. For example:

``` default
_quarto.yml
index.qmd
team.qmd
projects/
  planning.qmd
  retrospectives.qmd
```

Alternatively, to get started with a template project in a new directory, use `quarto create`: 

``` {.bash filename="Terminal"}
quarto create project confluence
```

As with documents, you can preview your project using the **Render** command in VS Code and RStudio, or by using `quarto preview` from the command line:

``` {.bash filename="Terminal"}
quarto preview
```

The project preview produces an HTML website with navigation automatically added to the sidebar. This navigation is for convenience, the navigation for the published pages will be handled internally by Confluence.

::: callout-tip
The project preview attempts to style your content as it will appear on Confluence, however, you may notice some differences in appearance.
:::

To publish your project run `quarto publish confluence` from your project folder:

``` {.bash filename="Terminal"}
quarto publish confluence 
```

You'll be walked through the same steps as publishing a single document, [setting up an account](#setting-up-account), if needed, and [selecting a destination](#selecting-destination) for your project on Confluence, before publishing your project to Confluence.

### Project Structure {#project-structure}

The hierarchy of documents inside folders in your project will be respected in the publishing process. Confluence's concept of folders is that pages can have children, so your folders will be represented by pages in Confluence.

When a project is published, a single page is created in Confluence to hold it. Documents at the top level of the project are published as pages nested under this project page. Folders inside the project are represented by a page, and any documents (or other folders) inside the folder are represented as pages nested under the folder page.

As an example, consider the following project structure:

```         
example-project/
├── _quarto.yml
├── project-roadmap.qmd
├── reports-folder
│   ├── 2023-01.qmd
│   └── 2023-03.qmd
└── team-members.qmd
```

The Confluence structure resulting from publishing this project to the top level of the space is shown below:

![](images/confluence-project-structure.png){fig-alt="A zoomed in view of the navigation sidebar in Confluence. Under Pages is a page called Project Example Site, nested under this page are pages called Team Members, Project Roadmap, and Reports-folder. Under the Reports-folder page are pages called: Reports, March, and January." width="60%"}

The titles used in the Confluence sidebar navigation are taken from the page and project title, as specified in the document YAML and `_quarto.yml` respectively, and generated from the folder name for folders. Quarto may add some additional characters to meet the Confluences requirement that every page in a space has a unique name.

### `index.qmd`

Pages in Confluence that represent folders will have no content unless an `index.qmd` is found inside the folder. If an `index.qmd` file exists its content will populate the folder page. For example, consider the following `index.qmd`:

````{.markdown filename="index.qmd"}
---
title: Reports
---

Monthly reports on project progress
````

Adding this to the folder `reports-folder` and re-publishing the site, changes the name of the page representing this folder to "Reports" and adds this contents to the page.

![](images/confluence-index.png){fig-alt="Screenshot of a page in Confluence titled Reports, with a single sentence 'Monthly reports on project progress'. In the sidebar navigation this page is called 'Reports' and is nested under the page called 'Project Example Site'."}

## Publishing Workflow {#publishing-workflow}

In Confluence, many people are able to make direct edits to pages. However, managing your content from Quarto requires a shift in perspective: edits to pages are made only in the Quarto project, and only one account should publish those changes to Confluence.

Publishing to Confluence is a one-way street: there is no way to bring back content edits from Confluence to your Quarto project. Edits that are made on Confluence will be overwritten next time the page is published from Quarto. Updating a page requires editing the document in Quarto, and rerunning:

``` {.bash filename="Terminal"}
quarto publish confluence 
```

To help avoid a situation where someone inadvertently edits a page being managed in Quarto, the permissions for pages are set when you publish so everyone with access to the space can view the page, but only you, the publisher, can edit the page.

![](images/confluence-permissions.png){fig-alt="Screenshot of the Confluence permissions on a page, with two items: Everyone is set to View; and Charlotte Wickham (Me) is set to Can Edit"}

Permission to edit the page includes publishing updates, so any updates to a page need to be published from the same account as the original publish.

::: callout-note

## Publishing without Control over Permissions

We attempt to detect if you are publishing to a destination where you do not have control over page permissions and you'll receive a warning. You may proceed with the publish, but any page you publish can be both viewed and edited by anyone with access to the space.

:::

If you delete a page on Confluence, and republish it from Quarto, you'll see the error:

```         
ERROR: API Error: 404 - Not Found
```

This occurs because Quarto stores and reuses the location of your page on Confluence in `_publish.yml`. If the page is deleted on Confluence, this location will no longer exist. To solve the problem, delete the corresponding entry in `_publish.yml`, and publish again. You'll then be prompted to set the destination. You can read more about `_publish.yml` in the [Publishing Settings](#publishing-settings) section.

## Authoring {#authoring}

Authoring for Confluence is very similar to authoring HTML documents and Quarto webpages. However, you should be aware of some key limitations as well as some features specific to Confluence publishing.

### Content Limitations

The `confluence-html` format supports nearly all of the standard Quarto markdown content types, including tables, callouts, and cross references.

However, there is currently no support for Citations, Videos, Diagrams, Tabsets, or Equations. In the future, we may add these features if there is a Confluence equivalent that can support the functionality.

### Links

When creating links between pages in your Confluence Project, you can provide the source file as the link target (rather than the path to the Confluence page). You can also add hash identifiers (`#`) to the source file if you want to link to a particular section in the document. For example:

``` markdown
[about](about.qmd)
[about](about.qmd#section)
```

### Raw Confluence Blocks

Raw Confluence blocks allow you to include content that should pass through Quarto unchanged and be interpreted directly by Confluence. For example, [Confluence's Storage Format](https://confluence.atlassian.com/doc/confluence-storage-format-790796544.html) includes specific tags for a task list. To include a Confluence task list in your document, use these tags inside a raw Confluence block:

````markdown
```{=confluence}
<ac:task-list>
    <ac:task>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body>task list item</ac:task-body>
    </ac:task>
</ac:task-list>
```
````

When published to Confluence this results in the following list:

![](images/confluence-task-list.png){fig-alt="A screenshot of list with one item. To the left of the item text is an unchecked checkbox." width=25%}


### Website Limitations

Confluence projects are a special type of website that don't support the traditional Website features like Listings, Themes and Navigation (as these things are taken care of internally by Confluence).

### Confluence Limitations

As discussed in [Publishing Workflow](#publishing-workflow) edits to page content made in Confluence are overwritten when content is published from Quarto. This is also the case for any inline comments made on Confluence. Page level emojis and page level comments are preserved across publishes.

## Publishing Settings {#publishing-settings}

Once you have published to Confluence, you might be interested in understanding how to manage your publishing and account settings.

### \_publish.yml

The `_publish.yml` file is used to specify the publishing destination. This file is automatically created (or updated) whenever you execute the `quarto publish` command, and is located within the project or document directory.

The service, id, and URL of the published content is specified in `_publish.yml`. For example:

``` yaml
- source: project
  confluence:
    - id: "5f3abafe-68f9-4c1d-835b-9d668b892001"
      url: "https://myteam.atlassian.net/wiki/spaces/TEAMSPACE/pages/123456/Plan"
```

The next time you publish the same document or project, the `_publish.yml` file will be used to provide account and space information so that you are not prompted for this information again.

If you have an existing Confluence Space that you want to publish to, you should manually create a `_publish.yml` file that looks like the example above, but with the appropriate `id` and `url` values for your document.

Account information is not stored in `_publish.yml`, so it is suitable for checking in to version control and being shared by multiple publishers.

### Account Management

You can list and remove saved Confluence accounts using the `quarto publish accounts` command:

``` markdown
$ quarto publish accounts
 ? Manage Publishing Accounts
 ❯ ✔ Confluence: jj@posit.co
   ✔ Netlify: jj@posit.co
 ❯ Use the arrow keys and spacebar to specify 
   accounts you would like to remove. Press 
   Enter to confirm the list of accounts you
   wish to remain available.
```


# quarto-web/docs/publishing/quarto-pub.qmd

---
title: "Quarto Pub"
provider: quarto-pub
provider-name: Quarto Pub
provider-publish-url: "https://njones.quarto.pub/blog"
---

## Overview

[Quarto Pub](https://quartopub.com) is a free publishing service for content created with Quarto. Quarto Pub is ideal for blogs, course or project websites, books, presentations, and personal hobby sites.

It's important to note that all documents and sites published to Quarto Pub are **publicly visible**. You should only publish content you wish to share publicly.

There are two ways to publish content to Quarto Pub (both are covered in more detail below):

1.  Use the `quarto publish` command to publish content rendered on your local machine (this is the recommend approach when you are getting started).

2.  If you are using GitHub, you can use a [GitHub Action] to automatically render your project and publish the resulting content whenever your code changes.

Before attempting your first publish, be sure that you have created a free [Quarto Pub](https://quartopub.com) account.

::: callout-note
Quarto Pub sites are publicly visible, can be no larger than 100 MB and have a *soft*limit of 10 GB of bandwidth per month. If you want to authenticate users, host larger sites, or use a custom domain, consider using a professional web publishing service like [Netlify](netlify.qmd) instead.
:::

{{< include _publish-command.md >}}

## Managing Sites

If you want to change the "slug" (or URL path) of a published site or remove the site entirely, you can use the site management interface at <https://quartopub.com>, which will display a list of all of your published sites:

![](images/quarto-pub-admin.png){.border}

Click on a site to navigate to an admin page that enables you to change the slug, make the site the default one for your account, or remove the site entirely:

![](images/quarto-pub-admin-site.png){.border}

## User Default Site

In addition to publishing documents and sites to paths within your Quarto Pub sub-domain (e.g. `https://username.quarto.pub/mysite/)` you can also designate one of your sites as the default site that users see when they navigate to your main sub-domain (e.g. `https://username.quarto.pub`). This is an ideal place to publish a blog or personal home page.

To promote one of your sites to the default site, go to your admin page at <https://quartopub.com>, navigate to the site you want to promote, check the **Default Site** option, then **Save** your modified options:

![](images/quarto-pub-default-site.png){.border}

## Multiple Accounts

If you are have multiple Quarto Pub accounts it's important to understand the relationship between the use of accounts in the CLI interface (`quarto publish`) and the use of accounts in your browser (for authenticating and managing sites).

When using `quarto publish`, there are a couple of scenarios where a web browser is launched:

1.  When you need to authorize the Quarto CLI to access your account.
2.  After publishing to open the admin page for your published site.

Before publishing with a Quarto Pub account from the CLI you should always be sure to log in to that account within your default web browser. This ensures that when the CLI launches the browser that it binds to the correct Quarto Pub account.

## Access Tokens

When you publish to Quarto Pub using `quarto publish` an access token is used to grant permission for publishing to your account. If no access token is available for a publish operation then the Quarto CLI will automatically launch a browser to authorize one:

``` markdown
$ quarto publish quarto-pub
? Authorize (Y/n) › 
❯ In order to publish to Quarto Pub you need to
  authorize your account. Please be sure you are
  logged into the correct Quarto Pub account in 
  your default web browser, then press Enter or 
  'Y' to authorize.
```

Authorization will launch your default web browser to confirm that you want to allow publishing from Quarto CLI. An access token will be generated and saved locally by the Quarto CLI. You can list and remove saved accounts using the `quarto publish accounts` command:

``` markdown
$ quarto publish accounts
 ? Manage Publishing Accounts
 ❯ ✔ Quarto Pub: jj@rstudio.com
   ✔ Netlify: jj@rstudio.com
 ❯ Use the arrow keys and spacebar to specify 
   accounts you would like to remove. Press 
   Enter to confirm the list of accounts you
   wish to remain available.
```

You can also view (and revoke) access tokens from the admin interface at <https://quartopub.com>:

![](images/quarto-pub-tokens.png){.border}

Within this interface you'll see any token you've created from the Quarto CLI. You may revoke this token if you no longer wish it to be active. Click the **New Token** button to create additional tokens that can be used for publishing non-interactively (e.g. from a CI service):

![](images/quarto-pub-new-token.png){.border}

Once you have an access token you can use it with `quarto publish` by defining the `QUARTO_PUB_AUTH_TOKEN` environment variable. For example:

``` {.bash filename="Terminal"}
# token created at https://quartopub.com/profile/
export QUARTO_PUB_AUTH_TOKEN="qpa_k4yWKEmlu5wkvx173Ls"

# publish to quarto-pub site specified within _publish.yml
quarto publish quarto-pub
```

See the article on [Publishing with CI](ci.qmd) for additional details on non-interactive use of `quarto publish`.

## GitHub Action

{{< include _github-action-basics.md >}}

``` {.yaml filename=".github/workflows/publish.yml"}
on:
  workflow_dispatch:
  push:
    branches: main

name: Quarto Publish

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4 

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2

      - name: Render and Publish 
        uses: quarto-dev/quarto-actions/publish@v2
        with:
          target: {{< meta provider >}}
          QUARTO_PUB_AUTH_TOKEN: ${{ secrets.QUARTO_PUB_AUTH_TOKEN }}
```

### Quarto Pub Credentials

The final step is to configure your GitHub Action with the credentials required for publishing. To do this you need to create a Quarto Pub personal access token and then configure your GitHub action to be able to read it:

1.  If you don't already have an access token, go to the Quarto Pub [account profile page](https://quartopub.com/profile), and click on **New Token** to create a token. Give this token a memorable name, and copy the token to the clipboard.

2.  Add the Quarto Pub access token to your repository's action **Secrets** (accessible within repository **Settings**). You will see a **New repository secret** button at the top right:

    ![](images/gh-new-repository-secret.png){.border}

    Click the button and add the personal access token from step 1 as a secret named `QUARTO_PUB_AUTH_TOKEN`:

    ![](images/gh-action-quarto-pub-secret.png){.border}

### Ignoring Output

{{< include _ignoring-output.md >}}

### Commit to Publish

Once you've specified your publishing action and {{< meta provider-name >}} credentials, and pushed your updated repository (including the `_freeze` directory) to GitHub, your action will run with this and subsequent commits, automatically rendering and publishing to {{< meta provider-name >}}.

{{< include _github-action-executing-code.md >}}

#### Example: Jupyter with venv

Here is a complete example of a GitHub Action that installs Python, Jupyter, and package dependencies from `requirements.txt`, then executes code and renders output to {{< meta provider-name >}}:

``` {.yaml filename=".github/workflows/publish.yml"}
on:
  workflow_dispatch:
  push:
    branches: main

name: Quarto Publish

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4 

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2
        
      - name: Install Python and Dependencies
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
          cache: 'pip'
      - run: pip install jupyter
      - run: pip install -r requirements.txt
      
      - name: Render and Publish 
        uses: quarto-dev/quarto-actions/publish@v2
        with:
          target: {{< meta provider >}}
          QUARTO_PUB_AUTH_TOKEN: ${{ secrets.QUARTO_PUB_AUTH_TOKEN }}
```

#### Example: Knitr with renv

Here is a complete example of a GitHub Action that installs R and package dependencies from `renv.lock`, then executes code and renders output to {{< meta provider-name >}}:

``` {.yaml filename=".github/workflows/publish.yml"}
on:
  workflow_dispatch:
  push:
    branches: main

name: Quarto Publish

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4 

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2
        
      - name: Install R
        uses: r-lib/actions/setup-r@v2
        with:
          r-version: '4.2.0'
      
      - name: Install R Dependencies 
        uses: r-lib/actions/setup-renv@v2
        with:
          cache-version: 1
      
      - name: Render and Publish
        uses: quarto-dev/quarto-actions/publish@v2
        with:
          target: {{< meta provider >}}
          QUARTO_PUB_AUTH_TOKEN: ${{ secrets.QUARTO_PUB_AUTH_TOKEN }}
```

### Additional Options

It's possible to have a Quarto project in a larger GitHub repository, where the Quarto project does not reside at the top-level directory. In this case, add a `path` input to the invocation of the `publish` action. For example:

``` yaml
- name: Render and Publish
  uses: quarto-dev/quarto-actions/publish@v2
  with:
    target: {{< meta provider >}}
    path: subdirectory-to-use
    QUARTO_PUB_AUTH_TOKEN: ${{ secrets.QUARTO_PUB_AUTH_TOKEN }}
```

By default, `quarto publish` will re-render your project before publishing it. However, if you store the rendered output in version control, you don't need the GitHub action to re-render the project. In that case, add the option `render: false` to the `publish` action:

``` yaml
- name: Render and Publish
  uses: quarto-dev/quarto-actions/publish@v2
  with:
    target: {{< meta provider >}}
    render: false
    QUARTO_PUB_AUTH_TOKEN: ${{ secrets.QUARTO_PUB_AUTH_TOKEN }}
```


# quarto-web/docs/publishing/ci.qmd

---
title: "Publishing with Continuous Integration (CI)"
---

## Overview

Continuous Integration (CI) refers to the practice of automatically publishing content from code checked in to a version control system. While publishing using CI is a bit more involved to configure, it has several benefits, including:

-   Content is automatically published whenever source code changes (you don't need to remember to explicitly render).

-   Rendering on another system ensures that your code is reproducible (but note that this can be double-edged sword if rendering has special requirements---see the discussion below on [Rendering for CI]).

-   Not checking rendered output into version control makes diffs smaller and reduces merge conflicts.

This article covers how to implement CI for Quarto using GitHub Actions (a service run by GitHub), ordinary shell commands (which can be made to work with any CI service), and with Posit Connect.

## Rendering for CI

Before you start using a CI server you'll need to think about where you want executable code (e.g. R, Python, or Julia code) to run and where you want `quarto render` to run. You might reflexively assume that you'll always want to run everything on the CI server, however doing so introduces a number of complexities:

1.  You need to make sure that the appropriate version of Quarto is available in the CI environment.

2.  You need to reconstitute all of the dependencies (required R, Python, or Julia packages) in the CI environment.

3.  If your code needed any special permissions (e.g. database or network access) those permissions need also be present on the CI server.

4.  Your project may contain documents that can no longer be easily executed (e.g. blog posts from several years ago that use older versions of packages).

In light of the above, you can think about rendering as a continuum that extends from running everything (including `quarto render`) locally all the way up to running everything remotely on CI:

-   **Local Execution and Rendering** --- Run everything in your local environment and then check output (e.g. the `_site` directory) into version control. In this scenario the CI server is merely making sure that the checked in content is copied/deployed to the right place every time you commit. You might choose this approach to place minimal requirements on software that needs to be present on the CI server.

-   **Local Execution with CI Rendering** --- Execute R, Python, or Julia code locally and use Quarto's ability to [freeze computational output](../projects/code-execution.qmd#freeze) to save the results of computations into the `_freeze` directory. Render the site on the CI server (which will use the computations stored in `_freeze`). Use this approach when its difficult to arrange fully re-executing code on the CI server.

-   **CI Execution and Rendering** --- Execute all code and perform rendering on the CI server. While this is the gold standard of automation and reproducibility, it will require you to capture your R, Python, or Julia dependencies (e.g. in an `renv.lock` file or `requirements.txt` file) and arrange for them to be installed on the CI server. You will also need to make sure that permissions (e.g. database access) required by your code are available on the CI server.

Below we'll describe how to implement each of these strategies using [GitHub Actions], ordinary [Shell Commands] (which you should be able to adapt to any CI environment), or [Posit Connect](rstudio-connect.qmd).

## GitHub Actions

[GitHub Actions](https://docs.github.com/en/actions){data-heading="GitHub Actions"} is a Continuous Integration service from GitHub, and an excellent choice if your source code is already managed it a GitHub repository. Quarto makes available a set of [standard](https://github.com/quarto-dev/quarto-actions) GitHub Actions that make it easy to install Quarto and then render and publish content.

Learn about using GitHub Actions with various publishing services here:

-   [Quarto Pub](quarto-pub#github-action)
-   [GitHub Pages](github-pages.qmd#github-action)
-   [Netlify](netlify.qmd#github-action)

If you want to use the standard Quarto actions as part of another workflow see the [GitHub Actions for Quarto](https://github.com/quarto-dev/quarto-actions) repository.

## Posit Connect

If you are publishing a source code version of your content to Posit Connect it's possible to configure Connect to retrieve the code from a Git repository and then render and execute on the Connect Server.

To learn more about this, see the documentation on [Git Backed Content](https://docs.rstudio.com/connect/user/git-backed/) for Posit Connect.

## Shell Commands

This section covers using the `quarto publish` command on a server where no user interaction is possible. This involves the following steps:

1.  Rendering your content.
2.  Specifying where to publish (which service/server, publishing target id, etc.).
3.  Providing the appropriate publishing credentials.

{{< include _netlify-ci-example.md >}}

Below we'll cover the various components of a publishing script as well as provide a few additional complete examples.

### Rendering for Publish

By default when you execute the publish command, your site or document will be automatically re-rendered:

```{.bash filename="Terminal"}
quarto publish
```

This is generally recommended, as it ensures that you are publishing based on the very latest version of your source code.

If you'd like to render separately (or not render at all) you can specify the `--no-render` option:

```{.bash filename="Terminal"}
quarto publish --no-render
```

By default, the call to `quarto publish` will execute all R, Python, or Julia code contained in your project. This means that you need to ensure that the requisite version of these tools (and any required packages) are installed on the CI server. How to do this is outside the scope of this article---to learn more about saving and restoring dependencies, see the article on [Virtual Environments](../projects/virtual-environments.qmd).

If you want to execute code locally then only do markdown rendering on CI, you can use Quarto's [freeze](../projects/code-execution.html#freeze) feature. For example, if you add this to your `_quarto.yml` file:

``` yaml
execute:
  freeze: true
```

Then when you render locally computations will run and their results saved in a `_freeze` folder at the root of your project. Then, when you run `quarto publish` or `quarto render` on the CI server these computations do not need to be re-run (only markdown rendering will occur on the server).

### Publishing Destination

There are two ways to specify publishing destinations for the `quarto publish` command:

1.  Via the contents of a `_publish.yml` file created from a previous publish.
2.  Using command line parameters (e.g. `--id` and `--server`).

When you execute the `quarto publish` command, a record of your publishing destination is written to a `_publish.yml` file alongside your source code. For example:

``` yaml
- source: project
  netlify:
    - id: "5f3abafe-68f9-4c1d-835b-9d668b892001"
      url: "https://tubular-unicorn-97bb3c.netlify.app"
```

You can check the `_publish.yml` file into source control so it is available when you publish from the CI server. If you execute the `quarto publish` command with no arguments and the above `_publish.yml` is in the project directory, then the publish will target Netlify with the indicated `id`:

```{.bash filename="Terminal"}
quarto publish netlify
```

You can also specify a publishing destination via explicit command line arguments. For example:

```{.bash filename="Terminal"}
quarto publish netlify --id 5f3abafe-68f9-4c1d-835b-9d668b892001
```

If you have multiple publishing targets saved within `_publish.yml` then the `--id` option can be used to select from among them.

### Publishing Credentials

You can specify publishing credentials either using environment variables or via command line parameters. The following environment variables are recognized for various services:

| Service         | Variables                              |
|-----------------|----------------------------------------|
| Quarto Pub      | `QUARTO_PUB_AUTH_TOKEN`                |
| Netlify         | `NETLIFY_AUTH_TOKEN`                   |
| Posit Connect   | `CONNECT_SERVER` and `CONNECT_API_KEY` |

Set these environment variables within your script before calling `quarto publish`. For example:

```{.bash filename="Terminal"}
export NETLIFY_AUTH_TOKEN="45fd6ae56c"
quarto publish netlify 
```

Note that you can also specify the publishing target `--id` as a command line argument. For example:

```{.bash filename="Terminal"}
export CONNECT_SERVER=https://connect.example.com/
export CONNECT_API_KEY=7C0947A852D8
quarto publish connect --id DDA36416-F950-4647-815C-01A24233E294
```

### Complete Examples

Here are a few complete examples that demonstrate various ways to write publishing shell scripts:

```{.bash filename="Terminal"}
# publish (w/o rendering) to quarto pub based on _publish.yml
export QUARTO_PUB_AUTH_TOKEN="45fd6ae56c"
quarto publish quarto-pub --no-render
```

```{.bash filename="Terminal"}
# render and publish to netlify based on _publish.yml
export NETLIFY_AUTH_TOKEN="45fd6ae56c"
quarto publish netlify
```

```{.bash filename="Terminal"}
# publish (w/o rendering) to netlify with explicit id
export NETLIFY_AUTH_TOKEN="45fd6ae56c"
quarto publish netlify --id DDA36416-F950-4647-815C-01A24233E294 --no-render
```

```{.bash filename="Terminal"}
# publish (w/o rendering) to connect based on _publish.yml
export CONNECT_SERVER=https://connect.example.com/
export CONNECT_API_KEY=7C0947A852D8
quarto publish connect --no-render
```

```{.bash filename="Terminal"}
# render and publish to connect with explicit id
export CONNECT_SERVER=https://connect.example.com/
export CONNECT_API_KEY=7C0947A852D8
quarto publish connect --id DDA36416-F950-4647-815C-01A24233E294
```


# quarto-web/docs/publishing/index.qmd

---
title: "Publishing Basics"
---

## Overview

There are a wide variety of ways to publish documents, presentations, and websites created using Quarto. Since content rendered with Quarto uses standard formats (HTML, PDFs, MS Word, etc.) it can be published anywhere. Additionally, there is a `quarto publish` command available for easy publishing to various popular services (GitHub, Netlify, Posit Connect, etc.) as well as various tools to make it easy to publish from a Continuous Integration (CI) system.

## Getting Started

To get started, review the documentation for using one of the following publishing services:

{{< include _providers.md >}}


# quarto-web/docs/publishing/other.qmd

---
title: "Other Services"
---

## Overview

There are a wide variety of ways to publish Quarto websites. Other articles cover publishing to [Quarto Pub](quarto-pub.qmd), [GitHub Pages](github-pages.qmd), [Netlify](netlify.qmd), and [Posit Connect](rstudio-connect.qmd). Below we'll describe some general guidelines as well as offer some specific advice for [Firebase](#google-firebase), [Site44], and [Amazon S3]. We'll mostly defer to the documentation provided by the various services, but will note any Quarto website specific configuration required.

The most important thing to understand is that website content is by default written to the `_site` sub-directory and book content to the `_book` directory (you can customize either using the `output-dir` option). Publishing is simply a matter of copying the output directory to a web server or web hosting service.

### Rendering for Publish

Prior to publishing you should always to a final render of your project:

```{.bash filename="Terminal"}
quarto render
```

This is particularly important to remember because changes you make to shared site configuration (e.g. `_quarto.yml`) aren't reflected across your entire site until your render the entire project. To ensure that your output is up to date before publishing you should always do a full `quarto render`.

## Firebase {#google-firebase}

Google Firebase has a [web hosting service](https://firebase.google.com/docs/hosting/quickstart) that enables easy deployment of websites using a set of command line tools.

Firebase websites by default deploy content from the `public` directory of the Firebase project directory. This means that you should set the `output-dir` to `"public"` within `_quarto.yml`:

``` yaml
project:
  type: website
  output-dir: public
```

## Site44 {data-link="Site44"}

[Site44](https://www.site44.com/) is a service that allows you to publish websites from within Dropbox folders. Site44 creates a `Dropbox/Apps/site44` directory, and any folders within that directory are published as websites.

The recommended workflow for deploying Quarto websites to Site44 is to develop your website in a separate project directory, and then, when it's ready for final publishing, copy the contents of the `_site` directory to the folder for your website.

## Amazon S3 {data-link="Amazon S3"}

If you are a user of Amazon Web Services you can serve your website directly from Amazon S3. Note however that this option is a bit more technically involved than GitHub Pages, Netlify, or Site44. See the article on [Hosting a Static Website on Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) for additional details.

## Other Hosts

Any web server or web host can be used to deploy a Quarto website. Here's a recent [CNET roundup](https://www.cnet.com/web-hosting/) of other web hosts you could consider. You can also deploy a Quarto website on any internal (intranet) web server.

You can also render and publish Quarto websites using a Continuous Integration (CI) service. See the articles on [Publishing with CI](ci.qmd) for additional details.


# quarto-web/docs/publishing/_confluence_examples/confluence-demo.qmd

---
title: Confluence Demo
format: confluence-html
---

## Overview

Write your content in Quarto documents and publish to Confluence.


# quarto-web/docs/manuscripts/publishing.qmd

---
title: "Publishing Quarto Manuscripts"
---

## Overview

::: callout-important

## Complete the Authoring Tutorial First

This page is a continuation of the [Authoring Manuscripts](authoring/) tutorial. We'll assume you've cloned the template repository, have made some changes, and are happy with the preview generated by Quarto.

:::

Publishing a Quarto manuscript is the process of taking the preview you've been viewing on your computer and making it available to anyone on the web.

We've set up the template manuscript to include most of the scaffolding needed to publish your manuscript to your repository's GitHub Pages site. Publishing your manuscript website is as simple as pushing your changes to your repo.

Since a Quarto manuscript is a special type of Quarto website, you can publish it any way you can publish a Quarto website. If GitHub Pages doesn't suit your needs you can learn about other options in [Publishing](/docs/publishing/).

On this page, you'll change one setting in your GitHub repo to authorize read and write permissions for GitHub Actions, then walk through the publishing process. 

## Authorize GitHub Actions

The template manuscript is configured with a GitHub Action in `.github/workflows/publish.yml`. This action is triggered when there is a push to the main branch; it renders your manuscript and puts the manuscript website source on the `gh-pages` branch. 

To ensure the action has permission to write to the `gh-pages` branch, you'll need to make one change to your repository settings. Go to your repository and navigate to: Settings \> Actions \> General \> Workflow Permissions. Check the "Read and Write Permissions" box.

![](images/github-action-setting.png){fig-alt="Screenshot of GitHub repository settings, showing a checked box next to the option 'Read and Write Permission', under the Workflow Permissions heading."}

::: callout-caution

## This GitHub Action will not evaluate your code 

The GitHub Action in `.github/workflows/publish.yml` does not set up any computational environments (e.g. Python or R), so is unable to evaluate code. 

Jupyter notebooks (`.ipynb`) include their output and do not need any special treatment. However, if your manuscript includes Quarto files (`.qmd`), you must first render locally to update the saved computational outputs in the `_freeze` directory.

If you instead want your GitHub Action to also evaluate code, read how to set it up in the [Executing Code section on the Publishing to GitHub page](https://quarto.org/docs/publishing/github-pages.html#executing-code).

:::

## Push to Publish

Publishing this manuscript to GitHub Pages is as simple as committing and pushing your changes, however we advise a full render first. On the Terminal, in your manuscript directory, run:

```{.bash filename="Terminal"} 
quarto render
```

::: callout-important

## The Render button isn't enough

The Render button in RStudio runs the command `quarto preview`, not `quarto render`. You'll need to explicitly run `quarto render` on the Terminal.

:::

Unlike `quarto preview` which generates outputs as needed, `quarto render` will generate all outputs (all the article formats and the manuscript website). It is also the command that will be run by the GitHub action, so verifying it locally first is a good way to avoid issues on GitHub.

If the render runs without issue, stage your changes. 

::: callout-caution

## Checked your staged files

We've added a few lines to `.gitignore` to ignore common files Quarto creates in the rendering process that don't need to be checked into version control. This means the files to stage should be the notebooks, and possibly items in the `_freeze` directory. 

If you've added any files to the project that you don't want to be pushed to GitHub, double-check you haven't staged them for the commit.

:::

Commit and push your changes to GitHub.

Once pushed, you should see the actions trigger in GitHub: "Quarto Publish" is the action we've added to render the site and push it to the `gh-pages` branch; "pages-build-deployment" is GitHub's action to deploy the `gh-pages` branch to your GitHub Pages URL.

![](images/github-publish-actions.png){fig-alt="Screenshot of the Actions page on a template repo. Under Actions, two workflows are listed: Quarto Publish and pages-build-deployment. Under All Workflows the same workflows appear both showing a green checkmark."}

Once both actions are complete, navigate to your repository's GitHub Page.

You can find your GitHub Pages website address in the Settings for your repository on GitHub under Pages.

![](images/github-pages-url.png){fig-alt="Screenshot of GitHub Pages Settings: under the heading GitHub Pages a dialog starting with 'Your page is live at:'  followed by a URL."} 

Your manuscript is now published!

## What Next?

You've now been through the full workflow of a Quarto manuscript: authoring content, previewing the generated manuscript and publishing it to GitHub Pages. When you are ready to dive into more detail, we have some recommendations on [Next Steps](next-steps.qmd). 




# quarto-web/docs/manuscripts/index.qmd

---
title: Quarto Manuscripts
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

Quarto manuscript projects provide a framework for writing and publishing scholarly articles. A Quarto manuscript lets you:

* Use one or more notebooks or `.qmd` documents as the source of content and computations, and then publish these computations alongside the manuscript, allowing readers to dive into your code.

* Produce manuscripts in multiple formats (including LaTeX or MS Word formats required by journals), and give readers easy access to all of the formats through a manuscript website.

The output of a Quarto manuscript is a website ([live example](https://quarto-ext.github.io/manuscript-template-jupyter/)). The article itself appears as the content of the website, and can include all the elements common to scholarly writing like figures, tables, equations, cross references and citations. The website also makes available other formats (e.g. PDF, Docx) as well as links to all of the computations used to create the article.

::: {layout="[[3,1]]"}

![Article Content](images/article-content.png){fig-alt="A screenshot of the content area on the manuscript webpage. Content shows a title block including the article title, authors, and abstract, body text, and an image with a caption." .border}

![Navigation](images/webpage-menu.png){fig-alt="A screenshot of the menu on the right hand side of the manuscript webpage. The menu has headings: Table of contents, Other Formats, Notebooks and Other Links." .border}

:::

On the right, you'll see navigation: a table of contents for the article itself followed by links to **Other Formats**, **Notebooks** and **Other Links**.

### Other Formats {.unnumbered .unlisted}

These links allow a reader to download alternative formats of your article. In this example, there is an MS Word version that may be useful for a reviewer to provide feedback and a PDF version that uses the American Geophysical Union's (AGU) template. Additionally, there is a MECA archive, a zip file that is designed to capture your article and its supporting documents into a single file suitable for sending to a publisher. 

### Notebooks {.unnumbered .unlisted}

These are links to notebooks included in the manuscript. The "Article Notebook" is the notebook version of the article itself. In this example, "Data Screening" is a notebook from which a single cell is embedded in the article. Any other notebooks that are included in the project, even if they are not directly used in the article will also appear here. 
    
When a reader visits any of these notebook links, they are served an HTML version of the notebook, allowing them to view the code and output without leaving their browser. In addition, a link to download the source code of the notebook is also provided.
    
![HTML view of the Data Screening notebook](images/notebook-view.png){.border fig-alt="Screenshot of the notebook view of data-screening.ipynb. The top of the page has a link Back to the Article and a button to Download Notebook. The content of the page includes some text and a cell displaying code."}
    
### Other Links {.unnumbered .unlisted}

Links that leave the manuscript webpage, for example to take a reader to the manuscript's GitHub Repo.


## Get Started {#get-started}

### Install Quarto {#install}

Manuscripts are a feature in the upcoming 1.4 release of Quarto and are still under active development. Before you get started, make sure you install the **latest pre-release** version of Quarto.

{{< include ../download/_download-pre.md >}}

### Choose Your Tool {#choose}

You can author Quarto manuscripts in any tool or notebook editor.
The tutorials below walk you through authoring Quarto manuscripts with a few common tools. 

Choose your tool to start learning:

::: {.tool .g-col-lg-9 .g-col-12}
<a href="authoring/jupyterlab.html" role="button" class="btn btn-outline-light"> ![](images/jupyter-logo.png){width="77" fig-alt="Jupyter logo."}Jupyter</a>

<a href="authoring/vscode.html" role="button" class="btn btn-outline-light"> ![](images/vscode-logo.png){width="77" fig-alt="VS Code logo."}VS Code</a>

<a href="authoring/rstudio.html" role="button" class="btn btn-outline-light"> ![](images/rstudio-logo.png){width="77" fig-alt="RStudio logo."}RStudio</a>
:::


# quarto-web/docs/manuscripts/components.qmd

---
title: "Manuscript Basics"
---

## Overview

Manuscripts are a type of Quarto project that allow you to write scholarly articles where computational notebooks are both the source of the article, and part of the published record.

If you are new to Quarto manuscripts, start with the [Manuscript Tutorial](/docs/manuscripts).

On this page, you can learn how to:

* Create a manuscript project
* Control the manuscript output with options in `_quarto.yml`
* Add a journal template

## Creating a Manuscript Project {#create}

To identify a project as a manuscript specify `type: manuscript` in your `_quarto.yml` configuration file:

``` {.yaml filename="_quarto.yml"}
project: 
  type: manuscript
```

Then, author your article content in either a Jupyter Notebook called `index.ipynb` or a Quarto document called `index.qmd`.

You can control many manuscript options with the `manuscript` key in your configuration file.
For instance, you can specify a file other than `index.*` for your article source using the `article` key, e.g.:

``` {.yaml filename="_quarto.yml"}
manuscript:
  article: earthquakes.qmd
```

If you would rather start with some template content, you can create a new manuscript project from the command line with:

``` {.bash filename="Terminal"}
quarto create project manuscript
```

## Including Notebooks

Any notebook files (`.qmd` or `.ipynb`) that are included in your project directory will become part of your manuscript.
These notebooks will be rendered to an HTML notebook view, and will be linked from your manuscript webpage under "Notebooks".

### Notebook Links

The text for link under "Notebooks" will be the notebook `title` as set in its YAML metadata, or if that isn't set, the first markdown heading in the notebook.
If neither exist, the link text will be the notebook file name.

You can also set the text using `notebooks`.
Use `notebook` to specify the path to the notebook, and `title` to set the link text:

``` {.yaml filename="_quarto.yml"}
manuscript:
  notebooks:
    - notebook: notebooks/data-screening.ipynb
      title: Data Processing
```

### External Notebooks

To provide links to notebooks that are hosted elsewhere, add the `url` option:

``` {.yaml filename="_quarto.yml"}
manuscript:
  notebooks:
    - notebook: index.ipynb
      title: Binder Jupyter Lab Demo
      url: http://mybinder.org/v2/gh/binder-examples/jupyterlab/master?urlpath=lab/tree/index.ipynb
```

If you want Quarto to produce an HTML notebook view from your notebook source, 
but you would like to provide a specific version for download, add the `download-url` option:

``` {.yaml filename="_quarto.yml"}
manuscript:
  notebooks:
    - notebook: notebooks/data-screening.ipynb
      title: Data Processing
      download-url: notebooks/data-screening-raw.ipynb
```

## Including Other Resources

Quarto will attempt to include resources needed to render your notebooks to HTML on the manuscript website.
However, you can also explicitly include resources using `resources`.
For example, to include a data file you've put in `data/earthquakes.csv` you would specify:

``` {.yaml filename="_quarto.yml"}
manuscript:
  resources:
    - data/earthquakes.csv
```

This ensures readers can access your data at: `{manuscript-url}/data/earthquakes.csv`.

## MECA Bundle

One of the formats a manuscript project can produce is a Manuscript Exchange Common Approach (MECA) bundle.
This bundle is a standardized way to transport your manuscript and its resources, including computational notebooks.

A MECA bundle is produced if the `jats` format is listed as an output format for your article:

``` {.yaml filename="_quarto.yml"}
format:
  html: default
  jats: default
```

Or, you can explicitly set `meca-bundle` to `true` in the `manuscript` options:

``` {.yaml filename="_quarto.yml"}
manuscript:
  meca-bundle: true
```

By default the MECA bundle is named after your article file, e.g. `index-meca.zip`, but you can also use `meca-bundle` to provide a file name:

``` {.yaml filename="_quarto.yml"}
manuscript:
  meca-bundle: "bundle.zip"
```

## Manuscript URL

Links to your notebooks in non-HTML formats are constructed using the URL of your manuscript website.
If your manuscript is published to GitHub Pages, Quarto will detect and set the URL for you.
However, if you publish to a different host, or the automatic detection isn't working, you can set the URL explicitly with `manuscript-url`:

``` {.yaml filename="_quarto.yml"}
manuscript:
  manuscript-url: www.posit.co
```

## Customizing Pages

The article page and notebook views on your manuscript site are HTML pages, and can be customized using options for the `html` format. 
A full list of options is available at [HTML Options](/docs/reference/formats/html.qmd).

### Theme

For example, you can change the visual styling of your page with the `theme` option by providing an existing theme name:

``` {.yaml filename="_quarto.yml"}
format:
  html: 
    theme: solar
```

You can read more at [HTML Theming](/docs/output-formats/html-themes.html).

### Commenting

Quarto also integrates with three tools to allow commenting on your manuscript site.
To enable commenting, use the `comments` option to the `html` format. 
For example, to enable [Hypothes.is](https://web.hypothes.is/) comments, you just need to add
`hypothesis: true`:

``` {.yaml filename="_quarto.yml"}
format:
  html: 
    comments:
      hypothesis: true
```

The other two tools available are [Utterances](https://utteranc.es/) and [Giscus](https://giscus.app/). You can read about setting them up at [HTML Basics: Commenting](/docs/output-formats/html-basics.html#commenting).

## Add a Journal Template

You can find a list of available journal formats on the [Quarto Extensions: Journal Articles](/docs/extensions/listing-journals.html) page.
To use a journal format, e.g. the [**acs**](https://github.com/quarto-journals/acs#american-chemical-society-acs) format, you'll need to complete two steps:

1.  Install the appropriate journal format.
    You'll most likely be installing in an existing project, so you'll use the `quarto install extension` command, e.g.:

    ``` {.bash filename="Terminal"}
    quarto install extension quarto-journals/acs
    ```

    The extension identifier, `quarto-journals/acs`, is the GitHub user and repository for the extension.
    You'll generally find this, and the exact installation command in the extension's documentation.

2.  Add the `format` to your configuration file:

    ``` {.yaml filename="_quarto.yml"}
    format:
      html: default
      docx: default
      jats: default
      acs-pdf: default
    ```

    The format will be the extension's name (`acs`), followed by an existing Quarto format (`-pdf`).


# quarto-web/docs/manuscripts/next-steps.qmd

---
title: "Next Steps"
---

## Learning More

You've seen the manuscript workflow, and examples of syntax in a complete template.
One way to start your own manuscript is to alter the contents of this template.
Alternatively, you could start from scratch.
Either way, here are some resources to help you with your next steps.

+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ### Basics          | Head to [**Manuscript Basics**](/docs/manuscripts/components.html) to:                                                                                                                                                                                                                                                                                         |
|                     |                                                                                                                                                                                                                                                                                                                                                                |
|                     | -   Learn how to turn a directory into a manuscript project by adding the `_quarto.yml` file                                                                                                                                                                                                                                                                   |
|                     |                                                                                                                                                                                                                                                                                                                                                                |
|                     | -   Start a new project with a minimal template using the `quarto create` command                                                                                                                                                                                                                                                                              |
|                     |                                                                                                                                                                                                                                                                                                                                                                |
|                     | -   Controlling manuscript settings in `_quarto.yml`                                                                                                                                                                                                                                                                                                           |
|                     |                                                                                                                                                                                                                                                                                                                                                                |
|                     | -   Add an output format for a specific journal                                                                                                                                                                                                                                                                                                                |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ### Quarto Projects | Quarto manuscripts are a type of [**Quarto project**](/docs/projects/quarto-projects.html), so anything you can do in a Quarto project applies to a manuscript. For instance, these pages in the Project documentation might be of interest:                                                                                                                   |
|                     |                                                                                                                                                                                                                                                                                                                                                                |
|                     | -   [Managing Execution](/docs/projects/code-execution.html): techniques to avoid expensive computations on every render.                                                                                                                                                                                                                                      |
|                     |                                                                                                                                                                                                                                                                                                                                                                |
|                     | -   [Virtual Environments](/docs/projects/virtual-environments.html): capture your computational environment to facilitate reproducing your work.                                                                                                                                                                                                              |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ### Publishing      | We set up the publishing workflow for the template repository, but you can publish your manuscript website any way you can [**publish a Quarto website**](https://quarto.org/docs/publishing/). For example, if you need to set up the workflow to publish to GitHub pages yourself, head to [Publishing to GitHub Pages](/docs/publishing/github-pages.html). |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


# quarto-web/docs/manuscripts/authoring/_workflow-ipynb.qmd

The basic workflow for writing a manuscript in Quarto is to make changes to your article content in `{{< meta tool.article-file >}}`, preview the changes with Quarto, and repeat. Let's try it out.

Open a new Terminal in {{< meta tool.name >}} and run:

``` {.bash filename="Terminal"}
quarto preview
```

You'll see some output from Quarto on the Terminal:

``` {.bash filename="Terminal"}
$ quarto preview
Preparing to preview
[1/1] {{< meta tool.article-file >}}

Watching files for changes
Browse at http://localhost:3806/
GET: /
```

And then, a browser window will open with a live preview of the manuscript.

You may find it helpful to move and resize your windows so that {{< meta tool.name >}} and the live preview are side by side.

![](images/jupyter-preview.png){fig-alt="A screenshot of two side by side browser windows. On the left, Jupyter Lab with the Terminal open displaying the command: quarto preview. On the right, a webpage with the address starting localhost:, and content starting with the header La Palma Earthquakes."}

The contents of the article is generated by `{{< meta tool.article-file >}}`. Go ahead and open this file in {{< meta tool.name >}}. 

![](images/jupyter-notebook.png){fig-alt="A screenshot of two side by side windows. On the left, Jupyter Lab with the file `index.ipynb` open. The first cell begins with a title La Palma Earthquakes. On the right, a webpage with the address starting localhost:, and content starting with the header La Palma Earthquakes."}

You'll dive into the details of this file next, but for now let's make a change and see what happens.

The first cell (starting with "La Palma Earthquakes") is a Markdown cell, enter Edit mode in this cell, and find the line:

``` yaml
title: La Palma Earthquakes
```

Change the line to:

``` yaml
title: La Palma Earthquake Mechanisms
```

Save the notebook, and you'll see the preview update automatically.

![](images/jupyter-edit-preview.png){fig-alt="Screenshot of two browser windows. On the left, Jupypter Lab with the file index.ipynb open, the first cell in edit mode, and with the text title: La Palma Earthquake Mechanisms. On the right, the article webpage with the title La Palma Earthquake Mechanisms."}

::: callout-tip
If you close the preview accidentally, you can navigate to it again by using the URL from the output in the Terminal, e.g. `http://localhost:3806/`. If you want to stop the preview, hit Crtl + C in the Terminal. You can start the preview again by running `quarto preview`.
:::



# quarto-web/docs/manuscripts/authoring/jupyterlab.qmd

---
title: "Authoring Manuscripts"
tool: 
  name: "Jupyter Lab"
  article-file: "index.ipynb"
  template-repo: "https://github.com/quarto-ext/manuscript-template-jupyter"
  is_jupyterlab: true
  is_rstudio: false
  is_vscode: false
---

{{< include _authoring-content.qmd >}}


# quarto-web/docs/manuscripts/authoring/_setup.qmd

::: {.content-visible when-meta="tool.is_jupyterlab"}
To follow along, you'll need to install the Jupyter Lab Quarto extension and clone the template repository.
:::

::: {.content-visible when-meta="tool.is_rstudio"}
To follow along, you'll need to clone the template repository.
:::

::: {.content-visible when-meta="tool.is_vscode"}
To follow along, you'll need to install the VS Code Quarto extension, install some Python packages, and clone the template repository.
:::

::: callout-important
## Install Quarto First

If you haven't already, make sure you've installed the pre-release version of Quarto, as described in the [Manuscript Overview](../index.qmd#install).
:::

::: {.content-visible when-meta="tool.is_jupyterlab"}
### Install the Jupyter Lab Quarto Extension

{{< include /docs/tools/_jupyter-lab-extension-install.qmd >}}
:::

::: {.content-visible when-meta="tool.is_vscode"}
### Install the Quarto VS Code Extension

Install the Quarto extension from the [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=quarto.quarto) or the [Open VSX Registry](https://open-vsx.org/extension/quarto/quarto).

### Install Python Packages

The template manuscript includes some executable Python code. To render Python code you'll need `jupyter` along with the packages specific to this code, `pandas`, and `matplotlib`:

```{.bash filename="Terminal"}
python3 -m pip install jupyter matplotlib pandas 
```

Alternatively, once you have the template repo below, you can use the file `requirements.txt` to get the packages you need.

:::

### Clone the Template Repository {#clone-repo}

To follow this tutorial you'll need your own copy of the [template repository]({{< meta tool.template-repo >}}), including all of its branches.

1.  Head to [GitHub to create a new repository from the template]({{< meta tool.template-repo >}}/generate).

    Provide a **Repository Name** and make sure you check **Include all branches**. Then **Create repository from template**. ![](images/github-create-from-template.png){fig-alt="Screenshot of GitHub's create a new repo from a template page. Repository name has been filled with manuscript-template, and the box labelled Include all branches is checked."}

2.  Once your repository is created, clone it to your local computer.

    ::: {.content-visible unless-meta="tool.is_rstudio"}
    You can do this any way you are comfortable, for instance in the Terminal, it might look like:

    ``` {.bash filename="Terminal"}
    git clone git@github.com:<username>/<repo-name>.git
    ```

    Where you use your own user name and repo name.
    :::

    ::: {.content-visible when-meta="tool.is_rstudio"}
    You can do this any way you are comfortable, but one approach is to use **File** > **New Project**. In the **New Project** dialog, select **From Version Control**, then **Git**, and copy and paste the repo URL from GitHub.
    :::

::: {.content-visible when-meta="tool.is_rstudio"}
![Template manuscript open in RStudio](images/rstudio-open.png){fig-alt="Screenshot of the RStudio IDE with a project called manuscript-template-rstudio-test open. The File pane shows the folders: _extensions, _freeze, .github, images, and notebooks; and the files: _quarto.yml, .gitignore, index.ipynb, README.md and references.bib."}
:::

::: {.content-visible when-meta="tool.is_jupyterlab"}
3.  You'll be working inside this directory throughout the tutorial, so if you are ready to proceed, navigate inside the directory, and start Jupyter Lab:

    ``` {.bash filename="Terminal"}
    cd manuscript-tutorial
    python3 -m jupyter lab
    ```

![Template manuscript opened in Jupyter Lab](images/jupyter-open.png){.border fig-alt="A screenshot of Jupyter Lab. The File Browser is open showing the folders: _extensions, images, and notebooks; and the files: _quarto.yml, index.ipynb, README.md and references.bib."}
:::

::: {.content-visible when-meta="tool.is_vscode"}
3.  You'll be working inside this directory throughout the tutorial, so if you are ready to proceed, open the directory in VS Code.

![Template manuscript open in VS Code](images/vscode-open.png){fig-alt="A screenshot of VS Code. The File Explorer is open showing the folders: _extensions, _freeze, .github, images, and notebooks; and the files: _quarto.yml, index.ipynb, README.md and references.bib."}
:::


# quarto-web/docs/manuscripts/authoring/_markdown.qmd

::: {.content-visible when-meta="tool.is_jupyterlab"}
Markdown cells in the document will be processed by Quarto's specific markdown syntax. Quarto's markdown syntax is based on [Pandoc Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown), which in turn is based on John Gruber's [Markdown](https://daringfireball.net/projects/markdown/), the same markdown Jupyter Notebooks use.
:::

::: {.content-visible unless-meta="tool.is_jupyterlab"}
Markdown cells in the document will be processed by Quarto's specific markdown syntax. Quarto's markdown syntax is based on [Pandoc Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown), which in turn is based on John Gruber's [Markdown](https://daringfireball.net/projects/markdown/). 
:::

As an example, the markdown to create the heading for the article's introduction is:

```markdown
## Introduction
```

First-level headings are reserved for the article title, so you'll use second-level and deeper headings to structure the sections in your article.

If Markdown syntax is unfamiliar, you might want to read about Quarto [Markdown Basics](/docs/authoring/markdown-basics.html). 


# quarto-web/docs/manuscripts/authoring/vscode.qmd

---
title: "Authoring Manuscripts"
tool: 
  name: "VS Code"
  article-file: "index.qmd"
  notebook-file: "data-screening.qmd"
  template-repo: "https://github.com/quarto-ext/manuscript-template-vscode"
  is_jupyterlab: false
  is_rstudio: false
  is_vscode: true
---

{{< include _authoring-content.qmd >}}


# quarto-web/docs/manuscripts/authoring/_front-matter.qmd

The YAML header consists of key-value pairs set using the syntax `key: value`. The header is often extensive for articles because it is used to specify much of the scholarly front matter, like the authors and their affiliations, and the abstract.

::: {.callout-tip appearance="simple" collapse="true"}
## Expand to see full YAML header for `{{< meta tool.article-file >}}`

``` yaml
title: La Palma Earthquakes
author:
  - name: Steve Purves
    orcid: 0000-0002-0760-5497
    corresponding: true
    email: steve@curvenote.com
    roles:
      - Investigation
      - Project administration
      - Software
      - Visualization
    affiliations:
      - Curvenote
  - name: Rowan Cockett
    orcid: 0000-0002-7859-8394
    corresponding: false
    roles: []
    affiliations:
      - Curvenote
keywords:
  - La Palma
  - Earthquakes
abstract: |
  In September 2021, a significant jump in seismic activity on the island of La Palma (Canary Islands, Spain) signaled the start of a volcanic crisis that still continues at the time of writing. Earthquake data is continually collected and published by the Instituto Geográphico Nacional (IGN). ...
plain-language-summary: |
  Earthquake data for the island of La Palma from the September 2021 eruption is found ...
key-points:
  - A web scraping script was developed to pull data from the Instituto Geogràphico Nacional into a machine-readable form for analysis
  - Earthquake events on La Palma are consistent with the presence of both mantle and crustal reservoirs.
date: last-modified
bibliography: references.bib
citation:
  container-title: Earth and Space Science
number-sections: true
```
:::

For example, at the top level the header in `{{< meta tool.article-file >}}` sets the following keys: `title`, `author`, `keywords`, `abstract`, `plain-language-summary`, `key-points`, `date`, `bibliography`, `citation`, and `number-sections`.

You've seen how editing the `title` key updated the title of the article on the manuscript webpage. The `title` key is also used by the PDF and Word formats, but not all of the keys are used in all formats. For instance, `keywords` is not used in the HTML, PDF or Word formats, but it is used inside the MECA archive.

You can read more about setting the front matter for your article in [Scholarly Front Matter](/docs/authoring/front-matter.qmd).


# quarto-web/docs/manuscripts/authoring/_workflow-qmd.qmd

The basic workflow for writing a manuscript in Quarto is to make changes to your article content in `{{< meta tool.article-file >}}`, preview the changes with Quarto, and repeat. Let's try it out.

Open `{{< meta tool.article-file >}}`. 

::: {.content-visible when-meta="tool.is_vscode"}
Preview the manuscript by hitting the **Preview** button located in the menu bar of the editor:

![](images/vscode-render-button.png){fig-alt="Screenshot of the source editor menu bar with the Render button highlighted."}
:::

::: {.content-visible when-meta="tool.is_rstudio"}
Render and preview the manuscript by hitting the **Render** button located in the menu bar of the editor:

![](images/rstudio-render-button.png){fig-alt="Screenshot of the source editor menu bar with the Render button highlighted."}
:::

::: {.content-visible when-meta="tool.is_vscode"}
You'll see some output from Quarto in the Terminal and then a live preview will appear in a new Quarto Preview pane.
:::

::: {.content-visible when-meta="tool.is_rstudio"}
You'll see some output from Quarto in the Background Jobs pane and then a live preview will appear in the Viewer pane.
:::

::: {.content-visible when-meta="tool.is_rstudio"}
![](images/rstudio-preview.png){fig-alt="Screenshot of the RStudio IDE. Open in the Source pane is a file called index.qmd. In the Viewer pane, a website starting with the header La Palma Earthquakes."}
:::

::: {.content-visible when-meta="tool.is_vscode"}
![](images/vscode-preview.png){fig-alt="Screenshot of the VS Code. Open in an Editor pane is a file called index.qmd. Open in a pane titled Quarto Preivew is a website starting with the header La Palma Earthquakes."}
:::


You'll dive into the details of this `{{< meta tool.article-file >}}` next, but for now let's make a change and see what happens.

Find the line:

``` yaml
title: La Palma Earthquakes
```

Change the line to:

``` yaml
title: La Palma Earthquake Mechanisms
```

::: {.content-visible when-meta="tool.is_rstudio"}
Save the notebook, re-render, and you'll see the preview update.

![](images/rstudio-edit.png){fig-alt="Screenshot of the RStudio IDE. Open in the Source pane is a file called index.qmd with the text, title: La Palma Earthquake Mechanisms. In the Viewer pane is an article webpage with the title La Palma Earthquake Mechanisms."}
:::

::: {.content-visible when-meta="tool.is_vscode"}
Save the notebook, hit Preview, and you'll see the preview update.

![](images/vscode-edit.png){fig-alt="Screenshot of VS Code.  Open in an Editor pane is a file called index.qmd with the text, title: La Palma Earthquake Mechanisms. In the Quarto Preview pane is an article webpage with the title La Palma Earthquake Mechanisms."}
:::


# quarto-web/docs/manuscripts/authoring/_embeds-ipynb.qmd

An alternative to including computations directly in the article notebook, is to embed output from other notebooks. This manuscript project includes the notebook `data-screening.ipynb` in the `notebooks/` folder.

To embed output from a notebook, you can use the `embed` shortcode. Quarto shortcodes are special markdown directives that generate content. The `embed` shortcode is used in main article file in the line:

``` {.markdown filename="index.ipynb" shortcodes="false"}
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


# quarto-web/docs/manuscripts/authoring/_overview.qmd

On this page, we'll show you how to author an academic manuscript with Quarto in {{< meta tool.name >}}. You'll learn how to:

-   Preview your manuscript using {{< meta tool.name >}}.

-   Add scholarly front matter to describe your article.

-   Add figures, tables, cross references, and citations with Quarto-specific markdown.

-   Include output from computations using inline code or embedded from external notebooks.

::: {.content-visible when-meta="tool.is_jupyterlab"}
The commands and syntax you'll learn will apply to any tool you might use to edit notebooks, not just Jupyter Lab. And, although we'll use Python code examples, Quarto works with any kernel, so you could use R or Julia instead. 
:::

::: {.content-visible when-meta="tool.is_rstudio"}
The syntax you'll learn will apply regardless of the tool you are using to edit notebooks. And although we'll use R code examples, you could use Python or Julia instead. 
:::

::: {.content-visible when-meta="tool.is_vscode"}
The syntax you'll learn will apply regardless of the tool you are using to edit notebooks. And although we'll use Python code examples, you could use R or Julia instead. 

::: callout-tip

## Do you mostly use `.ipynb`?

As a VS Code user, we recommend writing your article in a `.qmd` file. However, if you currently use VS Code primarily to work with `.ipynb` files, you may find the Jupyter Lab tutorial more applicable. Install the [Quarto extension for Jupyter Lab](#install-the-quarto-vs-code-extension), then pick up the Jupyter Lab tutorial at [Clone the Template Repository](jupyterlab.qmd#clone-repo). You might also like read about using [Quarto with VS Code's Notebook Editor](/docs/tools/vscode-notebook.html).
:::

:::

::: {.content-visible when-meta="tool.is_rstudio"}

::: callout-caution

## What's a notebook?

You'll see us refer to Quarto documents (`.qmd`) as notebooks throughout this tutorial. In fact, we'll use the term "notebook"  interchangeably to refer to a Quarto document (`.qmd`) or a Jupyter Notebook (`.ipynb`). Although there are implementation differences these formats are both designed to combine code and narrative - a feature that is central to being a computational notebook.

When Quarto prepares your manuscript for publication, both as website and a submission archive, your Quarto `.qmd` documents and their outputs will be made available as Jupyter notebooks. Jupyter Notebooks have the advantage that computational outputs are included in the notebook file - allowing a record of both your code and its results to travel through the publication process and become part of your manuscript's document of record.

:::

:::

### Is this tutorial for me?

We will assume you:

-   are comfortable using {{< meta tool.name >}} to open and edit files,
-   have a GitHub account, and are comfortable cloning a repo to your computer,
-   are comfortable navigating your file system, and executing commands in a Terminal.


# quarto-web/docs/manuscripts/authoring/_embeds-qmd.qmd

::: callout-note
## Embedding Quarto Notebooks

This section covers embedding outputs from Quarto documents (`.qmd`). You can also [embed outputs from Jupyter Notebooks (`.ipynb`)](/docs/authoring/notebook-embed.qmd).

:::

An alternative to including computations directly in the article notebook is to embed output from other notebooks. This manuscript project includes the notebook `{{< meta tool.notebook-file >}}` in the `notebooks/` folder.

To embed output from a notebook, you can use the `embed` shortcode. Quarto shortcodes are special markdown directives that generate content. The `embed` shortcode is used in main article file in the line:

::: {.content-visible when-meta="tool.is_rstudio"}
``` {.markdown filename="index.qmd" shortcodes="false"}
{{< embed notebooks/explore-earthquakes.qmd#fig-spatial-plot >}}
```
:::

::: {.content-visible when-meta="tool.is_vscode"}
``` {.markdown filename="index.qmd" shortcodes="false"}
{{< embed notebooks/data-screening.qmd#fig-spatial-plot >}}
```
:::

The double curly braces (`{{`) and angle brackets (`<`) indicate this is a shortcode. The `embed` shortcode requires a path to a notebook chunk. In this case, it's the file path to a source notebook, `{{< meta tool.notebook-file >}}`, followed by `#` and a chunk label. The chunk label is set using the Quarto chunk option `label` in `{{< meta tool.notebook-file >}}` notebook:

::: {.content-visible when-meta="tool.is_rstudio"}
````{.qmd filename="explore-earthquakes.qmd"}
```{{r}}
#| label: fig-spatial-plot
#| fig-cap: "Locations of earthquakes on La Palma since 2017"
#| fig-alt: "A scatterplot of earthquake locations plotting latitude 
#|   against longitude."
la_palma |> 
  ggplot(aes(Longitude, Latitude)) +
  geom_point(aes(color = Magnitude, size = 40-`Depth(km)`)) +
  scale_color_viridis_c(direction = -1) + 
  scale_size(range = c(0.5, 2), guide = "none") +
  theme_bw()
```
````
:::

::: {.content-visible when-meta="tool.is_vscode"}
````{.qmd filename="data-screening.qmd"}
```{{python}}
#| label: fig-spatial-plot
#| fig-cap: Locations of earthquakes on La Palma since 2017.
#| fig-alt: A scatterplot of earthquake locations plotting latitude against longitude.
from matplotlib import colormaps
cmap = colormaps['viridis_r']
ax = df.plot.scatter(x="Longitude", y="Latitude", 
                     s=47-df["Depth(km)"], c=df["Magnitude"], 
                     figsize=(12,10), grid="on", cmap=cmap)
colorbar = ax.collections[0].colorbar
colorbar.set_label("Magnitude")

plt.show()
```
````
:::

Just like any figure, using a label starting with `fig-` allows it to be cross referenced in the text. Any other options, like the figure caption (`fig-cap`) and alt text (`fig-alt`), can also be set in the source notebook.

Whenever you change the content of `{{< meta tool.notebook-file >}}`, including updating chunk options like the caption, it will be re-rendered. 
Consequently, the code in `{{< meta tool.notebook-file >}}` will also be re-run.

::: {.content-visible when-meta="tool.is_rstudio"}
To re-run the code in this notebook, you'll need to have the tidyverse package: 
``` r
install.packages("tidyverse")
```
:::


For example, if you edit the caption to:

```{.r}
#| fig-cap: "Earthquakes on La Palma since 2017."
```

You'll notice in the background `quarto preview` re-renders the file:
```{.bash filename="Terminal"}
processing file: {{< meta tool.notebook-file >}}
                                                                                    output file: {{< meta tool.notebook-file >}}

Rendering output notebook [notebooks/{{< meta tool.notebook-file >}}]
Rendering HTML preview [notebooks/{{< meta tool.notebook-file >}}]
```

And then the caption in the main article preview updates.


# quarto-web/docs/manuscripts/authoring/_citations.qmd

::: callout-tip

## Article Citation

This section describes adding citations in the text of your article. The citation for your own article that is displayed at the bottom of the article webpage is controlled using [Front Matter](#front-matter).

:::

To add citations you need a bibliography file, `.bib`, containing the citation data. You can specify this file in the document YAML with the `bibliography` option. For example, the citation data for `{{< meta tool.article-file >}}` is stored in `references.bib`:

```yaml
bibliography: references.bib
```

The file `references.bib` contains only one citation:

```{.bib filename="references.bib"}
@article{marrero2019,
  author = {Marrero, Jos{\' e} and Garc{\' i}a, Alicia and Berrocoso, Manuel and Llinares, {\' A}ngeles and Rodr{\' i}guez-Losada, Antonio and Ortiz, R.},
  journal = {Journal of Applied Volcanology},
  year = {2019},
  month = {7},
  pages = {},
  title = {Strategies for the development of volcanic hazard maps in monogenetic volcanic fields: the example of {La} {Palma} ({Canary} {Islands})},
  volume = {8},
  doi = {10.1186/s13617-019-0085-5},
}
```

To cite an article from the bibliography in your text, you use `@` followed by the citation identifier, e.g. `marrero2019`. For example, the article includes this line citing this reference: 

```markdown
Studies of the magma systems feeding the volcano, such as @marrero2019, have proposed ...
```

This renders as:

> Studies of the magma systems feeding the volcano, such as Marrero et al. (2019), have proposed ...

Hovering over the citation text reveals the full reference details. Clicking on the citation takes a reader to the reference in the References section at the end of the article:

![](images/article-references.png){fig-alt="Screenshot of the rendered article showing a section titled References. Below the title is a full reference starting 'Marrero, José, '." .border}



The above citation is an example where the author's names are incorporated into the sentence itself. Another common style is to place the citation within parentheses, often at the end of a sentence. You can achieve this by enclosing the citation syntax in square brackets `[`. For example,

```markdown
A prior study of the magma systems feeding the volcano proposed that there are two main magma reservoirs feeding the Cumbre Vieja volcano [@marrero2019].
```

This renders as:

> A prior study of the magma systems feeding the volcano proposed that there are two main magma reservoirs feeding the Cumbre Vieja volcano (Marrero et al. 2019).

There are many other syntax variations to include page numbers, chapters, or exclude the author names. You can read more in the [Citations & Footnotes](/docs/authoring/footnotes-and-citations.html) documentation.

::: {.content-visible unless-meta="tool.is_jupyterlab"}

The Visual Editor **Insert -> Citation** dialog has utilities for adding citations from their DOI, your Zotero library, and public databases like Crossref, PubMed and DataCite. This provides an easy way to build the  bibliography file (`.bib`) and generate the markdown citation syntax. 
:::


# quarto-web/docs/manuscripts/authoring/_visual-editor.qmd

The {{< meta tool.name >}} visual editor provides a [WYSIWYM](https://en.wikipedia.org/wiki/WYSIWYM) editing interface for Quarto notebooks. Some tasks, like adding citations, or creating tables, are easier in the visual editor - we'll point these out as we introduce them.

::: {.content-visible when-meta="tool.is_rstudio"}
::: {layout-ncol="2"}
![Source Editor](images/source-editor-rstudio.png){.border fig-alt="Screenshot of the file `index.qmd` open in the Source Editor. File shows line numbers and the raw markdown for inserting a figure and table."}

![Visual Editor](images/visual-editor-rstudio.png){.border fig-alt="Screenshot of the file `index.qmd` open in the Visual Editor. File shows a figure and table."}
:::
:::

::: {.content-visible when-meta="tool.is_vscode"}
::: {layout-ncol="2"}
![Source Editor](images/source-editor-vscode.png){.border fig-alt="Screenshot of the file `index.qmd` open in the Source Editor. File shows line numbers and the raw markdown for inserting a figure and table."}

![Visual Editor](images/visual-editor-vscode.png){fig-alt="Screenshot of the file `index.qmd` open in the Visual Editor. File shows a figure and table." .border}
:::
:::

::: {.content-visible when-meta="tool.is_rstudio"}
To toggle between source and visual editor modes, toggle the "Source" and "Visual" menu items at the top of the Source Editor window, or use the keyboard shortcut {{< kbd mac=Shift-Command-F4 win=Shift-Control-F4 >}}.

![](images/source-visual-buttons-rstudio.png){fig-alt="Screenshot of the Source Editor pane in RStudio. The Visual button in the toolbar at the top of the Editor pane is highlighted."}

You can read more about RStudio's visual editor at [Visual Editing in RStudio](/docs/visual-editor/).
:::

::: {.content-visible when-meta="tool.is_vscode"}
To toggle between source and visual editor modes, use the Editor menu and select "Edit in Visual Mode" or "Edit in Source Mode" mode, or use the keyboard shortcut {{< kbd mac=Shift-Command-F4 win=Shift-Control-F4 >}}.

![](images/source-visual-menu-vscode.png){fig-alt="Screenshot of the Editor menu in VS Code. The 'Edit in Visual Mode' item in the '...' menu is highlighted."}

There are other ways to switch modes, read about them, and other features of the visual editor at [Visual Editing in VS Code](/docs/visual-editor/vscode/).
:::

You can switch between the source and visual editor at any time - the location of your cursor and undo/redo history is preserved.


# quarto-web/docs/manuscripts/authoring/index.qmd

---
title: "Authoring Manuscripts"
include-in-header: ../_redirect.html
---


# quarto-web/docs/manuscripts/authoring/_authoring-content.qmd

{{< include ../_tool-chooser.md >}}

## Overview

{{< include _overview.qmd >}}

## Setup

{{< include _setup.qmd >}}

## Project Files

{{< include _files.qmd >}}

## Workflow

::: {.content-visible when-meta="tool.is_jupyterlab"}
{{< include _workflow-ipynb.qmd >}}
:::

::: {.content-visible unless-meta="tool.is_jupyterlab"}
{{< include _workflow-qmd.qmd >}}
:::

::: {.content-visible unless-meta="tool.is_jupyterlab"}
## Visual Editor

{{< include _visual-editor.qmd >}}

:::

## Notebook Structure

{{< include _structure.qmd >}}

## Front Matter

{{< include _front-matter.qmd >}}

## Markdown

{{< include _markdown.qmd >}}

## Computations {#inline-computations}

{{< include _inline-computations.qmd >}}

## Citations

{{< include _citations.qmd >}}

## Cross References {#cross-ref}

{{< include _cross-refs.qmd >}}

## Equations

{{< include _equations.qmd >}}

## Tables

{{< include _tables.qmd >}}

## Static Figures

{{< include _figures.qmd >}}

## External Embeds {#embed}

::: {.content-visible when-meta="tool.is_jupyterlab"}
{{< include _embeds-ipynb.qmd >}}
:::

::: {.content-visible unless-meta="tool.is_jupyterlab"}
{{< include _embeds-qmd.qmd >}}
:::

## Up Next

{{< include _footer.qmd >}}


# quarto-web/docs/manuscripts/authoring/_inline-computations.qmd

::: {.content-visible unless-meta="tool.is_rstudio"}
::: callout-tip
## Python Examples

This section uses Python code examples, but Quarto also supports R, Julia and Observable.

::: {.content-visible when-meta="tool.is_jupyterlab"}
You don't need to rerun the Python code to follow along, but if you would like to, you'll need the `matplotlib` and `numpy` packages.
:::
:::
:::

::: {.content-visible when-meta="tool.is_rstudio"}
::: callout-tip
## R Examples

This section uses R code examples, but Quarto also supports Python, Julia and Observable.
:::
:::

Your article can include executable code. By default, code itself will not display in the article, but any output including tables and figures will. When you include code in your article, you'll also get an additional link to the "Article Notebook" under Notebooks on the manuscript webpage. This is a rendered version of your article notebook that includes the code.

For example, `{{< meta tool.article-file >}}`, includes:

::: {.content-visible when-meta="tool.is_jupyterlab"}
``` python
import matplotlib.pyplot as plt
import numpy as np
eruptions = [1492, 1585, 1646, 1677, 1712, 1949, 1971, 2021]
```
:::

::: {.content-visible when-meta="tool.is_rstudio"}
``` r
eruptions <- c(1492, 1585, 1646, 1677, 1712, 1949, 1971, 2021)
n_eruptions <- length(eruptions)
```
:::

::: {.content-visible when-meta="tool.is_vscode"}
```{{python}}
import matplotlib.pyplot as plt
import numpy as np
eruptions = [1492, 1585, 1646, 1677, 1712, 1949, 1971, 2021]
```
:::

This code doesn't appear in the rendered article, but does in the "Article Notebook".

::: {.content-visible unless-meta="tool.is_rstudio"}
::: {layout-ncol=2}
![Rendered Article](images/code-webpage.png){.border fig-alt="Screenshot of the rendered article with a section starting with 'Let x denote'. No code is visible."}

![Article Notebook](images/code-article-notebook.png){.border fig-alt="Screenshot of the Article Notebook with a section starting with 'Let x denote'. Code is visible in two cells. The first cell starts 'import matplotlib'"}
:::
:::

::: {.content-visible when-meta="tool.is_rstudio"}
::: {layout-ncol=2}
![Rendered Article](images/code-webpage.png){.border fig-alt="Screenshot of the rendered article with a section starting with 'Let x denote'. No code is visible."}

![Article Notebook](images/code-article-notebook-r.png){.border fig-alt="Screenshot of the Article Notebook with a section starting with 'Let x denote'. Code is visible in two blocks. The first block starts 'eruptions <-'"}
:::
:::

You can add Quarto options to code cells by adding a `#|` comment to the top, followed by the option in YAML syntax. For example, adding the `echo` option with the value `true` would look like this:

::: {.content-visible when-meta="tool.is_jupyterlab"}
``` python
#| echo: true
import matplotlib.pyplot as plt
import numpy as np
eruptions = [1492, 1585, 1646, 1677, 1712, 1949, 1971, 2021]
```
:::

::: {.content-visible when-meta="tool.is_rstudio"}
```{{r}}
#| echo: true
eruptions <- c(1492, 1585, 1646, 1677, 1712, 1949, 1971, 2021)
n_eruptions <- length(eruptions)
```
:::

::: {.content-visible when-meta="tool.is_vscode"}
```{{python}}
#| echo: true
import matplotlib.pyplot as plt
import numpy as np
eruptions = [1492, 1585, 1646, 1677, 1712, 1949, 1971, 2021]
```
:::

The `echo` option describes whether the code is included in the rendered article. If you make this change and save `{{< meta tool.article-file >}}`, you'll see this code now appears in the article.

::: {.content-visible unless-meta="tool.is_rstudio"}
You can find a list of all the code cell options available on the [Jupyter Code Cell](/docs/reference/cells/cells-jupyter.html) reference page.
:::

::: {.content-visible when-meta="tool.is_rstudio"}
You can find a list of all the code cell options available on the [Knitr Code Cell](/docs/reference/cells/cells-knitr.html) reference page.
:::

The next code cell creates a figure:

::: {.content-visible when-meta="tool.is_jupyterlab"}
``` python
#| label: fig-timeline
#| fig-cap: Timeline of recent earthquakes on La Palma
#| fig-alt: An event plot of the years of the last 8 eruptions on La Palma.

plt.figure(figsize=(6, 1))
plt.eventplot(eruptions, lineoffsets=0, linelengths=0.1, color='black')
plt.gca().axes.get_yaxis().set_visible(False)
plt.ylabel('')
plt.show()
```
:::

::: {.content-visible when-meta="tool.is_rstudio"}
```{{r}}
#| label: fig-timeline
#| fig-cap: Timeline of recent earthquakes on La Palma
#| fig-alt: An event plot of the years of the last 8 eruptions on La Palma.
#| fig-height: 1.5
#| fig-width: 6
par(mar = c(3, 1, 1, 1) + 0.1)
plot(
  eruptions, rep(0, n_eruptions), 
  pch = "|", axes = FALSE
)
axis(1)
box()
```
:::

::: {.content-visible when-meta="tool.is_vscode"}
```{{python}}
#| label: fig-timeline
#| fig-cap: Timeline of recent earthquakes on La Palma
#| fig-alt: An event plot of the years of the last 8 eruptions on La Palma.

plt.figure(figsize=(6, 1))
plt.eventplot(eruptions, lineoffsets=0, linelengths=0.1, color='black')
plt.gca().axes.get_yaxis().set_visible(False)
plt.ylabel('')
plt.show()
```
:::

The `label` option is used to add an identifier to code cell and its output, for example to allow cross referencing. The prefix `fig-` is required for figure cross references, but the suffix, in this case `timeline`, is up to you. You'll learn more about [Cross References](#cross-ref) below. 

The option `fig-cap` provides the caption text displayed below the figure in the manuscript, and  `fig-alt` provides alt text for the figure, helping your manuscript webpage to meet accessibility guidelines. 

Computations are also a good way to include tables based on data. You can read more about doing this in the Quarto documentation on [Tables from Computations](/docs/authoring/tables.html#computations).

If you have code output you don't want to include in your article you can use `output: false`. For example, you may have a value that is helpful for writing your content, but you don't want it to appear in the article itself. The next code cell is an example:

::: {.content-visible when-meta="tool.is_jupyterlab"}
``` python
#| output: false
avg_years_between_eruptions = np.mean(np.diff(eruptions[:-1]))
avg_years_between_eruptions
```
:::

::: {.content-visible when-meta="tool.is_rstudio"}
```{{r}}
#| output: false
avg_years_between_eruptions <- mean(diff(eruptions[-n_eruptions]))
avg_years_between_eruptions
```
:::

::: {.content-visible when-meta="tool.is_vscode"}
```{{python}}
#| output: false
avg_years_between_eruptions = np.mean(np.diff(eruptions[:-1]))
avg_years_between_eruptions
```
:::

If you are viewing the rendered "Article Notebook", you'll see the value of `avg_years_between_eruptions` displayed below this code, but the value does not appear in the rendered article.

If you'd like to exclude a cell and its output from both the article and the rendered notebook, you could use `include: false` instead:

::: {.content-visible when-meta="tool.is_jupyterlab"}
``` python
#| include: false
avg_years_between_eruptions = np.mean(np.diff(eruptions[:-1]))
avg_years_between_eruptions
```
:::

::: {.content-visible when-meta="tool.is_rstudio"}
```{{r}}
#| include: false
avg_years_between_eruptions <- mean(diff(eruptions[-n_eruptions]))
avg_years_between_eruptions
```
:::

::: {.content-visible when-meta="tool.is_vscode"}
```{{python}}
#| include: false
avg_years_between_eruptions = np.mean(np.diff(eruptions[:-1]))
avg_years_between_eruptions
```
:::

::: {.content-visible unless-meta="tool.is_rstudio"}
You can also use computed values directly in your article text by using the `Markdown()` function from the IPython display module. Read more in [Inline Code](/docs/computations/execution-options.html#inline-code).
:::

::: {.content-visible when-meta="tool.is_rstudio"}
You can use computed values directly in your article text using the syntax `` `r expr` ``. For example, consider this line in `index.qmd`:

``` markdown
Based on data up to and including 1971, eruptions on La Palma happen every `r round(avg_years_between_eruptions, 1)` years on average.
```

When rendered, it displays as:

> Based on data up to and including 1971, eruptions on La Palma happen every 79.8 years on average.

You can read more about using code inline at [Inline Code](/docs/computations/execution-options.html#inline-code).
:::

Rather than including computations directly in your article you can also embed outputs from other notebooks, read more below in [Embedding Notebooks](#embed).

### When is code executed?

::: {.content-visible when-meta="tool.is_jupyterlab"}

By default, Quarto doesn't execute any code in `.ipynb` notebooks.
If you need to update cell outputs, run the appropriate cells, and save the notebook. 

:::

::: {.content-visible unless-meta="tool.is_jupyterlab"}

By default, Quarto will execute code in a `.qmd` notebook during the rendering process. This means, as you edit `index.qmd` you may notice messages that indicate code is being run.

This manuscript template uses Quarto's freeze feature, which allows us to avoid having to set up a computational environment on GitHub during the publishing process. Freeze saves the rendered versions of notebooks so that they are not re-rendered, and consequently, the code is not re-evaluated unless their source changes.

You may not have noticed, but the first time you rendered the manuscript no code was evaluated. This was because the template repo included the `_freeze/` folder, and the contents of `index.qmd` had not changed since the freeze was generated. As you change `index.qmd`, code will be re-evaluated, and the contents of `_freeze/` will be updated. Remember when you come to publish, you'll need to commit the changes in `_freeze/` as well.

:::



# quarto-web/docs/manuscripts/authoring/_structure.qmd

::: {.content-visible when-meta="tool.is_jupyterlab"}
The file `index.ipynb` is a Jupyter Notebook. Like any Jupyter Notebook it contains cells that could be raw, markdown or code. There are three features of this notebook that are Quarto specific:

-   The first cell contains a YAML header that is used to set document metadata, including scholarly front matter. This cell must start and end with a line of three dashes (`---`), and within these lines, content is parsed as YAML. You'll notice the cell itself is set to be a Markdown cell; this allows the Quarto Jupyter Lab Extension to visually emulate how some of these options will appear in the rendered document.

-   The other markdown cells use Quarto specific markdown syntax to include things like figures, tables, equations, cross references and citations.

-   Code cells may have special Quarto comments at the top that start with `#|`. These comments set Quarto options that control how the code and its output appear in the article.

The rest of this page walks you through the cells in this article from top to bottom, introducing you to the Quarto features you'll most likely need to write a scholarly article.
:::

::: {.content-visible unless-meta="tool.is_jupyterlab"}
The file `index.qmd` is a Quarto markdown file. It contains three types of content:

-   It starts with a YAML header that is used to set document metadata, including scholarly front matter. The YAML header starts and ends with a line of three dashes (`---`), and within these lines, content is parsed as YAML. 

-   It may include executable code chunks which start with three backticks followed by the code language in curly braces (e.g. ` ```{r} ` or ` ```{python} `). These code chunks may include Quarto comments at the top which start with `#|`. These comments set Quarto options that control how the code and its output appear in the article.

-   The rest of the document is interpreted as Quarto specific markdown, which allows you to include things like figures, tables, equations, cross references and citations.

The rest of this page walks you through this article from top to bottom, introducing you to the Quarto features you'll most likely need to write a scholarly article.
:::



# quarto-web/docs/manuscripts/authoring/_figures.qmd

To include a figure from a file, the markdown syntax looks like:

``` markdown
![Caption](file_path_to_image)
```

For example, to include the `la-palma-map.png` image from the `images/` folder in the project, along with the caption "Map of La Palma", you would write:

``` markdown
![Map of La Palma](images/la-palma-map.png)
```

::: callout-tip
## Image File Location

You don't have to store your images in a folder called `images/`, although it is a common convention. Your images can be anywhere **inside** your manuscript project directory, just make sure you include the full path to the image, relative to the location of `{{< meta tool.article-file >}}`.
:::

The actual markdown in `{{< meta tool.article-file >}}` includes a further attribute, `#fig-map` inside curly braces following the image path to provide a label for cross references:

``` markdown
![Map of La Palma](images/la-palma-map.png){#fig-map}
```

Another attribute that you may wish to add is `fig-alt`, the alt text to be provided for the image. For example:

``` markdown
![Map of La Palma](images/la-palma-map.png){#fig-map fig-alt="A map of the Canary Islands. The second most west island, La Palma, is highlighted."}
```

You can read more about including figures in Quarto documents, including how to resize figures and arrange multiple figures, on the Quarto docs [Figures](/docs/authoring/figures.qmd) page.


# quarto-web/docs/manuscripts/authoring/_equations.qmd

Quarto markdown can include equations specified in LaTeX notation. Use single dollar signs (`$`) to add an equation inline or double dollar signs (`$$`) to add a display equation. Both of these are illustrated in the following paragraph in `{{< meta tool.article-file >}}`:

``` markdown
Let $x$ denote the number of eruptions in a year. Then, $x$ can be modeled by a Poisson distribution

$$
p(x) = \frac{e^{-\lambda} \lambda^{x}}{x !}
$$ {#eq-poisson}

where $\lambda$ is the rate of eruptions per year. Using @eq-poisson, the probability of an eruption in the next $t$ years can be calculated.
```
Notice the display equation has a label added in curly braces after the closing `$$`. This allows it to be referenced using `@eq-poisson` in the text.

When rendered, this displays as:

> Let $x$ denote the number of eruptions in a year. Then, $x$ can be modeled by a Poisson distribution
> $$
> p(x) = \frac{e^{-\lambda} \lambda^{x}}{x !}
> $$ {#eq-poisson}
> where $\lambda$ is the rate of eruptions per year. Using @eq-poisson, the probability of an eruption in the next $t$ years can be calculated.


# quarto-web/docs/manuscripts/authoring/_footer.qmd

You've now covered the main features of Quarto for authoring a manuscript. You've edited `{{< meta tool.article-file >}}`, added resources like figures, notebooks or bibliographic data, and previewed the result.

Once, you are happy with the changes you've made, you'll need update your public manuscript webpage.

Head on to [Publishing](../publishing.qmd) to learn how to publish and share your manuscript with the world.



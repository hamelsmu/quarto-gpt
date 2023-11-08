# quarto-web/docs/visual-editor/content.qmd

---
title: "Content Editing"
---

Visual mode supports editing all of Pandoc markdown. Standard formatting commands (headings, bold, italic, etc.) work just the way they do in a conventional word processor.

See the [Using the Editor](index.qmd#using-the-editor) section for more details on how to access core editing commands. Note also that you can access all editing commands via [keyboard shortcuts](options.qmd#shortcuts).

Editing of links, images, blockquotes, lists, tables, etc. is also available, as is the ability to specify Pandoc attributes and insert special characters and emojis.

## Editing Tables

You can insert a table using the **Table** menu. You can then use either the main menu or a context menu to insert and delete table rows and columns:

![](images/visual-editing-table-context.png)

Note that if you select multiple rows or columns the insert or delete command will behave accordingly. For example, to insert 2 rows, first select 2 rows then use the insert command.

When you make a selection of multiple rows and/or columns as illustrated above, you can also copy and paste groups of cells within the table.

## Editing Lists

As described above, you can create a new list by just typing `-` or `1.` at the beginning of an empty paragraph. To add items to the list, just press **Enter** within a list item. To exit the list, press **Enter** within an empty list item.

While this covers many simple list editing tasks, there is a variety of other actions you may want to take within lists, including creating nested lists and adding paragraphs or code blocks to an exiting list item. From an empty list item (pictured at left), the following keyboard gestures can be used to do this:

| **Empty Item**<br> (*enter to exit list*) | **Tab**<br> (*add sublist*)                 | **Backspace** <br> (*add block*)          |
|------------------------|-------------------------|------------------------|
| ![](images/visual-editing-list-item.png)  | ![](images/visual-editing-list-sublist.png) | ![](images/visual-editing-list-block.png) |

You can also use **Shift+Tab** to lift a list item into the previous level.

### Tight Lists

Markdown distinguishes between normal and *tight* lists, where tight lists have less vertical spacing between items. In markdown source code, you designate a tight list by having no empty lines between your list items.

Visual mode creates normal lists by default (you can change this behavior via [Editor Options](options.qmd)). You can toggle between normal and tight lists using the <kbd>⌥⌘ 9</kbd> keyboard shortcut. You can also change the list type using the **Format -\> Edit Attributes** dialog (also accessible via the <kbd>F4</kbd> shortcut). If you have existing tight lists in your markdown source files, they will remain so within the visual editor.

## Pandoc Attributes

Several of Pandoc's block types (e.g. headings, code blocks, and divs) enable you to specify a set of [custom attributes](https://pandoc.org/MANUAL.html#heading-identifiers). Attributes include IDs and class names, as well as arbitrary key-value pairs that are passed through to output formats (e.g. as attributes for HTML tags). For these block types, an edit button will appear at the the top right when your cursor is within the block:

![](images/visual-editing-attributes.png)

Note that any ID as well as the first class specified within the attributes are also displayed. Click the edit button or use the <kbd>F4</kbd> keyboard shortcut to edit the attributes.

## Special Characters

### Hard Line Breaks

You can insert a [hard line break](https://practicaltypography.com/hard-line-breaks.html) using the **Insert -\> Special Characters -\> Hard Line Break** command or via the <kbd>⇧ Enter</kbd> keyboard shortcut.

### Non-Breaking Spaces

You can insert a [non-breaking space](https://en.wikipedia.org/wiki/Non-breaking_space) using the **Insert -\> Special Characters -\> Non-Breaking Space** command or via the <kbd>⌃ Space</kbd> keyboard shortcut. Non-breaking spaces are displayed with an alternate background color to distinguish them from normal spaces.

A markdown non-breaking space will result in the `&nbsp;` character within HTML output and a `~` character within LaTeX output.

### Emojis

To insert an emoji, you can use either the **Insert** menu or the requisite markdown shortcut plus auto-complete:

| **Insert -\> Special Characters -\> Emoji...** | Markdown Shortcut                               |
|------------------------------------|------------------------------------|
| ![](images/visual-editing-emoji-dialog.png)    | ![](images/visual-editing-emoji-completion.png) |

For markdown formats that support text representations of emojis (e.g. `:grinning:`), the text version will be written. For other formats the literal emoji character will be written. Currently, the [gfm](../output-formats/gfm.qmd) and [hugo](../output-formats/hugo.qmd) (with `enableEmoji = true` in the site config) formats both support text representation of emojis.

If you want to add support for markdown emoji output to another Quarto format, you can add the `emoji` extension to the `from` option in document metadata. For example:

``` yaml
---
title: "My Document"
from: markdown+emoji
---
```

### Unicode Symbols

To insert an arbitrary Unicode character, use **Insert -\> Special Characters -\> Unicode...**:

![](images/visual-editing-unicode.png)

You can search for characters either by name or by entering an explicit Unicode code point (e.g. "U+0420").

### Smart Punctuation

When the Pandoc [`smart`](https://pandoc.org/MANUAL.html#typography) extension is enabled (which it is by default), straight quotes are interpreted as curly quotes, `---` as em-dashes, `--` as en-dashes, and `...` as ellipses. In addition, non-breaking spaces are inserted after certain abbreviations, such as "Mr."

Visual mode supports these same transformations (so when you type `---` it becomes an em-dash). If you didn't intend for this transformation to occur just hit backspace and it will be reverted.

## Spell-Checking

When RStudio real time spell-checking is enabled (you can do this using **Spelling** preferences), misspelled words will be underlined as you type:

![](images/visual-editing-spelling.png)

To resolve a spelling error, right-click on the misspelled word, then either choose an alternate spelling, ignore the word (which applies to the current document only), or add the word to your user dictionary (which applies to all documents).

If you ignore a word by mistake, right-click it again to unignore it. If you want to edit your personal dictionary, use the **Edit User Dictionary...** button located within **Spelling** preferences.

## Commenting

When reviewing a document you often want to provide inline comments with suggested revisions. This is possible in Quarto using HTML comments (which are ignored by all output formats). Visual mode includes a command for inserting HTML comments as well as special highlighting treatment to easily parse out editing comments from surrounding text.

![](images/visual-editing-comment.png)

Note that the `#` prefix used in the comment is what triggers the special background highlighting. If you remove the `#` it will still be a valid HTML comment, but just won't be highlighted as shown above.

You can insert an HTML comment using the Comment button on the toolbar or via the <kbd>⇧⌘ C</kbd> keyboard shortcut. Remember, HTML comments won't show up in rendered output so they are ideal both for review but also for leaving yourself to-do notes within a document.

## CSS Styles

One of the benefits of authoring with markdown is that your content can be easily published to a wide variety of formats. This is possible in significant measure because of the limitations that markdown imposes: you author in terms of the structure and semantics of your content, rather than worrying about specifically how things will appear.

Sometimes however you know that you'll be publishing to HTML, and you want to exert more control over how things look. In this case, you can use [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) (Cascading Style Sheets) along with markdown to do custom formatting. This section covers how to:

1.  Define CSS styles for your document; and

2.  Apply those styles to entities within your document.

If you are new to CSS, you may want to [brush up on the basics](https://developer.mozilla.org/en-US/docs/Learn/CSS) before proceeding.

::: {.callout-note appearance="simple"}
CSS styles apply **only** to HTML output, and will not have any impact on the formatting of other output types like PDF or MS Word.
:::

### Defining Styles

The best way to include CSS styles is to create an external stylesheet (e.g. `styles.css`), then include it within the output options of your document. For example:

``` yaml
---
title: "CSS Demo"
format:
  html:
    css: styles.css
---
```

The `styles.css` file might look something like this:

``` css
.important {
  color: maroon;
}

.illustration {
  border: 1px solid rgb(230, 230, 230); 
}
```

Note that it's also possible to define styles inline with a [CSS code chunk](https://bookdown.org/yihui/rmarkdown/language-engines.html#javascript-and-css), but we recommend using an external file for easier manageability.

Within a markdown document you can apply one or more CSS classes to various document entities including headings, images, divs, and spans. CSS classes are applied using [pandoc attributes](content.qmd#pandoc-attributes). Once you've applied a class to an entity, it will derive its formatting from the CSS properties of the specified class.

### Headings

To add a CSS class to a heading, use the edit button at the top right of the heading that appears when your cursor is within it (or use the <kbd>F4</kbd> keyboard shortcut):

![](images/visual-editing-css-heading.png)

Note the presence of the `.important` class within the **Edit Attributes** dialog.

CSS classes applied to headings affect all content beneath the heading (an HTML `<section>` tag is wrapped around the content by Pandoc), so heading classes are a great way to provide custom styles for entire sections of your document.

::: {.callout-note appearance="simple"}
Note that the visual editor doesn't currently render content using styles applied through CSS classes so you won't see the custom formatting while editing. You will however see it when rendering and previewing the HTML version of the document.
:::

### Images

You can apply CSS classes to images (for example, to give them a special border) using the standard **Image** dialog. To do this, double-click the image (or use the <kbd>F4</kbd> shortcut with the image selected) and apply the desired classes:

![](images/visual-editing-css-image.png)

Note again that the visual editor won't display your image with the applied CSS classes while editing, however when actually rendering the document to HTML you'll see the styles reflected.

### Divs

Divs are special entities that allow you to apply identifiers and/or styles to a region of a document. Divs are block elements (like paragraphs).

You can create divs using the **Insert -\> Div** command, and you can apply attributes (including CSS classes) to divs the same way as you apply attributes to headings (clicking the edit button or using the <kbd>F4</kbd> keyboard shortcut when you are within a div):

![](images/visual-editing-css-div.png)

Note the presence of the `.important` class within the **Div Attributes** dialog.

### Spans

Spans are special entities that allow you to apply identifiers and/or styles to a region of text. Spans are inline formatting marks (like bold or italic).

Spans can be created by selecting text and using the **Format -\> Span** command:

![](images/visual-editing-css-span.png)

Here we've applied a span to the text "customize PDF reports" and we've used the span to apply the `.important` CSS class. Note that as with headings and images the formatting is not displayed in the visual editor, but will be visible when the document is rendered.


# quarto-web/docs/visual-editor/markdown.qmd

---
title: "Markdown Output"
---

## Overview

The Quarto visual editor generates markdown using Pandoc. This means that in some cases your markdown will be *rewritten* to conform to standard Pandoc idioms. For example, Pandoc inserts 3 spaces after list bullets and automatically escapes characters that might be used for markdown syntax.

Here is a list of conventions for Pandoc generated markdown that might differ from your own markdown writing style:

-   `*text*` is used in preference to `_text_`
-   Backtick code blocks are written as ```` ``` {.md} ```` rather than ```` ```md ````
-   Backtick code blocks with no attributes are rendered as 4-space indented code blocks
-   Horizontal rules are written as dashes spanning the full width of the document
-   Plain links are written as `<https://yihui.org>` rather than `https://yihui.org`
-   Bullet and numbered lists use additional leading spaces before list item content
-   The blockquote character (`>`) is included on each new line of a blockquote
-   Table captions are written below rather than above tables
-   Multiline HTML and TeX blocks use the explicit raw attribute (e.g. ```` ```{=tex} ````)
-   Inline footnotes are replaced with footnotes immediately below the paragraph
-   Nested divs use `:::` at all levels so long as their attributes are distinct
-   Unnumbered sections are designated with `{.unnumbered}` rather than `{-}`
-   Characters used for markdown syntax (e.g. `*`, `_`, or `#`) are always escaped

While some of this behavior might be bothersome at first, if you decide that visual editing mode is useful for your workflow it's probably best to just adapt to writing your own markdown the same way that Pandoc does. Note that you can also [configure source mode](#canonical-mode) to write markdown using these conventions, ensuring that the same markdown is written no matter which mode edits originate from.

## Writer Options

Some aspects of markdown output can be customized via global, project, or file-level options, including:

-   How to wrap / break lines (fixed column, sentence-per-line, etc.).
-   Where to write footnotes (below the current paragraph or section, or at the end of the document).
-   Whether to use the visual mode markdown writer when saving markdown from source mode (to ensure consistency between documents saved from either mode).

You can set these options within the **R Markdown** [Global Options](options.qmd#global-options) or [Project Options](options.qmd#project-options), or can alternatively set them on a per-file basis using YAML (as described below).

### Line Wrapping

By default, the visual editor writes Markdown with no line wrapping (paragraphs all occupy a single line). This matches the behavior of markdown source editing mode within RStudio.

However, if you prefer to insert line breaks at a particular column (e.g. 72 or 80), or to insert a line break after each sentence, you can set a global or per-project [editor option](options.qmd#global-options) to this effect.

You can also set this behavior on a per-document basis via the `wrap` option. For example, to wrap lines after 72 characters you would use this:

``` yaml
---
editor:
  markdown:
    wrap: 72
---
```

To insert a line break after each sentence, use `wrap: sentence`. For example:

``` yaml
---
editor:
  markdown:
    wrap: sentence
---
```

::: {.callout-note appearance="simple"}
The algorithm used for sentence wrapping will handle English and Japanese text well, but may not detect the end of sentences accurately for other languages.
:::

If you have enabled a global line wrapping option and want to turn off wrapping for a given document, use `wrap: none`.

### References

By default, references are written at the end of the block where their corresponding footnote appears. You can override this behavior using the `references` option.

For example, to write references at the end of sections rather than blocks you would use:

``` yaml
---
title: "My Document"
editor:
  markdown:
    references: 
      location: block
---
```

Valid values for the `references` option are `block`, `section`, and `document`.

Note that you can also set a global or per-project [editor option](options.qmd#global-options) to control reference writing behavior.

If you are aggregating a set of markdown documents into a larger work, you may want to make sure that reference identifiers are unique across all of your documents (e.g. you don't want to have `[^1]` appear multiple times). You can ensure uniqueness via the `prefix` option. For example:

``` yaml
---
title: "My Document"
editor:
  markdown:
    references: 
      location: block
      prefix: "mydoc"
---
```

This will result in footnotes in this document using the specified prefix (e.g. `[^mydoc-1]`), ensuring they are globally unique across the manuscript.

::: {.callout-note appearance="simple"}
Note that if you are within a Quarto [book](../books/book-basics.qmd) project then a references `prefix` is applied automatically so no changes to `editor: markdown` are required.
:::

### Canonical Mode {#canonical-mode}

If you have a workflow that involves editing in both visual and source mode, you may want to ensure that the same markdown is written no matter which mode edits originate from. You can accomplish this using the `canonical` option. For example:

``` yaml
---
title: "My Document"
editor:
  markdown:
    wrap: 72
    references: 
      location: block
    canonical: true
---
```

With `canonical: true`, edits in visual mode and source mode will result in identical markdown output. This is especially useful if you have multiple authors collaborating using version control, with a mixture of source and visual mode editing among the authors.

## Known Limitations

There are a handful of Pandoc markdown extensions not currently supported by visual editing. These are infrequently used extensions, so in all likelihood they won't affect documents you edit, but are still worth noting.

| Extension(s)             | Example            | Behavior                                 |
|--------------------------|--------------------|------------------------------------------|
| Inline footnotes         | \^\[inline\]       | Converted to numeric footnote.           |
| Footnote identifiers     | \[\^longnote\]     | Converted to numeric footnote.           |
| Example lists            | (\@) First example | Read/written as ordinary numbered lists. |
| Auto-list numbers        | #\. First item     | Read/written as ordinary numbered lists. |
| Reference links          | This is a \[link\] | Converted to ordinary links.             |
| MultiMarkdown attributes | \# Heading \[id\]  | Converted to Pandoc attributes.          |

The visual editor is unable to parse non-YAML title blocks (e.g. old-style % titles or MultiMarkdown titles) and also unable to parse non top-level YAML metadata blocks. If these forms of metadata are encountered, visual mode will fail to load with a warning.


# quarto-web/docs/visual-editor/technical.qmd

---
title: "Technical Writing"
engine: markdown
---

Visual mode includes extensive support for Quarto features frequently used in technical writing including [equations](#equations), [citations](#citations), [cross-references](#cross-references), [footnotes](#footnotes), [embedded code](#embedded-code), and [LaTeX](#latex-and-html). This article describes using these features in more depth.

## Equations {#equations}

LaTeX equations are authored using standard Pandoc markdown syntax (the editor will automatically recognize the syntax and treat the equation as math). When you aren't directly editing an equation it will appear as rendered math:

![](images/visual-editing-math.png){fig-alt="An RMarkdown document opened in the R Studio Visual Editor. The first section is titled 'Inline Math'. It displays two separate lines of text with inline mathematical text. The second section is titled 'Display Math'. It has a line containing two $ characters, a mathematical equation written in LaTeX below that, and a  a line containing two $ characters below that. Underneath that is the rendered output of the mathematical equation."}

As shown above, when you select an equation with the keyboard or mouse you can edit the equation's LaTeX. A preview of the equation will be shown below it as you type.

## Cross References {#cross-references}

[Cross References](../authoring/cross-references.qmd) make it easier for readers to navigate your document by providing numbered references and hyperlinks to various entities like figures, tables, and equations.

Every cross-referenceable entity requires a label (unique identifier) and caption (description). For example, this is a cross-referenceable figure:

``` markdown
![Elephant](elephant.png){#fig-elephant}
```

The presence of the caption ("Elephant") and label (`#fig-elephant`) make this figure referenceable. This enables you to use the following syntax to refer to it elsewhere in the document:

``` markdown
See @fig-elephant for an illustration.
```

Here is what this would look like rendered to HTML:

![](../authoring/images/crossref-figure.png){fig-alt="A line drawing of an elephant. The text 'Figure 1: Elephant' is centered beneath it. The text 'See fig. 1 for an illustration' is aligned to the left underneath that."}

See the article on [Cross References](../authoring/cross-references.qmd) for full documentation on creating cross references and customizing their display.

Use the **Insert -\> Cross Reference...** command to insert a cross reference:

![](images/visual-editing-insert-quarto-crossref.png){.border fig-alt="The 'Insert Cross Reference' window in R Studio. There is a vertical section taking approximately a quarter of the window on the left with options for 'All Types', 'Sections', 'Figures', 'Tables', 'Equations', 'Listings', and 'Theorems'. Running along the top of the right side of the window is a search bar with the text 'fig-env' typed out. Underneath that is a large search results pane that takes up the rest of the window. Each of the search results has a title of the form '@fig-env*', an image icon to the left, the file name where the figure was found the far right side, and some of the surrounding text from where the reference was found underneath it."}

You can also just type the prefix of a cross reference label (e.g. `@fig-env`) and select it via auto-complete:

![](images/visual-editing-complete-quarto-crossref.png){.border fig-alt="A document opened in the R Studio Visual Editor. The text '@fig-env' is highlighted in blue and a pop-up window displaying search results is displayed underneath it.  Each of the search results has a title of the form '@fig-env*', an image icon to the left, the file name where the figure was found the far right side, and some of the surrounding text from where the reference was found underneath it."}

Similar to hyperlinks, you can also navigate to the location of a cross-reference by clicking the popup link that appears when it's selected:

![](images/visual-editing-popup-quarto-crossref.png){.border fig-alt="A document opened in the R Studio Visual Editor. The text '@fig-break-point' is highlighted in blue and a pop-up window displaying where that text links to is displayed beneath it. The pop-up window has 'fig-break-point' in blue, underlined text on top, the text 'Break points provide the graphical equivalent of a browser statement' in black text underneath that, and the file name 'a5-debug.qmd' in light gray text beneath that."}

You can also navigate directly to any cross-reference using IDE global search:

![](images/visual-editing-search-quarto-crossref.png){.border fig-alt="The top part of an RStudio IDE window. The phrase 'fig-en' is typed into the search bar at the center top of the page and search results appear underneath it. Each of the search results has a title of the form 'fig-en*' in black, an image icon to the left, and the file location in parentheses and light gray text to the right."}

## Footnotes {#footnotes}

You can include footnotes using the **Insert -\> Footnote** command (or the <kbd>⇧⌘ F7</kbd> keyboard shortcut). Footnote editing occurs in a pane immediately below the main document:

![](images/visual-editing-footnote.png){.illustration fig-alt="A Markdown document containing three paragraphs opened in the R Studio visual editor. The sentence at the end of the paragraph has a superscript '1' at the end, indicating a footnote. This '1' is surrounded by a blue box. There is a section divider underneath the three paragraphs, under which is another paragraph labeled '1'. "}

::: {.callout-note appearance="simple"}
By default footnotes will be written in markdown immediately below the block in which they appear. You can customize this behavior via [editor options](options.qmd).
:::

## Embedded Code {#embedded-code}

Source code which you include in a Quarto document can either be for display only or can be executed by Jupyter or Knitr as part of rendering. Code can furthermore be either inline or block.

### Displaying Code

To display but not execute code, either use the **Insert -\> Code Block** menu item, or start a new line and type either:

1.  ```` ``` ```` (for a plain code block); or
2.  ```` ```<lang> ```` (where \<lang\> is a language) for a code block with syntax highlighting.

Then press the **Enter** key. To display code inline, simply surround text with backticks (`` `code` ``), or use the **Format -\> Code** menu item.

### Code Chunks

To insert an executable code chunk, use the **Insert -\> Code Chunk** menu item, or start a new line and type:

```` ```{r} ````

Then press the **Enter** key. Note that `r` could be another language supported by knitr (e.g. `python` or `sql`) and you can also include a chunk label and other chunk options.

To include inline R code, you just create normal inline code (e.g. by using backticks or the <kbd>⌘ D</kbd> shortcut) but preface it with `r`. For example, this inline code will be executed by knitr: `` `r Sys.Date()` ``. Note that when the code displays in visual mode it won't have the backticks (but they will still appear in source mode).

### Running Chunks

You can execute the currently selected R or Python code chunk using either the run button at the top right of the code chunk or using the <kbd>⇧⌘ Enter</kbd> keyboard shortcut:

![](images/visual-editing-execute-code.png){.illustration fig-alt="An R Markdown document opened in the R Studio Visual editor. There is some plain text, a code chunk with a gray background underneath that, and the plot resulting from executing that code underneath that. In the top right corner of the code chunk is a green arrow that is used for executing that code chunk."}

You can execute code chunks up to the current one using the toolbar button or using the <kbd>⌥⌘ P</kbd> keyboard shortcut.

## LaTeX and HTML {#latex-and-html}

You can also include raw LaTeX commands or HTML tags when authoring in visual mode. The raw markup will be automatically recognized and syntax highlighted. For example:

![](images/visual-editing-raw.png){fig-alt="An R Markdown document opened in the R Studio visual editor. The first line reads: 'The implementation of the \\pkg{shiny} package uses lots of 'proglang{JavaScript}. Both '\\pkg' and '\\proglang' are highlighted in pink, indicating that Visual Editor recognizes it as a LaTeX command. The second contains a <kbd> html tag highlighted in pink. Visual Editor recognizes this as an HTML tag and renders the results in the live document."}

The above examples utilize *inline* LaTex and HTML. You can also include blocks of raw content using the commands on the **Format -\> Raw** menu. For example, here is a document with a raw LaTeX block:

![](images/visual-editing-latex-block.png){fig-alt="An R Markdown document opened in the R Studio visual editor. There is raw LaTeX describing a table surrounded by a pink rectangle. The rectangle runs the width of the page. At the top right of the pink rectangle is the label 'latex' and another button labeled by three dots. The "}

::: {.callout-note appearance="simple"}
Note that Pandoc ignores LaTeX commands when not producing LaTeX based output, and ignores HTML tags when not producing HTML based output.
:::

## Citations {#citations}

Visual mode uses the standard Pandoc markdown representation for citations (e.g. `[@citation]`). Citations can be inserted from a variety of sources:

1.  Your document bibliography.
2.  [Zotero](#citations-from-zotero) personal or group libraries.
3.  [DOI](#citations-from-dois) (Document Object Identifier) references.
4.  Searches of [Crossref](https://www.crossref.org/), [DataCite](https://datacite.org/), or [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

If you insert citations from Zotero, DOI look-up, or a search then they are automatically added to your document bibliography.

### Bibliographies

Pandoc supports bibliographies in a wide variety of formats including BibTeX and CSL. Add a bibliography to your document using the `bibliography` YAML metadata field. For example:

``` yaml
---
title: "My Document"
bibliography: references.bib
link-citations: true
---
```

Note that we've also specified the `link-citations` option, which will make your citations hyperlinks to the corresponding bibliography entries.

See the [Pandoc Citations](https://pandoc.org/MANUAL.html#citation-syntax) documentation for additional information on bibliography formats.

### Inserting Citations

You insert citations by either using the **Insert -\> Citation** command or by using markdown syntax directly (e.g. `[@cite]` or `@cite`) .

Citations go inside square brackets and are separated by semicolons. Each citation must have a key, composed of '\@' + the citation identifier from the database, and may optionally have a prefix, a locator, and a suffix. The citation key must begin with a letter, digit, or `_`, and may contain alphanumerics, `_`, and internal punctuation characters (`:.#$%&-+?<>~/`). Here are some examples:

```{=html}
<div class="illustration document-example">
  <div>
    Blah Blah <span class="citation">[</span>see <span class="citation">@doe99</span>, pp. 33-35; also <span class="citation">@smith04</span>, chap. 1<span class="citation">]</span>.
  </div>

<div>
  Blah Blah <span class="citation">[</span><span class="citation">@doe99</span>, pp. 33-35, 38-39 and <em>passim</em><span class="citation">]</span>.
  </div>

<div>
  Blah Blah <span class="citation">[</span><span
    class="citation">@smith04</span>;
  <span class="citation">@doe99</span><span class="citation">]</span>.
</div>
  <div>Smith says blah <span class="citation">[</span><span class="citation">-@smith04</span><span class="citation">]</span>.
  </div>
</div>
```
You can also write in-text citations, as follows:

```{=html}
<div class="illustration document-example">
  <div>
    <span class="citation">@smith04</span> says blah.
  </div>
  <div>
    <span class="citation">@smith04</span> <span class="citation">[</span>p. 33<span class="citation">]</span> says blah.
  </div>
</div>
```
See the [Pandoc Citations](https://pandoc.org/MANUAL.html#citations) documentation for additional information on citation syntax.

Use the <kbd><img src="images/citation_2x.png" width="15" height="14"/></kbd> toolbar button or the <kbd>⇧⌘ F8</kbd> keyboard shortcut to show the **Insert Citation** dialog:

![](images/visual-editing-citation-search.png){.illustration fig-alt="The 'Insert Citation' window in RStudio. There is a vertical section that takes approximately a quarter of the window along the left side. Arranged vertically in this section are options for 'My Sources', 'Bibliography', 'Zotero', 'My Library', 'From DOI', 'Crossref', 'DataCite', and 'PubMed'. Along the top of the section on the right is a search bar. There is a black cursor over the words 'Search for citation' in light gray text. Underneath this search bar is a search results pane. Each of the search results has a title of the form '@citation-ref', an icon to the left, the title of the paper in light gray text underneath running along the length of the search result, and the citation in light gray text to the right. Running along the bottom of the window across both the left and right sections is a box with light gray text that says 'Select Citation Keys'. Underneath this and in the bottom left corner of the window is the text 'Add to bibliography' followed by a drop-down menu that currently has the value 'references.bib.' To the right of that is a button for the 'Use in-text citation' button. Finally, there are 'Insert' and 'Cancel' buttons arranged side-by-side."}

Note that you can insert multiple citations by using the add button on the right side of the item display.

#### Markdown Syntax

You can also insert citations directly using markdown syntax (e.g. `[@cite]`). When you do this a completion interface is provided for searching available citations:

![](images/visual-editing-citations.png){fig-alt="An R Markdown document opened in the R Studio Visual Editor. There is a cursor on at the end of the text '@R-htm', which is in brackets and comes after the text 'htmltools'. There is a dropdown menu underneath this text with search results that all begin '@R-htm'. Each of the search results has a title of the form '@R-htm' in bold, an icon to the left, the title of the cited reference underneath it in gray, and the citation in gray to the right."}

#### Citation IDs

Before inserting a citation from an external source you may wish to customize its ID. Within the **Insert Citation** dialog, click the edit button on the right side of citations to change their ID:

![](images/visual-editing-citations-id.png){.illustration fig-alt="The bottom section of the 'Insert Citation' menu in R Studio. There are two citations currently selected in the 'Selected Citations' section. Each of them are surrounded by a rectangle with rounded corners, and there is an 'x' button to the left of each of them. The first citation is currently selected and there is a cursor in citation ID, indicating that you are able to edit the ID."}

If you insert a new citation via code completion, you will also be provided with the opportunity to change its default citation ID.

For citations inserted from Zotero, you can also use the [Better BibTeX](https://retorque.re/zotero-better-bibtex/) plugin to generate citation IDs (this can be enabled via [Citation Options](options.qmd#citation-options) if you have Better BibTeX installed).

#### Citation Preview

Once you've inserted a citation, place the cursor over it to see a preview of it along with a link to the source if one is available:

![](images/visual-editing-cite-popup.png){fig-alt="An R Markdown document opened in the R Studio Visual Editor. The citation '@fayad2020' is surrounded in brackets. A citation preview that appears as a result of mousing over this citation is displayed. This preview includes a full citation in MLA format of the '@fayad2020' citation."}

### Citations from DOIs {#citations-from-dois}

Use the **From DOI** pane of the **Insert Citation** dialog to insert a citation based on a DOI (e.g. that you have retrieved from a PubMed or other search):

![](images/visual-editing-citation-insert-doi.png){.illustration fig-alt="The 'Insert Citation' window in RStudio. The 'From DOI' option is selected in the left hand section. There is a DOI in the search bar that runs along the top of the section on the right, and the document corresponding to that DOI appears in the search results underneath. The search result has the title of the paper in black, the year published and journal in gray underneath that, the authors in gray underneath that, and the hyperlinked DOI underneath that. To the left of the title is a journal paper icon."}

If you are using markdown syntax, you can also paste a [DOI](https://www.doi.org/) after the `[@` and it will be looked up:

![](images/visual-editing-citations-doi.png){.illustration fig-alt="An R Markdown document opened in the R Studio Visual Editor. There is a DOI in blue text surrounded by brackets in the text. There is a pop-up window over the document titled 'Citation from DOI:' followed by the same DOI.' There is a text box titled 'Citation Id' containing a suggested citation ID that has been highlighted. Underneath that is a text box with citation information. From top to bottom, the information contained is: 'Title', 'Authors', 'Issue Date', 'Publication', 'Page(s)', 'Publisher', and 'DOI'. Underneath that are two more boxes arranged side-by-side. On the left is the 'Create bibliography file:' field with the text 'references.bib' filled in. To the right is the 'Format' drop down menu with 'BibLaTeX' currently selected."}

Once you've confirmed that it's the correct work (and possibly modified the suggested ID), the citation will be inserted into the document and an entry for the work added to your bibliography.

### Citations from Search

Use the **Crossref**, **DataCite**, and **PubMed** panes of the **Insert Citation** dialog to search one of those services for a citation:

![](images/visual-editing-citations-crossref.png){.illustration fig-alt="The 'Insert Citation' window in RStudio. The 'Crossref' option is selected and the text 'xie knitr' is in the search bar at the top of the section on the right. In the search pane are the search results."}

Items inserted from a search will automatically be added to your bibliography.

Note that for PubMed queries you can use the full supported query syntax. For example, this query searches on the author and title fields: `Peterson[Author] AND Embolism[Title]`. You can learn more about building PubMed queries here: <https://pubmed.ncbi.nlm.nih.gov/advanced/>.

### Citations from Zotero {#citations-from-zotero}

[Zotero](https://zotero.org) is a popular free and open source reference manager. If you use Zotero, you can also insert citations directly from your Zotero libraries. If you have Zotero installed locally its location will be detected automatically and citations from your main library (**My Library**) will be available:

![](images/visual-editing-citations-zotero-browse.png){.illustration fig-alt="The 'Insert Citation' window in RStudio. The 'My Library' option is selected. The search bar at the top of the right section is empty, but the search results section is filled with the contents of a Zotero reference manager library. Each of the search result icons has a small 'Z' on the bottom right to indicate that the result comes from a Zotero library."}

Zotero references will also show up automatically in completions:

<img src="images/visual-editing-citation-completions.png" width="426" fig-alt="Someone has typed &apos;@&apos; in the Visual Editor. In light gray to the right of the &apos;@&apos; is a magnifying glass followed by the text &apos;or DOI&apos;. Underneath this is a pop-up menu showing available citations. Each citation has a title of the form &apos;@citation&apos; in black, the title of the cited material in gray underneath it, an icon to the left, and the reference to the right in gray. Some of the icons have a small red &apos;Z&apos; on the bottom right corner, indicating that the corresponding reference comes from a Zotero library."/>

Items from Zotero will appear alongside items from your bibliography with a small "Z" logo juxtaposed over them. If you insert a citation from Zotero that isn't already in your bibliography then it will be automatically added to the bibliography.

If you are running both RStudio and Zotero on your desktop, then no additional configuration is required for connecting to your Zotero library. If however you using RStudio Server and/or want to access your Zotero library over the web, then a few more steps are required (see the [Zotero Web API](#zotero-web-api) section for details).

#### Group Libraries {#group-libraries}

[Zotero Groups](https://www.zotero.org/support/groups) provide a powerful way to share collections with a class or work closely with colleagues on a project. By default, Zotero Group Libraries are not included in the **Insert Citation** dialog or citation completions. However, there are options available to use group libraries at a global, per-project, or per-document level.

For example, here we specify a project-level option to use the *Reproducible Research Series (Year 1)* group library:

<img src="images/visual-editing-citation-zotero-group.png" class="illustration" width="543" fig-alt="The Project Options pane in RStudio. The R Markdown section is selected. Under the &apos;Visual Mode: Zotero&apos; options, there is an option labeled &apos;Use libraries&apos; followed by a drop down menu with the value &apos;Selected Libraries&apos; currently selected. Underneath this is a white box different library options and buttons to select them. The &apos;My Library&apos; option is unselected and the &apos;Reproducible Research Series (Year 1) option is selected."/>

You can also specify one or more libraries within YAML. For example:

``` yaml
---
title: "Reproducible Research"
zotero: "Reproducible Research Series (Year 1)"
---
```

Note that you can also turn off Zotero entirely for a document using `zotero: false`:

``` yaml
---
title: "Reproducible Research"
zotero: false
---
```

#### Zotero Web API {#zotero-web-api}

If you are using RStudio Server and/or don't have Zotero installed locally, you can still access your Zotero library using the Zotero Web API (assuming you have a Zotero web account and have synced your libraries to your account).

::: {.callout-tip appearance="simple"}
If you are running RStudio Desktop, it's generally easier to also run Zotero on your desktop and access your library locally. That said, it is possible to access Zotero web libraries from RStudio Desktop if you prefer that configuration.
:::

##### API Access Key

RStudio accesses Zotero web libraries using the Zotero Web API, so the first step is to [create a Zotero account](https://www.zotero.org/user/register) and then configure Zotero to sync its data to your account. You can do this using the **Sync** tab of the Zotero preferences:

![](images/visual-editing-citations-zotero-sync.png){.illustration fig-alt="The Sync tab of Zotero preferences."}

Once you've configured your library to sync, you need to [create a Zotero API Key](https://www.zotero.org/settings/keys/new) to use with RStudio:

![](images/visual-editing-citations-zotero-keygen.png){.illustration fig-alt="The 'New Private Key' section of Zotero. The 'Allow library access' option is selected."}

Follow the instructions to create a new access key. Note that if you want to use [Group Libraries](#group-libraries) with RStudio that you should change the default to provide read-only access to groups (as illustrated above).

Be sure to **record your key** after generating it (i.e. copy it to the clipboard and/or save it somewhere more permanent) as you won't be able to view it again after you navigate away.

Finally, go to the **R Markdown -\> Citations** preferences to connect Zotero to RStudio using your key:

<img src="images/visual-editing-citations-zotero-options.png" class="illustration" width="585" fig-alt="The global options menu in R Studio. The Citations subsection of the R Markdown section is selected, and there is a value pasted into the &apos;Zotero Web API Key&apos; box."/>

Set the Zotero Library option to "Web", then paste in your Zotero Web API Key. You can use **Verify Key...** button to confirm that your Zotero API key is working correctly.

Once you've confirmed your connection you are ready to start inserting citations from Zotero.


# quarto-web/docs/visual-editor/index.qmd

---
title: "Visual Editing in RStudio"
---

## Overview

The Quarto visual editor provides a [WYSIWYM](https://en.wikipedia.org/wiki/WYSIWYM) editing interface for all of Pandoc markdown, including tables, citations, cross-references, footnotes, divs/spans, definition lists, attributes, raw HTML/TeX, and more. The visual editor also includes support for executing code cells and viewing their output inline:

![](images/visual-editing.png){fig-alt="An RMarkdown file opened in the RStudio visual editor. The page is titled 'Filter joins'. Underneath is a table containing R syntax, mathematical notation, and definitions for the semi- and anti-joins. Underneath this table is an R code chunk that displays a graphical representation of a semi-join."}

The visual editor doesn't attempt to abstract away or obscure the underlying markdown document. Rather, it aims to provide a highly productive writing interface for people that love markdown. You can also still use most markdown constructs (e.g., \## or **bold**) directly for formatting.

### Switching Modes

Markdown documents can be edited in either source or visual mode. To switch into visual mode for a given document, use the <kbd>Source</kbd> or <kbd>Visual</kbd> button at the top-left of the document toolbar (or alternatively the <kbd>⌘⇧ F4</kbd> keyboard shortcut):

![](images/visual-editing-switch-modes.png){fig-alt="A snippet of an RStudio window showing the options bar at the top of a Quarto document."}

Note that you can switch between source and visual mode at any time (editing location and undo/redo state will be preserved when you switch).

## Getting Started

The Quarto visual editor is currently available as a feature of the [RStudio IDE](https://posit.co/download/rstudio-desktop/). The visual editor will eventually also be made available in standalone form.

To get started with the visual editor, download the latest release of RStudio ({{< var rstudio.current_release >}}) for your platform from:

<https://posit.co/download/rstudio-desktop/>

## Using the Editor

### Keyboard Shortcuts

There are keyboard shortcuts for all basic editing tasks. Visual mode supports both traditional keyboard shortcuts (e.g. <kbd>⌘ B</kbd> for bold) as well as markdown shortcuts (using markdown syntax directly). For example, enclose `**bold**` text in asterisks or type `##` and press space to create a second level heading. Here are some of the most commonly used shortcuts:

| Command      | Keyboard Shortcut | Markdown Shortcut |
|--------------|:-----------------:|:-----------------:|
| Bold         |  <kbd>⌘ B</kbd>   |    `**bold**`     |
| Italic       |  <kbd>⌘ I</kbd>   |    `*italic*`     |
| Code         |  <kbd>⌘ D</kbd>   |   `` `code` ``    |
| Heading 1    |  <kbd>⌥⌘ 1</kbd>  |        `#`        |
| Heading 2    |  <kbd>⌥⌘ 2</kbd>  |       `##`        |
| Heading 3    |  <kbd>⌥⌘ 3</kbd>  |       `###`       |
| Link         |   <kbd>⌘ K</kbd>  |     `<href>`      |
| R Code Chunk |  <kbd>⌥⌘ I</kbd>  | ```` ```{r} ````  |

See the [editing shortcuts](options.qmd#shortcuts) article for a complete list of all shortcuts.

### Insert Anything

You can also use the catch-all <kbd>⌘ /</kbd> shortcut to insert just about anything. Just execute the shortcut then type what you want to insert. For example:

::: {layout-ncol="2"}
![](images/visual-editing-omni-list.png){fig-alt="There is a line of text (with a cursor at the end) where someone has typed '/lis'. There is a drop-down menu underneath this with options for 'Bullet List', 'Numbered List', and 'Definition List' arranged vertically. The title of each item is bolded, has a small icon to the left, and a small description in lighter gray text underneath it."}

![](images/visual-editing-omni-math.png){fig-alt="There is a line of text (with a cursor at the end) where someone has typed '/ma'. There is a drop-down menu underneath this with options for 'Inline Math', 'Display Math', and 'Image...' arranged vertically. The title of each item is bolded, has a small icon to the left, and a small description in lighter gray text underneath it."}
:::

If you are at the beginning of a line (as displayed above), you can also enter plain `/` to invoke the shortcut.

### Editor Toolbar

The editor toolbar includes buttons for the most commonly used formatting commands:

![](images/visual-editing-toolbar.png){fig-alt="A snippet of an RStudio window showing the options bar at the top of an RMarkdown document."}

Additional commands are available on the **Format**, **Insert**, and **Table** menus:

| Format                                                                                           | Insert                                                                                           | Table                                                                                          |
|------------------------|------------------------|------------------------|
| ![](images/visual-editing-format-menu.png){fig-alt="The contents of the Format drop down menu."} | ![](images/visual-editing-insert-menu.png){fig-alt="The contents of the Insert drop down menu."} | ![](images/visual-editing-table-menu.png){fig-alt="The contents of the Table drop down menu."} |

## Learning More

Check out the following articles to learn more about visual markdown editing:

-   [Technical Writing](technical.qmd) covers features commonly used in scientific and technical writing, including citations, cross-references, footnotes, equations, embedded code, and LaTeX.

-   [Content Editing](content.qmd) provides more depth on visual editor support for tables, lists, pandoc attributes, CSS styles, comments, symbols/emojis, etc.

-   [Shortcuts & Options](options.qmd) documents the two types of shortcuts you can use with the editor: standard keyboard shortcuts and markdown shortcuts and describes various options for configuring the editor.

-   [Markdown Output](markdown.qmd) describes how the visual editor parses and writes markdown and describes various ways you can customize this.

# quarto-web/docs/visual-editor/options.qmd

---
title: "Shortcuts & Options"
---

## Shortcuts

Visual mode supports both traditional keyboard shortcuts (e.g. <kbd>⌘ B</kbd> for bold) as well as markdown shortcuts (using markdown syntax directly). For example, enclose `**bold**` text in asterisks or type `##` and press space to create a second level heading.

Here are the available keyboard and markdown shortcuts:

| Command             |  Keyboard Shortcut  |  Markdown Shortcut   |
|---------------------|:-------------------:|:--------------------:|
| Bold                |   <kbd>⌘ B</kbd>    |      `**bold**`      |
| Italic              |   <kbd>⌘ I</kbd>    |      `*italic*`      |
| Code                |   <kbd>⌘ D</kbd>    |     `` `code` ``     |
| Strikeout           |                     |     `~~strike~~`     |
| Subscript           |                     |       `~sub~`        |
| Superscript         |                     |      `^super^`       |
| Heading 1           |   <kbd>⌥⌘ 1</kbd>   |         `#`          |
| Heading 2           |   <kbd>⌥⌘ 2</kbd>   |         `##`         |
| Heading 3           |   <kbd>⌥⌘ 3</kbd>   |        `###`         |
| Heading Attributes  |                     |    `{#id .class}`    |
| Link                |   <kbd>⌘ K</kbd>    |       `<href>`       |
| Blockquote          |                     |         `>`          |
| Code Block          |  <kbd>⇧⌘ \\</kbd>   |    ```` ``` ````     |
| R Code Chunk        |   <kbd>⌥⌘ I</kbd>   |   ```` ```{r} ````   |
| Raw Block           |                     | ```` ```{=html} ```` |
| Div                 |                     |        `:::`         |
| Bullet List         |                     |         `-`          |
| Ordered List        |                     |         `1.`         |
| Tight List          |   <kbd>⌥⌘ 9</kbd>   |                      |
| List Check          |                     |        `[x]`         |
| Emoji               |                     |      `:smile:`       |
| Definition          |                     |         `:`          |
| Non-Breaking Space  | <kbd>⌃ Space</kbd>  |                      |
| Hard Line Break     | <kbd>⇧ Enter</kbd>  |                      |
| Paragraph           |   <kbd>⌥⌘ 0</kbd>   |                      |
| Image               |   <kbd>⇧⌘ I</kbd>   |                      |
| Footnote            |  <kbd>⇧⌘ F7</kbd>   |                      |
| Citation            |  <kbd>⇧⌘ F8</kbd>   |         `[@`         |
| Table               |   <kbd>⌥⌘ T</kbd>   |                      |
| Editing Comment     |   <kbd>⇧⌘ C</kbd>   |                      |
| Select All          |   <kbd>⌘ A</kbd>    |                      |
| Clear Formatting    |   <kbd>⌘ \\</kbd>   |                      |
| Edit Attributes     |    <kbd>F4</kbd>    |                      |
| Run Code Chunk      | <kbd>⇧⌘ Enter</kbd> |                      |
| Run Previous Chunks |  <kbd>⇧⌥⌘ P</kbd>   |                      |

::: {.callout-tip appearance="simple"}
For markdown shortcuts, if you didn't intend to use a shortcut and want to reverse its effect, just press the backspace key.
:::

## Insert Anything

You can also use the catch-all <kbd>⌘ /</kbd> shortcut to insert just about anything. Just execute the shortcut then type what you want to insert. For example:

::: {layout-ncol="2"}
![](images/visual-editing-omni-list.png){fig-alt="There is a line of text (with a cursor at the end) where someone has typed '/lis'. There is a drop-down menu underneath this with options for 'Bullet List', 'Numbered List', and 'Definition List' arranged vertically. The title of each item is bolded, has a small icon to the left, and a small description in lighter gray text underneath it."}

![](images/visual-editing-omni-math.png){fig-alt="There is a line of text (with a cursor at the end) where someone has typed '/ma'. There is a drop-down menu underneath this with options for 'Inline Math', 'Display Math', and 'Image...' arranged vertically. The title of each item is bolded, has a small icon to the left, and a small description in lighter gray text underneath it."}
:::

If you are at the beginning of a line (as displayed above) you can also enter plain `/` to invoke the shortcut.

## Global Options

You can customize visual editing options within **R Markdown -> Visual** (note that the visual editor was originally created for use with R Markdown so its options are located there --- these options are also applicable to usage with Quarto):

<img src="images/visual-editing-options.png" class="illustration" width="585" fig-alt="The global options window in RStudio. It is currently displaying the Visual subsection of the R Markdown section."/>

| Option                                              | Description                                                                                                                                                                                           |
|-----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use visual editing by default                       | Switch to visual mode immediately when creating new documents.                                                                                                                                        |
| Show document outline by default                    | Show the navigational outline when opening documents in visual mode.                                                                                                                                  |
| Editor content width                                | Maximum width for editing content. This is intended to keep editing similar to the width that users will see.                                                                                         |
| Editor font size                                    | Base font size for editor content (default: inherit from IDE settings).                                                                                                                               |
| Show margin column indicator in code blocks         | Show vertical line that indicates location of editing margin column (e.g. 80).                                                                                                                        |
| Default spacing between list items                  | Whether to use tight or normal spacing between list items by default. See [Tight Lists](content.qmd#tight-lists) for details.                                                                         |
| Automatic text wrapping (line breaks)               | When writing markdown, automatically insert line breaks after sentences or at a specified column (default: flow text; no auto-wrapping). See [Line Wrapping](markdown.qmd#line-wrapping) for details. |
| Write references at end of current                  | Write references (footnotes) at the end of the block or section where they appear, or at the end of the document. See [References](markdown.qmd#references) for details.                              |
| Write canonical visual mode markdown in source mode | Use the visual mode markdown writer when saving markdown from source mode (ensure consistency between documents saved from either mode).                                                              |

## Citation Options

You can customize visual editor citation options within **R Markdown -> Citations**:

<img src="images/visual-editing-options-citations.png" class="illustration" width="585" fig-alt="The global options window in RStudio. It is currently displaying the Citation subsection of the R Markdown section."/>

| Option                                                 | Description                                                                                                                                                                                 |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Zotero Library                                         | Location of [Zotero](technical.qmd#citations-from-zotero) citation library (Local or Web).                                                                                                  |
| Zotero Data Directory                                  | Location of Zotero local data directory.                                                                                                                                                    |
| Use libraries                                          | Zotero libraries to use as reference sources.                                                                                                                                               |
| Use Better BibTeX for citation keys and BibTeX export. | Optionally use [Better BibTeX](https://retorque.re/zotero-better-bibtex/) to generate citation keys and export BibTeX from Zotero (this option appears only if Better BibTeX is installed). |

## Project Options

Global options that affect the way markdown is written can also be customized on a per-project basis. You can do this using the **R Markdown** pane of the **Project Options** dialog:

<img src="images/visual-editing-project-options.png" class="illustration" width="541" fig-alt="The Project Options dialog in RStudio. It is currently displaying the R Markdown section."/>

By default projects inherit the current global settings for markdown writing and Zotero libraries.

## File Options

Global and project options that affect the way markdown is written can also be customized on a per-file basis . You can do this by including an `editor: markdown` key in the YAML front matter of your document. For example:

``` yaml
---
title: "My Document"
author: "Jane Doe"
editor:
  markdown:
    wrap: 72
---
```

You might want to do this to ensure that multiple authors on different workstations use the same markdown writing options.

You can also instruct RStudio to use these same options when saving files from source mode. To do this add the `canonical` option. For example:

``` yaml
---
editor:
  markdown:
    wrap: 72
    canonical: true
---
```

With `canonical: true`, edits in visual mode and source mode will result in identical markdown output. This is especially useful if you have multiple authors collaborating using version control, with a mixture of source and visual mode editing among the authors.

See the documentation on [Writer Options](markdown.qmd#writer-options) for additional details on markdown writing options.


# quarto-web/docs/visual-editor/vscode/index.qmd

---
title: "Visual Editing in VS Code"
---

## Overview

The [Quarto VS Code Extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto) includes a visual markdown editor that supports all of Quarto's markdown syntax including tables, citations, cross-references, footnotes, divs/spans, definition lists, attributes, raw HTML/TeX, and more:

![](/docs/visual-editor/images/vscode-visual-editor.png){.border width="609"}

You can switch between visual and source mode at any time and can even edit documents concurrently in both modes. To switch between visual and source mode:

1.  Use the <kbd>⇧⌘ F4</kbd> keyboard shortcut.

2.  Use the context menu from anywhere in a document:

    ![](/docs/visual-editor/images/vscode-visual-editor-context-menu.png){.border width="609"}

3.  Use the **Edit in Visual Mode** and **Edit in Source Mode** commands:

    ![](/docs/visual-editor/images/vscode-visual-mode-command.png){.border width="609"}

4.  Use the editor menu:

    ![](/docs/visual-editor/images/vscode-visual-mode-menu.png){.border width="609"}

You can also right click a `.qmd` document in the file explorer and select the **Open With...** command, which will prompt you for the editor to open the file with:

![](/docs/visual-editor/images/vscode-visual-editor-default-mode.png){.border width="609"}

Note that this menu also provides an option to configure the default editor for `.qmd` files: use this if you want to primarily edit in visual mode and occasionally switch to source mode.

## Keyboard Shortcuts

Visual mode supports both traditional keyboard shortcuts (e.g. <kbd>⌘ B</kbd> for bold) as well as markdown shortcuts (using markdown syntax directly). For example, enclose `**bold**` text in asterisks or type `##` and press space to create a second level heading.

Here are the available keyboard and markdown shortcuts:

| Command            | Keyboard Shortcut  |   Markdown Shortcut   |
|--------------------|:------------------:|:---------------------:|
| Bold               |   <kbd>⌘ B</kbd>   |      `**bold**`       |
| Italic             |   <kbd>⌘ I</kbd>   |      `*italic*`       |
| Code               |   <kbd>⌘ D</kbd>   |     `` `code` ``      |
| Strikeout          |                    |     `~~strike~~`      |
| Subscript          |                    |        `~sub~`        |
| Superscript        |                    |       `^super^`       |
| Heading 1          |  <kbd>⌥⌘ 1</kbd>   |          `#`          |
| Heading 2          |  <kbd>⌥⌘ 2</kbd>   |         `##`          |
| Heading 3          |  <kbd>⌥⌘ 3</kbd>   |         `###`         |
| Heading Attributes |                    |    `{#id .class}`     |
| Link               |   <kbd>⌘ K</kbd>   |       `<href>`        |
| Blockquote         |                    |          `>`          |
| Code Block         |  <kbd>⇧⌘ \\</kbd>  |     ```` ``` ````     |
| Code Cell          |  <kbd>⌥⌘ I</kbd>   | ```` ```{python} ```` |
| Raw Block          |                    | ```` ```{=html} ````  |
| Div                |                    |         `:::`         |
| Bullet List        |                    |          `-`          |
| Ordered List       |                    |         `1.`          |
| Tight List         |  <kbd>⌥⌘ 9</kbd>   |                       |
| List Check         |                    |         `[x]`         |
| Emoji              |                    |       `:smile:`       |
| Definition         |                    |          `:`          |
| Non-Breaking Space | <kbd>⌃ Space</kbd> |                       |
| Hard Line Break    | <kbd>⇧ Enter</kbd> |                       |
| Paragraph          |  <kbd>⌥⌘ 0</kbd>   |                       |
| Image              |  <kbd>⇧⌘ I</kbd>   |                       |
| Footnote           |  <kbd>⇧⌘ F7</kbd>  |                       |
| Citation           |  <kbd>⇧⌘ F8</kbd>  |         `[@`          |
| Table              |  <kbd>⌥⌘ T</kbd>   |                       |
| Editing Comment    |  <kbd>⇧⌘ C</kbd>   |                       |
| Select All         |   <kbd>⌘ A</kbd>   |                       |
| Clear Formatting   |  <kbd>⌘ \\</kbd>   |                       |
| Edit Attributes    |   <kbd>F4</kbd>    |                       |

::: {.callout-tip appearance="simple"}
For markdown shortcuts, if you didn't intend to use a shortcut and want to reverse its effect, just press the backspace key.
:::

## Insert Anything

You can also use the catch-all <kbd>⌘ /</kbd> shortcut to insert just about anything. Just execute the shortcut then type what you want to insert. For example:

::: {layout-ncol="2"}
![](../images/visual-editing-omni-list.png){fig-alt="There is a line of text (with a cursor at the end) where someone has typed '/lis'. There is a drop-down menu underneath this with options for 'Bullet List', 'Numbered List', and 'Definition List' arranged vertically. The title of each item is bolded, has a small icon to the left, and a small description in lighter gray text underneath it." width="400"}

![](../images/visual-editing-omni-math.png){fig-alt="There is a line of text (with a cursor at the end) where someone has typed '/ma'. There is a drop-down menu underneath this with options for 'Inline Math', 'Display Math', and 'Image...' arranged vertically. The title of each item is bolded, has a small icon to the left, and a small description in lighter gray text underneath it." width="400"}
:::

If you are at the beginning of a line (as displayed above), you can also enter plain `/` to invoke the shortcut.

## Editor Toolbar

The editor toolbar includes buttons for the most commonly used formatting commands:

![](/docs/visual-editor/images/vscode-visual-editor-toolbar.png){.border width="609"}

Additional commands are available on the **Format**, **Insert**, and **Table** menus:

| Format                                                                                                            | Insert                                                                                                            | Table                                                                                                           |
|------------------------|------------------------|------------------------|
| ![](../images/vscode-visual-editor-format-menu.png){.border fig-alt="The contents of the Format drop down menu."} | ![](../images/vscode-visual-editor-insert-menu.png){.border fig-alt="The contents of the Insert drop down menu."} | ![](../images/vscode-visual-editor-table-menu.png){.border fig-alt="The contents of the Table drop down menu."} |

## Editor Options

There are a variety of VS Code options available to configure the behavior of the visual editor. You can locate these options by filtering on `quarto.visualEditor` in the settings pane:

![](/docs/visual-editor/images/vscode-visual-editor-options.png){.border width="609"}

Options enable configuration of appearance (font size, content width, etc.), markdown output (e.g. column wrapping), spell checking, and default spacing for lists.

## Zotero Citations

[Zotero](https://zotero.org) is a popular free and open source reference manager. The Quarto visual editor integrates directly with Zotero, enabling you to use the **Insert Citation** command to use references from your Zotero libraries:

![](/docs/visual-editor/images/visual-editing-citations-zotero-browse.png){.illustration fig-alt="The 'Insert Citation' dialog. The 'My Library' option is selected. The search bar at the top of the right section is empty, but the search results section is filled with the contents of a Zotero reference manager library. Each of the search result icons has a small 'Z' on the bottom right to indicate that the result comes from a Zotero library."}

Zotero references will also show up automatically in visual editor completions:

<img src="/docs/visual-editor/images/visual-editing-citation-completions.png" width="426" fig-alt="Someone has typed &apos;@&apos; in the Visual Editor. In light gray to the right of the &apos;@&apos; is a magnifying glass followed by the text &apos;or DOI&apos;. Underneath this is a pop-up menu showing available citations. Each citation has a title of the form &apos;@citation&apos; in black, the title of the cited material in gray underneath it, an icon to the left, and the reference to the right in gray. Some of the icons have a small red &apos;Z&apos; on the bottom right corner, indicating that the corresponding reference comes from a Zotero library."/>

Items from Zotero will appear alongside items from your bibliography with a small "Z" logo juxtaposed over them. If you insert a citation from Zotero that isn't already in your bibliography then it will be automatically added to the bibliography.

If you are running both VS Code and Zotero on your desktop, then no additional configuration is required for connecting to your Zotero library. If however you using VS Code in a web browser and/or want to access your Zotero library over the web, then a few more steps are required (see the [Zotero Web API](#zotero-web-api) section for details).

### Group Libraries {#group-libraries}

[Zotero Groups](https://www.zotero.org/support/groups) provide a powerful way to share collections with a class or work closely with colleagues on a project. By default, Zotero Group Libraries are not included in the **Insert Citation** dialog or citation completions. However, you can use the *Quarto \> Zotero: Group Libraries* option to activate one or more group libraries (either globally, or per-workspace):

![](/docs/visual-editor/images/visual-editing-vscode-zotero-libraries.png){.illustration width="563"}

After you've added a group library to the list, a sync will be performed and you should see the library in the **Insert Citation** dialog. If you don't, double check the exact spelling of the group library name you are configuring (you may even want to copy and paste it from Zotero so you are certain to get it right).

### Zotero Web API {#zotero-web-api}

If you are using VS Code in a web browser and/or don't have Zotero installed locally, you can still access your Zotero library using the Zotero Web API (assuming you have a Zotero web account and have synced your libraries to your account).

::: {.callout-tip appearance="simple"}
If you are running VS Code on your desktop it's generally easier to also run Zotero on your desktop and access your library locally. That said, it is possible to access Zotero web libraries from VS Code on the desktop if you prefer that configuration.
:::

#### API Access Key

Zotero integration uses the Zotero Web API, so the first step is to [create a Zotero account](https://www.zotero.org/user/register) and then configure Zotero to sync its data to your account. You can do this using the **Sync** tab of the Zotero preferences:

![](/docs/visual-editor/images/visual-editing-citations-zotero-sync.png){.illustration fig-alt="The Sync tab of Zotero preferences." width="675"}

Once you've configured your library to sync, you need to [create a Zotero API Key](https://www.zotero.org/settings/keys/new):

![](/docs/visual-editor/images/visual-editing-citations-zotero-keygen.png){.illustration fig-alt="The 'New Private Key' section of Zotero. The 'Allow library access' option is selected." width="675"}

Follow the instructions to create a new access key. Note that if you want to use [Group Libraries](#group-libraries), you should change the default to provide read-only access to groups (as illustrated above).

Be sure to **record your key** after generating it (i.e. copy it to the clipboard and/or save it somewhere more permanent) as you won't be able to view it again after you navigate away.

#### Library Configuration

Finally, go to Zotero settings and specify that you'd like to use your `web` Zotero library rather than a local one:

![](/docs/visual-editor/images/vscode-zotero-web-config.png){.border}

You'll then be promoted to enter your Zotero Web API Key:

![](/docs/visual-editor/images/visual-editing-zotero-vscode-setup.png){.illustration width="601"}

After you provide your API key and it is validated, an initial sync of your Zotero libraries is performed. After this, you are ready to start inserting citations from Zotero.

::: callout-note
If you need to change your Zotero API key, you can always execute the **Quarto: Zotero - Connect Web Library** command. To force a sync of your web library, execute the **Quarto: Zotero - Sync Web Library** command (note that your web library is synced automatically so it is unlikely you'll need to use this command explicitly).
:::

## Markdown Output

The Quarto visual editor generates markdown using Pandoc. This means that in some cases your markdown will be *rewritten* to conform to standard Pandoc idioms. For example, Pandoc inserts 3 spaces after list bullets and automatically escapes characters that might be used for markdown syntax.

Here is a list of conventions for Pandoc generated markdown that might differ from your own markdown writing style:

-   `*text*` is used in preference to `_text_`
-   Backtick code blocks are written as ```` ``` {.md} ```` rather than ```` ```md ````
-   Backtick code blocks with no attributes are rendered as 4-space indented code blocks
-   Horizontal rules are written as dashes spanning the full width of the document
-   Plain links are written as `<https://yihui.org>` rather than `https://yihui.org`
-   Bullet and numbered lists use additional leading spaces before list item content
-   The blockquote character (`>`) is included on each new line of a blockquote
-   Table captions are written below rather than above tables
-   Multiline HTML and TeX blocks use the explicit raw attribute (e.g. ```` ```{=tex} ````)
-   Inline footnotes are replaced with footnotes immediately below the paragraph
-   Nested divs use `:::` at all levels so long as their attributes are distinct
-   Unnumbered sections are designated with `{.unnumbered}` rather than `{-}`
-   Characters used for markdown syntax (e.g. `*`, `_`, or `#`) are always escaped

While some of this behavior might be bothersome at first, if you decide that visual editing mode is useful for your workflow it's probably best to just adapt to writing your own markdown the same way that Pandoc does.

### Writer Options

Some aspects of markdown output can be customized via global, project, or file-level options, including:

-   How to wrap / break lines (fixed column, sentence-per-line, etc.).
-   Where to write footnotes (below the current paragraph or section, or at the end of the document).
-   Wheter to write inline or reference style links.

You can specify these options in one of two ways:

1.  As a global or per-workspace VS Code option (you can find the options that affect markdown output by filtering on `quarto.visualEditor.markdown`).

2.  Specifying them within document or project level YAML (described below).

#### Line Wrapping

By default, the visual editor writes Markdown with no line wrapping (paragraphs all occupy a single line). However, if you prefer to insert line breaks at a particular column (e.g. 72 or 80), or to insert a line break after each sentence, you can use the `quarto.visualEditor.markdownWrap` and `quarto.visualEditor.markdownWrapColumn` options accessible from the settings editor in VS Code.

You can also set this behavior on a per-document or per-project basis via the `wrap` option. For example, to wrap lines after 72 characters you would use this:

``` yaml
---
editor:
  markdown:
    wrap: 72
---
```

To insert a line break after each sentence, use `wrap: sentence`. For example:

``` yaml
---
editor:
  markdown:
    wrap: sentence
---
```

::: {.callout-note appearance="simple"}
The algorithm used for sentence wrapping will handle English and Japanese text well, but may not detect the end of sentences accurately for other languages.
:::

If you have enabled a global line wrapping option and want to turn off wrapping for a given document, use `wrap: none`.

#### References

By default, references (footnotes and reference links) are written at the end of the block where their corresponding footnote appears. You can override this behavior using the `quarto.visualEditor.markdownReferences` VS Code setting or by using the `references` option within document or project YAML.

For example, to write references at the end of sections rather than blocks you would use:

``` yaml
---
title: "My Document"
editor:
  markdown:
    references: 
      location: block
---
```

Valid values for the `references` option are `block`, `section`, and `document`.

If you are aggregating a set of markdown documents into a larger work, you may want to make sure that reference identifiers are unique across all of your documents (e.g. you don't want to have `[^1]` appear multiple times). You can ensure uniqueness via the `prefix` option. For example:

``` yaml
---
title: "My Document"
editor:
  markdown:
    references: 
      location: block
      prefix: "mydoc"
---
```

This will result in footnotes in this document using the specified prefix (e.g. `[^mydoc-1]`), ensuring they are globally unique across the manuscript.

::: {.callout-note appearance="simple"}
Note that if you are within a Quarto [book](../../books/book-basics.qmd) project then a references `prefix` is applied automatically so no changes to `editor` options are required.
:::

#### Links

Links are written inline by default, however they can be written as reference links (below content as with footnotes) by adding the `links: true` option to the `references` section of document or project YAML. For example:

``` yaml
---
title: "My Document"
editor:
  markdown:
    references: 
      location: block
      links: true
---
```

You can alternatively enable reference links using the VS Code `quarto.visualEditor.markdownReferenceLinks` option.

### Known Limitations

There are a handful of Pandoc markdown extensions not currently supported by visual editing. These are infrequently used extensions, so in all likelihood they won't affect documents you edit, but are still worth noting.

| Extension(s)             | Example            | Behavior                                 |
|---------------------|-------------------|--------------------------------|
| Inline footnotes         | \^\[inline\]       | Converted to numeric footnote.           |
| Footnote identifiers     | \[\^longnote\]     | Converted to numeric footnote.           |
| Example lists            | (\@) First example | Read/written as ordinary numbered lists. |
| Auto-list numbers        | #\. First item     | Read/written as ordinary numbered lists. |
| Reference links          | This is a \[link\] | Converted to ordinary links.             |
| MultiMarkdown attributes | \# Heading \[id\]  | Converted to Pandoc attributes.          |

The visual editor is unable to parse non-YAML title blocks (e.g. old-style % titles or MultiMarkdown titles) and also unable to parse non top-level YAML metadata blocks. If these forms of metadata are encountered, visual mode will fail to load with a warning.

Note that support for reference links can be enabled via the `editor: markdown: references: links` option in document or project YAML, or the VS Code `quarto.visualEditor.markdownReferenceLinks` option. Reference links will be written according the reference location option (either the `block` or `section` in which they appear, or alternatively at the end of the `document`).

# quarto-web/docs/interactive/index.qmd

---
title: "Interactivity"
execute: 
  echo: false
---

## Overview

Adding interactivity to an article is a great way to help readers explore the concepts and data you are presenting more deeply. There are three ways to add interactive components to Quarto documents:

1.  Create custom JavaScript visualizations using [Observable JS](ojs/).

2.  Use the [Shiny](shiny/) R package to add interactivity to Knitr engine documents.

3.  Incorporate [Jupyter Widgets](widgets/jupyter.qmd) or [htmlwidgets](widgets/htmlwidgets.qmd) (for the Jupyter and Knitr engines, respectively) into your document.

Each of these techniques has distinct benefits and drawbacks in terms of expressiveness, ease of development, and deployment requirements. We'll touch on these considerations briefly below, then provide links to more in depth documentation for learning more.

## Observable JS

Quarto includes native support for [Observable JS](https://observablehq.com/@observablehq/observables-not-javascript), a set of enhancements to vanilla JavaScript created by [Mike Bostock](https://en.wikipedia.org/wiki/Mike_Bostock) (also the author of [D3](https://d3js.org/)). Observable JS is distinguished by its [reactive runtime](https://github.com/observablehq/runtime), which is especially well suited for interactive data exploration and analysis.

Here's an example that provides slider inputs to condition the behavior of a visualization:

```{ojs}
//| panel: sidebar
viewof talentWeight = Inputs.range([-2, 2], { value: 0.7, step: 0.01, label: "talent weight" })
viewof looksWeight = Inputs.range([-2, 2], { value: 0.7, step: 0.01, label: "looks weight" })
viewof minimum = Inputs.range([-2, 2], { value: 1, step: 0.01, label: "minimum fame" })
```

```{ojs}
//| panel: fill
{
  const w = 400
  const h = 400;
  const result = d3.create("svg").attr("width", w).attr("height", h);
  const margin = 20;
  const xScale = d3.scaleLinear().domain([-2, 2]).range([margin, w - margin]);
  const yScale = d3.scaleLinear().domain([-2, 2]).range([h - margin, margin]);
  const points = result
    .append("g")
    .selectAll("circle")
    .data(actors)
    .join(enter => {
       const sel = enter
         .append("circle")
         .attr("r", 3)
         .attr("cx", d => xScale(d.talent))
         .attr("cy", d => yScale(d.looks))
         .attr("fill", d3.lab(50, 40, 20));
       return sel.filter(d => d.fame <= minimum)
         .attr("fill", "rgb(200, 200, 200)")
         .attr("r", 2);
    });
    
  const linearRegression = regression.regressionLinear()
    .x(d => d.talent)
    .y(d => d.looks)
    .domain([-2, 2]);

  const chosenActors = actors
    .filter(d => d.fame > minimum);

  const line = result
    .append("g")
    .append("line")
    .attr("stroke", d3.lab(20, 40, 20))
    .attr("stroke-width", 1.5)
    .datum(linearRegression(chosenActors))
    .attr("x1", d => xScale(d[0][0]))
    .attr("x2", d => xScale(d[1][0]))
    .attr("y1", d => yScale(d[0][1]))
    .attr("y2", d => yScale(d[1][1]));


  const xAxis = d3.axisBottom(xScale).ticks(3);
  result.append("g")
    .attr("transform", `translate(0, ${yScale(0)})`)
    .call(xAxis);

  result.append("text")
    .attr("x", xScale(0.05))
    .attr("y", yScale(2))
    .text("Looks");

  result.append("text")
    .attr("y", yScale(0.1))
    .attr("x", xScale(-2))
    .text("Talent");

  const yAxis = d3.axisLeft(yScale).ticks(3);
  result.append("g")
    .attr("transform", `translate(${xScale(0)}, 0)`)
    .call(yAxis);
  
  return result.node();
}
```

```{python}
import numpy
import pandas as pd
ojs_define(points = pd.DataFrame(dict(
    x = numpy.random.randn(100),
    y = numpy.random.randn(100))))
```

```{ojs}
actors = transpose(points).map(v => ({
  talent: v.x,
  looks: v.y,
  fame: v.x * talentWeight + v.y * looksWeight
}));
```

```{ojs}
transpose = function(df)
{
  const keys = Object.keys(df);
  return df[keys[0]]
    .map((v, i) => Object.fromEntries(keys.map(key => [key, df[key][i] || undefined])))
    .filter(v => Object.values(v).every(e => e !== undefined));
}
regression = require('d3-regression@1');
```

Observable JS uses some special keywords and a custom runtime to make JavaScript reactive. For example, the "minimum fame" slider in the example above was created with the following code:

``` js
viewof minimum = Inputs.range([-2, 2], { 
  value: 1, step: 0.01, 
  label: "minimum fame"
})
```

It's then referenced as a normal JavaScript variable in code that creates the plot:

``` js
sel.filter(d => d.fame <= minimum)
```

As the user interacts with the slider, the `minimum` value is updated and any code that references it is automatically re-executed.

One benefit of using JavaScript for interactive documents is that all the logic and computation is performed on the client (so no server is required for deployment).

To learn more see the articles on [Observable JS](ojs/).

## Shiny

The Shiny package provides a flexible, easy to use framework for creating interactive web applications with R. Quarto in turn includes support for embedding Shiny components and applets into documents created with the Knitr engine.

Here's a live example of Shiny interactive components along with a brief explanation of the code required to create them:

::: {.border layout-ncol="2"}
```{=html}
 <iframe id="example1" src="https://gallery.shinyapps.io/goog-trend-index/" style="border: none; width: 100%; height: 720px" frameborder="0"></iframe>
```
<div>

<br/>

Shiny comes with a variety of built in input widgets. With minimal syntax it is possible to include widgets like the ones shown on the left in your apps:

``` r
# Select type of trend to plot
selectInput(inputId = "type", 
            label = strong("Trend index"),
            choices = unique(trend_data$type),
            selected = "Travel")
```

Displaying outputs is equally hassle-free:

``` r
mainPanel(
  plotOutput(outputId = "lineplot", 
             height = "300px"),
)
```

Build your plots or tables as you normally would in R, and make them reactive with a call to the appropriate render function:

``` r
output$lineplot <- renderPlot({
  plot(x = selected_trends()$date, 
       y = selected_trends()$close, 
       type = "l",
       xlab = "Date", 
       ylab = "Trend index")
})
```

</div>
:::

Shiny makes it very straightforward to create interactive documents using only R. Unlike using JavaScript though, you will need to [deploy](shiny/running.qmd#deployment) documents that use Shiny to a server.

To learn more see the articles on [Using Shiny with Quarto](shiny/).

## Widgets

[Jupyter Widgets](https://jupyter.org/widgets) and [htmlwidgets](https://www.htmlwidgets.org/) are great ways to incorporate interactivity into your documents if you don't know JavaScript and prefer to work exclusively in Python or R. They also run entirely client-side so can be deployed within normal static HTML documents.

For example, the following Python code is all that is required to embed a Leaflet map into a Jupyter engine document:

```{python}
#| echo: fenced
from ipyleaflet import Map, Marker, basemaps, basemap_to_tiles
m = Map(
  basemap=basemap_to_tiles(
    basemaps.NASAGIBS.ModisTerraTrueColorCR, "2017-04-08"
  ),
  center=(52.204793, 360.121558),
  zoom=4
)
m.add_layer(Marker(location=(52.204793, 360.121558)))
m
```

To learn more see these articles on using widgets with Quarto:

-   [Jupyter Widgets](widgets/jupyter.qmd) (Jupyter engine).

-   [htmlwidgets](widgets/htmlwidgets.qmd) (Knitr engine).

## Layout

Once you've gotten familiar with using various interactive components see the article on [Component Layout](layout.qmd) to learn how to:

-   Group inputs into an [input panel](layout.qmd#input-panel).

-   Present multiple outputs in a [tabset panel](layout.qmd#tabset-panel).

-   Use a [full page layout](layout.qmd#full-page-layout) rather than the default article layout.

-   Add a [sidebar panel](layout.qmd#sidebar-panel) for inputs in a full page layout.

-   Create custom [panel layouts](layout.qmd#panel-layout) to arrange outputs into rows and columns.

## Observable JS on the RStudio IDE
  
Observable JS offers full access to [NPM](https://www.npmjs.com/) libraries, and these tend to use JS features that require the Electron version of the RStudio IDE [daily builds](https://dailies.rstudio.com/). If you plan on using Observable JS in the RStudio IDE, we recommend the Electron daily builds.


# quarto-web/docs/interactive/layout.qmd

---
title: "Component Layout"
execute:
  echo: false
---

## Overview

When you introduce interactive components into a document you'll want to be sure to lay them out in a fashion that optimizes for readability and navigation.

There are of course a wide variety of ways you can incorporate interactivity spanning from visualizations embedded within a longer-form article all the way up to a more application/dashboard style layout. We'll cover both of these layout scenarios below.

We'll use examples from both [Observable JS](ojs/) and [Shiny](shiny/) interactive documents---if you aren't familiar with the code/syntax used for a given example just focus on the enclosing layout markup rather than the application code.

## Input Panel

If you have several inputs, you may want to group them inside an input panel (code block with option `panel: input` or div with class `.panel-input`). For example:

![](images/article-input-panel-columns.png)

The inputs are grouped in a panel and laid out in three columns by adding the `panel: input` and `layout-ncol: 3` options to the OJS code cell:

```{{ojs}}
//| panel: input
//| layout-ncol: 3

viewof ch = checkbox({
  title: "Passport color:",
  options: [
    { value: "red", label: "Red" },
    { value: "green", label: "Green" },
    { value: "blue", label: "Blue" },
    { value: "black", label: "Black" }
  ],
  value: ["red", "green", "blue", "black"],
  submit: false
})

viewof type = radio({
  title: "Representation:",
  options: [
    { label: 'Passports', value: 'p' },
    { label: 'Circles', value: 'c' }
  ],
  value: 'p'
})

viewof k = slider({
  title: "Symbol size:",
  min: 1,
  max: 10,
  value: 3,
  step: 1
})
```

## Tabset Panel

If you want to allow users to toggle between multiple visualizations, use a tabset (div with class `.panel-tabset`). Include a heading (e.g. `##`) for each tab in the tabset.

For example, here are a plot and data each presented in their own tab:

```{ojs}
data = FileAttachment("ojs/palmer-penguins.csv").csv({typed: true})
```

::: panel-tabset
## Plot

```{ojs}
Plot.rectY(data, 
  Plot.stackY(
    Plot.binX( 
      {y: "count"}, 
      {x: "body_mass_g", fill: "species", thresholds: 20})
    )
  ).plot({
    facet: {
      data,
      x: "sex"
    },
    marks: [Plot.frame()]
  })
```

## Data

```{ojs}
Inputs.table(data)
```
:::

Here is the markup and code used to create the tabset:

    ::: {.panel-tabset}

    ## Plot

    ```{{ojs}}
    Plot.rectY(data, 
      Plot.stackY(
        Plot.binX( 
          {y: "count"}, 
          {x: "body_mass_g", fill: "species", thresholds: 20})
        )
      ).plot({
        facet: {
          data,
          x: "sex"
        },
        marks: [Plot.frame()]
      })
    ```

    ## Data

    ```{{ojs}}
    Inputs.table(filtered)
    ```

    :::

## Full Page Layout

By default Quarto documents center their content within the document viewport, and don't exceed a maximum width of around 900 pixels. This behavior exists to optimize readability, but for an application layout you generally want to occupy the entire page.

To do this, add the `page-layout: custom` option. For example:

``` yaml
format: 
  html:
    page-layout: custom
```

Here's an example of a Shiny application that occupies the full width of the browser:

![](shiny/images/iris-k-means.png){.border}

You'll also note that the inputs are contained within a sidebar---the next section describes how to create sidebars.

## Sidebar Panel

Sidebars are created using divs with class `.panel-sidebar`. You can do this using a markdown div container (as illustrated above for `.panel-input`), or, if the entire contents of your sidebar is created from a single code cell, by adding the `panel: sidebar` option to the cell.

Sidebar panels should always have an adjacent panel with class `.panel-fill` or `.panel-center` which they will be laid out next to. The former (`.panel-fill`) will fill all available space, the latter (`.panel-center`) will leave some horizontal margin around its content.

For example, here is the source code of the user-interface portion of the Shiny application displayed above:

    ---
    title: "Iris K-Means Clustering"
    format: 
      html:
        page-layout: custom
    server: shiny
    ---

    ```{{r}}
    #| panel: sidebar
    vars <- setdiff(names(iris), "Species")
    selectInput('xcol', 'X Variable', vars)
    selectInput('ycol', 'Y Variable', vars, selected = vars[[2]])
    numericInput('clusters', 'Cluster count', 3, min = 1, max = 9)
    ```

    ```{{r}}
    #| panel: fill
    plotOutput('plot1')
    ```

The `panel: fill` option is added to the plot output chunk. You can alternately use `panel: center` if you want to leave some horizontal margin around the contents of the panel.

Adding the `panel` option to a code chunk is shorthand for adding the CSS class to its containing div (i.e. it's equivalent to surrounding the code chunk with a div with class e.g. `panel-fill`).

Here's an example of using a sidebar with OJS inputs:

![](images/application-sidebar-panel.png)

To do this you would use the following code:

    ```{{ojs}}
    //| panel: sidebar

    viewof myage = {
      const myage = select({
        title: "Quelle classe d'âge voulez-vous cartographier ?",
        options: ages,
        value: "80etplus"
      });
      return myage;
    }

    viewof pctvax = slider({
      title: '<br/>Objectif de vaccination',
      description: '200% signifie 2 doses par personnes pour tout le monde',
      min: 50,
      max: 200,
      value: 200,
      step: 10,
      format: v => v + "%"
    })

    viewof overlay = radio({
      title: "Écarter les cercles",
      options: [{ label: 'Oui', value: 'Y' }, { label: 'Non', value: 'N' }],
      value: 'N'
    })

    viewof label = radio({
      title: "Numéros des départements",
      options: [{ label: 'Afficher', value: 'Y' }, { label: 'Masquer', value: 'N' }],
      value: 'N'
    })
    ```

    ```{{ojs}}
    //| panel: fill

    (vaccine visualization code)

    ```

## Panel Layout

You can arrange multiple interactive components into a panel using the `layout` attribute of a containing div. For example, here we have a main visualization in the first row and two ancillary visualizations in the second row:

![](images/application-panel-layout.png){.border}

As described in the article on [Figures](../authoring/figures.qmd#complex-layouts), you can arrange panels of figures in very flexible fashion using the `layout` attribute. For the example above we enclosed the three visualizations in the following div:

``` default
::: {layout="[ [1], [1,1] ]"}

(outputs)

:::
```

Note that you can apply the `layout` attribute to a div that is already a panel (e.g. `.panel-fill`) to specify layout for content adjacent to a sidebar. So the following markup is also valid:

``` default
::: {.panel-sidebar}

(inputs)

:::

::: {.panel-fill layout="[ [1], [1,1] ]"}

(outputs)

:::
```

The `layout` attribute is an array of arrays, each of which defines a row of the layout. Above we indicate that we want the first row to encompass the first visualization, and then to split the next two equally over the second row.

The values in rows don't need to add up to anything in particular (they are relative within each row), so we could have just as well have specified different relative widths for the second row if that was better suited to presenting our data:

``` default
::: {layout="[ [1], [3,2] ]"}

(outputs)

:::
```


# quarto-web/docs/interactive/shiny/execution.qmd

---
title: "Execution Contexts"
---

## Overview

Shiny interactive documents can contain both code that executes at render time as well as code that executes on the server in response to user actions and changes in input values. A solid understanding of these execution contexts is important both to have the right mental model during development as well as to optimize the performance of your document.

## Render & Server Contexts

To break this down more clearly, let's revisit the "Hello, Shiny" document we started with in the introduction to interactive documents:

    ---
    title: "Old Faithful"
    format: html
    server: shiny
    ---

    ```{{r}}
    sliderInput("bins", "Number of bins:", 
                min = 1, max = 50, value = 30)
    plotOutput("distPlot")
    ```

    ```{{r}}
    #| context: server
    output$distPlot <- renderPlot({
      x <- faithful[, 2]  # Old Faithful Geyser data
      bins <- seq(min(x), max(x), length.out = input$bins + 1)
      hist(x, breaks = bins, col = 'darkgray', border = 'white')
    })
    ```

Here is how execution breaks down for this document:

1.  The first code chunk that contains the calls to `sliderInput()` and `plotOutput()` will execute when you render the document (e.g. `quarto render old-faithful.qmd`).

2.  The second code chunk with the `context: server` option will *not* execute at render time, but rather will execute only when the document is served.

It's critical to understand that the two chunks are run in completely separate R sessions. That means that you cannot access variables created in the first chunk within the second, and vice-versa. The is analogous to the `ui.R` and `server.R` scripts that compose most normal Shiny applications.

Of course, it's quite useful to be able to re-use code between contexts, and we'll cover some ways to do this in the [Sharing Code](#sharing-code) section below.

::: {.callout-tip appearance="simple"}
In order to make the code of interactive documents straightforward to understand and work with, we strongly recommend that your server contexts (there can be more than one) be located *at the bottom* of the document. This makes the separate execution environments more clear in the flow of the document source code.
:::

### server.R {.unlisted}

There is one other option if you prefer to have a stronger separation. You can restrict your `.qmd` file to *only* code that will execute at render time, and then split out the server code into a separate `server.R` file.

Re-writing our example in this fashion would look like this:

##### old-faithful.qmd {.tabset}

    ---
    title: "Old Faithful"
    format: html
    server: shiny
    ---

    ```{{r}}
    sliderInput("bins", "Number of bins:", 
                min = 1, max = 50, value = 30)
    plotOutput("distPlot")
    ```

##### server.R

``` r
function(input, output, session) {
  output$distPlot <- renderPlot({
    x <- faithful[, 2]  # Old Faithful Geyser data
    bins <- seq(min(x), max(x), length.out = input$bins + 1)
    hist(x, breaks = bins, col = 'darkgray', border = 'white')
  })
}
```

This is perhaps a bit less convenient but does align better with the traditional `ui.R` / `server.R` separation that exists in traditional Shiny applications.

## Sharing Code {#sharing-code}

Sharing code between rendering contexts works a bit differently depending on if your code is in a single `.qmd` file or if it uses `server.R`. We'll cover both scenarios below.

### Single File

#### context: setup

To have code execute in both rendering and serving contexts, create a code chunk with `context: setup`. For example:

```{{r}}
#| context: setup
#| include: false

# load libraries
library(dplyr)

# load data
dataset <- import_data("data.csv")
dataset <- sample_n(dataset, 1000)
```

This code will execute at both render time as well as when the server is created for each new user session. Note that we also specify `include: false` to make sure that code, warnings, and output from the chunk are not included in the rendered document.

#### context: data

The loading and manipulation of data often dominates the startup time of Shiny applications. Since interactive documents are executed in two phases (the initial render and then the serving of the document to users) we can perform the expensive data manipulations during rendering and then simply load the data when starting up the application.

You can define prerendered data by adding the `context: data` option to an R code chunk. The chunk will be executed during render and any R objects it creates will be saved to an .RData file, which will then be loaded during Shiny server startup. For example, we could take the the setup chunk illustrated above and factor out the data loading into its own chunk:

```{{r}}
#| context: data
#| include: false

dataset <- import_data("data.csv")
dataset <- sample_n(dataset, 1000)
```

Note that R objects created within a `context: data` chunk are available to both the UI rendering and server contexts.

#### Knitr cache

You can further improve the performance of data rendering by adding the `cache: true` option to the data chunk. This will cause the code chunk to be re-executed only when required. For example:

```{{r}}
#| context: data
#| include: false
#| cache: true
#| cache.extra: !expr file.info("data.csv")$mtime

dataset <- import_data("data.csv")
dataset <- sample_n(dataset, 1000)
```

In this example the cache will be invalidated if either the R code in the chunk changes or the modification time of the "data.csv" file changes (this is accomplished using the `cache.extra` option).

You can also invalidate an existing cache by removing the `_cache` directory alongside with your interactive document.

#### context: server-start

There is one additional execution context that enables you to share code and data across multiple user sessions. Chunks with `context: server-start` execute once when the Shiny document is first run and are *not* re-executed for each new user of the document. Using `context: server-start` is appropriate for several scenarios including:

1.  Establishing shared connections to remote servers (e.g. databases, Spark contexts, etc.).

2.  Creating reactive values intended to be shared across sessions (e.g. with [reactivePoll](http://shiny.rstudio.com/reference/shiny/latest/reactivePoll.html) or [reactiveFileReader](http://shiny.rstudio.com/reference/shiny/latest/reactiveFileReader.html)).

For example:

```{{r}}
#| context: server-start

library(DBI)
db <- dbConnect(...)
```

### Multiple Files

If your interactive document uses a `.qmd` file to define the user-interface and a `server.R` file for the server, you can put shared code in a file named `global.R`. Functions and variables defined within `global.R` will be available both during render as well as during execution of the server.

In this scenario your interactive document consists of 3 source files:

| File       | Description                                                                                       |
|------------|---------------------------------------------------------------------------------------------------|
| `doc.qmd`  | Markdown content as well as Shiny inputs and outputs (e.g. `sliderInput()`, `plotOutput()`, etc.) |
| `server.R` | Main server function with reactive expressions, assignments to outputs, etc.                      |
| `global.R` | Code shared between `doc.qmd` and `server.R`.                                                     |


# quarto-web/docs/interactive/shiny/index.qmd

---
title: "Shiny"
---

## Introduction

If you are an R user, you may already be familiar with [Shiny](https://shiny.rstudio.com), a package that makes it easy to build interactive web apps with R.

When using the Knitr computation engine, Quarto documents can include embedded Shiny components (e.g. a plot with sliders that control its inputs) or even simple Shiny applications that include several components.

This section covers integrating Shiny with Quarto and assumes that you already have basic familiarity with Shiny. To learn more about Shiny please visit <https://shiny.rstudio.com>.

::: {.callout-note appearance="simple"}
In order to run the examples below you will need the very latest version of the **rmarkdown** package (v2.10), which you can install with:

``` r
 install.packages("rmarkdown")
```
:::

## Hello, Shiny

For example, here's a document that contains a plot of the "Old Faithful" dataset along with a slider to control the number of bins:

![](images/old-faithful.png){.border}

Here's the source code for this example:

    ---
    title: "Old Faithful"
    format: html
    server: shiny
    ---

    ```{{r}}
    sliderInput("bins", "Number of bins:", 
                min = 1, max = 50, value = 30)
    plotOutput("distPlot")
    ```

    ```{{r}}
    #| context: server
    output$distPlot <- renderPlot({
      x <- faithful[, 2]  # Old Faithful Geyser data
      bins <- seq(min(x), max(x), length.out = input$bins + 1)
      hist(x, breaks = bins, col = 'darkgray', border = 'white')
    })
    ```

There are two important differences between this document and a normal static document:

1.  The inclusion of `server: shiny` within the document's options, which instructs Quarto to run a Shiny Server behind the document:

    ``` yaml
    ---
    title: "Old Faithful"
    format: html
    server: shiny
    ---
    ```

2.  The inclusion of `context: server` as an option in the second code chunk, which delineates this R code as running within the Shiny Server (this is the code you would typically put in `server.R`):

    ```{{r}}
    #| context: server
    ```

We'll cover running and deploying Quarto documents with Shiny components in the article on [Running Documents](running.qmd). Before that though, let's cover a more in-depth example.

## Custom Layout

Here's an example that includes multiple inputs as well as a more application like page layout with a sidebar:

![](images/iris-k-means.png){.border}

Here's the source code for this example:

    ---
    title: "Iris K-Means Clustering"
    format: 
      html:
        page-layout: custom
    server: shiny
    ---

    ```{{r}}
    #| panel: sidebar
    vars <- setdiff(names(iris), "Species")
    selectInput('xcol', 'X Variable', vars)
    selectInput('ycol', 'Y Variable', vars, selected = vars[[2]])
    numericInput('clusters', 'Cluster count', 3, min = 1, max = 9)
    ```

    ```{{r}}
    #| panel: fill
    plotOutput('plot1')
    ```

    ```{{r}}
    #| context: server
    selectedData <- reactive({
        iris[, c(input$xcol, input$ycol)]
      })

    clusters <- reactive({
      kmeans(selectedData(), input$clusters)
    })

    output$plot1 <- renderPlot({
      palette(c("#E41A1C", "#377EB8", "#4DAF4A", "#984EA3",
        "#FF7F00", "#FFFF33", "#A65628", "#F781BF", "#999999"))

      par(mar = c(5.1, 4.1, 0, 1))
      plot(selectedData(),
           col = clusters()$cluster,
           pch = 20, cex = 3)
      points(clusters()$centers, pch = 4, cex = 4, lwd = 4)
    })
    ```

There are a few things worth noting in this example:

1.  The YAML front-matter includes the `page-layout: custom` option (to indicate we want our content to occupy the entire page rather than being centered with padding).
2.  We add `panel: sidebar` and `panel: fill` to the two code chunks that define the user-interface to specify that we want them laid out in special panel containers.
3.  We again use `context: server` on the last R code chunk to indicate that it contains the Shiny Server code.

#### Page Layout

Some interactive documents you create will use narrative interspersed with Shiny components and some (like this example) will be full page applications. Some may even by hybrids---for example imagine a sidebar on the left containing inputs that control outputs interspersed with narrative in the main document body.

See the article on [Component Layout](../layout.qmd) to learn more about the available tools for managing the layout of interactive documents.

## Examples

Here are some deployed examples of Quarto documents that use Shiny:

| Example                                                            | Source                       | Description                                                                                  |
|--------------------------------------------------------------------|------------------------------|----------------------------------------------------------------------------------------------|
| [Old Faithful](https://jjallaire.shinyapps.io/shiny-old-faithful/) | [Code](https://git.io/J0qnQ) | Demonstrates incorporating an interactive plot into the main flow of a document.             |
| [K-Means](https://jjallaire.shinyapps.io/shiny-k-means/)           | [Code](https://git.io/J0qnj) | Demonstrates using a more "application-like" page layout (sidebar and main panel)            |
| [Diamonds](https://jjallaire.shinyapps.io/shiny-diamonds/)         | [Code](https://git.io/J0qcR) | Demonstrates an alternate way to layout inputs (at the bottom of the page in three columns). |

## Learning More

To learn more about Shiny interactive documents see the following articles:

-   [Running Documents](running.qmd) covers how to run interactive documents both within RStudio and at the command line, as well as how to deploy them to end users.

-   [Execution Contexts](execution.qmd) goes in depth on when different code blocks (e.g. rendering vs. serving) run as well as how to cache expensive computations for more responsive documents.

-   [External Resources](resources.qmd) describes how to make sure that Shiny can locate resources (e.g. CSS, JS, images, etc.) that you include in your document.

-   [Component Layout](../layout.qmd) enumerates the various techniques you can use to layout interactive components within your documents.

If you are using both JavaScript and Shiny to create interactive documents, you might also be interested in the article on using [Shiny Reactives with OJS](../ojs/shiny.qmd).


# quarto-web/docs/interactive/shiny/running.qmd

---
title: "Running Documents"
---

## Overview

There are a number of ways to run Shiny interactive documents:

1.  Use **Run Document** within the RStudio IDE.
2.  Use the `quarto serve` command line interface.
3.  Deploy them to a server for use by a wider audience.

We'll cover all of these scenario in depth here. Note that in order to run interactive Shiny documents you will to install the very latest version of the **rmarkdown** package (v2.10) which you can install as follows:

``` r
install.packages("rmarkdown")
```

## RStudio IDE

While you are developing an interactive document it will likely be most convenient to run within RStudio.

Note that you need RStudio {{< var rstudio.min_version >}} or a later version in order to run Quarto interactive documents. You can download the latest release ({{< var rstudio.current_release >}}) here <https://posit.co/download/rstudio-desktop/>.

Click the **Run Document** button while editing a Shiny interactive document to render and view the document within the IDE:

![](images/rstudio-ide.png){.border}

When you make changes, just click **Run Document** again to see them reflected in the document preview.

Two options you may want to consider enabling are **Run on Save** and **Preview in Viewer Pane** (by default previews occur in an external window). You can access these options on the editor toolbar:

![](images/rstudio-ide-options.png){.border}

## Command Line

You can also run Shiny interactive documents from the command line via `quarto serve`. For example:

```{.bash filename="Terminal"}
quarto serve document.qmd
```

There are a number of options to the `serve` command to control the port and host of the document server as well as whether a browser is automatically opened for the running document. You can learn more about these options with `quarto serve help`.

If you are within an R session you can also use the **quarto** R package to run a document:

``` r
library(quarto)
quarto_serve("document.qmd")
```

## Deployment

### ShinyApps

You can publish Shiny interactive documents to the [ShinyApps](http://shinyapps.io/) hosted service. To do this you should ensure that you have:

1.  An account on ShinyApps (use the [signup form](http://shinyapps.io/) to create an account).

2.  The very latest versions of the **rsconnect** and **quarto** R packages. You can install them as follows:

    ``` r
    install.packages("rsconnect")
    install.packages("quarto")
    ```

You can then deploy your interactive document using the `quarto_publish_app()` function of the **quarto** package. You can do this as follows (working from the directory that contains your document):

``` r
library(quarto)
quarto_publish_app(server = "shinyapps.io")
```

If you are using RStudio you can also use the **Publish** button <kbd>![](../../output-formats/images/publish-button.png){width="21"}</kbd> available when working with an interactive document:

![](images/rstudio-ide-publish.png){.border width="587"}

Note that you should always **Run Document** locally prior to publishing your document (as this will create the `.html` file that is served on ShinyApps.

### Hugging Face

HuggingFace Spaces provides an SDK for deploying Shiny for R applications. Learn more about using HuggingFace with Shiny for R here: <https://huggingface.co/docs/hub/spaces-sdks-docker-shiny#shiny-for-r>.

### Posit Connect

[Posit Connect](https://www.rstudio.com/products/connect/) is a server product from Posit for secure sharing of applications, reports, and plots. You can publish Shiny interactive documents to Posit Connect in much the same way as described above for [ShinyApps].

First, make sure you very latest development versions of the **rsconnect** and **quarto** R packages. You can install them as follows:

``` r
install.packages("rsconnect")
install.packages("quarto")
```

Next, deploy your interactive document using the `quarto_publish_app()` function of the **quarto** package, providing the domain name or IP address of your Posit Connect installation via the `server` parameter. You can do this as follows (working from the directory that contains your document):

``` r
library(quarto)
quarto_publish_app(server = "rsc.example.com")
```

If you are using RStudio you can also use the **Publish** button <kbd>![](../../output-formats/images/publish-button.png){width="21"}</kbd> as described above in the ShinyApps documentation:

![](images/rstudio-ide-rsc-publish.png){.border width="573"}

As with ShinyApps, you should always **Run Document** locally prior to publishing your document (as this will create the `.html` file that is served by Posit Connect).


# quarto-web/docs/interactive/shiny/resources.qmd

---
title: "External Resources"
---

## Overview

There are two types of external resource file that might be referenced from within a Shiny interactive document:

1.  Files referenced from R code (e.g. R scripts, datasets, configuration files, etc.); and

2.  Static assets referenced from the web document (e.g. CSS style-sheets, images, etc.)

Below we'll describe how each of these resource types are handled within interactive documents.

## Code Resources

For files referenced from R code, you can reference anything located within the directory of (or sub-directories of) the main `.qmd` file. This is no different than with any other `.qmd` file or even R script.

Similarly, files created by executing R code (e.g. figures generated from code chunks) are automatically located in the document `_files` directory alongside the HTML output file. No special handling is required for these files.

## Asset Resources

Many interactive documents will consist of only the generated HTML and figures located in the `_files` directory. However, in some cases you may want to add static images, CSS files, or other assets to your document.

In these cases, you need to be sure to locate the files within one of the following specially named sub-directories to ensure they can be located by the Shiny server:

| Directory | Description                                  |
|:----------|:---------------------------------------------|
| `images/` | Image files (e.g. PNG, JPEG, etc.)           |
| `css/`    | CSS stylesheets                              |
| `js/`     | JavaScript scripts                           |
| `www/`    | Any other files (e.g. downloadable datasets) |

The reason that all files within the directory of the main `.qmd` can't be referenced from within the web document is that many of these files are application source code and data, which may not be something you want to be downloadable by end users. By restricting the files which can be referenced to the above directories you can control which files are downloadable and which are not.

\


# quarto-web/docs/interactive/shiny/_examples/k-means/shiny-k-means.qmd

---
title: "Iris K-Means Clustering"
format: 
  html:
    page-layout: full
    code-tools:
      source: https://github.com/quarto-dev/quarto-web/blob/main/docs/interactive/shiny/_examples/k-means/shiny-k-means.qmd
server: shiny
---

```{r}
#| panel: sidebar
vars <- setdiff(names(iris), "Species")
selectInput('xcol', 'X Variable', vars)
selectInput('ycol', 'Y Variable', vars, selected = vars[[2]])
numericInput('clusters', 'Cluster count', 3, min = 1, max = 9)
```

```{r}
#| panel: fill
plotOutput('plot1')
```

```{r}
#| context: server
selectedData <- reactive({
    iris[, c(input$xcol, input$ycol)]
  })

clusters <- reactive({
  kmeans(selectedData(), input$clusters)
})

output$plot1 <- renderPlot({
  palette(c("#E41A1C", "#377EB8", "#4DAF4A", "#984EA3",
    "#FF7F00", "#FFFF33", "#A65628", "#F781BF", "#999999"))

  par(mar = c(5.1, 4.1, 0, 1))
  plot(selectedData(),
       col = clusters()$cluster,
       pch = 20, cex = 3)
  points(clusters()$centers, pch = 4, cex = 4, lwd = 4)
})
```


# quarto-web/docs/interactive/shiny/_examples/diamonds/shiny-diamonds.qmd

---
title: "Diamonds Explorer"
format:
  html:
    page-layout: full
    code-tools: 
      source: https://github.com/quarto-dev/quarto-web/blob/main/docs/interactive/shiny/_examples/diamonds/shiny-diamonds.qmd 
server: shiny
---

```{r}
#| context: setup
library(ggplot2)
dataset <- diamonds
```

```{r}
#| panel: fill
plotOutput('plot')
```

::: {layout-ncol="3"}
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
:::

```{r}
#| context: server

dataset <- reactive({
  diamonds[sample(nrow(diamonds), input$sampleSize),]
})
 
output$plot <- renderPlot({
  
  p <- ggplot(dataset(), aes_string(x=input$x, y=input$y)) + geom_point()
  
  if (input$color != 'None')
    p <- p + aes_string(color=input$color)
  
  facets <- paste(input$facet_row, '~', input$facet_col)
  if (facets != '. ~ .')
    p <- p + facet_grid(facets)
  
  if (input$jitter)
    p <- p + geom_jitter()
  if (input$smooth)
    p <- p + geom_smooth()
  
  print(p)
  
})
```


# quarto-web/docs/interactive/shiny/_examples/covid19-bicartogram/covid19-bicartogram.qmd

---
title: "COVID-19 cases per state"
format:
  html:
    code-tools:
      source: https://github.com/quarto-dev/quarto-web/blob/main/docs/interactive/shiny/_examples/covid19-bicartogram/covid19-bicartogram.qmd
server: shiny
---

```{ojs}
//| panel: sidebar
viewof ojsDateStart = Inputs.text({label: "Date start", type: "date", min: "2020-01-01", max:"2021-08-31", value: "2021-08-01"});
viewof ojsDateEnd = Inputs.text({label: "Date end", type: "date", min: "2020-01-01", max:"2021-08-31", value: "2021-08-08"});
```

::: panel-tabset
## Map

```{ojs}
import { chart, objectMap } with { covidDorlingData as data, casesScale as areaScaleA, deathsScale as areaScaleB } from "@cscheid/bivariate-dorling-cartogram";
chart
```

## Scatter

```{ojs}
Plot.plot({
  x: {
    type: "log"
  },
  y: {
    type: "log"
  },
  marks: [
    Plot.dot(covidDorlingData, {x: "cases", y: "deaths"})
  ]
})
```

## Data

```{ojs}
{
  const result = covidDorlingData.map(d => ({
    state: d.name,
    cases: d.cases,
    deaths: d.deaths
  }));
  return Inputs.table(result)
}
```
:::

```{ojs}
function datePicker(min, max, value, label)
{
  const div = html`<div></div>`;
  const id = `${String(Math.random()).slice(2)}`
  const labelEl = html`<label for=${id}> ${label}</label>`;
  const inputEl = html`<input type=date min="${min}$ max="${max}" value="${value}" id=${id}>`;
  div.appendChild(inputEl);
  div.appendChild(labelEl);
  div.date = inputEl;
  return div;
}

rows = transpose(summary_data)

casesScale =  d3.scaleSqrt().domain([0, d3.max(rows, d => d.cases)]).range([0, 60])

deathsScale = d3.scaleSqrt().domain([0, d3.max(rows, d => d.deaths)]).range([0, 60])

covidDorlingData = {
  const allStates = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","District of Columbia","Florida","Georgia","Guam","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Northern Mariana Islands","Ohio","Oklahoma","Oregon","Pennsylvania","Puerto Rico","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virgin Islands","Virginia","Washington","West Virginia","Wisconsin","Wyoming"];
  const fmt = d3.format(",");
  const result = rows.map(d => ({
    cases: d.cases,
    deaths: d.deaths,
    areaA: d.cases,
    areaB: d.deaths,
    name: d.state,
    tooltip: `${d.state}:\n${fmt(d.cases)} cases\n${fmt(d.deaths)} deaths`,
    fixed: ["Hawaii", "Alaska"].indexOf(d.state) !== -1
  }));
  const existingRows = new Set();
  rows.forEach(d => {
    existingRows.add(d.state);
  })
  allStates.forEach(state => {
    if (existingRows.has(state))
      return;
    result.push({ name: state, areaA: 0, areaB: 0, fillA: "none",  fillB: "none", stroke: "none", fixed: false });
  });

  return result;
}
```

### About

The map displayed in this dashboard is a [bivariate cartogram](https://observablehq.com/@cscheid/bivariate-dorling-cartogram).

```{r}
#| context: server-start
library(tidyverse)
covid_data <- read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")
```

```{r}
#| context: server
get_cases <- function(s, e) {
  t1 <- covid_data %>% filter(date == s) %>% select(cases, deaths, state);
  t2 <- covid_data %>% filter(date == e) %>% select(cases, deaths, state);
  t3 <- inner_join(t1, t2, "state");
  t3 %>% mutate(cases = cases.y - cases.x, deaths = deaths.y - deaths.x) %>% select(state, cases, deaths)
}

summary_data = reactive({
  get_cases(substring(input$ojsDateStart, 1, 10), 
            substring(input$ojsDateEnd, 1, 10))
})
ojs_define(summary_data)
```


# quarto-web/docs/interactive/shiny/_examples/old-faithful/shiny-old-faithful.qmd

---
title: "Old Faithful"
format: 
  html:
    code-tools: 
      source: https://github.com/quarto-dev/quarto-web/tree/main/docs/interactive/shiny/_examples/old-faithful/shiny-old-faithful.qmd
server: shiny
---

Data on eruptions of the Old Faithful geyser in Yellowstone National Park,
Wyoming, USA. The data was collected continuously from August 1st until
August 15th, 1985.

```{r}
sliderInput("bins", "Number of bins:", min = 1, max = 50, value = 30)
plotOutput("distPlot")
```

The data consists of 299 pairs of measurements, referring to the time interval
between the starts of successive eruptions and the duration of the subsequent
eruption.

Click the **Code** button above to see the source code for this example.

```{r}
#| context: server
output$distPlot <- renderPlot({
  x <- faithful[, 2]  # Old Faithful Geyser data
  bins <- seq(min(x), max(x), length.out = input$bins + 1)
  hist(x, breaks = bins, col = 'darkgray', border = 'white')
})
```


# quarto-web/docs/interactive/ojs/ojs-cells.qmd

---
title: "OJS Cells"
execute:
  echo: fenced
---

OJS code cells `{ojs}` behave a bit differently than cells in traditional notebooks, and have many options available to control their display and layout.

## Cell Execution

A critical difference between OJS cell execution and traditional notebooks is that in OJS cells do not need to be defined in any particular order.

Because execution is fully reactive, the runtime will automatically execute cells in the correct order based on how they reference each other. This is more akin to a spreadsheet than a traditional notebook with linear cell execution.

For example, in this cell we reference a variable that is not yet defined (it's defined immediately below):

```{ojs}
x + 5
```

```{ojs}
x = 10
```

This code works because the Observable runtime automatically determines the correct order of execution for the cells.

## Cell Output

By default, OJS cells show their full source code and output within rendered documents. Depending on the type of document you are creating you might want to change this behavior either globally or for individual cells.

### Code Visibility

The `echo` option controls whether cells display their source code. To prevent display of code for an entire document, set the `echo: false` option in YAML metadata:

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

### Output Visibility

OJS cell output is also displayed by default. You can change this at a global or (more likely) per-cell level using the `output` option. For example, here we disable output for a cell:

```{{ojs}}
//| output: false
data
```

Note that cells which only carry assignments do not print their output by default. For example, this assignment won't print anything:

```{ojs}
//| echo: fenced
dummy1 = "aHiddenAssignment"
```

If you want to print even the results of assignments, you can specify the `output: all` option. For example:

```{ojs}
//| echo: fenced
//| output: all
dummy2 = [{key: 1, value: [1, 2, [3, 4], dummy1]}]
```

If you click the inspector you'll see it expand to reveal the data as JSON.

### Code Display

We talked about showing and hiding source code above, but what about controlling exactly how it's displayed?

There are options available for customizing the appearance of code blocks (highlighting, background, border, etc.) as well as how horizontal overflow is handled. See the article on [HTML Code Blocks](../../output-formats/html-code.qmd) for all of the details.

One option we wanted to specifically highlight here is code folding, which enables you to collapse code but still provide an option for users to view it. This is especially handy for custom JavaScript visualizations as they often span dozens of lines of code.

Add the `code-fold: true` option to a code cell to enable code folding (you can also enable this globally). For example, click the "Code" button to show the code block (note the `code-fold: true` option is specified)

```{ojs}
//| code-fold: true
pdata = FileAttachment("palmer-penguins.csv").csv({typed: true})

Plot.plot({
  facet: {
    data: pdata,
    x: "sex",
    y: "species",
    marginRight: 80
  },
  marks: [
    Plot.frame(),
    Plot.rectY(pdata, 
      Plot.binX(
        {y: "count"}, 
        {x: "body_mass_g", thresholds: 20, fill: "species"}
      )
    ),
    Plot.tickX(pdata, 
      Plot.groupZ(
        {x: "median"}, 
        {x: "body_mass_g",
         z: d => d.sex + d.species,
         stroke: "#333",
         strokeWidth: 2
        }
      )
    )
  ]
})
```

## Cell Layout

There are additional `panel` and `layout` options which you can add to OJS cells to customize how their output is presented. Here's a version of some of the previous examples we've used presented with a sidebar and tabset:

```{ojs}
//| echo: false
filtered = pdata.filter(function(penguin) {
  return bill_length_min < penguin.bill_length_mm &&
         islands.includes(penguin.island);
})
```

```{ojs}
//| echo: false
//| output: true
//| panel: sidebar
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

::: panel-tabset
## Plot

```{ojs}
//| echo: false
//| output: true
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

## Data

```{ojs}
//| echo: false
Inputs.table(filtered)
```
:::

We created this layout by first adding the `panel: sidebar` option to the cell with our inputs:

```{{ojs}}
//| panel: sidebar

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

We then added a tabset (div of class `.panel-tabset`) with **Plot** and **Data** tabs (headings within the div define the tabs):

    ::: {.panel-tabset}

    ## Plot

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

    ## Data

    ```{{ojs}}
    Inputs.table(filtered)
    ```

    :::

See the [Layout](examples/layout.qmd) example for the full source code.

Learn more in the article on [Layout](../layout.qmd) for interactive documents.

## Cell Figures

OJS cells can also be rendered as numbered, [cross-referenceable](../../authoring/cross-references.qmd) figures. To do this, add the `label` and `fig-cap` options to the cell. For example:

```{ojs}
//| echo: fenced
//| label: fig-penguin-body-mass
//| fig-cap: "Penguin body mass by sex and species"
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

See @fig-penguin-body-mass for further illustration.

To reference the figure use its label in a markdown [cross reference](../../authoring/cross-references.qmd):

``` markdown
See @fig-penguin-body-mass for further illustration.
```


# quarto-web/docs/interactive/ojs/data-sources.qmd

---
title: "Data Sources"
format: html
execute:
  echo: fenced
---

## Overview

There are a wide variety of way to make data available to OJS:

-   Read CSV, JSON, SQLite, and more using the [FileAttachments](https://github.com/observablehq/stdlib#file-attachments) API.

-   Use the `ojs_define()` function to make data processed in Python or R available to `{ojs}` cells.

-   Make calls to Web APIs for online services and data stores.

We'll explore all of these techniques below.

## File Attachments

Use the [FileAttachment](https://github.com/observablehq/stdlib#file-attachments) function from the standard library to read data from a file. For example, here we read and plot a CSV of NOAA's Monthly [CO2 concentration data](https://gml.noaa.gov/ccgg/trends/data.html) from Mauna Loa:

```{ojs}
data = {
  const co2data = await FileAttachment("co2_mm.csv")
    .csv({ typed: true } );
  return co2data.map(d => { 
    d["decimal date"] = Number(d["decimal date"]);
    d.average = Number(d.average); 
    return d; 
  });
}
Plot.plot({
  marks: [
    Plot.line(data, 
      { x: "decimal date", y: "average"}, 
      { stroke: "black" }
    )
  ]
})
```

Note that we specified the `typed: true` option to the `csv()` function. When this option is specified [d3.autoType](https://observablehq.com/@d3/d3-autotype) is used to automatically detect numbers, dates, etc. and convert them to the correct JavaScript types. This is highly recommend when you know that your data is compatible with automatic type detection.

Here are the methods available for structured data formats:

| Method                                                                                                                       | Description                          |
|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| [csv](https://github.com/observablehq/stdlib#attachment_csv)                                                                 | Comma separated values               |
| [tsv](https://github.com/observablehq/stdlib#attachment_tsv)                                                                 | Tab separated values                 |
| [json](https://github.com/observablehq/stdlib#attachment_json)                                                               | JSON (JavaScript objects)            |
| [sqlite](https://github.com/observablehq/stdlib#attachment_sqlite)                                                           | SQLite database client               |
| [arrow](https://github.com/observablehq/stdlib/blob/8d9f4d18df0b237a5e0870a6f39584048007aca7/src/fileAttachment.mjs#L59-L62) | Apache Arrow IPC file (uncompressed) |

There are also methods to get the raw data as a [blob](https://github.com/observablehq/stdlib#attachment_blob), [text](https://github.com/observablehq/stdlib#attachment_text), [image](https://github.com/observablehq/stdlib#attachment_image), or [stream](https://github.com/observablehq/stdlib#attachment_stream).

Note that if you are using the `arrow()` method the Apache Arrow IPC file (Feather V2 file) should be written uncompressed. For example:

```` markdown
```{{r}}
arrow::write_feather(
  mtcars, 
  "data.arrow", 
  compression = "uncompressed"
)
```

```{{ojs}}
data = FileAttachment("data.arrow").arrow()
```
````

## Python and R

The data you want to use with OJS might not always be available in raw form. Often you'll need to read and preprocess the raw data using Python or R. You can perform this preprocessing during document render (in an `{r}` or `{python}` code cell) and then make it available to `{ojs}` cells via the `ojs_define()` function.

Here's an example. We'll read the same data into R, do some grouping and summarization, then make it available to OJS using `ojs_define`:

```{r}
#| output: false

library(readr)
library(dplyr)

co2 = read_csv("co2_mm.csv")  %>% 
  group_by(year) %>% 
  summarize(max = max(average))

ojs_define(co2data = co2)
```

Note that we could have done the same thing using Python (the `ojs_define` function is available in any document that uses R or Python).

Now we plot the data using [Observable Plot](https://github.com/observablehq/plot):

```{ojs}
yearlyChart = Plot.plot({
  marks: [
    Plot.line(transpose(co2data), 
      {x: "year", y: "max"}, 
      { stroke: "black" }
    )
  ]}
)
```

See the [NOAA C02](examples/noaa-co2.qmd) example for the full source code.

### Transpose

You'll note one additional twist in the OJS code above: we call the `transpose` function on our `co2data` before plotting it. The `transpose` function is built in to Quarto's OJS engine, and will convert column-oriented datasets (like the ones used in Python and R) into the row-oriented datasets used by many JavaScript plotting libraries (including [Plot](https://github.com/observablehq/plot)).

For example, the following JSON data emitted from R or Python:

``` json
{
  "year": [1958, 1959, 1960],
  "max":  [317.51, 318.29, 320.04]
}
```

Is converted to the following via the call to `transpose`:

``` json
[
  { "year": 1959, "max": 317.51 },
  { "year": 1960, "max": 318.29 },
  { "year": 1960, "max": 320.04 }
]
```

Check the documentation for whatever plotting library you are using from OJS to see whether a call to `transpose` is required.

## Web APIs

You can use the [`d3.json()`](https://github.com/d3/d3-fetch/blob/v3.0.1/README.md#json) function to read JSON data from web services and data sources. Here we query the GitHub API for data on contributions to the Python pandas package:

```{ojs}
d3 = require('d3')

contributors = await d3.json(
  "https://api.github.com/repos/pandas-dev/pandas/stats/contributors"
)

commits = contributors.map(contributor => {
  const author = contributor.author;
  return {
    name: author.login,
    title: author.login,
    group: author.type,
    value: contributor.total
  }
})
```

View the data sorted by number of commits:

```{ojs}
Inputs.table(commits, { sort: "value", reverse: true })
```

See the [GitHub API](examples/github.qmd) example for the full source code.


# quarto-web/docs/interactive/ojs/libraries.qmd

---
title: "Libraries"
format: html
execute:
  echo: fenced
---

## Overview

There are three types of library you'll generally use with OJS:

1.  [Observable core libraries](https://github.com/observablehq) automatically available in every document.

2.  Third-party JavaScript libraries from [npm](https://docs.npmjs.com/about-packages-and-modules) and [ObservableHQ](https://observablehq.com).

3.  Custom libraries you and/or your colleagues have created

In this document we'll provide a high-level overview of the core libraries and some examples of using third-party libraries ([D3](#d3) and [Arquero](#arquero)). Creating your own libraries is covered in the article on [Code Reuse](code-reuse.qmd).

## Stdlib

The Observable standard library provides the core capabilities that underlie rendering content and loading code and data. Some particularly important components of the standard library include:

| Component                                                                  | Description                                       |
|----------------------------------------------------------------------------|---------------------------------------------------|
| [DOM](https://github.com/observablehq/stdlib#dom)                          | Dynamically creating DOM elements                 |
| [FileAttachments](https://github.com/observablehq/stdlib#file-attachments) | Reading files in a variety of formats             |
| [require](https://github.com/observablehq/stdlib#require)                  | Importing third-party modules from NPM and GitHub |

You can find complete documentation for the standard library at <https://github.com/observablehq/stdlib>.

::: {.callout-note}

Quarto always embeds a specific version of ObservableHQ's runtime, which means that Quarto might be behind the very latest ObservableHQ version on their website.
If you need to use the latest version of Plot (or other core libraries), you can use the `import` function to import the latest version directly from a CDN. For example:

```ojs
Plot = import("https://esm.sh/@observablehq/plot")
```

:::

## Inputs

The Observable inputs library provides widgets that can be bound to reactive expressions via the `viewof` keyword. Some particularly useful input include:

| Component                                                   | Description                                   |
|-------------------------------------------------------------|-----------------------------------------------|
| [Radio](https://github.com/observablehq/inputs#Radio)       | Choose from mutually exclusive set of options |
| [Checkbox](https://github.com/observablehq/inputs#Checkbox) | Choose one or more options from a list        |
| [Range](https://github.com/observablehq/inputs#Range)       | Slider for continuous numeric values          |
| [Select](https://github.com/observablehq/inputs#Select)     | Drop down select box                          |
| [Table](https://github.com/observablehq/inputs#Table)       | Select one or more rows from a table          |

You can find complete documentation for all of the inputs at <https://github.com/observablehq/inputs>.

## Plot

Observable Plot is a JavaScript library for exploratory data visualization. Plot is built upon a set of core concepts ([Marks](https://observablehq.com/@observablehq/plot-marks), [Scales](https://observablehq.com/@observablehq/plot-scales), [Transforms](https://observablehq.com/@observablehq/plot-transforms), and [Facets](https://observablehq.com/@observablehq/plot-facets)) that can be composed together to create custom visualizations.

Here's an example of a histogram of the weight of Olympic athletes created with Plot:

```{ojs}
athletes = FileAttachment("athletes.csv").csv({typed: true})

Plot.plot({
  grid: true,
  facet: {
    data: athletes,
    y: "sex"
  },
  marks: [
    Plot.rectY(
      athletes, 
      Plot.binX({y: "count"}, {x: "weight", fill: "sex"})
    ),
    Plot.ruleY([0])
  ]
})
```

You can find complete documentation for Observable plot <https://github.com/observablehq/plot>.

## D3 {#d3}

[D3.js](https://d3js.org/) is a JavaScript library for manipulating documents based on data. D3 is capable of creating just about any interactive graphic you can imagine!

Here's a zoomable sunburst diagram (originally published [here](https://observablehq.com/@d3/zoomable-sunburst%3E)) created with D3. Only two layers of the hierarchy are shown at a time. Click a node to zoom in, or the center to zoom out.

```{ojs}
//| echo: false
//| output: true
sunburst = {
  const root = partition(flareData);

  root.each(d => d.current = d);

  const svg = d3.create("svg")
      .attr("viewBox", [0, 0, width, width])
      .style("font", "15px sans-serif");

  const g = svg.append("g")
      .attr("transform", `translate(${width / 2},${width / 2})`);

  const path = g.append("g")
    .selectAll("path")
    .data(root.descendants().slice(1))
    .join("path")
      .attr("fill", d => { while (d.depth > 1) d = d.parent; return color(d.data.name); })
      .attr("fill-opacity", d => arcVisible(d.current) ? (d.children ? 0.6 : 0.4) : 0)
      .attr("d", d => arc(d.current));

  path.filter(d => d.children)
      .style("cursor", "pointer")
      .on("click", clicked);

  path.append("title")
      .text(d => `${d.ancestors().map(d => d.data.name).reverse().join("/")}\n${format(d.value)}`);

  const label = g.append("g")
      .attr("pointer-events", "none")
      .attr("text-anchor", "middle")
      .style("user-select", "none")
    .selectAll("text")
    .data(root.descendants().slice(1))
    .join("text")
      .attr("dy", "0.35em")
      .attr("fill-opacity", d => +labelVisible(d.current))
      .attr("transform", d => labelTransform(d.current))
      .text(d => d.data.name);

  const parent = g.append("circle")
      .datum(root)
      .attr("r", radius)
      .attr("fill", "none")
      .attr("pointer-events", "all")
      .on("click", clicked);

  function clicked(event, p) {
    parent.datum(p.parent || root);

    root.each(d => d.target = {
      x0: Math.max(0, Math.min(1, (d.x0 - p.x0) / (p.x1 - p.x0))) * 2 * Math.PI,
      x1: Math.max(0, Math.min(1, (d.x1 - p.x0) / (p.x1 - p.x0))) * 2 * Math.PI,
      y0: Math.max(0, d.y0 - p.depth),
      y1: Math.max(0, d.y1 - p.depth)
    });

    const t = g.transition().duration(750);

    // Transition the data on all arcs, even the ones that aren’t visible,
    // so that if this transition is interrupted, entering arcs will start
    // the next transition from the desired position.
    path.transition(t)
        .tween("data", d => {
          const i = d3.interpolate(d.current, d.target);
          return t => d.current = i(t);
        })
      .filter(function(d) {
        return +this.getAttribute("fill-opacity") || arcVisible(d.target);
      })
        .attr("fill-opacity", d => arcVisible(d.target) ? (d.children ? 0.6 : 0.4) : 0)
        .attrTween("d", d => () => arc(d.current));

    label.filter(function(d) {
        return +this.getAttribute("fill-opacity") || labelVisible(d.target);
      }).transition(t)
        .attr("fill-opacity", d => +labelVisible(d.target))
        .attrTween("transform", d => () => labelTransform(d.current));
  }
  
  function arcVisible(d) {
    return d.y1 <= 3 && d.y0 >= 1 && d.x1 > d.x0;
  }

  function labelVisible(d) {
    return d.y1 <= 3 && d.y0 >= 1 && (d.y1 - d.y0) * (d.x1 - d.x0) > 0.03;
  }

  function labelTransform(d) {
    const x = (d.x0 + d.x1) / 2 * 180 / Math.PI;
    const y = (d.y0 + d.y1) / 2 * radius;
    return `rotate(${x - 90}) translate(${y},0) rotate(${x < 180 ? 0 : 180})`;
  }

  return svg.node();
}
```

To use D3 in an `{ojs}` cell, first import it using the [require](https://github.com/observablehq/stdlib#require) function (which loads modules hosted at [jsDelivr](https://www.jsdelivr.com/)):

```{{ojs}}
d3 = require("d3@7")
```

Then, use d3 as needed to create your visualization. For example, here are the first few lines of the cell that creates the visualization above:

```{{ojs}}
sunburst = {
  const root = partition(flareData);
  root.each(d => d.current = d);
  const svg = d3.create("svg")
      .attr("viewBox", [0, 0, width, width])
      .style("font", "15px sans-serif");

  // ...remainder of implementation
  
  return svg.node();
}
```

See the [Sunburst](examples/sunburst.qmd) example for the complete source code. To learn more about D3, visit <https://d3js.org/>.

## Arquero {#arquero}

[Arquero](https://uwdata.github.io/arquero/) is a JavaScript library for query processing and transformation of array-backed data tables. Following the [relational algebra](https://en.wikipedia.org/wiki/Relational_algebra) and inspired by the design of [dplyr](https://dplyr.tidyverse.org/), Arquero provides a fluent API for manipulating column-oriented data frames.

Here we'll import Arquero (`aq`) and an alias to Arquero operations (`op`), read a dataset, then filter, aggregate, and view the data:

```{ojs}
import { aq, op } from '@uwdata/arquero'
penguins = aq.loadCSV("palmer-penguins.csv")
penguins
  .groupby('species')
  .filter(p => p.body_mass_g > 0)
  .rollup({
    count: op.count(),
    avg_mass: op.average('body_mass_g')
   })
  .view()
```

See the [Arquero](examples/arquero.qmd) example for complete source code. To learn more about using Arquero, see the [Introducing Arquero](https://observablehq.com/@uwdata/introducing-arquero) tutorial.

## Modules

### NPM

The [require](https://github.com/observablehq/stdlib#require) function in the standard library can be used to import [npm modules](https://docs.npmjs.com/about-packages-and-modules) (which are served from the [jsDelivr](https://www.jsdelivr.com/) CDN):

```{{ojs}}
d3 = require("d3")
topojson = require("topojson")
```

Modules can optionally include an `@` sign with a version. For example:

```{{ojs}}
d3 = require("d3@7")
```

See the [jsDelivr documentation](https://www.jsdelivr.com) for additional details. Note that the require function automatically prepends the prefix `https://cdn.jsdelivr.net/npm/` when resolving imports, so where the jsDeliver documentation says to use this URL:

    https://cdn.jsdelivr.net/npm/package@version/file

You need only pass this to `require`:

    package@version/file

### ObservableHQ

Notebooks published on <http://observablehq.com> can also be compiled and downloaded as [JavaScript modules](https://observablehq.com/@observablehq/downloading-and-embedding-notebooks#notebooks-as-es-modules).

While notebooks often have their own embedded dataset, you can actually replace this data with your own when you import them! Returning to the sunburst example from above, here we `import` a notebook and use the `with` keyword to provide our own value for `data`:

```{ojs}
pdata = FileAttachment("population.json").json()
import { chart } with { pdata as data } from "@d3/zoomable-sunburst"
chart
```

::: {.callout-warning appearance="simple"}
One important restriction to be aware of is that not all notebooks published on ObservableHQ have an open-source license. Notebooks need to [explicitly tagged with a license](https://observablehq.com/@observablehq/licenses) as an indication that it's okay to use them outside of ObservableHQ.

You can see the license for a notebook in its header area. For, example this notebook is tagged with the ISC license:

![](images/observable-license.png)

You should check the license of ObservableHQ notebooks before you import them. See the documentation on [notebook licenses](https://observablehq.com/@observablehq/licenses) for additional details on how to do this.
:::

## Appendix {.hidden .unlisted}

```{ojs}
flareData = FileAttachment("examples/flare-2.json").json()
```

```{ojs}
partition = flareData => {
  const root = d3.hierarchy(flareData)
      .sum(d => d.value)
      .sort((a, b) => b.value - a.value);
  return d3.partition()
      .size([2 * Math.PI, root.height + 1])
    (root);
}
```

```{ojs}
color = d3.scaleOrdinal(d3.quantize(d3.interpolateRainbow, flareData.children.length + 1))
```

```{ojs}
format = d3.format(",d")
```

```{ojs}
width = 932
```

```{ojs}
radius = width / 6
```

```{ojs}
arc = d3.arc()
    .startAngle(d => d.x0)
    .endAngle(d => d.x1)
    .padAngle(d => Math.min((d.x1 - d.x0) / 2, 0.005))
    .padRadius(radius * 1.5)
    .innerRadius(d => d.y0 * radius)
    .outerRadius(d => Math.max(d.y0 * radius, d.y1 * radius - 1))
```

```{ojs}
d3 = require("d3@7")
```


# quarto-web/docs/interactive/ojs/shiny.qmd

---
title: "Shiny Reactives"
from: markdown-grid_tables
format: html
---

## Overview

Earlier we described how to use the `ojs_define()` function to make data from Python and R available in OJS cells. In this scenario, data pre-processing is done once during render time then all subsequent interactions are handled on the client.

But what if you want to do data transformation dynamically in response to user inputs? This is also possible with `ojs_define()`, as it can be passed not just static values but also Shiny reactives (assuming it's running inside a Shiny [interactive document](../shiny/)).

## Hello, Shiny

Here is the [K-Means Clustering](https://shiny.rstudio.com/gallery/kmeans-example.html) example from the Shiny Gallery implemented with an OJS client and Shiny Server:

[![](images/kmeans-shiny-ojs.png){.border}](https://jjallaire.shinyapps.io/kmeans-shiny-ojs/)

You can see the document deployed at <https://jjallaire.shinyapps.io/kmeans-shiny-ojs/>.

### Source Code

Let's take a look at the source code. On the client we have familiar looking OJS inputs and a plot laid out using `panel: sidebar` and `panel: fill`:

    ```{{ojs}}
    //| panel: sidebar
    vars = ["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width"]
    viewof xcol = Inputs.select(vars, {label: "X Variable"})
    viewof ycol = Inputs.select(vars, {label: "Y Variable", value: vars[1]})
    viewof count = Inputs.range([1, 9], {label: "Cluster Count", step: 1, value: 3})
    ```

    ```{{ojs}}
    //| panel: fill
    Plot.plot({
      color: {
        type: "ordinal",
        scheme: "category10"
      },
      marks: [
        Plot.dot(transpose(selectedData), {
          x: xcol,
          y: ycol,
          fill: (d, i) => clusters.cluster[i],
        }),
        Plot.dot(clusters.centers, { 
          x: d => d[0],
          y: d => d[1],
          r: 10,
          stroke: "black",
          fill: (d, i) => i + 1
        }),
      ]
    })
    ```

Note that the plotting code references the variables `selectedData` and `clusters`. These will be provided by reactive expressions within the Shiny server code. Note also that we use the `transpose()` function to reshape the data into the row-oriented format that the Plot library expects.

Here is the server code:

```{{r}}
#| context: server

selectedData <- reactive({
  iris[, c(input$xcol, input$ycol)]
})

clusters <- reactive({
  kmeans(selectedData(), input$count)
})

ojs_define(selectedData, clusters)
```

We designate this code as running on the server via the `context: server` option.

Note that we reference several inputs that were defined by `viewof` expressions on the client (e.g. `input$xcol`). When these inputs change they will cause the appropriate server side reactives to re-execute.

We create two reactive values (`selectedData` and `clusters`) and provide them to the client using `ojs_define()`. The plot will be automatically re-drawn on the client side when these values change.

## Examples

Here are some examples that demonstrate various ways to use OJS with Shiny:

| Example                                                        | Source                       | Description                                                                                                        |
|----------------------------------------------------------------|------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [K-Means](https://jjallaire.shinyapps.io/kmeans-shiny-ojs/)    | [Code](https://git.io/J0kPK) | Simple example of binding OJS inputs to Shiny inputs and shiny reactives to OJS plots.                             |
| [Binning](https://jjallaire.shinyapps.io/binning-shiny-ojs/)   | [Code](https://git.io/J0kPu) | Demonstrates fast binning of a medium sized dataset (32mb) on the server.                                          |
| [Data Binding](https://jjallaire.shinyapps.io/data-shiny-ojs/) | [Code](https://git.io/J0kPl) | Demonstrates importing a notebook from <https://observablehq.com> and binding it's data field to a Shiny reactive. |

## Bindings

### OJS to Shiny

In the example above we took advantage of the fact that by default OJS `viewof` expressions are automatically propagated to Shiny inputs (e.g `input$xcol`). This provides a reasonable separation of concerns, and prevents excess network traffic in the case that you have large OJS variables.

However, if you want to use other OJS variables as Shiny inputs this is also possible using the `ojs-export` option. The default behavior maps to the following configuration:

``` yaml
---
server:
  type: shiny
  ojs-export: viewof
---
```

You can also specify `ojs-export: all` to cause all OJS reactives to be bound to Shiny inputs:

``` yaml
---
server:
  type: shiny
  ojs-export: all
---
```

Alternatively, you can specify a list of OJS reactives by name (including using `~` to filter out reactives), and optionally combine this with the `viewof` and/or `all` options. For example:

``` yaml
---
server:
  type: shiny
  ojs-export: [all, ~large_dataset]
---
```

### Shiny to OJS

Less common but occasionally useful is the ability to bind Shiny inputs into OJS. By default no such bindings occur, however you can use the `ojs-import` option to opt-in for specific Shiny inputs. For example:

``` yaml
---
server: 
  type: shiny
  ojs-import: [minimum, maximum]
---
```


# quarto-web/docs/interactive/ojs/index.qmd

---
title: "Observable JS"
execute:
  echo: false
---

## Overview

Quarto includes native support for [Observable JS](https://observablehq.com/@observablehq/observables-not-javascript), a set of enhancements to vanilla JavaScript created by [Mike Bostock](https://en.wikipedia.org/wiki/Mike_Bostock) (also the author of [D3](https://d3js.org/)). Observable JS is distinguished by its [reactive runtime](https://github.com/observablehq/runtime), which is especially well suited for interactive data exploration and analysis.

The creators of Observable JS (Observable, Inc.) run a hosted service at <https://observablehq.com/> where you can create and publish notebooks. Additionally, you can use Observable JS ("OJS") in standalone documents and websites via its [core libraries](https://github.com/observablehq). Quarto uses these libraries along with a [compiler](https://github.com/asg017/unofficial-observablehq-compiler/tree/beta) that is run at render time to enable the use of OJS within Quarto documents.

OJS works in any Quarto document (plain markdown as well as Jupyter and Knitr documents). Just include your code in an `{ojs}` executable code block. Documents that use OJS need to run on the `http://` or `https://` protocol and not the `file://` protocol. The rest of this article explains the basics of using OJS with Quarto.

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


# quarto-web/docs/interactive/ojs/_reactivity.qmd

---
title: "Reactivity"
---

The interactivity in interactive Quarto documents comes from the
*reactive* values provided by Observable's JavaScript dialect.

# Basics

## Inputs

```{ojs}
//| echo: false
md`There are a number of built-in reactive values in Observable you can use, and they automatically change as needed. For example, the local time of day (in milliseconds) is available as the \`now\` variable: ${now}; the width of the Quarto text area is available as \`width\`: ${width}. If you use these values as inputs in your code, you expressions will automatically be recomputed as the values change. For the full set of built-in values, see the [standard library documentation](https://github.com/observablehq/stdlib/blob/main/README.md).`
```

To obtain values from user input, start with Observable's Inputs
library, which gives you a simple way to create interactive inputs:

```{ojs}
viewof number = Inputs.range([10, 100], { value: 50, step: 1 })
viewof text = Inputs.text()
```

That `viewof` statement is special to Observable's runtime.  For now,
just remember that input value expressions should have `viewof` in
front of them.

## Outputs

An interactive output is just a JavaScript expression. If that
expression includes reactive inputs, the Observable runtime library will
automatically update the output when the input changes:

```{ojs}
md`Output: **You typed "${text}" into the text box, and the slider value is ${number}.**`
```

Outputs can be anything that JavaScript can create, including HTML and
SVG elements. This green rectangle below will change with the value of the
slider:

```{ojs}
//| echo: false
{
  let result = DOM.svg(width, 50);
  let rect = svg`<rect width=${number} height="30" y="10" x="10" fill="green"></rect>`
  let label = svg`<text>${text}</text>`;
  result.appendChild(rect);
  rect.appendChild(label);
  return result;
}
```

# Example: [conditioning on a collider](http://www.the100.ci/2017/03/14/that-one-weird-third-variable-problem-nobody-ever-mentions-conditioning-on-a-collider/)

Imagine a simplistic scenario where the **fame** of an actor is a weighted function of **talent** and **looks**, each measured as independent quantities.

```{ojs}
//| echo: false
viewof talentWeight = Inputs.range([-2, 2], { value: 0.7, step: 0.01, label: "talent weight" })
viewof looksWeight = Inputs.range([-2, 2], { value: 0.7, step: 0.01, label: "looks weight" })
viewof minimum = Inputs.range([-2, 2], { value: 1, step: 0.01, label: "minimum fame" })
```

The data for the actors visualization is computed in Python:

```{python}
import numpy
import pandas as pd
ojs_define(points = pd.DataFrame(dict(
    x = numpy.random.randn(100),
    y = numpy.random.randn(100))))
```

The *fame* value for each actor, on the other hand, uses the JavaScript UI elements and so
is computed as a JavaScript value:

```{ojs}
//| output: false 
actors = transpose(points).map(v => ({
  talent: v.x,
  looks: v.y,
  fame: v.x * talentWeight + v.y * looksWeight
}));
```

If we look at actors that are talented or good-looking, a surprising phenomenon happens: there appears to be a causal relationship between two independent variables. 
This idea that "the better a famous actor looks, the less talented they are" manifests itself in our model as a sloped line fit.
The reality, however, is that it's simply more common for actors to be good-looking but not too talented or talented but not too good-looking, than it is for actors to be good-looking *and* talented. 

```{ojs}
//| label: fig-collider
//| fig-cap: "An example of conditioning on a collider. When you fit a regression line to a dataset that has undergone a selection process that depends on multiple values, there exists a dependency between the two values, but there's no causation relationship."
//| echo: false
{
  const result = d3.create("svg").attr("width", width).attr("height", 300);
  const margin = 20;
  const xScale = d3.scaleLinear().domain([-2, 2]).range([margin, 300 - margin]);
  const yScale = d3.scaleLinear().domain([-2, 2]).range([300 - margin, margin]);
  const points = result
    .append("g")
    .selectAll("circle")
    .data(actors)
    .join(enter => {
       const sel = enter
         .append("circle")
         .attr("r", 3)
         .attr("cx", d => xScale(d.talent))
         .attr("cy", d => yScale(d.looks))
         .attr("fill", d3.lab(50, 40, 20));
       return sel.filter(d => d.fame <= minimum)
         .attr("fill", "rgb(200, 200, 200)")
         .attr("r", 2);
    });
    
  const linearRegression = regression.regressionLinear()
    .x(d => d.talent)
    .y(d => d.looks)
    .domain([-2, 2]);

  const chosenActors = actors
    .filter(d => d.fame > minimum);

  const line = result
    .append("g")
    .append("line")
    .attr("stroke", d3.lab(20, 40, 20))
    .attr("stroke-width", 1.5)
    .datum(linearRegression(chosenActors))
    .attr("x1", d => xScale(d[0][0]))
    .attr("x2", d => xScale(d[1][0]))
    .attr("y1", d => yScale(d[0][1]))
    .attr("y2", d => yScale(d[1][1]));


  const xAxis = d3.axisBottom(xScale).ticks(3);
  result.append("g")
    .attr("transform", `translate(0, ${yScale(0)})`)
    .call(xAxis);

  result.append("text")
    .attr("x", xScale(0.05))
    .attr("y", yScale(2))
    .text("Looks");

  result.append("text")
    .attr("y", yScale(0))
    .attr("x", xScale(2))
    .text("Talent");

  const yAxis = d3.axisLeft(yScale).ticks(3);
  result.append("g")
    .attr("transform", `translate(${xScale(0)}, 0)`)
    .call(yAxis);
  
  return result.node();
}
```

# More details

## All the inputs in the standard library

There are many ready-made input UI elements: see the [Observable documentation]() for details.

## Reactivity in depth

TBF

* Generators
* Converting callback style to reactive style
* Converting reactive style to callback style

<!-- Includes + Definitions -->

```{ojs}
//| echo: false
//| output: false
transpose = function(df)
{
  const keys = Object.keys(df);
  return df[keys[0]]
    .map((v, i) => Object.fromEntries(keys.map(key => [key, df[key][i] || undefined])))
    .filter(v => Object.values(v).every(e => e !== undefined));
}
regression = require('d3-regression@1');
```


# quarto-web/docs/interactive/ojs/code-reuse.qmd

---
title: "Code Reuse"
---

As you build larger Quarto projects (like [websites](../../websites/) and [books](../../books/)) that incorporate OJS, you'll likely want to re-use code, data, and output across different pages.

## Modules

JavaScript modules are directly supported in Quarto's OJS blocks. For example, if we have the following source file `square.js`:

``` js
export function square(x) {
  return x * x;
}
```

Then you can import and use the `square()` function as follows:

```{ojs}
import { square } from "./square.js"
square(5)
```

## Data

You may be using Python or R to pre-process data that is then provided to OJS via the `ojs_define()` function (this is described in more depth in the [Data Sources](data-sources.html#python-and-r) article). If you want to share data prepared in this fashion you can import it directly from another `.qmd`.

For example, here we import the `co2data` that we read and pre-processed with dplyr in [`data-sources.qmd`](data-sources.qmd):

```{ojs}
import { co2data } from "./data-sources.qmd";
Inputs.table(transpose(co2data))
```

## Output

You can import any reactive value from another `.qmd` file. Here, we're reusing a chart directly from [`data-sources.qmd`](data-sources.qmd):

```{ojs}
import { yearlyChart } from "./data-sources.qmd";
yearlyChart
```


# quarto-web/docs/interactive/ojs/examples/population.qmd

---
title: "Population"
format: 
  html:
    code-tools: true
    toc: false
---

This example demonstrates importing a notebook from ObervableHQ and replacing its data with data of our own (the code and data for this example were originally published  [here](https://github.com/observablehq/examples/tree/main/custom-data)).

First we read from a local JSON file into `population`:

```{ojs}
population = FileAttachment("population.json").json()
```

Then we import from <https://observablehq.com/@d3/zoomable-sunburst> and specify that we'd like to use `population` instead of the data built in to the notebook:

```{ojs}
import { chart } with { population as data } from "@d3/zoomable-sunburst"
```

Finally, we display the chart:

```{ojs}
chart
```



# quarto-web/docs/interactive/ojs/examples/github.qmd

---
title: "GitHub API"
format: 
  html:
    toc: false
    code-tools: true
---

Demonstration of using the [GitHub API](https://developer.github.com/v3). 

```{ojs}
//| code-fold: true
viewof repo = Inputs.radio(
  [
    "pandas-dev/pandas",
    "tidyverse/ggplot2",
  ], 
  { label: "Repo:", value: "pandas-dev/pandas"}
)
```

```{ojs}
//| code-fold: true
import { chart } with { commits as data } from "@d3/d3-bubble-chart"
chart
```


## Data

```{ojs}
d3 = require('d3')
contributors = await d3.json(
  "https://api.github.com/repos/" + repo + "/stats/contributors"
)
commits = contributors.map(contributor => {
  const author = contributor.author;
  return {
    name: author.login,
    title: author.login,
    group: author.type,
    value: contributor.total
  }
})
```

```{ojs}
Inputs.table(commits, { sort: "value", reverse: true })
```




# quarto-web/docs/interactive/ojs/examples/sunburst.qmd

---
title: "Sunburst"
subtitle: "Originally published at <https://observablehq.com/@d3/zoomable-sunburst>"
author: "Mike Bostock"
date: "2018-04-30"
license: ISC License
format: 
  html:
    toc: false
    code-tools: true
---

This variant of a [sunburst diagram](https://observablehq.com/@d3/sunburst) shows only two layers of the hierarchy at a time. Click a node to zoom in, or the center to zoom out. Compare to an [icicle](https://observablehq.com/@d3/zoomable-icicle).

```{ojs}
//| code-fold: true
sunburst = {
  const root = partition(flareData);

  root.each(d => d.current = d);

  const svg = d3.create("svg")
      .attr("viewBox", [0, 0, width, width])
      .style("font", "15px sans-serif");

  const g = svg.append("g")
      .attr("transform", `translate(${width / 2},${width / 2})`);

  const path = g.append("g")
    .selectAll("path")
    .data(root.descendants().slice(1))
    .join("path")
      .attr("fill", d => { while (d.depth > 1) d = d.parent; return color(d.data.name); })
      .attr("fill-opacity", d => arcVisible(d.current) ? (d.children ? 0.6 : 0.4) : 0)
      .attr("d", d => arc(d.current));

  path.filter(d => d.children)
      .style("cursor", "pointer")
      .on("click", clicked);

  path.append("title")
      .text(d => `${d.ancestors().map(d => d.data.name).reverse().join("/")}\n${format(d.value)}`);

  const label = g.append("g")
      .attr("pointer-events", "none")
      .attr("text-anchor", "middle")
      .style("user-select", "none")
    .selectAll("text")
    .data(root.descendants().slice(1))
    .join("text")
      .attr("dy", "0.35em")
      .attr("fill-opacity", d => +labelVisible(d.current))
      .attr("transform", d => labelTransform(d.current))
      .text(d => d.data.name);

  const parent = g.append("circle")
      .datum(root)
      .attr("r", radius)
      .attr("fill", "none")
      .attr("pointer-events", "all")
      .on("click", clicked);

  function clicked(event, p) {
    parent.datum(p.parent || root);

    root.each(d => d.target = {
      x0: Math.max(0, Math.min(1, (d.x0 - p.x0) / (p.x1 - p.x0))) * 2 * Math.PI,
      x1: Math.max(0, Math.min(1, (d.x1 - p.x0) / (p.x1 - p.x0))) * 2 * Math.PI,
      y0: Math.max(0, d.y0 - p.depth),
      y1: Math.max(0, d.y1 - p.depth)
    });

    const t = g.transition().duration(750);

    // Transition the data on all arcs, even the ones that aren’t visible,
    // so that if this transition is interrupted, entering arcs will start
    // the next transition from the desired position.
    path.transition(t)
        .tween("data", d => {
          const i = d3.interpolate(d.current, d.target);
          return t => d.current = i(t);
        })
      .filter(function(d) {
        return +this.getAttribute("fill-opacity") || arcVisible(d.target);
      })
        .attr("fill-opacity", d => arcVisible(d.target) ? (d.children ? 0.6 : 0.4) : 0)
        .attrTween("d", d => () => arc(d.current));

    label.filter(function(d) {
        return +this.getAttribute("fill-opacity") || labelVisible(d.target);
      }).transition(t)
        .attr("fill-opacity", d => +labelVisible(d.target))
        .attrTween("transform", d => () => labelTransform(d.current));
  }
  
  function arcVisible(d) {
    return d.y1 <= 3 && d.y0 >= 1 && d.x1 > d.x0;
  }

  function labelVisible(d) {
    return d.y1 <= 3 && d.y0 >= 1 && (d.y1 - d.y0) * (d.x1 - d.x0) > 0.03;
  }

  function labelTransform(d) {
    const x = (d.x0 + d.x1) / 2 * 180 / Math.PI;
    const y = (d.y0 + d.y1) / 2 * radius;
    return `rotate(${x - 90}) translate(${y},0) rotate(${x < 180 ? 0 : 180})`;
  }

  return svg.node();
}
```

```{ojs}
flareData = FileAttachment("flare-2.json").json()

partition = flareData => {
  const root = d3.hierarchy(flareData)
      .sum(d => d.value)
      .sort((a, b) => b.value - a.value);
  return d3.partition()
      .size([2 * Math.PI, root.height + 1])
    (root);
}

color = d3.scaleOrdinal(
  d3.quantize(d3.interpolateRainbow, flareData.children.length + 1)
)

format = d3.format(",d")

width = 932

radius = width / 6

arc = d3.arc()
    .startAngle(d => d.x0)
    .endAngle(d => d.x1)
    .padAngle(d => Math.min((d.x1 - d.x0) / 2, 0.005))
    .padRadius(radius * 1.5)
    .innerRadius(d => d.y0 * radius)
    .outerRadius(d => Math.max(d.y0 * radius, d.y1 * radius - 1))
```


# quarto-web/docs/interactive/ojs/examples/penguins.qmd

---
title: "Penguins"
format:
  html:
    toc: false
    echo: false
    keep-hidden: true
    code-tools: true
---

A simple example based on Allison Horst's [Palmer Penguins](https://allisonhorst.github.io/palmerpenguins/) dataset. Here we look at how penguin body mass varies across both sex and species (use the provided inputs to filter the dataset by bill length and island):

```{ojs}
//| panel: input
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

::: {.panel-tabset}

## Plot

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

## Data

```{ojs}
Inputs.table(filtered)
```

:::

```{ojs}
data = FileAttachment("palmer-penguins.csv").csv({ typed: true })
```

```{ojs}
filtered = data.filter(function(penguin) {
  return bill_length_min < penguin.bill_length_mm &&
         islands.includes(penguin.island);
})
```



# quarto-web/docs/interactive/ojs/examples/arquero.qmd

---
title: "Arquero"
format:
  html:
    code-tools: true
---

Simple demonstration of [Arquero](https://uwdata.github.io/arquero/) using Allison Horst's [Palmer Penguins](https://allisonhorst.github.io/palmerpenguins/) dataset. 

```{ojs}
import { aq, op } from '@uwdata/arquero'
penguins = aq.loadCSV("palmer-penguins.csv")

penguins.view()

penguins
  .groupby('species')
  .filter(d => d.body_mass_g > 0)
  .rollup({
    count: op.count(),
    avg_mass: op.average('body_mass_g')
   })
  .view()
```

If you want to use inputs in an arquero query, you can use the `params` method of table.
Below is a simple example of filtering a dataset by the values provided.

```{ojs}
//| panel: input
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
penguins
  .params({
    blm: bill_length_min,
    i: islands
  })
  .filter((d, $) => op.includes($.i, d.island) && d.bill_length_mm > $.blm)
  .view()
```


# quarto-web/docs/interactive/ojs/examples/noaa-co2.qmd

---
title: "NOAA CO2"
format: 
  html:
    code-tools: true
---

Read and plot a CSV of NOAA's Monthly [CO2 concentration data](https://gml.noaa.gov/ccgg/trends/data.html) from Mauna Loa:

```{ojs}
data = {
  const co2data = await FileAttachment("co2_mm.csv")
    .csv({ typed: true });
  return co2data.map(d => { 
    d["decimal date"] = Number(d["decimal date"]);
    d.average = Number(d.average); 
    return d; 
  });
}
Plot.plot({
  marks: [
    Plot.line(data, 
      { x: "decimal date", y: "average"}, 
      { stroke: "black" }
    )
  ]
})
```

Read the same data into R, do some grouping and summarization, then make it available using `ojs_define`:

```{r}
#| output: false
#| warning: false
library(readr)
library(dplyr)

co2 = read_csv("co2_mm.csv")  %>% 
  group_by(year) %>% 
  summarize(max = max(average))

ojs_define(co2data = co2)
```

Now plot the summarized data:

```{ojs}
Plot.plot({
  marks: [
    Plot.line(transpose(co2data), 
      {x: "year", y: "max"}, 
      { stroke: "black" }
    )
  ]}
)
```


# quarto-web/docs/interactive/ojs/examples/layout.qmd

---
title: "Layout"
format:
  html:
    echo: false
    code-tools: true
    page-layout: full
    toc: false
---

You can control the layout of OJS content in a number of ways.

## `page-layout: full`

This example uses `page-layout: full` to have its contents occupy the entire width of the page:

``` yaml
---
title: "Layout"
format: 
  html: 
    page-layout: full
---
```

Enclose the inputs in a sidebar panel and the outputs in a tabset panel (click the "Code" button at top right to see the full source code):

```{ojs}
//| panel: sidebar
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

::: {#penguins-tabset .panel-tabset .ojs-track-layout}
## Plot

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

## Data

```{ojs}
Inputs.table(filtered)
```
:::

Read and filter the data based on the user's inputs:

```{ojs}
//| echo: true
data = FileAttachment("palmer-penguins.csv").csv({typed: true})
filtered = data.filter(function(penguin) {
  return bill_length_min < penguin.bill_length_mm &&
         islands.includes(penguin.island);
})
```

## `width` and `layoutWidth`: fine-grained layout tracking

Like ObservableHQ, `ojs` cells support the reactive `width` which tracks the `clientWidth` of the main HTML element. 

```{ojs}
//| echo: true
width
```

In addition, if you need the widths of specific parts of the layout, use the CSS class `ojs-track-layout` in a div. Quarto's OJS runtime tracks all such divs in `layoutWidth`. In this example, the tabset above has id `penguins-tabset`, and you can see its `clientWidth` reactively below. If this webpage is sufficiently wide, the sidebar will take up some of the space and the width of the resulting tabset will be smaller:

```{ojs}
//| echo: true
layoutWidth
```


# quarto-web/docs/interactive/ojs/examples/_shiny/binning/binning-shiny-ojs.qmd

---
title: "Visualizing 1 million points with OJS + Shiny"
format:
  html:
    code-tools: 
      source: https://github.com/quarto-dev/quarto-web/blob/main/docs/interactive/ojs/examples/_shiny/binning/binning-shiny-ojs.qmd
server: shiny
---

This example visualizes 1 million x/y points using 2D binning. The user can choose the number of bins.

This version uses client-side OJS to provide an input slider and the visualization, but uses server-side Shiny code to provide the data and perform the binning.

Combining OJS and Shiny in this way gives us huge gains in efficiency and performance. Compare this to a client-only implementation here: <https://connect.rstudioservices.com/01-binning-ojs/01-binning-ojs.html>.

Click the **Code** button above to see the source code.

```{ojs}
viewof bins = Inputs.range([10, 100], {value: 10, step: 1, label: "Bins"})
```

```{ojs}
Plot.plot({
  width: 600,
  height: 600,
  color: {
    scheme: "blues"
  },
  marks: [
    Plot.rect(transpose(rects), {x1: "x1", x2: "x2", y1: "y1", y2: "y2", fill: "z"})
  ]
})
```

```{r}
#| context: server-start
library(readr)
library(ggplot2)
library(dplyr)

# points.csv can be generated by running https://git.io/J0kMj
points <- read_csv("points.csv", col_types = "dd")

# Quick and dirty 2D binning implementation
bin2d <- function(x, y, breaks = 30) {
  stopifnot(length(x) == length(y))
  
  # Create cut points for the x dimension's bins
  xbreaks <- seq.int(min(x), max(x), length.out = breaks)
  # Put each x coordinate in a bin
  xbin <- cut(x, breaks = xbreaks, include.lowest = TRUE)
  
  # Now the same for y
  ybreaks <- seq.int(min(y), max(y), length.out = breaks)
  ybin <- cut(y, breaks = ybreaks, include.lowest = TRUE)
  
  # Count the number of x/y points in each 2D bin; result is a matrix
  binned <- table(xbin, ybin)

  # Convert to the data frame format that Observable Plot expects.
  # Note that the order of arguments to expand.grid matters; the
  # results need to line up with the matrix when it's turned into a vector
  cbind(
    expand.grid(x1 = head(xbreaks, -1), y1 = head(ybreaks, -1)),
    expand.grid(x2 = tail(xbreaks, -1), y2 = tail(ybreaks, -1)),
    z = as.vector(binned)
  )
}
```

```{r}
#| context: server

bins_debounced <- reactive(req(input$bins)) %>% debounce(125)

df <- reactive({
  bin2d(points$x, points$y, bins_debounced())
})

ojs_define(rects = df)
```


# quarto-web/docs/interactive/ojs/examples/_shiny/data/data-shiny-ojs.qmd

---
title: "Notebook with Data from Shiny"
format:
  html:
    code-tools: 
      source: https://github.com/quarto-dev/quarto-web/blob/main/docs/interactive/ojs/examples/_shiny/data/data-shiny-ojs.qmd
server: shiny
---

This example takes the existing Observable notebook [\@d3/hexbin](https://observablehq.com/@d3/hexbin) and renders the interesting parts in this page (the input slider and the output plot).

We also replace the data in the original notebook with our own copy of the data from Shiny, adding the ability to filter the data.

Click the **Code** button above to see the source code.

```{ojs}
// Import the hexbin notebook, replacing its data with our own
import {viewof radius, chart} with {data as data} from "@d3/hexbin";

// The data used by the chart is this: a transposed version of the
// diamonds Shiny reactive that is defined in the R chunk below.
data = transpose(diamonds)
```

```{ojs}
//| panel: sidebar
viewof radius

viewof cut = {
  const levels = ["Fair", "Good", "Very Good", "Premium", "Ideal"];
  return Inputs.select(levels, {value: levels, multiple: true, label: "Filter by cut:"});
}
```

```{ojs}
//| panel: fill
chart
```

```{r}
#| context: server
library(dplyr)

diamonds <- reactive({
  ggplot2::diamonds %>%
    filter(cut %in% input$cut) %>%
    select(x = carat, y = price)
})
ojs_define(diamonds)
```


# quarto-web/docs/interactive/ojs/examples/_shiny/kmeans/kmeans-shiny-ojs.qmd

---
title: "OJS and Shiny Reactives"
format: 
  html:
    code-tools: 
      source: https://github.com/quarto-dev/quarto-web/blob/main/docs/interactive/ojs/examples/_shiny/kmeans/kmeans-shiny-ojs.qmd
server:
  type: shiny
---

[K-Means Clustering](https://shiny.rstudio.com/gallery/kmeans-example.html) example 
from the Shiny Gallery implemented with an OJS client and Shiny Server.

The source code for client and server are shown below. Alternatively,
click **Code** and **View Source** above to see the source in full.

```{ojs}
//| panel: sidebar

vars = ["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width"]
viewof xcol = Inputs.select(vars, {label: "X Variable", value: vars[0]})
viewof ycol = Inputs.select(vars, {label: "Y Variable", value: vars[1]})
viewof count = Inputs.range([1, 9], {label: "Cluster Count", step: 1, value: 3})
```

```{ojs}
//| panel: fill

Plot.plot({
  color: {
    type: "ordinal",
    scheme: "category10"
  },
  marks: [
    Plot.dot(transpose(selectedData), {
      x: xcol,
      y: ycol,
      fill: (d, i) => clusters.cluster[i],
    }),
    Plot.dot(clusters.centers, { 
      x: d => d[0],
      y: d => d[1],
      r: 10,
      stroke: "black",
      fill: (d, i) => i + 1
    }),
  ]
})
```

```{r}
#| context: server-start

library(readr)
library(ggplot2)
library(dplyr)
```

```{r}
#| context: server

selectedData <- reactive({
  req(input$xcol)
  req(input$ycol)
  iris[, c(input$xcol, input$ycol)]
})

clusters <- reactive({
  req(input$count)
  kmeans(selectedData(), input$count)
})

ojs_define(selectedData, clusters)
```


::: {.panel-tabset}

### OJS Client

```{{ojs}}
//| panel: sidebar

vars = ["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width"]
viewof xcol = Inputs.select(vars, {label: "X Variable", value: vars[0]})
viewof ycol = Inputs.select(vars, {label: "Y Variable", value: vars[1]})
viewof count = Inputs.range([1, 9], {label: "Cluster Count", step: 1, value: 3})
```

```{{ojs}}
//| panel: fill

Plot.plot({
  color: {
    type: "ordinal",
    scheme: "category10"
  },
  marks: [
    Plot.dot(transpose(selectedData), {
      x: xcol,
      y: ycol,
      fill: (d, i) => clusters.cluster[i],
    }),
    Plot.dot(clusters.centers, { 
      x: d => d[0],
      y: d => d[1],
      r: 10,
      stroke: "black",
      fill: (d, i) => i + 1
    }),
  ]
})
```

### Shiny Server

```{{r}}
#| context: server-start

library(readr)
library(ggplot2)
library(dplyr)
```

```{{r}}
#| context: server

selectedData <- reactive({
  req(input$xcol)
  req(input$ycol)
  iris[, c(input$xcol, input$ycol)]
})

clusters <- reactive({
  req(input$count)
  kmeans(selectedData(), input$count)
})

ojs_define(selectedData, clusters)
```


:::


# quarto-web/docs/interactive/widgets/jupyter.qmd

---
title: "Jupyter Widgets"
toc: false
---

## Overview

[Jupyter Widgets](https://jupyter.org/widgets) enable you to use JavaScript visualization libraries like [Leaflet](https://ipyleaflet.readthedocs.io/en/latest/), [Plotly](https://plotly.com/python/), and [threejs](https://pythreejs.readthedocs.io/) directly from Python.

If you are using the Jupyter engine with Quarto this is a great way to incorporate interactivity without learning JavaScript.

## Leaflet Example

Including Jupyter Widgets within a Quarto document is as easy as including a plot. For example, here is how we embed a [Leaflet](https://ipyleaflet.readthedocs.io/en/latest/) map:

```{python}
from ipyleaflet import Map, Marker, basemaps, basemap_to_tiles
m = Map(
  basemap=basemap_to_tiles(
    basemaps.NASAGIBS.ModisTerraTrueColorCR, "2017-04-08"
  ),
  center=(52.204793, 360.121558),
  zoom=4
)
m.add_layer(Marker(location=(52.204793, 360.121558)))
m
```

To learn about available Jupyter Widgets visit <https://jupyter.org/widgets>.

## Plotly

Plotly is an interactive graphics library that can also be used with the Jupyter engine. Here's an example of using [Plotly](https://plotly.com/python/):

```{python}
import plotly.express as px
import plotly.io as pio
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", 
                 color="species", 
                 marginal_y="violin", marginal_x="box", 
                 trendline="ols", template="simple_white")
fig.show()
```

::: {.callout-note}
If you are using Plotly within the VS Code Notebook Editor you will need to add a line of code to ensure that your plots can be seen both within VS Code and when rendered to HTML by Quarto. You can do this by configuring the Plotly [default renderer](https://plotly.com/python/renderers/#setting-the-default-renderer) as follows:

```{{python}}
import plotly.io as pio
pio.renderers.default = "plotly_mimetype+notebook_connected"
```

This workaround is required because when running within VS Code, Plotly chooses a default rendering that can't be easily exported to HTML (for more background, see this [GitHub Issue](https://github.com/microsoft/vscode-jupyter/issues/6999) and related discussion). Note that this workaround is only required for the VS Code Notebook Editor (it is not required if you are using Jupyter Lab or if you are editing a plain-text `.qmd` file).
:::


# quarto-web/docs/interactive/widgets/htmlwidgets.qmd

---
title: "htmlwidgets for R"
---

## Overview

The [htmlwidgets](http://www.htmlwidgets.org) package enables you to use JavaScript visualization libraries like [Leaflet](http://rstudio.github.io/leaflet/), [Plotly](https://plot.ly/r/), [dygraphs](http://rstudio.github.io/dygraphs/), and [threejs](https://bwlewis.github.io/rthreejs/) directly from R.

If you are using the Knitr engine with Quarto this is a great way to incorporate interactivity without learning JavaScript or requiring a Shiny Server to view your document.

## Usage

Including htmlwidgets within a Quarto document is as easy as including an R plot. For example, here is how we embed a [Leaflet](http://rstudio.github.io/leaflet/) map:

```{{r}}
library(leaflet)
leaflet() %>%
  addTiles() %>%  # Add default OpenStreetMap map tiles
  addMarkers(lng=174.768, lat=-36.852, popup="The birthplace of R")
```

```{r}
#| echo: false
#| fig.height: 3
library(leaflet)
leaflet() %>%
  addTiles() %>%  # Add default OpenStreetMap map tiles
  addMarkers(lng=174.768, lat=-36.852, popup="The birthplace of R")
```

## Layout

You can also use `layout` options with htmlwidgets. For example, here we provide a custom `layout` to arrange three [dygraph](http://rstudio.github.io/dygraphs/) time series plots:

```{{r}}
#| layout: [[1,1], [1]]
library(dygraphs)
dygraph(fdeaths, "Female Deaths")
dygraph(mdeaths, "Male Deaths")
dygraph(ldeaths, "All Deaths")
```

```{r}
#| echo: false
#| fig.height: 3
#| layout: [[1,1], [1]]
library(dygraphs)
dygraph(fdeaths, "Female Deaths")
dygraph(mdeaths, "Male Deaths")
dygraph(ldeaths, "All Deaths")
```

See the article on [Figures](../../authoring/figures.qmd#complex-layouts) for additional documentation on custom layouts.

To learn about available htmlwidgets see the [showcase page](http://www.htmlwidgets.org/showcase_leaflet.html) and the [htmlwidget gallery](http://gallery.htmlwidgets.org/).


# quarto-web/docs/output-formats/html-basics.qmd

---
title: "HTML Basics"
format: html
comments:
  hypothesis: true
---

## Overview

Use the `html` format to create HTML output. For example:

``` yaml
---
title: "My document"
format:
  html:
    toc: true
    html-math-method: katex
    css: styles.css
---
```

This example highlights a few of the options available for HTML output. This document covers these and other options in detail. See the HTML [format reference](../reference/formats/html.qmd) for a complete list of all available options.

## Table of Contents

Use the `toc` option to include an automatically generated table of contents in the output document. Use the `toc-depth` option to specify the number of section levels to include in the table of contents. The default is 3 (which means that level-1, 2, and 3 headings will be listed in the contents). For example:

``` yaml
toc: true
toc-depth: 2
```

Use the `toc-expand` option to specify how much of the table of contents to show initially (defaults to 1 with auto-expansion as the user scrolls). Use `true` to expand all or `false` to collapse all.

``` yaml
toc: true
toc-expand: 2
```

You can customize the title used for the table of contents using the `toc-title` option:

``` yaml
toc-title: Contents
```

If you want to exclude a heading from the table of contents, add both the `.unnumbered` and `.unlisted` classes to it:

``` markdown
### More Options {.unnumbered .unlisted}
```

The HTML format by default floats the table of contents to the right. You can alternatively position it at the `left`, or in the `body`. For example:

``` yaml
format:
  html:
    toc: true
    toc-location: left
```

The floating table of contents can be used to navigate to sections of the document and also will automatically highlight the appropriate section as the user scrolls. The table of contents is responsive and will become hidden once the viewport becomes too narrow. See an example on the right of this page.

Note that the `toc-location` option is not available when you disable the standard HTML theme (e.g. if you specify the `theme: none` or `theme: pandoc` option).

{{< include _document-options-section-numbering.md >}}

## CSS Styles

To add a CSS stylesheet to your document, just provide the `css` option. For example:

``` yaml
format:
  html: 
    css: styles.css
```

Using the `css` option works well for simple tweaks to document appearance. If you want to do more extensive customization see the documentation on [HTML Themes](html-themes.qmd).

## LaTeX Equations

By default, LaTeX equations are rendered using [MathJax](https://www.mathjax.org/). Use the `html-math-method` option to choose another method. For example:

``` yaml
format:
  html:
    html-math-method: katex
```

You can also specify a `url` for the library to load for a given method:

``` yaml
html-math-method:
  method: mathjax
  url: "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
```

Available math rendering methods include:

| Method    | Description                                                                                                                                                                                                                      |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `mathjax` | Use [MathJax](https://www.mathjax.org/) to display embedded TeX math in HTML output. The default configuration for [MathJax](https://docs.mathjax.org/) is [`tex-chtml-full.js`](https://docs.mathjax.org/en/latest/web/components/combined.html?highlight=tex-chtml-full.js#tex-chtml-full) which loads all [MathJax's extensions](https://docs.mathjax.org/en/latest/input/tex/extensions.html) except `colorv2` and `physics` (available using `\require{physics}`).                                                                                                                                         |
| `katex`   | Use [KaTeX](https://github.com/Khan/KaTeX) to display embedded TeX math in HTML output.                                                                                                                                          |
| `webtex`  | Convert TeX formulas to `<img>` tags that link to an external script that converts formulas to images.                                                                                                                           |
| `gladtex` | Enclose TeX math in `<eq>` tags in HTML output. The resulting HTML can then be processed by [GladTeX](https://humenda.github.io/GladTeX/) to produce images of the typeset formulas and an HTML file with links to these images. |
| `mathml`  | Convert TeX math to [MathML](https://www.w3.org/Math/) (note that currently only Firefox and Safari natively support MathML)                                                                                                     |
| `plain`   | No special processing (formulas are put inside a `span` with `class="math").`                                                                                                                                                    |

Note that there is more detailed documentation on each of these options in the Pandoc [Math Rendering in HTML](https://pandoc.org/MANUAL.html#math-rendering-in-html) documentation.

## Tabsets

You can use tabsets to present content that will vary in interest depending on the audience. For example, here we provide some example code in a variety of languages:

::: panel-tabset
## R

``` r
fizz_buzz <- function(fbnums = 1:50) {
  output <- dplyr::case_when(
    fbnums %% 15 == 0 ~ "FizzBuzz",
    fbnums %% 3 == 0 ~ "Fizz",
    fbnums %% 5 == 0 ~ "Buzz",
    TRUE ~ as.character(fbnums)
  )
  print(output)
}
```

## Python

``` python
def fizz_buzz(num):
  if num % 15 == 0:
    print("FizzBuzz")
  elif num % 5 == 0:
    print("Buzz")
  elif num % 3 == 0:
    print("Fizz")
  else:
    print(num)
```

## Java

``` java
public class FizzBuzz
{
  public static void fizzBuzz(int num)
  {
    if (num % 15 == 0) {
      System.out.println("FizzBuzz");
    } else if (num % 5 == 0) {
      System.out.println("Buzz");
    } else if (num % 3 == 0) {
      System.out.println("Fizz");
    } else {
      System.out.println(num);
    }
  }
}
```

## Julia

``` julia
function FizzBuzz(num)
  if num % 15 == 0
    println("FizzBuzz")
  elseif num % 5 == 0
    println("Buzz")
  elseif num % 3 == 0
    println("Fizz")
  else
    println(num)
  end
end
```
:::

Create a tabset via a markdown div with the class name panel-tabset (e.g. `::: {.panel-tabset}`). Each top-level heading within the div creates a new tab. For example, here is the markdown used to implement the first two tabs displayed above:

```` markdown
::: {.panel-tabset}
## R

``` {.r}
fizz_buzz <- function(fbnums = 1:50) {
  output <- dplyr::case_when(
    fbnums %% 15 == 0 ~ "FizzBuzz",
    fbnums %% 3 == 0 ~ "Fizz",
    fbnums %% 5 == 0 ~ "Buzz",
    TRUE ~ as.character(fbnums)
  )
  print(output)
}
```

## Python

``` {.python}
def fizz_buzz(num):
  if num % 15 == 0:
    print("FizzBuzz")
  elif num % 5 == 0:
    print("Buzz")
  elif num % 3 == 0:
    print("Fizz")
  else:
    print(num)
```

:::
````

### Tabset Groups

If you have multiple tabsets that include the same tab names, you can define a tabset `group`. Tabs within a `group` are all switched together (so in the example above once a reader switches to R or Python in one tabset the others will follow along). For example:

``` markdown
::: {.panel-tabset group="language"}
## R

Tab content

## Python

Tab content
:::
```

## Self Contained

HTML documents typically have a number of external dependencies (e.g. images, CSS style sheets, JavaScript, etc.). By default these dependencies are placed in a `_files` directory alongside your document. For example, if you render `report.qmd` to HTML:

``` {.bash filename="Terminal"}
quarto render report.qmd --to html
```

Then the following output is produced:

``` ini
report.html
report_files/
```

You might alternatively want to create an entirely self-contained HTML document (with images, CSS style sheets, JavaScript, etc. embedded into the HTML file). You can do this by specifying the `embed-resources` option:

``` yaml
format:
  html:
    embed-resources: true
```

This will produce a standalone HTML file with no external dependencies, using `data:` URIs to incorporate the contents of linked scripts, style sheets, images, and videos. The resulting file should be self contained, in the sense that it needs no external files and no net access to be displayed properly by a browser.

## Anchor Sections

Hover over a section title to see an anchor link. Enable/disable this behavior with:

``` yaml
format:
  html:
    anchor-sections: true
```

Anchor links are also automatically added to figures and tables that have a [cross reference](../authoring/cross-references.qmd) defined.

## Smooth Scrolling

Enable smooth scrolling within the page. By default, smooth scroll is not enabled. Enable/disable it with:

``` yaml
format:
  html:
    smooth-scroll: true
```

## External Links

By default external links (i.e. links that don't target the current site) receive no special visual adornment or navigation treatment (the current page is navigated). You can use the following options to modify this behavior:

+---------------------------+--------------------------------------------------------------------------------------------------------------------+
| Option                    | Description                                                                                                        |
+===========================+====================================================================================================================+
| `link-external-icon`      | `true` to show an icon next to the link to indicate that it's external (e.g. [external](#){.external}).            |
+---------------------------+--------------------------------------------------------------------------------------------------------------------+
| `link-external-newwindow` | `true` to open external links in a new browser window or tab (rather than navigating the current tab).             |
+---------------------------+--------------------------------------------------------------------------------------------------------------------+
| `link-external-filter`    | A regular expression that can be used to determine whether a link is an internal link. For example                 |
|                           |                                                                                                                    |
|                           | `^(?:http:|https:)\/\/www\.quarto\.org\/custom`                                                                    |
|                           |                                                                                                                    |
|                           | will treat links that start with http://www.quarto.org as internal links (and others will be considered external). |
+---------------------------+--------------------------------------------------------------------------------------------------------------------+

External links are identified either using the `site-url` (if provided) or using the `window.host` if no `site-url` or `link-external-filter` is provided. For example, here we enable both options and a custom filter:

``` yaml
format:
  html:
    link-external-icon: true
    link-external-newwindow: true
    link-external-filter: '^(?:http:|https:)\/\/www\.quarto\.org\/custom'
```

You can also specify one or both of these behaviors for an individual link using the `.external` class and `target` attribute. For example:

``` python
[example](https://example.com){.external target="_blank"}
```

## Reference Popups

If you hover your mouse over the citation and footnote in this sentence you'll see a popup displaying the reference contents:

   Hover over @xie2015 to see a reference to the definitive book on knitr[^1].

This behavior is enabled by default. You can disable it with the following options:

``` yaml
format:
  html:
    citations-hover: false
    footnotes-hover: false
```

## Commenting

This page has commenting with [Hypothes.is](https://web.hypothes.is/) enabled via the following YAML option:

``` yaml
comments:
  hypothesis: true
```

You can see the Hypothesis UI at the far right of the page. Rather than `true`, you can specify any of the available Hypothesis [embedding options](https://h.readthedocs.io/projects/client/en/latest/publishers/config.html) as a sub-key of `hypothesis`. For example:

``` yaml
comments:
  hypothesis: 
    theme: clean
```

You can enable [Utterances](https://utteranc.es/){.external} commenting using the `utterances` option. Here you need to specify at least the GitHub repo you want to use for storing comments:

``` yaml
comments:
  utterances:
    repo: quarto-dev/quarto-docs
```

You can also specify the other options [documented here](https://utteranc.es/).

You may also enable [Giscus](https://giscus.app) for commenting using the `giscus` option. Giscus will store comments in the 'Discussions' of a Github repo.

``` yaml
comments:
  giscus: 
    repo: quarto-dev/quarto-docs
```

Like utterances, you need to specify at least the Git repo you want to use for storing comments. In addition, the repo that you use must:

1.  Be public

2.  Have the Giscus app installed.

3.  Have discussion enabled

Review the [Giscus documentation](https://giscus.app) for instructions on setting up Giscus in your repository. Additional options are [covered here](/docs/reference/projects/websites.html#giscus).

### Disabling Comments

If you have comments enabled for an entire website or book, you can selectively disable comments for a single page by specifying `comments: false`. For example:

``` yaml
title: "Home Page"
comments: false
```

## Includes

{{< include _document-options-includes.md >}}

For example:

``` yaml
format:
  html:
    include-in-header:
      - text: |
          <script src="https://examples.org/demo.js"></script>
      - file: analytics.html
      - comments.html
    include-before-body: header.html
```

## Minimal HTML

The default Quarto HTML output format includes several features by default, including bootstrap themes, anchor sections, reference popups, tabsets, code block copying, and responsive figures. You can disable all of these built in features at once using the `minimal` option. For example:

``` yaml
---
title: "My Document"
format:
  html:
    minimal: true
---
```

When specifying `minimal: true` you can still selectively re-enable features you do want, for example:

``` yaml
---
title: "My Document"
format:
  html:
    minimal: true
    code-copy: true
---
```

[^1]: knitr is an R package for creating dynamic documents.


# quarto-web/docs/output-formats/html-code.qmd

---
title: "HTML Code Blocks"
format: 
  html:
    code-tools: true
execute:
  warning: false
---

## Overview

There are wide variety of options available to customize the display of source code within HTML documents, including:

1.  Hiding some or all code that was executed by [Knitr](https://yihui.name/knitr) or [Jupyter](https://jupyter.org).
2.  Code folding for executed code (hidden by default and expandable by readers).
3.  Handling code that overflows the available horizontal display space.
4.  View the source code of the markdown file used to generate the document.
5.  Syntax highlighting themes and other options to control the appearance of code.
6.  Copy to clipboard button for code blocks.
7.  Generating hyperlinks to online documentation for functions used within code blocks via the [downlit](https://downlit.r-lib.org/) package (note that this option currently only works when using the Knitr engine).

Details on using all of these options are provided below.

## Hiding Code

For many documents you may want to hide all of the executable source code used to produce dynamic outputs. You can do this by specifying `echo: false` in the document `execute` options. For example:

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

## Folding Code

Use the `code-fold` option to include code but have it hidden by default using the HTML `<details>` tag. For example, click the **Code** button to see the code that produced this plot.

```{r}
#| code-fold: true

library(ggplot2)
dat <- data.frame(cond = rep(c("A", "B"), each=10),
                  xvar = 1:20 + rnorm(20,sd=3),
                  yvar = 1:20 + rnorm(20,sd=3))

ggplot(dat, aes(x=xvar, y=yvar)) +
  geom_point(shape=1) + 
  geom_smooth() 
```

Here we specify both `code-fold: true` as well as custom summary text (the default is just "Code" as shown above):

``` yaml
format:
  html:
    code-fold: true
    code-summary: "Show the code"
```

Valid values for `code-fold` include:

| Value   | Behavior                     |
|---------|------------------------------|
| `false` | No folding (default)         |
| `true`  | Fold code (initially hidden) |
| `show`  | Fold code (initially shown)  |

Use the `code-fold` and `code-summary` chunk attributes to control this on a chunk-by-chunk basis:

```{{r}}
#| code-fold: true
#| code-summary: "Show the code"
```

## Code Overflow

In some cases the width of source code will overflow the available horizontal display space. By default, this will result in a horizontal scroll bar for the code block. However if you prefer not to have scrollbars you can have the longer lines wrap instead.

To set the global default behavior use the `code-overflow` option. For example:

``` yaml
format:
  html:
    code-overflow: wrap
```

Valid values for `code-overflow` are:

| Option   | Description                                                                                  |
|------------------|------------------------------------------------------|
| `scroll` | Scroll code blocks that exceed available width (default, corresponds to `white-space: pre`). |
| `wrap`   | Wrap lines of code that exceed available width (corresponds to `white-space: pre-wrap`).     |

You can also override the global default on a per-code-block basis. For computational cells you do this with the `code-overflow` cell option:

```{{python}}
#| code-overflow: wrap

# very long line of code....
```

For a static code block, add the `.code-overflow-scroll` or `.code-overflow-wrap` CSS class:

```` python
```{.python .code-overflow-wrap}
# very long line of code....
```
````

Note that irrespective of these options, code will always wrap within printed HTML output (as it would otherwise be clipped off the edge of the page).

## Code Tools

You can include a **Code** menu in the header of your document that provides various tools for readers to interact with the source code. Specify `code-tools: true` to activate these tools:

``` yaml
format:
  html:
    code-fold: true
    code-tools: true
```

If you have a document that includes folded code blocks then the **Code** menu will present options to show and hide the folded code as well as view the full source code of the document:

![](images/code-tools-01.png){.border fig-alt="A screen shot of the header of a rendered Quarto document showing the result of setting both the code-fold and code-tools option to true. There is a drop-down menu labeled 'Code' to the right of the page title with a triangle pointing down. The menu is open and there are three options listed vertically beneath it: 'Hide All Code,' 'Show All Code,' and 'View Source.'"}

This document specifies `code-tools: true` in its options so you should see the **Code** menu above next to the main header.

You can control which of these options are made available as well as the "Code" caption text using sub-options of `code-tools`. For example, here we specify that we want only "View Source" (no toggling of code visibility) and no caption on the code menu:

``` yaml
format:
  html: 
    code-tools:
      source: true
      toggle: false
      caption: none
```

By default, the source code is embedded in the document and shown in a popup window like this:

![](images/code-tools-source.png){fig-alt="A screenshot of this webpage with a pop-up window labeled 'Source Code' over it. This 'Source Code' window contains the raw markdown and R code used to write this page. There is an 'X' on the upper right corner of the 'Source Code' pop up to close it."}

You can alternatively specify a URL for the value of `source`:

``` yaml
format:
  html: 
    code-tools:
      source: https://github.com/quarto-dev/quarto-web/blob/main/index.md
```

If you are within a project and have specified a `repo-url` option then you can just use `repo` and the correct link to your source file will be generated:

``` yaml
format:
  html: 
    code-tools:
      source: repo
```

Note that the `code-tools` option is not available when you disable the standard HTML theme (e.g. if you specify the `theme: none` option).

## Appearance

By default code blocks are rendered with a left border whose color is derived from the current theme. You can customize code chunk appearance with some simple options that control the background color and left border. Options can either be booleans to enable or disable the treatment or can be legal CSS color strings (or they could even be SASS variable names!).

Here is the default appearance for code blocks (`code-block-background: true`):

![](images/code-bg.png){fig-alt="A block of code with a gray background."}

You can instead use a left border treatment using the `code-block-border-left` option:

``` yaml
code-block-border-left: true
```

![](images/code-default.png){fig-alt="A block of code with a gray vertical stripe running along its left border. This code block has no background."}

You can combine a background and border treatment as well as customize the left border color:

``` yaml
code-block-bg: true
code-block-border-left: "#31BAE9"
```

![](images/code-custom.png){fig-alt="A block of code with a gray background and a blue vertical stripe running along its left border."}

## Code Filename

Use the `filename` attribute on code blocks If you are documenting the contents of a file and want to be especially clear about the name of the file the code is associated with.

For example, the following code:

```` markdown
```{.python filename="matplotlib.py"}
import matplotlib.pyplot as plt
plt.plot([1,23,2,4])
plt.show()
```
````

Results in this HTML output:

![](images/code-filename.png)

Non-HTML formats will still have the filename, but it will simply be shown in bold above the code block.

## Highlighting

Pandoc will automatically highlight syntax in [fenced code blocks](https://pandoc.org/MANUAL.html#fenced-code-blocks) that are marked with a language name. For example:

    ```python
    1 + 1
    ```

Pandoc can provide syntax highlighting for over 140 different languages (see the output of `quarto pandoc --list-highlight-languages` for a list of all of them). If you want to provide the appearance of a highlighted code block for a language not supported, just use `default` as the language name.

You can specify the code highlighting style using `highlight-style` and specifying one of the supported themes. These themes are "adaptive", which means they will automatically switch between a dark and light mode based upon the theme of the website. These are designed to work well with sites that include a dark and light mode.

-   a11y
-   arrow
-   atom-one
-   ayu
-   breeze
-   github
-   gruvbox

All of the standard Pandoc themes are also available:

-   pygments
-   tango
-   espresso
-   zenburn
-   kate
-   monochrome
-   breezedark
-   haddock

As well as an additional set of extended themes, including:

-   dracula
-   monokai
-   nord
-   oblivion
-   printing
-   radical
-   solarized
-   vim-dark

The `highlight-style` option determines which theme is used. For example:

``` yaml
highlight-style: github
```

Highlighting themes can provide either a single highlighting definition or two definitions, one optimized for a light colored background and another optimized for a dark color background. When available, Quarto will automatically select the appropriate style based upon the code chunk background color's darkness. Users may always opt to specify the full name (e.g. `atom-one-dark`) to by pass this automatic behavior.

By default, code is highlighted using the `arrow` theme, which is optimized for accessibility. We've additionally introduced the `arrow-dark` theme which is designed to provide accessible highlighting against dark backgrounds.

Examples of the light and dark themes:

#### Arrow (light)

![](images/arrow.png){fig.alt="A block of code showcasing the Arrow (light) theme."}

#### Arrow (dark)

![](images/arrow-dark.png){fig.alt="A block of code showcasing the Arrow (dark) theme."}

#### Ayu (light)

![](images/ayu.png){fig.alt="A block of code showcasing the Ayu (light) theme."}

#### Ayu (dark)

![](images/ayu-dark.png){.preview-image fig.alt="A block of code showcasing the Ayu (dark) theme."}

### Custom Highlighting

In addition to the built in themes available for syntax highlighting, you can also specify your own syntax highlighting by providing the path to a valid theme file (which is based upon the KDE XML syntax highlighting descriptions). Highlighting is implemented using [skylighting](https://github.com/jgm/skylighting).

For example:

``` yaml
---
highlight-style: custom.theme
---
```

In addition, if you'd like to provide adaptive themes, you may also pass both a light and dark theme file:

``` yaml
---
highlight-style:
  light: custom-light.theme
  dark: custom-dark.theme
---
```

Note that as with adaptive text higlighting themes, when you provide a dark and light `highlight-style`, background colors specified in the themes will be ignored in favor of the overall theme specified background colors.

{{< include _code-annotation.md >}}

## Line Numbers

If you want to display line numbers alongside the code block, add the `code-line-numbers` option. For example:

``` yaml
format:
  html:
    code-line-numbers: true
```

Here's how a code block with line numbers would display:

``` {.python code-line-numbers="true"}
import matplotlib.pyplot as plt
plt.plot([1,23,2,4])
plt.show()
```

You can also enable line numbers for an individual code block using the `code-line-numbers` attribute. For example:

```` python
``` {.python code-line-numbers="true"}
import matplotlib.pyplot as plt
plt.plot([1,23,2,4])
plt.show()
```
````

## Executable Blocks

The documentation on [computations](/docs/get-started/computations/) covers how to include executable code blocks (code which is actually executed, with its output being included in the rendered document). We won't additionally cover that here, but we will talk about how to include code blocks that demonstrate executable syntax (e.g. for writing a tutorial).


{{< include ../computations/_unexecuted-blocks.md >}}

## Copy Button

Hover over the code block below and you will see a copy icon in the top-right corner:

```{r eval=FALSE}
library(dygraphs)
dygraph(nhtemp, main = "New Haven Temperatures") %>% 
  dyRangeSelector(dateWindow = c("1920-01-01", "1960-01-01"))
```

This behavior is enabled by default but you configure it using the `code-copy` option:

``` yaml
format:
  html:
    code-copy: false
```

Valid values for `code-copy` include:

|         |                                |
|---------|--------------------------------|
| `hover` | Show button on hover (default) |
| `true`  | Always show code copy button   |
| `false` | Never show code copy button    |

## Code Linking

The `code-link` option enables hyper-linking of functions within code blocks to their online documentation:

``` yaml
format:
  html:
    code-link: true
```

Code linking is currently implemented only for the knitr engine (via the [downlit](https://downlit.r-lib.org) package).
A limitation of downlit currently prevents code linking if `code-line-numbers` and/or `code-annotations` are also `true`.


# quarto-web/docs/output-formats/ms-word.qmd

---
title: Word Basics
format: html
---

## Overview

Use the `docx` format to create MS Word output. For example:

``` yaml
---
title: "My Document"
format:
  docx:
    toc: true
    number-sections: true
    highlight-style: github
---
```

This example highlights a few of the options available for MS Word output. This document covers these and other options in detail. See the Word [format reference](../reference/formats/docx.qmd) for a complete list of all available options.

To learn about creating custom templates for use with the `docx` format, see the article on [Word Templates](ms-word-templates.qmd).

{{< include _document-options-begin.md >}}



# quarto-web/docs/output-formats/all-formats.qmd

---
title: All Formats
format: html
tbl-colwidths: [30,70]
---

## Overview

Pandoc supports a huge array of output formats, all of which can be used with Quarto. To use any Pandoc format just use the `format` option or the `--to` command line option.

For example, here's some YAML that specifies the use of the `html` format as well as a couple of format options:

``` yaml
---
title: "My Document"
format: 
  html:
    toc: true
    code-fold: true
---
```

Alternatively you can specify the use of a format on the command line:

``` {.bash filename="Terminal"}
quarto render document.qmd --to html
```

See below for a list of all output formats by type along with links to their reference documentation.

## Documents

|                                            |                                                                                   |
|--------------------------|----------------------------------------------|
| [HTML](../reference/formats/html.qmd)      | HTML is a markup language used for structuring and presenting content on the web. |
| [PDF](../reference/formats/pdf.qmd)        | PDF is a file format for creating print-ready paged documents.                    |
| [MS Word](../reference/formats/docx.qmd)   | MS Word is the word processor included with Microsoft Office.                     |
| [OpenOffice](../reference/formats/odt.qmd) | OpenDocument is an open standard file format for word processing documents.       |
| [ePub](../reference/formats/epub.qmd)      | ePub is an e-book file format that is supported by many e-readers.                |

## Presentations

|                                                             |                                                                                 |
|-------------------------------|-----------------------------------------|
| [Revealjs](../reference/formats/presentations/revealjs.qmd) | Revealjs is an open source HTML presentation framework.                         |
| [PowerPoint](../reference/formats/presentations/pptx.qmd)   | PowerPoint is the presentation editing software included with Microsoft Office. |
| [Beamer](../reference/formats/presentations/beamer.qmd)     | Beamer is a LaTeX class for producing presentations and slides.                 |

## Markdown

|                                                            |                                                                                                                   |
|--------------------------|----------------------------------------------|
| [GitHub](../reference/formats/markdown/gfm.qmd)            | GitHub Flavored Markdown (GFM) is the dialect of Markdown that is currently supported for user content on GitHub. |
| [CommonMark](../reference/formats/markdown/commonmark.qmd) | CommonMark is a strongly defined, highly compatible specification of Markdown.                                    |
| [Hugo](../output-formats/hugo.qmd)             | Hugo is an open-source static website generator.                                                                  |
| [Docusaurus](../output-formats/docusaurus.qmd) | Docusaurus is an open-source markdown documentation system.                                                       |
| [Markua](../reference/formats/markdown/markua.qmd)         | Markua is a markdown variant used by Leanpub.                                                                     |

## Wikis

|                                                      |                                                                                                                   |
|-------------------------|------------------------------------------------|
| [MediaWiki](../reference/formats/wiki/mediawiki.qmd) | MediaWiki is the native document format of Wikipedia.                                                             |
| [DokuWiki](../reference/formats/wiki/dokuwiki.qmd)   | DokuWiki is a simple to use and highly versatile open source wiki software that doesn't require a database.       |
| [ZimWiki](../reference/formats/wiki/zimwiki.qmd)     | Zim is a graphical text editor used to maintain a collection of wiki pages.                                       |
| [Jira Wiki](../reference/formats/wiki/jira.qmd)      | Jira Wiki is the native document format for the Jira issue tracking and project management system from Atlassian. |
| [XWiki](../reference/formats/wiki/xwiki.qmd)         | XWiki is an open-source enterprise wiki system.                                                                   |

## More Formats

|                                                    |                                                                                                                                                                                                |
|-------------------|-----------------------------------------------------|
| [JATS](../reference/formats/jats.qmd)              | JATS (Journal Article Tag Suite) is an XML format for marking up and exchanging journal content.                                                                                               |
| [Jupyter](../reference/formats/ipynb.qmd)          | Jupyter Notebooks combine software code, computational output, explanatory text and multimedia resources in a single document.                                                                 |
| [ConTeXt](../reference/formats/context.qmd)        | ConTeXt is a system for typesetting documents based on TEX and METAPOST.                                                                                                                       |
| [RTF](../reference/formats/rtf.qmd)                | The Rich Text Format (RTF) is a file format for for cross-platform document interchange.                                                                                                       |
| [reST](../reference/formats/rst.qmd)               | reStructuredText is an easy-to-read, what-you-see-is-what-you-get plaintext markup syntax and parser system.                                                                                   |
| [AsciiDoc](../reference/formats/asciidoc.qmd)      | AsciiDoc is a text document format for writing documentation, articles, and books, ebooks, slideshows, web pages, man pages and blogs.                                                         |
| [Org-Mode](../reference/formats/org.qmd)           | Org-Mode is an Emacs major mode for keeping notes, authoring documents, creating computational notebooks, and more.                                                                            |
| [Muse](../reference/formats/muse.qmd)              | Emacs Muse is an authoring and publishing environment for Emacs.                                                                                                                               |
| [GNU Texinfo](../reference/formats/texinfo.qmd)    | Texinfo is the official documentation format of the GNU project.                                                                                                                               |
| [Groff Man Page](../reference/formats/man.qmd)     | The Groff (GNU troff) man page document formats consists of plain text mixed with formatting commands that produce ASCII/UTF8 for display at the terminal.                                     |
| [Groff Manuscript](../reference/formats/ms.qmd)    | The Groff (GNU troff) manuscript format consists of plain text mixed with formatting commands that produces PostScript, PDF, or HTML.                                                          |
| [Haddock markup](../reference/formats/haddock.qmd) | Haddock is a tool for automatically generating documentation from annotated Haskell source code.                                                                                               |
| [OPML](../reference/formats/opml.qmd)              | OPML (Outline Processor Markup Language) is an XML format for outlines.                                                                                                                        |
| [Textile](../reference/formats/textile.qmd)        | Textile is a simple text markup language that makes it easy to structure content for blogs, wikis, and documentation.                                                                          |
| [DocBook](../reference/formats/docbook.qmd)        | DocBook is an XML schema particularly well suited to books and papers about computer hardware and software.                                                                                    |
| [InDesign](../reference/formats/icml.qmd)          | ICML is an XML representation of an Adobe InDesign document.                                                                                                                                   |
| [TEI Simple](../reference/formats/tei.qmd)         | TEI Simple aims to define a new *highly-constrained* and *prescriptive* subset of the Text Encoding Initiative (TEI) Guidelines suited to the representation of early modern and modern books. |
| [FictionBook](../reference/formats/fb2.qmd)        | FictionBook is an open XML-based e-book format.                                                                                                                                                |

```{=html}
<style type="text/css">
main h2 {
  border-bottom: none;
}  
  
</style>
```



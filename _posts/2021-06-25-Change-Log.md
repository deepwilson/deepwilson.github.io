---
title: "Change Log"
description: "A log of changes and personalizations I've made to the blog after incoporating the default fastpages Minima and Oriol's Mssively."
layout: post
comments: false
search_exclude: false
---

<!-- omit in toc -->
## <div align="center">--- Change Log ---</div>

<!-- omit in toc -->
<div align="right">

---

<!-- omit in toc -->
### TOC
- [Editing The Look Of Flash Alerts](#editing-the-look-of-flash-alerts)
- [Editing The Look Of Inline Markdown Code](#editing-the-look-of-inline-markdown-code)
- [Editing The Look Of Jupyter Code Cells](#editing-the-look-of-jupyter-code-cells)
- [Fix Scrollbars Not Showing For Overflowing Notebook Cells](#fix-scrollbars-not-showing-for-overflowing-notebook-cells)
- [Editing The Size Of Normal Text](#editing-the-size-of-normal-text)
- [Fix #Collapse-Output Not Working For Notebooks](#fix-collapse-output-not-working-for-notebooks)
- [Editing The Look Of Images](#editing-the-look-of-images)

</div>

---

### Editing The Look Of Flash Alerts
file: _sass\minima\fastpages-styles.scss

<details>
<summary>code:</summary> 

```scss
.flash {
position: relative;
padding: 10px 10px;
border-style: solid;
border-width: 4px;
border-radius: 10px;
}
```
</details>

### Editing The Look Of Inline Markdown Code

file: _sass\minima\colorschemes\fastpages-dracula-highlight.scss

<details open>
<summary>code:</summary>

```scss
.highlight {
    ✒ sass\minima\colorschemes\fastpages-dracula-highlight.scss

    // background: $dt-code-cell-background !important;
    color: $dt-gray-light !important;
    pre, code {
    background: $dt-code-cell-background;
    color: $dt-gray-light;
    border-left: 10px solid $dt-code-cell-background;
    border-left: 10px solid $dt-code-cell-background;
    border-top: 10px solid $dt-code-cell-background;
    border-bottom: 10px solid $dt-code-cell-background;
    border-radius: 15px !important;
    }
```
</details>

### Editing The Look Of Jupyter Code Cells

file: _sass\minima\syntax_highlight_base.scss

<details>
<summary>code:</summary> 
some code needed to be commented out due to style conflicts in other .scss files

```scss
// .input_area pre, .input_area div {
//     margin-bottom: 2rem !important;
//     margin-top: 1.5rem !important;
//     padding-bottom: 0 !important;
//     padding-top: 0 !important;
//     background: $dt-code-cell-background;
//     -webkit-font-smoothing: antialiased;
//     text-rendering: optimizeLegibility;
//     font-family: Menlo, Monaco, Consolas, "Lucida Console", Roboto, Ubuntu, monospace;
//     border-radius: 5px;
//     font-size: 100%;
//     font-weight: 350; // make code have slightly more weight than text
// }

.input_area pre {
    border-left: 10px solid $dt-code-cell-background;
    border-left: 10px solid $dt-code-cell-background;
    border-top: 10px solid $dt-code-cell-background;
    border-bottom: 10px solid $dt-code-cell-background;
    border-radius: 10px !important;
}
```
</details>

### Fix Scrollbars Not Showing For Overflowing Notebook Cells

file: _sass\base\_typography.scss

<details>
<summary>code:</summary>

```scss
.re {
    -webkit-overflow-scrolling: touch;
    font-family: _font(family-fixed);
    font-size: 0.9rem;
    margin: 0 0 _size(element-margin) 0;
    // this fixed the issue with scrollbars
    overflow: auto !important;

    code {
    display: block;
    line-height: 1.75;
    padding: 1rem 1.5rem;
    }
}
```
</details>

### Editing The Size Of Normal Text

file: _sass\base\_typography.scss

<details>
<summary>code:</summary>

```scss
body, input, select, textarea {
    // controls the font type of the blog text (unformatted markdowns)
    font-family: _font(family);
    font-weight: _font(weight);
    font-size: 1rem;
    line-height: 2.375;
}
```
</details>

### Fix #Collapse-Output Not Working For Notebooks

file: _action_files\hide.tpl

<details>
<summary>code:</summary> 
replace the pertinent block

<!-- {% raw %} & {% endraw %} disables tag processing -->
{% raw %}
```scss
{% block output_group -%}
{%- if cell.metadata.collapse_output -%}
    <details class="description">
    <summary class="btn btn-sm" data-open="Hide Output" data-close="Show Output"></summary>
        <p>{{ super() }}</p>
    </details>
{%- elif cell.metadata.hide_output -%}
{%- else -%}
    {{ super()  }}
{%- endif -%}
{% endblock output_group %}
```
{% endraw %}
</details>

### Editing The Look Of Images

file: _sass\minima\fastpages-styles.scss

<details>
<summary>code:</summary>

```scss
.post img {
    display: block;
    vertical-align: top;
    margin-left: auto;
    border: groove;
    margin-right: auto;
}
```
</details>

---
**template**

    ### editing ...

    file:

    <details>
    <summary>code:</summary>
    ```scss
    **code**
    ```
    <\details>
---





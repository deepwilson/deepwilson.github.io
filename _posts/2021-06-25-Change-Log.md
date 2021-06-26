---
title: "Change Log"
description: "A log of changes and personalizations I've made to the blog after incoporating the default fastpages Minima and Oriol's Mssively."
layout: post
toc: true
categories: [markdown]
comments: false
search_exclude: false
---
<!--  -->
{::options parse_block_html="true" /}
<!--  -->

### Editing The Look Of Flash Alerts
file: _sass\minima\fastpages-styles.scss

<details open>
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

<details open>
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

<details open>
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

<details open>
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

<details open>
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

<details open>
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

### Fix posts not Hiding

files: index.html; _layouts\blog.html; _layouts\categories.html; _layouts\tags.html

add `hide: true` to the `front matter` of the post; you could also set `search_exclude = true` but that means the only way the hidden post can be accessed is through its permalink (for example, setting `permalink: /hidden/:title/`)

<details open>
<summary>code:</summary>

{% raw %}
```scss
{% for post in ***** %}
  {% if post.hide != true %}
    *****
  {% endif %}
{% endfor %}
```
{% endraw %}

</details>

<!--  -->
{::options parse_block_html="false" /}  
<!--  -->
---
**template**

    ### editing ...

    file:

    <details open>
    <summary>code:</summary>

    ```scss
    **code**
    ```

    </details>
---





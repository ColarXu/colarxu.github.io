---
description: What is HTML?  HTML stands for HypeText Markup Language, it provides
  structure to the content appearing on a website....
lastmod: '2022-06-03T15:54:59.802Z'
publishDate: '2022-06-02T18:50:47.594Z'
tags:
- 教程
- Web
title: 'WebDev 01: Introduction to HTML'
---

## What is HTML?

HTML stands for HypeText Markup Language, it provides structure to the content appearing on a website. 

## HTML Elements

**tag**: `<h1></h1>`
**element**: `<h1>Colar</h1>`

### basic ones

- `<body></body>`: only content inside the opening and closing body tags can be displayed to the screen.
- `<h1></h1> <h6></h6>`: six different headings.
- `<div></div>`: short for division, a container that divides the page into sections.
- `<p></p>`: plain text.
- `<span></span>`: separate a piece of content form other content. `<p><span>Self-driving cars</span> are anticipated to replace up to 2 million jobs over the next two decades.</p>`

### styling text

- `<em></em>`: emphasize text, italic
- `<strong></strong>`: highlight text
- `<br>`: line break.

### lists

- **unordered lists**

```html
<ul>
  <li>apple</li>
  <li>pineapple</li>
  <li>watermelon</li>
</ul>
```

- **ordered lists**

```html
<ol>
  <li>one</li>
  <li>two</li>
  <li>three</li>
</ol>
```

### other content

- **image**: `<img src="image-location" alt="image-description" />`, src is short for source, alt is short for alternative text.
- **video**: `<video src="video-location" width="320" height="240" controls> Video not supported </video>` controls instruct the browser to include basic video controls such as pausing and playing. 

### attribute

- `<div id="intro">`
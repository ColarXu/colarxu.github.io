---
lastmod: '2022-06-03T15:55:14.724Z'
publishDate: '2022-06-02T19:54:35.828Z'
tags:
- 教程
- Web
title: 'WebDev 02: HTML Document Standards'
---

## Document Type Declaration

`<!DOCTYPE html>`: the declaration specifying the version of HTML for the browser, put it on the first line of code to tell the browser what type of document to expect.

## HTML Structure

```html
<!DOCTYPE html>
<html>
  <head>
    <title></title>
  </head>
  <body>
    content that displayed to the screen.
  </body>
</html> 

```
- `<html></html>`: enclose all the HTML code.
- `<head></head>`: metadata, tell the browser about the page itself, not displayed on the webpage.
- `<title></title>`: the title of the web page.
- `<body></body>`: only content inside the opening and closing body tags can be displayed to the screen.

### Links

- **absolute links**: linking to other website `<a href="URL" target="_blank">text</a>` href refers to hyperlink reference, `target="_blank"` means opening the link in a new tab.
- **relative links**: linking to internal path in the same folder `<a href="internal path(./contact.html">Contact</a>`.
- **turn image into link**: `<a href="link" target="_blank"><img src="image-location" alt="image despriction"/></a>`
- **linking to same page**: target `<div id="name">`, then `<a href="#name"></a>`, click the link then scroll to the section you target.

### Comments

`<!-- comments -->`

---
[HTML Element Reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)
---
tags: [教程, Web]
title: 'WebDev 04: Beginner CSS'
publishDate: '2022-06-04T06:17:08.960Z'
lastmod: '2022-06-04T07:10:32.266Z'
---

CSS add styles to web page. Each element have several style properties.

## Basic Propeties

**font-famiy**

```css
h1 {
  font-family: Georgia;
}
```

- the specific font must be installed 
- use [Web safe fonts](https://www.cssfontstack.com/), or the font you choose may not appear the same between all browsers and operating system.
- when the name of a typeface consists of more than one word, enclose the name in quotes, like 'Courier New'.

**font-size**

```css
p {
  font-size: 18px;
}
```

- `px` means pixels

**font-weight**

```css
p{
  font-weight: bold;
}
```

- normal or bold.

**text-align**

```css
h1 {
  text-align: right;
}
```

- left, right, center, justify(两端对齐)

**color**

```css
h1{
  color: red;
  background-color: blue;
}
```

- `color`: the color of the element itself.
- `backgound-color`: the background color of the element.

**opacity**

```css
.overlay {
  opacity: 0.5;
}
```

- 1 represent 100%, fully visible.
- 0 represent 0%, fully invisible.

**background-image**

```css
.main-banner {
  background-image: url('https://www.example.com/image.jpg'); 
}
```
- set the background of an element to display an image.
- you can use relative path as well.

**important**

```css
p {
  color: blue !important;
}
```

- override other any style. 




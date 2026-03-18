---
lastmod: '2022-06-07T14:38:14.744Z'
publishDate: '2022-06-04T07:29:01.242Z'
tags:
- 教程
- Web
title: 'WebDev 05: CSS Color'
---

## Hex and RGB

- Hex value: #8FBC8F 
- RGB value: rgb(143, 188, 143)

These two kinds of vuales are interchangeable, but it is wise to use just one value in coding.

## HSL

```css
color: hsl(120, 60%, 70%);
```

shorts for hue-saturation-lightness.

- Hue: the first number, represents the degree of the hue, between 0 and 360.
- Saturation: refers to the intensity or purity of the color, value ranges from 0% to 100%, the higher the color becomes richer, or grayer.  
- Lightness: refers to the light or dark of color, value ranges from 0% to 100%, the higher the color becomes lighter, or dimmer.

## Opacity and  Alpha

```css
color: hsla(34, 100%, 50%, 0.1);
```

The fourth value `a` alpha, means opacity. It ranges from 0 to 1, if the alpha is 0, the color will be completely transparent; if the alpha is 1, the color would be opaque.

```css
color : rbga(234, 45, 98, 0.33);
```

When it comes to RBG color, just add a fourth at the end of rbg value to represent opacity. 

When it comes to Hex color, you can add two-digit at the end of the value to represent opacity. It ranges from 00(transparent) to FF(opaque).

Alpha can only be used with HSL, GRB and hex colors. We cannot add the alpha value to name colors like green.
---
tags: [教程, Web]
title: 'WebDev 03: HTML Table'
publishDate: '2022-06-03T02:44:07.009Z'
lastmod: '2022-06-03T15:55:34.965Z'
---

## Table Code Structure 
```html
<table>
  <thead>
    <tr>
      <th scope="col"></th>
      <td></td>
    </tr>
  </thead>
  <tbody>
    <tr>
    </tr>
  </tbody>
  <tfoot>
    <tr>
    </tr>
  </tfoot>
</table>
```

## Table Element

- `<table></table>`: contain all the tabular data.
- `<thead></thead>`: the heading of a long table.
- `<tbody></tbady>`: the body of the long table.
- `<tr></tr>`: add table rows.
- `<th></th>`: add table heading. `<th scope="col">colum heading</th>`, `<th scope="row>row heading</th>`, `<th></th>` blank heading.
- `<td></td>`: add table data. `<td colspan="number">` let table data across several columns, `<td rowspan="number">` let table data across several rows. 
- `<tfoot></tfoot>`: the bottom part of a long table.
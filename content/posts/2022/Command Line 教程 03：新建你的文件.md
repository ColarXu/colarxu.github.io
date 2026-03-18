---
lastmod: '2022-04-16T14:04:27.202Z'
publishDate: '2022-04-16T10:03:02.200Z'
tags:
- Command Line
- 教程
title: "Command Line \b教程 03：新建文件和文件夹"
---

[上一期](https://colarxu.github.io/posts/2022/command-line-%E6%95%99%E7%A8%8B-02%E5%9C%A8%E8%AE%A1%E7%AE%97%E6%9C%BA%E9%87%8C%E6%95%A3%E6%AD%A5/)我们学了三个命令：

- `ls` 查看当前目录下的文件和文件夹
- `cd` 切换不同的文件目录
- `pwd` 显示当前文件夹的路径

从此具备了在计算机的文件夹丛林里漫游的能力。

好吧，走也走了，看也看了。现在就来动动手，学习怎么往计算机里加东西吧。

## mkdir 命令：新建文件夹

`mkdir` 即 make directory，新建文件夹（目录）的意思。

在 Terminal 中输入 `mkdir 文件夹名称`，就可以在当前文件夹下，新建一个子文件夹。

很简单对吧？感觉比用鼠标右键新建文件夹要更快呢。

如果你想把文件夹建在别的地方，就这样来： `mkdir ~/xxx/xxx/xxx/文件夹名称`。`~` 指的是根目录，那些 xxx 就是你目标文件夹的路径。

## touch 命令：新建文件

`touch` 命令跟 `mkdir` 的原理是一样的。只不过前者是新建文件，后者是新建文件夹。

请注意，`touch` 命令只能新建**纯文本文件**，比如 txt 和 md 文件，其他类型的文件可是建不了的。

举个例子，`touch ~/desktop/note.md`，便是在桌面新建一个名为 note 的 markdown 文档（`~` 是根目录，桌面 desktop 是根目录的子文件夹）。 

对了，**当新建一个文件的时候，一定不要忘记加上文件的后缀名**。漏了后缀名，电脑可是不会搭理这个命令的哟。

## cat 命令：查看文件内容

在 Terminal 中，我们无需打开文件，就可以查看文件里的内容。

我悄悄地在刚才新建的文件 note.md 中贴了一行诗，现在就去看看吧。

输入命令 `cat ~/desktop/note.md`（如果你在 desktop 这个文件目录，输入 `cat note.md` 就行了）。

然后你会看见：

```
colarxu@MacBook-Air ~ % cat ~/desktop/note.md

O friends, I am mad with love, and no one sees.    
```
See？不用真的打开文件，在 Terminal 里面就可以看到那句诗了。

## echo 命令：往文件里加内容

既然可以在 Terminal 里查看文件内容，那可不可以在里面写东西呢？

当然是可以的，用 `echo` 命令就行了。

比如，我想在 note.md 文档里加一段文字的话，输入 `echo "This is not true.” >> ~/desktop/note.md` 就行了。

```
colarxu@MacBook-Air ~ % echo "This is not true." >> ~/desktop/note.md 
colarxu@MacBook-Air ~ % cat ~/desktop/note.md 

O friends, I am mad with love, and no one sees.This is not true.
```

在 `echo` 后面的双引号 `“”` 里写下要添加的内容，后面跟上 `>>`，再输入目标文件的路径，那句话就写进去了。

注意，如果命令中间，你用的是 `>` 而不是 `>>` 的话，**你新添加的内容，会把原有的内容给覆盖掉**。

除了 `echo` 命令，你还可以用 `cat` 命令来往文件里添加内容。

举个例子：

- `cat note.md > poem.md` 用 note 里的内容「覆盖」poem 的内容。
- `cat note.md >> poem.md` 把 note 的内容添加到 poem 里面。

你们注意到没有？`echo` 命令是把一段文本添加到一个文件里面去，而 `cat` 命令是把一个文件的内容，添加到另一个文件里去。如果被添加的对象文件不存在，则会自动新建一个。

## 小结

好了，一次学这么多就够了。照例回顾一下。

这一期，我们学了四组命令：

- `mkdir 文件夹名称` 在当前文件夹内部，新建一个子文件夹。
- `touch 文件名称.文件类型（如 txt、md）` 在当前文件夹内部，新建一个文件。
- `cat 文件名称.文件类型` 显示该文件的内容。 
- `echo “想增加的内容” >> 文件名称.文件类型` 在文件中新增内容。

下一期，我们将学习如何删除、移动和复制文件。再会再会~
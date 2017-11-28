
# gv-dot-colorizer - A graphviz DOT colorizer


## Introduction

The purpose of this tool is to colorize nodes in a graph as produced by [`LLVM`][1] `opt` using specific node
attributes. 

In our case, the only current application is on graphs that represent control flow (i.e. Control Flow Graphs), thus the
nodes correspond to basic blocks in source code.

Currently, the criteria for coloring nodes are hard-coded, but they can easily be changed by adapting the script
`gv-dot-colorize.py`.


## Requirements

- [GraphViz][2] `dot`
- [NetworkX][3]


## How to use

1. Simply provide the location of the `DOT` file to the main script, e.g.:  
   
   `gv-dot-colorizer.sh foo.cfg`

    The script will create 2 files, a modified `DOT` file and its corresponding `PDF`.  Both produced files will retain
    their initial name, although they will get their suffices augmented with the word `colorized`. Both files will be
    generated in the same directory as their source `DOT` file.


[1]: llvm.org
[2]: www.graphviz.org
[3]: https://networkx.github.io


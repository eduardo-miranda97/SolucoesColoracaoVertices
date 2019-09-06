param H >= 1 integer;
set I := 1..H;
set V := 1..H;
set E within {V, V};

var x {V, I} binary;
var w {I} binary;

minimize num_colors:
    sum {i in I} w[i];

subject to one_color {v in V}:
    sum {i in I} x[v, i] = 1;

subject to unique_color {(u, v) in E, i in I}:
    x[u, i] + x[v, i] <= w[i];


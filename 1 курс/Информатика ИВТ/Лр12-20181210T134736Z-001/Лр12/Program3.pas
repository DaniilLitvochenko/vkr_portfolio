program lr12;

const
  n=3;

var
  A: array [1..n, 1..n] of integer;
  i, j, k: integer;

begin

  k := 2;
  
  for i := 1 to n do
  begin
    for j := 1 to n do
    begin
      A[i, j] := random(100);
    end;
  end;
  
  for i:=1 to n do
  writeln(A[i]);

for i := 1 to n do
  begin
    for j := 1 to n do
    begin
      if (i + j )< k then
        A[i, j] := 0;
    end;
    k := k + 2;
  end;
  
  writeln();
  for i:=1 to n do
  writeln(A[i])
end.


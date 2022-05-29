program lr12;

const
  n = 3;

var
  A: array [1..n, 1..n] of integer;
  i, j, sum, max: integer;

begin
  sum := 0;
  
  for i := 1 to n do
  begin
    for j := 1 to n do
    begin
      A[i, j] := random(100);
    end;
  end;
  
  max := A[1,1];
  
  for i := 1 to n do
    writeln(A[i]);
    
  for i := 1 to n do
  begin
    for j := 1 to n do
    begin
      if A[i, j] >= max then
        max := A[i, j];
      sum := sum + A[i, j];
    end;
  end;
  
  writeln(sum);
  writeln(max);
end.
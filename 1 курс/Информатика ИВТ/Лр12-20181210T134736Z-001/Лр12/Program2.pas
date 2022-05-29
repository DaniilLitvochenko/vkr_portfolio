program lr12;

const
  n=3;

var
  A: array [1..n, 1..n] of integer;
  i, j, gl, pob: integer;

begin
  gl := 0;
  pob := 0;
  
  for i := 1 to n do
  begin
    for j := 1 to n do
    begin
      A[i, j] := random(100);
    end;
  end;
  
  for i:=1 to n do
    writeln(A[i]);
    
  j := n;
  
  for i := 1 to n do
  begin
    gl := gl + A[i, i];
    pob := pob + A[i, j];
    j := j - 1;
  end;
  
  writeln(gl);
  writeln(pob);
end.
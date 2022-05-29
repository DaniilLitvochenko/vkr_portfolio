program lr10;

var
  a: array [1..10] of integer;
  i, max, ind, j: integer;

begin
  for i := 1 to 10 do
    a[i] := Random(100);
  writeln(a); 
  for i := 1 to 9 do
  begin
    max := a[i]; 
    ind := i;
    for j := i + 1 to 10 do
      if a[j] > max then
      begin
        max := a[j];
        ind := j;
      end;
    a[ind] := a[i];
    a[i] := max;
  end;  
  writeln(a);  
end.
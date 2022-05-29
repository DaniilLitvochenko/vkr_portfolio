program lr12;

const
  n = 3;

var
  A: array [1..n, 1..n] of integer;
  IND: array [1..n] of integer;
  b, i, j, l, sum, temp: integer;

begin
  for i := 1 to n do
  begin
    for j := 1 to n do
    begin
      A[i, j] := random(100);
    end;
  end;
  
  for i := 1 to n do
    writeln(A[i]);
  
  for i := 1 to n do
  begin
    sum := 0;
    for j := 1 to n do
    begin
      sum := sum + a[i, j];
    end;
    IND[i] := sum;
    writeln(IND[i]);
  end;
  
  for i := 1 to n - 1 do
  begin
    for l := i + 1 to n do
    begin
      if IND[i] > IND[l] then
      begin
        for j := 1 to n do
        begin
          b := a[i, j];
          a[i, j] := a[l, j];
          a[l, j] := b;
        end;
        temp := IND[i];
        IND[i] := IND[l];
        IND[l] := temp;
      end;
    end;
  end;
  
  for i := 1 to n do
    writeln(A[i]);
  for i := 1 to n do
    writeln(IND[i]);
end.
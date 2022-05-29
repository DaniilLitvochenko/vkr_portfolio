program lr11;

var
  X: array [1..10] of integer;
  i, k: integer;
  a, d1, d2, d3, y: real;

function f(x,i: integer): real;
var
  z: integer;
  y: real;
begin
  y:=0;
  for z := 0 to 10 do
  begin
    if (z mod 2) = 0 then
    begin
      y := y + ((power(z, x) + x) / 3628800);
    end;
  end;
f:=y;
end;

begin
  for i := 1 to 10 do
    X[i] := random(100);
  writeln(x);
  writeln('Введите а: ');
  readln(a);
  writeln('Введите k: ');
  readln(k);
  writeln('Введите промежутки d: ');
  readln(d1, d2, d3);
  for i := 1 to 10 do
  begin
    if (d1 <= X[i]) and (X[i] < d2) then
    begin
      y := Power((a + X[i]), 1 / k);
      writeln('y[', i, ']=', y);
    end;
    if (d2 < X[i]) and (X[i] <= d3) then
    begin
     y:=f(X[i],i);
     writeln('y[', i, ']=', y);  
    end;
  end;
end.
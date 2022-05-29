program lr11;

var
  a, i, fc, sum, temp: integer;


function f(n: integer): integer;
var
  i, fc: integer;
begin
  fc := 1;
  begin
    for i := 2 to n do
      fc := fc * i;
  end;
  f := fc;
end;

begin
  writeln('Введите а: ');
  readln(a);
  i := 1;
  while sum <= a do
  begin
    sum := sum + f(i);
    i := i + 1;
    temp := i
  end;
  if sum > a then
  begin
    sum := 0;
    temp := temp - 2;
    for i := 1 to temp do
    begin
      writeln(f(i));
      sum := sum + f(i);
    end;
  end
  else
  begin
    sum := 0;
    for i := 1 to temp do
    begin
      sum := sum + f(i);
    end;
  end;
  writeln('Cумма: ',sum);
end.
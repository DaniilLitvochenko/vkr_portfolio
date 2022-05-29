program lr7;

var
  a, sum: integer;

begin
  sum := 0;
  while sum <= 10 do
    begin
  sum:=0;
  readln(a);
    while a <> 0 do
    begin
      sum := sum + (a mod 10);
      a := a div 10;
    end;
    writeln(sum);
  end;
end.
program lr9;

var 
  a,inp: real;  

begin
a:=random(100)+1;
writeln('Число загадано');
while inp<>a do
begin
readln(inp);
if a>inp then writeln('Больше чем ', inp);
if a<inp then writeln('Меньше чем ', inp);
end;
writeln('Вы победили комплюхтер')
end.
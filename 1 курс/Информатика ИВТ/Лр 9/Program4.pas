program lr9;

var 
    v,vi: integer;
begin
writeln('Введите число ворон: ');
readln(v);
if (v<=20) and (v>=10) then
begin
writeln(v,' ворон');
end
else
begin
vi:=v mod 10;
case vi of
1: writeln(v,' ворона');
2,3,4: writeln(v,' вороны');
0,5,6,7,8,9: writeln(v,' ворон');
end;
end;
end.
program lr5;

var n: integer;
 
function geom(n:integer):real;
var a,b: real;
    i: integer;
begin
a:=1;
for i:=1 to n do
begin
writeln('Введите число: ');
readln(b);
b:=abs(b);
a:=a*b;
end;
a:=exp(ln(a) * 1/n); 
geom:=a;
end;

begin
writeln('Введите кол-во чисел: ');
readln(n);
writeln('Ответ: ',geom(n));
end.
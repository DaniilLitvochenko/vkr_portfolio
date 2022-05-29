program z2;
const
a = -10;
b = 10;
e = 0.000001;
var
x,xi:real;

function F(x:real):real;
begin
F:=(2*x*x*x-9*x*x-60*x+1)/(6*x*x-16*x-60);
end;

begin
xi:=0;
repeat
x:=xi;
xi:=x-F(x);
until abs(xi-x)<= e;
writeln('Ответ ',xi);
end.
program lr11;

var x,y: real;

begin
writeln('Введите х: ');
readln(x);
if x>=1 then
y:=(1/2)*x
else 
if (0<=x) and(x<1)then
y:=(1/3)*x
else 
y:=(1/4)*abs(x);
writeln('y = ',y);
end.
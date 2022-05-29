program lr5;

var s,res,a,b,c: real;
    i: integer;

function herone(a,b,c: real):real;

var p,s:real;

begin
p:=(a+b+c)/2;
s:=sqrt(p*(p-a)*(p-b)*(p-c));
herone:=s;
end;

begin
res:=0;
for i:=1 to 4 do
begin
writeln('Введите стороны ',i,'-ого треугольника: ');
readln(a,b,c);
res:=res+herone(a,b,c);
end;
writeln('Площадь фигуры равна: ',res);
end.